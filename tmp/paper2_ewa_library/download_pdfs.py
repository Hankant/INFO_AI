from __future__ import annotations

import json
import re
import subprocess
import time
import unicodedata
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path


ROOT = Path(r"E:\Info_AI")
METADATA = ROOT / "tmp" / "paper2_ewa_library" / "metadata.json"
BIB = ROOT / "defense_project" / "latex" / "references.bib"
PDF_DIR = ROOT / "defense_project" / "reference_materials" / "papers_originals" / "paper2_ewa"


def existing_bib_keys() -> tuple[dict[str, str], set[str]]:
    raw = BIB.read_text(encoding="utf-8")
    by_doi: dict[str, str] = {}
    keys: set[str] = set()
    matches = list(re.finditer(r"(?m)^@\w+\{([^,]+),", raw))
    for index, match in enumerate(matches):
        key = match.group(1).strip()
        keys.add(key)
        end = matches[index + 1].start() if index + 1 < len(matches) else len(raw)
        block = raw[match.start() : end]
        doi_match = re.search(r'(?im)^\s*doi\s*=\s*[\{"]([^\}"]+)', block)
        if doi_match:
            by_doi[doi_match.group(1).strip().lower()] = key
    return by_doi, keys


def ascii_key_part(value: str) -> str:
    value = unicodedata.normalize("NFKD", value)
    value = "".join(char for char in value if not unicodedata.combining(char))
    return re.sub(r"[^A-Za-z0-9]", "", value)


def make_key(item: dict, used: set[str]) -> str:
    cr = item.get("crossref") or {}
    authors = cr.get("author") or []
    family = (authors[0].get("family") if authors else "") or "Paper"
    year = item.get("normalized", {}).get("year") or "ND"
    base = f"{ascii_key_part(family)}{year}"
    key = base
    suffix = ord("a")
    while key in used:
        key = f"{base}{chr(suffix)}"
        suffix += 1
    used.add(key)
    return key


def candidates(item: dict) -> list[str]:
    urls: list[str] = []
    oa = item.get("openalex") or {}
    for location_name in ("best_oa_location", "primary_location"):
        location = oa.get(location_name) or {}
        if location.get("pdf_url"):
            urls.append(location["pdf_url"])
    for location in oa.get("locations") or []:
        if location and location.get("pdf_url"):
            urls.append(location["pdf_url"])

    for link in (item.get("crossref") or {}).get("link") or []:
        url = link.get("URL")
        content_type = (link.get("content-type") or "").lower()
        if url and ("pdf" in content_type or "/pdf" in url.lower()):
            urls.append(url)

    seen: set[str] = set()
    return [url for url in urls if not (url in seen or seen.add(url))]


def fetch_pdf(url: str, temp_path: Path) -> tuple[bytes | None, str, str]:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124 Safari/537.36",
            "Accept": "application/pdf,text/html;q=0.8,*/*;q=0.5",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=35) as response:
            data = response.read(60 * 1024 * 1024)
            final_url = response.geturl()
            content_type = response.headers.get("Content-Type", "")
    except Exception as exc:
        first_detail = f"{type(exc).__name__}: {exc}"
    else:
        if len(data) >= 10_000 and data[:1024].lstrip().startswith(b"%PDF-"):
            return data, final_url, f"ok ({len(data)} bytes; {content_type})"
        first_detail = f"not_pdf ({len(data)} bytes; {content_type})"

    curl = subprocess.run(
        [
            "curl.exe",
            "-L",
            "--silent",
            "--show-error",
            "--fail",
            "--retry",
            "1",
            "--connect-timeout",
            "12",
            "--max-time",
            "70",
            "-A",
            "Mozilla/5.0",
            "-o",
            str(temp_path),
            url,
        ],
        capture_output=True,
        text=True,
        timeout=80,
    )
    if curl.returncode == 0 and temp_path.exists():
        curl_data = temp_path.read_bytes()
        temp_path.unlink()
        if len(curl_data) >= 10_000 and curl_data[:1024].lstrip().startswith(b"%PDF-"):
            return curl_data, url, f"ok_curl ({len(curl_data)} bytes)"
        curl_detail = f"curl_not_pdf ({len(curl_data)} bytes)"
    else:
        curl_detail = f"curl_failed ({curl.returncode}): {curl.stderr.strip()}"
        if temp_path.exists():
            temp_path.unlink()
    return None, url, f"{first_detail}; {curl_detail}"


def main() -> None:
    records = json.loads(METADATA.read_text(encoding="utf-8"))
    doi_to_key, used = existing_bib_keys()
    PDF_DIR.mkdir(parents=True, exist_ok=True)

    for doi in sorted(records):
        item = records[doi]
        item["bib_key"] = doi_to_key.get(doi) or make_key(item, used)

    def download_one(doi: str) -> tuple[str, dict]:
        item = records[doi]
        target = PDF_DIR / f"{item['bib_key']}.pdf"
        if target.exists() and target.stat().st_size >= 10_000:
            return doi, {"status": "existing", "path": str(target), "bytes": target.stat().st_size}

        attempts: list[dict] = []
        for url in candidates(item):
            temp_path = PDF_DIR / f".{item['bib_key']}.download"
            data, final_url, detail = fetch_pdf(url, temp_path)
            attempts.append({"url": url, "final_url": final_url, "detail": detail})
            if data is not None:
                target.write_bytes(data)
                return doi, {
                    "status": "downloaded",
                    "path": str(target),
                    "bytes": len(data),
                    "source_url": final_url,
                    "attempts": attempts,
                }
        return doi, {"status": "not_downloaded", "attempts": attempts}

    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = {executor.submit(download_one, doi): doi for doi in sorted(records)}
        for index, future in enumerate(as_completed(futures), 1):
            doi, result = future.result()
            records[doi]["pdf"] = result
            print(
                f"[{index:02d}/{len(records)}] {records[doi]['bib_key']}: {result['status']}",
                flush=True,
            )

    METADATA.write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding="utf-8")
    downloaded = sum(item.get("pdf", {}).get("status") in {"downloaded", "existing"} for item in records.values())
    print(f"Usable local PDFs: {downloaded}/{len(records)}")


if __name__ == "__main__":
    main()
