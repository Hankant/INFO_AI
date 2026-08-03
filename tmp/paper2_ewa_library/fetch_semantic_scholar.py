from __future__ import annotations

import json
import subprocess
import urllib.error
import urllib.request
from pathlib import Path


PATH = Path(r"E:\Info_AI\tmp\paper2_ewa_library\metadata.json")


def main() -> None:
    records = json.loads(PATH.read_text(encoding="utf-8"))
    ordered = sorted(records)
    payload = json.dumps({"ids": [f"DOI:{records[key]['doi']}" for key in ordered]}).encode()
    request = urllib.request.Request(
        "https://api.semanticscholar.org/graph/v1/paper/batch?fields=title,year,authors,abstract,openAccessPdf,externalIds,url",
        data=payload,
        method="POST",
        headers={
            "Content-Type": "application/json",
            "User-Agent": "Info-AI-Literature-Library/1.0",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=45) as response:
            results = json.load(response)
    except Exception as exc:
        print(f"urllib failed: {type(exc).__name__}: {exc}; trying curl")
        curl = subprocess.run(
            [
                "curl.exe",
                "-L",
                "--silent",
                "--show-error",
                "--fail",
                "--max-time",
                "60",
                "-H",
                "Content-Type: application/json",
                "--data-binary",
                payload.decode(),
                "https://api.semanticscholar.org/graph/v1/paper/batch?fields=title,year,authors,abstract,openAccessPdf,externalIds,url",
            ],
            capture_output=True,
            text=True,
            timeout=70,
        )
        if curl.returncode != 0:
            print(f"curl failed ({curl.returncode}): {curl.stderr}")
            return
        results = json.loads(curl.stdout)

    for key, result in zip(ordered, results):
        records[key]["semantic_scholar"] = result
    PATH.write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding="utf-8")
    found = sum(bool(result) for result in results)
    pdfs = sum(bool((result or {}).get("openAccessPdf")) for result in results)
    abstracts = sum(bool((result or {}).get("abstract")) for result in results)
    print(f"Semantic Scholar matched {found}/{len(results)}; abstracts={abstracts}; OA PDFs={pdfs}")


if __name__ == "__main__":
    main()
