from __future__ import annotations

import io
import json
import subprocess
import tarfile
from pathlib import Path


ROOT = Path(r"E:\Info_AI")
META = ROOT / "tmp" / "paper2_ewa_library" / "metadata.json"
PDF_DIR = ROOT / "defense_project" / "reference_materials" / "papers_originals" / "paper2_ewa"


DIRECT = {
    "Dietvorst2015": "https://repository.upenn.edu/server/api/core/bitstreams/4d24c079-228b-47bd-ba8c-166eeddee8de/content",
    "Camerer1999": "https://authors.library.caltech.edu/api/records/kgnbx-e2z22/files/1468-0262.00054_1_.pdf/content",
    "Logg2019": "https://www.hbs.edu/ris/Publication%20Files/17-086_610956b6-7d91-4337-90cc-5bb5245316a8.pdf",
    "Choi2026": "https://www.repository.cam.ac.uk/bitstreams/2f8fdfda-15d7-48c4-afe5-330c8bd1c7e9/download",
}

INSECURE_TLS = {
    "Landes2026": "https://kar.kent.ac.uk/113194/1/Landes%20et%20al%202026%20Cognition%20.pdf",
}

PMC_PACKAGES = {
    "Vaccaro2024": "https://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_package/d9/25/PMC11659167.tar.gz",
    "Kobis2025": "https://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_package/0b/bb/PMC12488497.tar.gz",
}


def valid_pdf(data: bytes) -> bool:
    return len(data) >= 10_000 and data[:1024].lstrip().startswith(b"%PDF-")


def curl_bytes(url: str, insecure: bool = False) -> bytes | None:
    args = [
        "curl.exe",
        "-L",
        "--silent",
        "--show-error",
        "--fail",
        "--retry",
        "1",
        "--connect-timeout",
        "15",
        "--max-time",
        "120",
        "-A",
        "Mozilla/5.0",
    ]
    if insecure:
        args.append("--insecure")
    args.append(url)
    result = subprocess.run(args, capture_output=True, timeout=135)
    if result.returncode:
        print(f"  curl failed: {result.stderr.decode(errors='replace').strip()}")
        return None
    return result.stdout


def save(key: str, data: bytes, source_url: str, records: dict, note: str = "") -> bool:
    if not valid_pdf(data):
        print(f"{key}: rejected non-PDF ({len(data)} bytes)")
        return False
    path = PDF_DIR / f"{key}.pdf"
    path.write_bytes(data)
    for item in records.values():
        if item.get("bib_key") == key:
            item["pdf"] = {
                "status": "downloaded",
                "path": str(path),
                "bytes": len(data),
                "source_url": source_url,
                "source_note": note,
            }
            break
    print(f"{key}: saved {len(data)} bytes")
    return True


def main() -> None:
    records = json.loads(META.read_text(encoding="utf-8"))
    PDF_DIR.mkdir(parents=True, exist_ok=True)

    for key, url in DIRECT.items():
        data = curl_bytes(url)
        if data:
            save(key, data, url, records, "institutional or author repository")

    for key, url in INSECURE_TLS.items():
        data = curl_bytes(url, insecure=True)
        if data:
            save(
                key,
                data,
                url,
                records,
                "institutional repository; TLS validation bypassed because the local network presented an untrusted chain",
            )

    for key, url in PMC_PACKAGES.items():
        package = curl_bytes(url)
        if not package:
            continue
        with tarfile.open(fileobj=io.BytesIO(package), mode="r:gz") as archive:
            pdf_members = [member for member in archive.getmembers() if member.name.lower().endswith(".pdf")]
            if not pdf_members:
                print(f"{key}: PMC package contains no PDF")
                continue
            member = max(pdf_members, key=lambda value: value.size)
            handle = archive.extractfile(member)
            data = handle.read() if handle else b""
            save(key, data, url, records, "PubMed Central open-access package")

    META.write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding="utf-8")
    usable = sum(item.get("pdf", {}).get("status") in {"downloaded", "existing"} for item in records.values())
    print(f"Usable local PDFs: {usable}/{len(records)}")


if __name__ == "__main__":
    main()
