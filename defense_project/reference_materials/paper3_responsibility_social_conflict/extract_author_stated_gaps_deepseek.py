#!/usr/bin/env python3
"""Extract author-stated gaps, limitations, future directions, and critiques.

The script sends page-marked text from local PDFs to the DeepSeek Chat
Completions API. Every returned quotation is checked against the indicated PDF
page before it is admitted to the aggregate outputs.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.request
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

from pypdf import PdfReader


CATEGORIES = {
    "identified_research_gap": "作者用于说明本研究必要性的既有研究缺口",
    "acknowledged_limitation_or_remaining_gap": "作者承认的本研究局限、边界或仍未解决的问题",
    "future_research_direction": "作者明确提出的未来研究方向",
    "critique_of_prior_literature": "作者对既有文献、理论、方法或证据的明确批评",
    "author_stated_theoretical_outlook": "作者明确提出的理论含义、理论延伸或未来理论工作",
}

OUTLOOK_TYPES = {
    "theory_extension",
    "construct_refinement",
    "mechanism_specification",
    "boundary_condition",
    "theory_integration",
    "cross_level_link",
    "competing_explanation",
    "method_or_measurement_only",
    "context_or_population_only",
    "policy_or_practice_only",
    "not_applicable",
}

THEORY_OUTLOOK_TYPES = {
    "theory_extension",
    "construct_refinement",
    "mechanism_specification",
    "boundary_condition",
    "theory_integration",
    "cross_level_link",
    "competing_explanation",
}

SYSTEM_PROMPT = r"""
You are an evidence extraction engine for academic full text. Return one JSON
object only. Do not propose a research question, infer an unstated gap, improve
the authors' argument, or add outside knowledge.

Extract only statements explicitly made by the paper's authors in the supplied
pages. Use exactly these four categories:

1. identified_research_gap: a missing, understudied, unresolved, inconsistent,
   or insufficiently tested issue in prior knowledge that the authors use to
   motivate their own study.
2. acknowledged_limitation_or_remaining_gap: a limitation, boundary condition,
   uncertainty, or unresolved issue that the authors acknowledge about their
   own study or conclusions.
3. future_research_direction: an explicit recommendation or concrete direction
   for future research.
4. critique_of_prior_literature: an explicit criticism of the theory, methods,
   measurement, setting, assumptions, or evidence in earlier literature.

Exclusion rules:
- Exclude generic background, broad importance claims, and descriptions of what
  the current paper contributes.
- Exclude anything that requires your inference. Absence of evidence is not a
  gap unless the authors say so.
- Exclude statements found only in references, headers, footers, editor text,
  reviewer text, or supplementary navigation.
- Do not convert a limitation into a future direction unless the authors do.
- Do not classify disagreement with a result as criticism unless the authors
  explicitly identify a defect, omission, restriction, or inadequacy.
- One item must contain a short continuous quotation from a single marked page.
  Copy the quotation verbatim. Never repair wording or silently join fragments.
- `page` must be the integer shown in the nearest [[PAGE N]] marker.
- `author_claim_cn` is a restrained Chinese paraphrase of that quotation only.
- `target_of_critique` is required only for critique_of_prior_literature; use an
  empty string for all other categories.
- If the supplied pages contain no qualifying statement, return an empty items
  array. This is preferable to a speculative extraction.

