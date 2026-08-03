from __future__ import annotations

import html
import http.client
import json
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path


ROOT = Path(r"E:\Info_AI")
PAPER2 = ROOT / "主Agent" / "文章项目" / "02_AI授权_EWA"
OUT = ROOT / "tmp" / "paper2_ewa_library" / "metadata.json"


def get_json(url: str) -> dict | None:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Info-AI-Literature-Library/1.0 (academic metadata verification)",
            "Accept": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=12) as response:
            return json.load(response)
    except (
        urllib.error.URLError,
        TimeoutError,
        json.JSONDecodeError,
        http.client.IncompleteRead,
        OSError,
    ) as exc:
        return {"_error": f"{type(exc).__name__}: {exc}"}


def strip_tags(value: str | None) -> str:
    if not value:
        return ""
    value = re.sub(r"<[^>]+>", " ", value)
    return re.sub(r"\s+", " ", html.unescape(value)).strip()


def extract_references() -> dict[str, dict]:
    records: dict[str, dict] = {}
    for path in sorted(PAPER2.glob("*.md")):
        lines = path.read_text(encoding="utf-8").splitlines()
        start = next(
            (
                i
                for i, line in enumerate(lines)
                if re.match(r"^##\s+(参考文献|References)\s*$", line)
            ),
            None,
        )
        if start is None:
            continue
        for line in lines[start + 1 :]:
            match = re.search(r"https://doi\.org/([^\s]+)", line, re.I)
            if not match:
                continue
            doi_display = match.group(1).rstrip(".")
            doi = doi_display.lower()
            item = records.setdefault(
                doi,
                {
                    "doi": doi_display,
                    "citations": [],
                    "source_files": [],
                },
            )
            item["citations"].append(line.strip())
            item["source_files"].append(path.name)
    return records


def main() -> None:
    records = extract_references()
    def fetch_one(doi: str) -> tuple[str, dict]:
        item = records[doi]
        quoted = urllib.parse.quote(item["doi"], safe="")
        crossref = get_json(f"https://api.crossref.org/works/{quoted}")
        item["crossref"] = (crossref or {}).get("message", crossref)

        oa_id = urllib.parse.quote(f"https://doi.org/{item['doi']}", safe="")
        openalex = get_json(f"https://api.openalex.org/works/{oa_id}")
        item["openalex"] = openalex

        cr = item.get("crossref") or {}
        item["normalized"] = {
            "title": (cr.get("title") or [""])[0],
            "author": cr.get("author") or [],
            "year": ((cr.get("published-print") or cr.get("published-online") or {}).get("date-parts") or [[None]])[0][0],
            "container": (cr.get("container-title") or [""])[0],
            "abstract": strip_tags(cr.get("abstract")),
            "type": cr.get("type", ""),
            "url": cr.get("URL", f"https://doi.org/{item['doi']}"),
        }
        return doi, item

    with ThreadPoolExecutor(max_workers=8) as executor:
        futures = {executor.submit(fetch_one, doi): doi for doi in sorted(records)}
        for index, future in enumerate(as_completed(futures), 1):
            try:
                doi, item = future.result()
            except Exception as exc:  # preserve the rest of the batch
                doi = futures[future]
                item = records[doi]
                item["fetch_error"] = f"{type(exc).__name__}: {exc}"
                item.setdefault("normalized", {"title": ""})
            print(
                f"[{index:02d}/{len(records)}] {item['doi']} | {item['normalized']['title'][:70]}",
                flush=True,
            )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {OUT} ({len(records)} records)")


if __name__ == "__main__":
    main()