JSON schema example:
{
  "items": [
    {
      "category": "future_research_direction",
      "verbatim_quote": "Future research should examine ...",
      "page": 12,
      "section": "Discussion",
      "author_claim_cn": "作者建议未来研究检验……",
      "target_of_critique": ""
    }
  ],
  "no_items_reason": ""
}
""".strip()

PROMPT_V2_PATH = Path(__file__).resolve().with_name("paper3_author_gap_prompt_v2.txt")
if PROMPT_V2_PATH.is_file():
    SYSTEM_PROMPT = PROMPT_V2_PATH.read_text(encoding="utf-8").strip()


@dataclass(frozen=True)
class PageText:
    page: int
    text: str


@dataclass(frozen=True)
class Chunk:
    pages: tuple[PageText, ...]

    @property
    def first_page(self) -> int:
        return self.pages[0].page

    @property
    def last_page(self) -> int:
        return self.pages[-1].page

    @property
    def marked_text(self) -> str:
        return "\n\n".join(f"[[PAGE {p.page}]]\n{p.text}" for p in self.pages)


def parse_args() -> argparse.Namespace:
    here = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(
        description="Extract only author-explicit research gaps and outlooks from local PDFs."
    )
    parser.add_argument("--manifest", type=Path, default=here / "manifest.csv")
    parser.add_argument(
        "--pdf-root",
        type=Path,
        default=here.parent,
        help="Recursive PDF search root; defaults to the shared reference_materials directory.",
    )
    parser.add_argument("--output-dir", type=Path, default=here / "author_stated_gaps_v2_theory")
    parser.add_argument("--base-url", default=os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com"))
    parser.add_argument("--model", default=os.getenv("DEEPSEEK_MODEL", "deepseek-v4-pro"))
    parser.add_argument("--api-key-env", default="DEEPSEEK_API_KEY")
    parser.add_argument("--max-chars", type=int, default=24_000)
    parser.add_argument("--max-output-tokens", type=int, default=5_000)
    parser.add_argument("--timeout", type=int, default=180)
    parser.add_argument("--retries", type=int, default=4)
    parser.add_argument("--sleep-seconds", type=float, default=0.5)
    parser.add_argument("--limit", type=int)
    parser.add_argument("--keys", nargs="*", help="Only process these bib_key values.")
    parser.add_argument("--force", action="store_true", help="Reprocess completed paper JSON files.")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Inventory and parse PDFs without calling DeepSeek.",
    )
    return parser.parse_args()


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def read_manifest(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    required = {"bib_key", "title", "year", "local_pdf"}
    missing = required.difference(rows[0].keys() if rows else set())
    if missing:
        raise ValueError(f"Manifest is missing columns: {', '.join(sorted(missing))}")
    return rows


def safe_stem(value: str) -> str:
    cleaned = re.sub(r"[^A-Za-z0-9_.-]+", "_", value.strip())
    return cleaned or "unnamed"


def locate_pdf(row: dict[str, str], pdf_root: Path, manifest_dir: Path) -> Path | None:
    candidates: list[Path] = []
    local_pdf = row.get("local_pdf", "").strip()
    if local_pdf:
        raw = Path(local_pdf)
        candidates.append(raw if raw.is_absolute() else manifest_dir / raw)
        candidates.append(pdf_root / raw.name)

    bib_key = row["bib_key"].strip()
    candidates.append(pdf_root / f"{bib_key}.pdf")
    for candidate in candidates:
        if candidate.is_file():
            return candidate.resolve()

    wanted = {f"{bib_key}.pdf".casefold()}
    if local_pdf:
        wanted.add(Path(local_pdf).name.casefold())
    for candidate in pdf_root.rglob("*.pdf"):
        if candidate.name.casefold() in wanted:
            return candidate.resolve()
    return None


def extract_pdf_pages(path: Path) -> list[PageText]:
    with path.open("rb") as handle:
        if handle.read(5) != b"%PDF-":
            raise ValueError("file does not start with a PDF header")
    reader = PdfReader(str(path), strict=False)
    if reader.is_encrypted:
        try:
            reader.decrypt("")
        except Exception as exc:  # pragma: no cover - depends on source file
            raise ValueError("encrypted PDF cannot be opened") from exc

    pages: list[PageText] = []
    for page_number, page in enumerate(reader.pages, start=1):
        try:
            text = page.extract_text() or ""
        except Exception:
            text = ""
        text = text.replace("\x00", "").strip()
        pages.append(PageText(page=page_number, text=text))
    return pages


def chunk_pages(pages: Iterable[PageText], max_chars: int) -> list[Chunk]:
    chunks: list[Chunk] = []
    current: list[PageText] = []
    current_chars = 0
    for page in pages:
        addition = len(page.text) + 24
        if current and current_chars + addition > max_chars:
            chunks.append(Chunk(tuple(current)))
            current = []
            current_chars = 0
        current.append(page)
        current_chars += addition
    if current:
        chunks.append(Chunk(tuple(current)))
    return chunks


def api_endpoint(base_url: str) -> str:
    base = base_url.rstrip("/")
    return base if base.endswith("/chat/completions") else base + "/chat/completions"


def call_deepseek(
    *,
    api_key: str,
    base_url: str,
    model: str,
    title: str,
    bib_key: str,
    chunk: Chunk,
    max_output_tokens: int,
    timeout: int,
    retries: int,
) -> tuple[dict[str, Any], dict[str, Any]]:
    user_prompt = (
        f"Paper key: {bib_key}\n"
        f"Paper title: {title}\n"
        f"PDF pages supplied: {chunk.first_page}-{chunk.last_page}\n\n"
        "Extract qualifying evidence from the following page-marked full text "
        "and return JSON.\n\n"
        f"{chunk.marked_text}"
    )
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt},
        ],
        "response_format": {"type": "json_object"},
        "thinking": {"type": "disabled"},
        "temperature": 0,
        "max_tokens": max_output_tokens,
    }
    request = urllib.request.Request(
        api_endpoint(base_url),
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
        method="POST",
    )

    last_error: Exception | None = None
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                api_result = json.loads(response.read().decode("utf-8"))
            choice = api_result["choices"][0]
            if choice.get("finish_reason") == "length":
                raise ValueError("DeepSeek output was truncated (finish_reason=length)")
            content = choice["message"].get("content")
            if not content or not content.strip():
                raise ValueError("DeepSeek returned empty JSON content")
            parsed = json.loads(strip_json_fence(content))
            usage = api_result.get("usage") or {}
            return parsed, usage
        except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError, KeyError, json.JSONDecodeError, ValueError) as exc:
            last_error = exc
            retryable = not isinstance(exc, urllib.error.HTTPError) or exc.code in {408, 409, 429, 500, 502, 503, 504}
            if attempt + 1 >= retries or not retryable:
                break
            time.sleep(min(2 ** attempt, 12))
    raise RuntimeError(f"DeepSeek request failed after {retries} attempts: {last_error}")


def strip_json_fence(content: str) -> str:
    content = content.strip()
    match = re.fullmatch(r"```(?:json)?\s*(.*?)\s*```", content, flags=re.DOTALL | re.IGNORECASE)
    return match.group(1) if match else content


def normalize_for_match(text: str) -> str:
    text = unicodedata.normalize("NFKC", text)
    text = text.replace("\u00ad", "")
    text = re.sub(r"(?<=\w)-\s+(?=\w)", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip().casefold()


def normalize_words_for_match(text: str) -> str:
    """Ignore PDF typography/citation markers while preserving lexical sequence."""
    text = normalize_for_match(text)
    text = re.sub(r"[^\w]+", " ", text, flags=re.UNICODE)
    tokens = [
        token
        for token in re.sub(r"\s+", " ", text).strip().split()
        if not token.isdigit() and token not in {"ref", "refs"}
    ]
    return " ".join(tokens)


def has_explicit_theory_outlook_marker(text: str) -> bool:
    patterns = [
        r"\bfuture\b",
        r"\bmore work\b",
        r"\bremain(?:s|ed)? (?:open|unknown|unclear|unexplored|to be)\b",
        r"\bneed(?:s|ed)? to\b",
        r"\bshould\b",
        r"\bcall(?:s|ed)? for\b",
        r"\bhelpful for improv(?:e|ing)\b",
        r"\b(?:improv|extend|revis|refin|integrat|challeng)(?:e|es|ed|ing)\b.{0,80}\b(?:theory|model|framework|construct)\b",
        r"\btheoretical implication(?:s)?\b",
    ]
    normalized = normalize_for_match(text)
    return any(re.search(pattern, normalized) for pattern in patterns)


def validate_items(
    parsed: dict[str, Any], chunk: Chunk
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    accepted: list[dict[str, Any]] = []
    rejected: list[dict[str, Any]] = []
    page_lookup = {p.page: p.text for p in chunk.pages}
    raw_items = parsed.get("items", [])
    if not isinstance(raw_items, list):
        return [], [{"reason": "items_is_not_a_list", "raw_item": raw_items}]

    for raw in raw_items:
        if not isinstance(raw, dict):
            rejected.append({"reason": "item_is_not_an_object", "raw_item": raw})
            continue
        item = dict(raw)
        category = item.get("category")
        quote = str(item.get("verbatim_quote", "")).strip()
        try:
            page = int(item.get("page"))
        except (TypeError, ValueError):
            page = -1

        reasons: list[str] = []
        if category not in CATEGORIES:
            reasons.append("invalid_category")
        if not quote:
            reasons.append("empty_quote")
        if page not in page_lookup:
            reasons.append("page_outside_chunk")
        elif quote:
            normalized_quote = normalize_for_match(quote)
            normalized_page = normalize_for_match(page_lookup[page])
            word_quote = normalize_words_for_match(quote)
            word_page = normalize_words_for_match(page_lookup[page])
            if normalized_quote in normalized_page:
                item["quote_verification_method"] = "normalized_exact"
            elif word_quote and word_quote in word_page:
                item["quote_verification_method"] = "exact_word_sequence_typography_normalized"
            else:
                reasons.append("quote_not_found_on_indicated_page")
        if category == "critique_of_prior_literature" and not str(item.get("target_of_critique", "")).strip():
            reasons.append("critique_target_missing")

        item["page"] = page
        item["section"] = str(item.get("section", "unknown")).strip() or "unknown"
        item["author_claim_cn"] = str(item.get("author_claim_cn", "")).strip()
        item["target_of_critique"] = str(item.get("target_of_critique", "")).strip()
        for field in [
            "outlook_type",
            "theory_or_construct_original_terms",
            "theory_source_or_citation",
            "analysis_level",
            "current_theoretical_limit_cn",
            "proposed_theoretical_move_cn",
            "relationship_or_prediction_to_test_cn",
            "methodological_detail_cn",
        ]:
            value = item.get(field, "")
            if isinstance(value, list):
                value = "; ".join(str(part) for part in value)
            item[field] = str(value).strip()
        method_only = item.get("method_only", False)
        item["method_only"] = method_only is True or str(method_only).strip().lower() == "true"

        if category in {"future_research_direction", "author_stated_theoretical_outlook"}:
            if item["outlook_type"] not in OUTLOOK_TYPES:
                reasons.append("invalid_or_missing_outlook_type")
        if category == "author_stated_theoretical_outlook":
            if item["method_only"]:
                reasons.append("theoretical_outlook_marked_method_only")
            if not item["theory_or_construct_original_terms"]:
                reasons.append("theory_or_construct_term_missing")
            if not item["proposed_theoretical_move_cn"]:
                reasons.append("proposed_theoretical_move_missing")
            if not has_explicit_theory_outlook_marker(quote):
                reasons.append("explicit_future_or_theory_change_marker_missing")
        if reasons:
            rejected.append({"reason": ";".join(reasons), "raw_item": item})
        else:
            item["quote_verified"] = True
            item.setdefault("quote_verification_method", "normalized_exact")
            accepted.append(item)
    return accepted, rejected


def deduplicate(items: Iterable[dict[str, Any]]) -> list[dict[str, Any]]:
    seen: set[tuple[str, str]] = set()
    result: list[dict[str, Any]] = []
    for item in items:
        identity = (item["category"], normalize_for_match(item["verbatim_quote"]))
        if identity in seen:
            continue
        seen.add(identity)
        result.append(item)
    return result


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def completed_result(path: Path) -> bool:
    if not path.is_file():
        return False
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return False
    return data.get("status") in {"processed", "processed_no_items"}


def revalidate_existing_rejections(existing: dict[str, Any]) -> tuple[dict[str, Any], int, int]:
    """Re-audit accepted items and recover typography-only rejects."""
    source_pdf = Path(str(existing.get("source_pdf", "")))
    old_rejections = existing.get("rejected_items", [])
    old_items = existing.get("items", [])
    if not source_pdf.is_file() or (not old_rejections and not old_items):
        return existing, 0, 0
    try:
        pages = {page.page: page for page in extract_pdf_pages(source_pdf)}
    except Exception:
        return existing, 0, 0

    retained: list[dict[str, Any]] = []
    demoted: list[dict[str, Any]] = []
    for item in old_items:
        try:
            page_number = int(item.get("page"))
        except (AttributeError, TypeError, ValueError):
            demoted.append({"reason": "invalid_existing_item", "raw_item": item})
            continue
        page = pages.get(page_number)
        if page is None:
            demoted.append({"reason": "page_outside_document", "raw_item": item})
            continue
        accepted, rejected = validate_items({"items": [item]}, Chunk((page,)))
        if accepted:
            retained.extend(accepted)
        else:
            demoted.append(rejected[0] if rejected else {"reason": "revalidation_failed", "raw_item": item})

    recovered: list[dict[str, Any]] = []
    remaining: list[dict[str, Any]] = []
    for rejection in [*old_rejections, *demoted]:
        raw_item = rejection.get("raw_item") if isinstance(rejection, dict) else None
        if not isinstance(raw_item, dict):
            remaining.append(rejection)
            continue
        try:
            page_number = int(raw_item.get("page"))
        except (TypeError, ValueError):
            remaining.append(rejection)
            continue
        page = pages.get(page_number)
        if page is None:
            remaining.append(rejection)
            continue
        accepted, rejected = validate_items({"items": [raw_item]}, Chunk((page,)))
        if accepted:
            recovered.extend(accepted)
        else:
            updated = dict(rejection)
            if rejected:
                updated["reason"] = rejected[0]["reason"]
            remaining.append(updated)

    if recovered:
        retained.extend(recovered)
    existing["items"] = deduplicate(retained)
    existing["rejected_items"] = remaining
    if recovered or demoted:
        existing["revalidated_at"] = utc_now()
    return existing, len(recovered), len(demoted)


def process_paper(
    row: dict[str, str], args: argparse.Namespace, api_key: str | None
) -> tuple[dict[str, Any], dict[str, Any] | None]:
    bib_key = row["bib_key"].strip()
    paper_file = args.output_dir / "papers" / f"{safe_stem(bib_key)}.json"
    if not args.force and completed_result(paper_file):
        existing = json.loads(paper_file.read_text(encoding="utf-8"))
        existing, recovered_count, demoted_count = revalidate_existing_rejections(existing)
        if recovered_count or demoted_count:
            write_json(paper_file, existing)
        return {
            "bib_key": bib_key,
            "title": row.get("title", ""),
            "status": "skipped_completed",
            "source_pdf": existing.get("source_pdf", ""),
            "accepted_count": len(existing.get("items", [])),
            "rejected_count": len(existing.get("rejected_items", [])),
            "detail": (
                f"existing result retained; {recovered_count} rejects recovered; {demoted_count} items demoted by current rules"
                if recovered_count or demoted_count
                else "existing verified result retained"
            ),
        }, existing

    pdf = locate_pdf(row, args.pdf_root, args.manifest.parent)
    if pdf is None:
        return {
            "bib_key": bib_key,
            "title": row.get("title", ""),
            "status": "missing_full_text",
            "source_pdf": "",
            "accepted_count": 0,
            "rejected_count": 0,
            "detail": f"declared local_pdf={row.get('local_pdf', '') or '[blank]'}",
        }, None

    try:
        pages = extract_pdf_pages(pdf)
    except Exception as exc:
        return {
            "bib_key": bib_key,
            "title": row.get("title", ""),
            "status": "invalid_pdf",
            "source_pdf": str(pdf),
            "accepted_count": 0,
            "rejected_count": 0,
            "detail": str(exc),
        }, None

    extractable_chars = sum(len(page.text.strip()) for page in pages)
    if extractable_chars < 200:
        return {
            "bib_key": bib_key,
            "title": row.get("title", ""),
            "status": "no_extractable_text",
            "source_pdf": str(pdf),
            "accepted_count": 0,
            "rejected_count": 0,
            "detail": f"only {extractable_chars} extracted characters; OCR may be required",
        }, None

    chunks = chunk_pages(pages, args.max_chars)
    if args.dry_run:
        return {
            "bib_key": bib_key,
            "title": row.get("title", ""),
            "status": "dry_run_ready",
            "source_pdf": str(pdf),
            "accepted_count": 0,
            "rejected_count": 0,
            "detail": f"{len(pages)} pages; {extractable_chars} characters; {len(chunks)} API chunks",
        }, None
    if not api_key:
        return {
            "bib_key": bib_key,
            "title": row.get("title", ""),
            "status": "api_key_missing",
            "source_pdf": str(pdf),
            "accepted_count": 0,
            "rejected_count": 0,
            "detail": f"set environment variable {args.api_key_env}",
        }, None

    accepted_all: list[dict[str, Any]] = []
    rejected_all: list[dict[str, Any]] = []
    usage_totals: dict[str, int] = {}
    chunk_log: list[dict[str, Any]] = []
    for index, chunk in enumerate(chunks, start=1):
        try:
            parsed, usage = call_deepseek(
                api_key=api_key,
                base_url=args.base_url,
                model=args.model,
                title=row.get("title", ""),
                bib_key=bib_key,
                chunk=chunk,
                max_output_tokens=args.max_output_tokens,
                timeout=args.timeout,
                retries=args.retries,
            )
            accepted, rejected = validate_items(parsed, chunk)
            accepted_all.extend(accepted)
            for item in rejected:
                item.update({"chunk": index, "pages": f"{chunk.first_page}-{chunk.last_page}"})
            rejected_all.extend(rejected)
            chunk_log.append(
                {
                    "chunk": index,
                    "pages": f"{chunk.first_page}-{chunk.last_page}",
                    "accepted": len(accepted),
                    "rejected": len(rejected),
                    "no_items_reason": parsed.get("no_items_reason", ""),
                }
            )
            for key, value in usage.items():
                if isinstance(value, int):
                    usage_totals[key] = usage_totals.get(key, 0) + value
        except Exception as exc:
            result = {
                "status": "api_error",
                "bib_key": bib_key,
                "title": row.get("title", ""),
                "source_pdf": str(pdf),
                "model": args.model,
                "processed_at": utc_now(),
                "failed_chunk": index,
                "failed_pages": f"{chunk.first_page}-{chunk.last_page}",
                "error": str(exc),
                "items": deduplicate(accepted_all),
                "rejected_items": rejected_all,
                "chunk_log": chunk_log,
                "usage": usage_totals,
            }
            write_json(paper_file, result)
            return {
                "bib_key": bib_key,
                "title": row.get("title", ""),
                "status": "api_error",
                "source_pdf": str(pdf),
                "accepted_count": len(result["items"]),
                "rejected_count": len(rejected_all),
                "detail": str(exc),
            }, result
        if args.sleep_seconds:
            time.sleep(args.sleep_seconds)

    accepted_all = deduplicate(accepted_all)
    result = {
        "status": "processed" if accepted_all else "processed_no_items",
        "bib_key": bib_key,
        "title": row.get("title", ""),
        "year": row.get("year", ""),
        "doi": row.get("doi", ""),
        "domain": row.get("domain", ""),
        "theory": row.get("theory", ""),
        "source_pdf": str(pdf),
        "model": args.model,
        "processed_at": utc_now(),
        "page_count": len(pages),
        "chunk_count": len(chunks),
        "items": accepted_all,
        "rejected_items": rejected_all,
        "chunk_log": chunk_log,
        "usage": usage_totals,
    }
    write_json(paper_file, result)
    return {
        "bib_key": bib_key,
        "title": row.get("title", ""),
        "status": result["status"],
        "source_pdf": str(pdf),
        "accepted_count": len(accepted_all),
        "rejected_count": len(rejected_all),
        "detail": f"{len(pages)} pages in {len(chunks)} chunks",
    }, result


def load_all_paper_results(output_dir: Path) -> list[dict[str, Any]]:
    results: list[dict[str, Any]] = []
    for path in sorted((output_dir / "papers").glob("*.json")):
        try:
            result = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        if result.get("status") in {"processed", "processed_no_items", "api_error"}:
            results.append(result)
    return results


def write_status_csv(path: Path, statuses: list[dict[str, Any]]) -> None:
    fields = [
        "bib_key",
        "title",
        "status",
        "source_pdf",
        "accepted_count",
        "rejected_count",
        "detail",
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(statuses)


def write_aggregate_csv(path: Path, paper_results: list[dict[str, Any]]) -> None:
    fields = [
        "bib_key",
        "title",
        "year",
        "doi",
        "domain",
        "theory",
        "category",
        "category_cn",
        "verbatim_quote",
        "page",
        "section",
        "author_claim_cn",
        "target_of_critique",
        "outlook_type",
        "theory_or_construct_original_terms",
        "theory_source_or_citation",
        "analysis_level",
        "current_theoretical_limit_cn",
        "proposed_theoretical_move_cn",
        "relationship_or_prediction_to_test_cn",
        "method_only",
        "methodological_detail_cn",
        "quote_verified",
        "quote_verification_method",
        "source_pdf",
        "model",
        "processed_at",
    ]
    rows: list[dict[str, Any]] = []
    for paper in paper_results:
        for item in paper.get("items", []):
            rows.append(
                {
                    **{key: paper.get(key, "") for key in ["bib_key", "title", "year", "doi", "domain", "theory"]},
                    **item,
                    "category_cn": CATEGORIES.get(item.get("category", ""), ""),
                    "source_pdf": paper.get("source_pdf", ""),
                    "model": paper.get("model", ""),
                    "processed_at": paper.get("processed_at", ""),
                }
            )
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def md_escape(text: Any) -> str:
    return str(text).replace("|", "\\|").strip()


def write_markdown(path: Path, paper_results: list[dict[str, Any]], statuses: list[dict[str, Any]]) -> None:
    lines = [
        "# Paper 3：作者原文 Gap、局限、未来方向与前文批评",
        "",
        f"生成时间（UTC）：{utc_now()}",
        "",
        "## 证据规则",
        "",
        "- 仅收录作者在全文中明确写出的内容。",
        "- 每条英文引文已由程序在对应 PDF 页内反向匹配。",
        "- 模型推断、无法定位的引文和类别不合格项均不进入本文件。",
        "- `processing_status.csv` 记录缺失全文、损坏 PDF、无可提取文本和 API 错误。",
        "",
        "## 全文处理覆盖",
        "",
        "| 状态 | 篇数 |",
        "|---|---:|",
    ]
    counts: dict[str, int] = {}
    for row in statuses:
        counts[row["status"]] = counts.get(row["status"], 0) + 1
    for status, count in sorted(counts.items()):
        lines.append(f"| {md_escape(status)} | {count} |")

    lines.extend(["", "## 理论展望优先索引", ""])
    theory_item_count = 0
    for paper in sorted(paper_results, key=lambda x: (str(x.get("year", "")), x.get("title", ""))):
        theory_items = [
            item
            for item in paper.get("items", [])
            if item.get("outlook_type") in THEORY_OUTLOOK_TYPES
            and item.get("category") in {"future_research_direction", "author_stated_theoretical_outlook"}
        ]
        if not theory_items:
            continue
        theory_item_count += len(theory_items)
        lines.extend([f"### {paper.get('bib_key', '')}: {paper.get('title', '')}", ""])
        for item in theory_items:
            lines.append(f"> {item['verbatim_quote']}")
            lines.append("")
            lines.append(f"- 类型：{item.get('outlook_type', '')}")
            lines.append(f"- 位置：PDF p. {item.get('page', '')}；section: {item.get('section', 'unknown')}")
            if item.get("theory_or_construct_original_terms"):
                lines.append(f"- 原始理论/构念：{item['theory_or_construct_original_terms']}")
            if item.get("current_theoretical_limit_cn"):
                lines.append(f"- 作者指出的理论不足：{item['current_theoretical_limit_cn']}")
            if item.get("proposed_theoretical_move_cn"):
                lines.append(f"- 作者提出的理论推进：{item['proposed_theoretical_move_cn']}")
            if item.get("relationship_or_prediction_to_test_cn"):
                lines.append(f"- 待检验关系/命题：{item['relationship_or_prediction_to_test_cn']}")
            lines.append("")
    if theory_item_count == 0:
        lines.append("当前已处理全文中没有通过原文校验的理论型展望。")

    lines.extend(["", "## 逐篇完整证据", ""])

    for paper in sorted(paper_results, key=lambda x: (str(x.get("year", "")), x.get("title", ""))):
        items = paper.get("items", [])
        if not items:
            continue
        lines.extend(
            [
                "",
                f"## {paper.get('bib_key', '')}: {paper.get('title', '')}",
                "",
                f"- Year: {paper.get('year', '')}",
                f"- DOI: {paper.get('doi', '') or '未记录'}",
                f"- Source PDF: `{paper.get('source_pdf', '')}`",
            ]
        )
        for category, category_cn in CATEGORIES.items():
            category_items = [item for item in items if item.get("category") == category]
            if not category_items:
                continue
            lines.extend(["", f"### {category_cn}", ""])
            for item in category_items:
                lines.append(f"> {item['verbatim_quote']}")
                lines.append("")
                lines.append(
                    f"- 位置：PDF p. {item['page']}；section: {item.get('section', 'unknown')}"
                )
                lines.append(f"- 忠实释义：{item.get('author_claim_cn', '')}")
                if item.get("target_of_critique"):
                    lines.append(f"- 批评对象：{item['target_of_critique']}")
                if item.get("outlook_type") and item.get("outlook_type") != "not_applicable":
                    lines.append(f"- 展望类型：{item['outlook_type']}")
                if item.get("theory_or_construct_original_terms"):
                    lines.append(f"- 原始理论/构念术语：{item['theory_or_construct_original_terms']}")
                if item.get("theory_source_or_citation"):
                    lines.append(f"- 文中理论来源：{item['theory_source_or_citation']}")
                if item.get("analysis_level"):
                    lines.append(f"- 分析层级：{item['analysis_level']}")
                if item.get("current_theoretical_limit_cn"):
                    lines.append(f"- 作者指出的理论不足：{item['current_theoretical_limit_cn']}")
                if item.get("proposed_theoretical_move_cn"):
                    lines.append(f"- 作者提出的理论推进：{item['proposed_theoretical_move_cn']}")
                if item.get("relationship_or_prediction_to_test_cn"):
                    lines.append(f"- 待检验关系/命题：{item['relationship_or_prediction_to_test_cn']}")
                if item.get("methodological_detail_cn"):
                    lines.append(f"- 方法性内容：{item['methodological_detail_cn']}")
                lines.append(f"- 原文校验：通过（{item.get('quote_verification_method', 'normalized_exact')}）")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_rejections(path: Path, paper_results: list[dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8") as handle:
        for paper in paper_results:
            for item in paper.get("rejected_items", []):
                payload = {
                    "bib_key": paper.get("bib_key", ""),
                    "title": paper.get("title", ""),
                    "source_pdf": paper.get("source_pdf", ""),
                    **item,
                }
                handle.write(json.dumps(payload, ensure_ascii=False) + "\n")


def main() -> int:
    args = parse_args()
    args.manifest = args.manifest.resolve()
    args.pdf_root = args.pdf_root.resolve()
    args.output_dir = args.output_dir.resolve()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir / "papers").mkdir(parents=True, exist_ok=True)

    rows = read_manifest(args.manifest)
    if args.keys:
        wanted = set(args.keys)
        rows = [row for row in rows if row["bib_key"] in wanted]
    if args.limit is not None:
        rows = rows[: args.limit]

    api_key = os.getenv(args.api_key_env)
    statuses: list[dict[str, Any]] = []
    for index, row in enumerate(rows, start=1):
        print(f"[{index}/{len(rows)}] {row['bib_key']}", flush=True)
        status, _ = process_paper(row, args, api_key)
        statuses.append(status)
        print(f"  -> {status['status']}: {status['detail']}", flush=True)

    write_status_csv(args.output_dir / "processing_status.csv", statuses)
    results = load_all_paper_results(args.output_dir)
    write_aggregate_csv(args.output_dir / "all_verified_items.csv", results)
    theory_results: list[dict[str, Any]] = []
    for paper in results:
        theory_paper = dict(paper)
        theory_paper["items"] = [
            item
            for item in paper.get("items", [])
            if item.get("outlook_type") in THEORY_OUTLOOK_TYPES
            and item.get("category") in {"future_research_direction", "author_stated_theoretical_outlook"}
        ]
        theory_results.append(theory_paper)
    write_aggregate_csv(args.output_dir / "theory_outlook_only.csv", theory_results)
    write_markdown(args.output_dir / "author_stated_gap_matrix.md", results, statuses)
    write_rejections(args.output_dir / "rejected_items.jsonl", results)

    print(f"Outputs: {args.output_dir}")
    print(f"Papers in this run: {len(statuses)}")
    print(f"Verified items in aggregate: {sum(len(p.get('items', [])) for p in results)}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except KeyboardInterrupt:
        print("Interrupted; completed paper JSON files remain resumable.", file=sys.stderr)
        raise SystemExit(130)
