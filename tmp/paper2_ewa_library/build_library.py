from __future__ import annotations

import csv
import html
import json
import re
from collections import defaultdict
from pathlib import Path


ROOT = Path(r"E:\Info_AI")
PAPER2_DIR = ROOT / "主Agent" / "文章项目" / "02_AI授权_EWA"
NAV_PATH = PAPER2_DIR / "Paper2_EWA_参考文献导航.md"
REF_DIR = ROOT / "defense_project" / "reference_materials"
COLLECTION_DIR = REF_DIR / "paper2_ewa"
PDF_DIR = REF_DIR / "papers_originals" / "paper2_ewa"
BIB_PATH = ROOT / "defense_project" / "latex" / "references.bib"
KG_DIR = REF_DIR / "knowledge_graph"
META_PATH = ROOT / "tmp" / "paper2_ewa_library" / "metadata.json"
SUMMARIES_PATH = ROOT / "tmp" / "paper2_ewa_library" / "summaries_zh.json"
PREEXISTING_PAPER2_BIB_KEYS = {
    "Dietvorst2015",
    "LeeSee2004",
    "Logg2019",
    "YinNgiamTanTeo2025",
}


CATEGORY_CONCEPT = {
    "反馈、绩效与激励": "feedback_performance_incentives",
    "算法建议与人机协作": "human_algorithm_collaboration",
    "动机性信念": "motivated_beliefs",
    "动态学习与 EWA": "dynamic_learning_ewa",
    "算法厌恶与欣赏": "algorithm_aversion_appreciation",
    "自利结果与公平判断": "self_interest_fairness_judgment",
    "信任与校准基础": "trust_calibration_foundations",
    "不可信 AI 与依赖后果": "untrustworthy_ai_reliance",
    "披露与治理": "disclosure_governance",
    "信任修复": "trust_repair",
    "AI 委托与责任": "ai_delegation_responsibility",
    "信任与使用的分离": "trust_use_separation",
    "绩效信息与透明度": "performance_information_transparency",
}


MANUAL_SOURCE_URLS = {
    "Brunnermeier2005": "https://www.princeton.edu/~markus/research/papers/optimal_expectations.pdf",
    "Camerer1999": "https://authors.library.caltech.edu/records/kgnbx-e2z22",
    "Choi2026": "https://www.repository.cam.ac.uk/bitstreams/2f8fdfda-15d7-48c4-afe5-330c8bd1c7e9/download",
    "Dietvorst2015": "https://repository.upenn.edu/handle/20.500.14332/43355",
    "Dietvorst2018": "https://repository.upenn.edu/handle/20.500.14332/39569",
    "Epley2004": "https://uploads-ssl.webflow.com/5c484e0f4aa6f839dc553c45/5c81a22c717955777e7351c9_EpleyCaruso2004.pdf",
    "Festinger1959": "https://web.mit.edu/curhan/www/docs/Articles/15341_Readings/Motivation/Festinger_Carlsmith_1959_Cognitive_consequences_of_forced_compliance.pdf",
    "Logg2019": "https://www.hbs.edu/ris/Publication%20Files/17-086_610956b6-7d91-4337-90cc-5bb5245316a8.pdf",
}


def normalize_doi(value: str) -> str:
    return value.strip().rstrip(".").replace("\\", "").lower()


def clean_text(value: str | None) -> str:
    if not value:
        return ""
    value = re.sub(r"<[^>]+>", " ", value)
    return re.sub(r"\s+", " ", html.unescape(value)).strip()


def paper_title(item: dict) -> str:
    oa = item.get("openalex") or {}
    return clean_text(item.get("normalized", {}).get("title") or oa.get("title"))


def paper_year(item: dict) -> str:
    oa = item.get("openalex") or {}
    value = item.get("normalized", {}).get("year") or oa.get("publication_year") or ""
    return str(value)


def crossref_authors(item: dict) -> list[str]:
    authors = []
    for author in (item.get("crossref") or {}).get("author") or []:
        family = clean_text(author.get("family"))
        given = clean_text(author.get("given"))
        name = f"{family}, {given}".strip().strip(",")
        if name:
            authors.append(name)
    if authors:
        return authors
    for authorship in (item.get("openalex") or {}).get("authorships") or []:
        name = clean_text((authorship.get("author") or {}).get("display_name"))
        if name:
            authors.append(name)
    return authors


def reference_years(item: dict) -> list[str]:
    values = []
    for citation in item.get("citations") or []:
        values.extend(re.findall(r"\((19\d{2}|20\d{2})\)", citation))
    return sorted(set(values))


def existing_bib() -> tuple[dict[str, str], set[str]]:
    raw = BIB_PATH.read_text(encoding="utf-8")
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
            by_doi[normalize_doi(doi_match.group(1))] = key
    return by_doi, keys


def bib_value(value: str) -> str:
    return value.replace("%", r"\%").replace("&", r"\&").replace("#", r"\#")


def bib_entry(item: dict) -> str:
    cr = item.get("crossref") or {}
    crossref_type = cr.get("type") or item.get("normalized", {}).get("type") or "journal-article"
    entry_type = {
        "journal-article": "article",
        "proceedings-article": "inproceedings",
        "book-chapter": "incollection",
        "book": "book",
        "report": "techreport",
    }.get(crossref_type, "misc")
    authors = " and ".join(crossref_authors(item))
    fields: list[tuple[str, str]] = [
        ("author", authors),
        ("title", paper_title(item)),
        ("year", paper_year(item)),
    ]
    container = clean_text(((cr.get("container-title") or [""])[0]))
    if entry_type == "article" and container:
        fields.append(("journal", container))
    elif container:
        fields.append(("booktitle", container))
    for source, target in (
        ("publisher", "publisher"),
        ("volume", "volume"),
        ("issue", "number"),
        ("page", "pages"),
    ):
        value = clean_text(cr.get(source))
        if value:
            if target == "pages":
                value = re.sub(r"(?<=\d)-(?=\d)", "--", value)
            fields.append((target, value))
    fields.extend(
        [
            ("doi", item["doi"]),
            ("url", f"https://doi.org/{item['doi']}"),
            ("note", "DOI metadata verified for the Paper 2 EWA linked library on 2026-08-03"),
        ]
    )
    body = "\n".join(f"  {name} = {{{bib_value(value)}}}," for name, value in fields if value)
    body = body.rstrip(",")
    return f"@{entry_type}{{{item['bib_key']},\n{body}\n}}"


def append_missing_bib(records: dict[str, dict]) -> int:
    by_doi, _ = existing_bib()
    missing = [item for doi, item in sorted(records.items()) if normalize_doi(doi) not in by_doi]
    if not missing:
        return 0
    marker = "% Paper 2 / EWA linked library — DOI metadata verified 2026-08-03"
    raw = BIB_PATH.read_text(encoding="utf-8").rstrip()
    addition = "\n\n" + marker + "\n" + "\n\n".join(bib_entry(item) for item in missing) + "\n"
    BIB_PATH.write_text(raw + addition, encoding="utf-8")
    return len(missing)


def update_source_markdown(records: dict[str, dict]) -> int:
    changed_files = 0
    for path in sorted(PAPER2_DIR.glob("*.md")):
        if path == NAV_PATH:
            continue
        lines = path.read_text(encoding="utf-8").splitlines()
        start = next(
            (index for index, line in enumerate(lines) if re.match(r"^##\s+(参考文献|References)\s*$", line)),
            None,
        )
        if start is None:
            continue
        changed = False
        for index in range(start + 1, len(lines)):
            match = re.search(r"https://doi\.org/([^\s]+)", lines[index], re.I)
            if not match:
                continue
            doi = normalize_doi(match.group(1))
            item = records.get(doi)
            if not item:
                continue
            key = item["bib_key"]
            local_pdf = PDF_DIR / f"{key}.pdf"
            summary_link = f"[中文总结](./{NAV_PATH.name}#{key.lower()})"
            if local_pdf.exists():
                original_link = f"[本地原文](../../../defense_project/reference_materials/papers_originals/paper2_ewa/{key}.pdf)"
            else:
                original_link = f"[官方原文](https://doi.org/{item['doi']})"
            base_line = lines[index].split(" · [中文总结]", 1)[0]
            new_line = f"{base_line} · {summary_link} · {original_link}"
            if new_line != lines[index]:
                lines[index] = new_line
                changed = True
        if changed:
            path.write_text("\n".join(lines) + "\n", encoding="utf-8")
            changed_files += 1
    return changed_files


def citation_locations(records: dict[str, dict]) -> dict[str, list[dict]]:
    result: dict[str, list[dict]] = defaultdict(list)
    for path in sorted(PAPER2_DIR.glob("*.md")):
        if path == NAV_PATH:
            continue
        for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            match = re.search(r"https://doi\.org/([^\s]+)", line, re.I)
            if not match:
                continue
            doi = normalize_doi(match.group(1))
            item = records.get(doi)
            if item:
                result[item["bib_key"]].append(
                    {"file": str(path.relative_to(ROOT)), "line": line_number}
                )
    return result


def make_navigation(records: dict[str, dict], summaries: dict[str, dict]) -> None:
    rows = sorted(records.values(), key=lambda item: item["bib_key"].lower())
    local_count = sum((PDF_DIR / f"{item['bib_key']}.pdf").exists() for item in rows)
    lines = [
        "# Paper 2 / EWA 参考文献导航",
        "",
        f"> 本页连接 Paper 2 文件夹中 5 份带参考文献目录的 Markdown。共 **{len(rows)}** 个唯一 DOI；**{local_count}** 篇已有可直接打开的本地 PDF，其余条目保留 DOI/出版社原文页。",
        ">",
        "> 使用方式：回到任一原 MD 的“参考文献”部分，点击“中文总结”跳到本页对应卡片；点击“本地原文”直接打开 PDF。没有开放 PDF 的条目会显示“官方原文”。",
        "",
        "## 快速索引",
        "",
        "| Key | 年份 | 文献 | 主题 | 原文状态 |",
        "|---|---:|---|---|---|",
    ]
    for item in rows:
        key = item["bib_key"]
        summary = summaries[key]
        local = (PDF_DIR / f"{key}.pdf").exists()
        status = "[本地 PDF](../../../defense_project/reference_materials/papers_originals/paper2_ewa/{0}.pdf)".format(key) if local else "[官方页](https://doi.org/{0})".format(item["doi"])
        lines.append(
            f"| [{key}](#{key.lower()}) | {paper_year(item)} | {paper_title(item)} | {summary['category']} | {status} |"
        )

    lines.extend(["", "## 文献卡片", ""])
    for item in rows:
        key = item["bib_key"]
        summary = summaries[key]
        local_path = PDF_DIR / f"{key}.pdf"
        authors = "; ".join(crossref_authors(item)) or "作者元数据待补"
        citation = item.get("citations", [""])[0]
        sources = "、".join(f"[{name}](./{name})" for name in sorted(set(item.get("source_files") or [])))
        official_year = paper_year(item)
        cited_years = reference_years(item)
        year_note = ""
        if cited_years and official_year and any(year != official_year for year in cited_years):
            year_note = f"\n- **版本年份提示**：当前 MD 出现 {', '.join(cited_years)}；Crossref/OpenAlex 当前出版元数据为 {official_year}。正文引用时应按采用的版本统一。"
        if local_path.exists():
            original = f"[打开本地 PDF](../../../defense_project/reference_materials/papers_originals/paper2_ewa/{key}.pdf)"
            source_url = (item.get("pdf") or {}).get("source_url") or MANUAL_SOURCE_URLS.get(key)
            if source_url:
                original += f" · [PDF 来源页]({source_url})"
            basis = "本地 PDF 已保存；当前中文卡片以论文摘要、元数据和项目引用语境为主，必要时可继续逐页精读。"
        else:
            original = f"[DOI / 出版社原文页](https://doi.org/{item['doi']})"
            has_abstract = bool(item.get("normalized", {}).get("abstract") or (item.get("openalex") or {}).get("abstract_inverted_index"))
            basis = "Crossref/OpenAlex 摘要与元数据。" if has_abstract else "题名、出版元数据及项目现有引用语境；尚未逐页核对全文。"
        lines.extend(
            [
                f"## {key}",
                "",
                f"**{paper_title(item)}**",
                "",
                f"- **作者 / 年份**：{authors} ({official_year})",
                f"- **主题**：{summary['category']}",
                f"- **总结**：{summary['summary']}",
                f"- **对 Paper 2 的作用与边界**：{summary['relevance']}",
                f"- **原文入口**：{original}",
                f"- **DOI**：[{item['doi']}](https://doi.org/{item['doi']})",
                f"- **出现于**：{sources}",
                f"- **总结依据**：{basis}{year_note}",
                "",
                f"> {citation}",
                "",
                "[返回快速索引](#快速索引)",
                "",
            ]
        )
    NAV_PATH.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def make_collection_files(records: dict[str, dict], summaries: dict[str, dict], added_bib: int) -> None:
    COLLECTION_DIR.mkdir(parents=True, exist_ok=True)
    rows = sorted(records.values(), key=lambda item: item["bib_key"].lower())
    batch_added_bib = sum(item["bib_key"] not in PREEXISTING_PAPER2_BIB_KEYS for item in rows)
    local_count = sum((PDF_DIR / f"{item['bib_key']}.pdf").exists() for item in rows)
    manifest_path = COLLECTION_DIR / "manifest.csv"
    with manifest_path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(
            [
                "bib_key",
                "title",
                "year",
                "doi",
                "category",
                "original_status",
                "local_pdf",
                "source_markdown",
                "reference_years",
            ]
        )
        for item in rows:
            key = item["bib_key"]
            local = PDF_DIR / f"{key}.pdf"
            writer.writerow(
                [
                    key,
                    paper_title(item),
                    paper_year(item),
                    item["doi"],
                    summaries[key]["category"],
                    "local_pdf" if local.exists() else "doi_only",
                    str(local.relative_to(REF_DIR)) if local.exists() else "",
                    "; ".join(sorted(set(item.get("source_files") or []))),
                    "; ".join(reference_years(item)),
                ]
            )
    readme = f"""# Paper 2 / EWA 文献子集合

本目录是共享文献库中的 Paper 2 可点击子集合，不是独立文献库。

- 唯一 DOI：{len(rows)}
- 本批新增到主 `references.bib`：{batch_added_bib}
- 已保存本地 PDF：{local_count}
- DOI/出版社页待获取 PDF：{len(rows) - local_count}

## 入口

- [中文总结与原文导航](../../../主Agent/文章项目/02_AI授权_EWA/Paper2_EWA_参考文献导航.md)
- [状态清单](./manifest.csv)
- [本地原文目录](../papers_originals/paper2_ewa/)
- [主 BibTeX](../../latex/references.bib)

`manifest.csv` 是本批次的机器可读状态表；原 MD 的每条参考文献已加入“中文总结”以及“本地原文/官方原文”链接。
"""
    (COLLECTION_DIR / "README.md").write_text(readme, encoding="utf-8")
    batch = f"""# Paper 2 / EWA 文献入库记录（2026-08-03）

- 扫描范围：`主Agent/文章项目/02_AI授权_EWA` 中 5 份含正式参考文献目录的 Markdown。
- 参考文献行：89；唯一 DOI：{len(rows)}。
- DOI 存在性与元数据：通过 DOI/Crossref/OpenAlex 核验；未发现不存在的 DOI。
- 主 BibTeX：新增 {batch_added_bib} 条；已有条目沿用原 key，避免重复。
- 原文：{local_count} 篇本地 PDF 已通过文件头与最小体积检查；其余 {len(rows) - local_count} 篇保留官方 DOI/出版社入口。
- 导航：每个原 MD 的参考文献条目均连接到中文卡片和原文入口。
- 知识图谱：新增条目已并入 `papers.json`、`papers.csv`、`categories.json` 与 `concepts.json`；原有共被引边不作推断性扩充。

注意：卡片是快速研究入口，不等于逐页精读笔记。没有本地 PDF 且缺少摘要的条目已明确标注“尚未逐页核对全文”。
"""
    (COLLECTION_DIR / "batch_2026-08-03_summary.md").write_text(batch, encoding="utf-8")


def append_section(path: Path, marker: str, content: str) -> None:
    raw = path.read_text(encoding="utf-8")
    if marker in raw:
        return
    path.write_text(raw.rstrip() + "\n\n" + content.strip() + "\n", encoding="utf-8")


def update_library_docs(records: dict[str, dict]) -> None:
    local_count = sum((PDF_DIR / f"{item['bib_key']}.pdf").exists() for item in records.values())
    bib_count = len(re.findall(r"(?m)^@\w+\{", BIB_PATH.read_text(encoding="utf-8")))
    all_pdf_count = len(list((REF_DIR / "papers_originals").rglob("*.pdf")))

    readme_path = REF_DIR / "README.md"
    raw = readme_path.read_text(encoding="utf-8")
    marker = "### Paper 2 / EWA 可点击子集合（2026-08-03）"
    if marker not in raw:
        section = f"""### Paper 2 / EWA 可点击子集合（2026-08-03）

- [中文总结与原文导航](../../主Agent/文章项目/02_AI授权_EWA/Paper2_EWA_参考文献导航.md)
- [批次状态清单](./paper2_ewa/manifest.csv)
- [批次入库记录](./paper2_ewa/batch_2026-08-03_summary.md)
- [本地 PDF 目录](./papers_originals/paper2_ewa/)

本批覆盖 50 个唯一 DOI，{local_count} 篇已有本地 PDF，其余条目保留 DOI/出版社入口。原 Paper 2 Markdown 的参考文献行已可直接跳转到中文卡片与原文。

---

"""
        raw = raw.replace("## 二、入库流程", section + "## 二、入库流程", 1)
    raw = re.sub(r"\| `references\.bib` 条目总数 \| \*\*\d+\*\*[^\n]*", f"| `references.bib` 条目总数 | **{bib_count}** |", raw)
    raw = re.sub(r"\| 已下载 PDF \| \*\*\d+\*\*[^\n]*", f"| 已下载 PDF | **{all_pdf_count}** |", raw)
    readme_path.write_text(raw, encoding="utf-8")

    append_section(
        REF_DIR / "to_collect.md",
        "## Paper 2 / EWA 批次（2026-08-03）",
        f"""## Paper 2 / EWA 批次（2026-08-03）

- 唯一 DOI：{len(records)}
- 已保存本地 PDF：{local_count}
- 尚无本地 PDF、保留 DOI/出版社入口：{len(records) - local_count}
- 逐条状态：[paper2_ewa/manifest.csv](./paper2_ewa/manifest.csv)
""",
    )
    append_section(
        REF_DIR / "verified_links.md",
        "## Paper 2 / EWA DOI 核验（2026-08-03）",
        """## Paper 2 / EWA DOI 核验（2026-08-03）

50 个唯一 DOI 均由 DOI/Crossref/OpenAlex 元数据确认存在。逐条 DOI、题名、出版年份、本地 PDF 状态及来源 Markdown 见 [paper2_ewa/manifest.csv](./paper2_ewa/manifest.csv)。

部分 INFORMS 文献在项目旧稿中使用 online-first 年份，而 Crossref 当前使用卷期出版年份；导航卡片已逐条提示，不自动改写正文年份。
""",
    )


def update_knowledge_graph(records: dict[str, dict], summaries: dict[str, dict]) -> None:
    locations = citation_locations(records)
    papers_path = KG_DIR / "papers.json"
    papers_data = json.loads(papers_path.read_text(encoding="utf-8"))
    existing = {paper["key"]: paper for paper in papers_data["papers"]}

    for item in sorted(records.values(), key=lambda value: value["bib_key"].lower()):
        key = item["bib_key"]
        cr = item.get("crossref") or {}
        authors = crossref_authors(item)
        concept = CATEGORY_CONCEPT[summaries[key]["category"]]
        local = PDF_DIR / f"{key}.pdf"
        if key in existing:
            paper = existing[key]
            paper["has_pdf"] = local.exists()
            for value in ("paper2_ewa", concept):
                if value not in paper.setdefault("concepts", []):
                    paper["concepts"].append(value)
            seen = {(entry.get("file"), entry.get("line")) for entry in paper.setdefault("cited_in", [])}
            for entry in locations.get(key, []):
                if (entry["file"], entry["line"]) not in seen:
                    paper["cited_in"].append(entry)
            continue
        crossref_type = cr.get("type") or "journal-article"
        entry_type = {
            "journal-article": "article",
            "proceedings-article": "inproceedings",
            "book-chapter": "incollection",
            "book": "book",
            "report": "techreport",
        }.get(crossref_type, "misc")
        journal = clean_text(((cr.get("container-title") or [""])[0])) if entry_type == "article" else ""
        booktitle = clean_text(((cr.get("container-title") or [""])[0])) if entry_type != "article" else ""
        pages = clean_text(cr.get("page"))
        pages = re.sub(r"(?<=\d)-(?=\d)", "--", pages)
        paper = {
            "key": key,
            "type": entry_type,
            "title": paper_title(item),
            "authors": authors,
            "authors_raw": " and ".join(authors),
            "year": paper_year(item),
            "journal": journal,
            "booktitle": booktitle,
            "publisher": clean_text(cr.get("publisher")),
            "volume": clean_text(cr.get("volume")),
            "number": clean_text(cr.get("issue")),
            "pages": pages,
            "doi": item["doi"],
            "eprint": "",
            "url": f"https://doi.org/{item['doi']}",
            "note": "Paper 2 EWA linked library; DOI metadata verified 2026-08-03",
            "venue": journal or booktitle or clean_text(cr.get("publisher")),
            "category": "paper2_ewa",
            "concepts": ["paper2_ewa", concept],
            "has_pdf": local.exists(),
            "cited_in": locations.get(key, []),
        }
        papers_data["papers"].append(paper)
        existing[key] = paper

    papers_data["papers"].sort(key=lambda paper: (str(paper.get("year", "")), paper["key"]))
    papers_data["paper_count"] = len(papers_data["papers"])
    papers_data["generated_at"] = "2026-08-03"
    papers_data["categories"] = sorted(set(paper.get("category", "uncategorized") for paper in papers_data["papers"]))
    papers_path.write_text(json.dumps(papers_data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    category_path = KG_DIR / "categories.json"
    category_data = json.loads(category_path.read_text(encoding="utf-8"))
    category_data["generated_at"] = "2026-08-03"
    category_data["category_to_papers"]["paper2_ewa"] = sorted(item["bib_key"] for item in records.values())
    category_data["category_descriptions"]["paper2_ewa"] = "Paper 2 AI reliance, trust calibration, EWA, motivated beliefs, incentives, disclosure, and delegation"
    category_data["category_count"] = len(category_data["category_to_papers"])
    category_path.write_text(json.dumps(category_data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    concepts_path = KG_DIR / "concepts.json"
    concepts_data = json.loads(concepts_path.read_text(encoding="utf-8"))
    concepts_data["generated_at"] = "2026-08-03"
    concept_map = concepts_data["concept_to_papers"]
    concept_map["paper2_ewa"] = sorted(item["bib_key"] for item in records.values())
    for item in records.values():
        concept = CATEGORY_CONCEPT[summaries[item["bib_key"]]["category"]]
        values = set(concept_map.get(concept, []))
        values.add(item["bib_key"])
        concept_map[concept] = sorted(values)
    concepts_data["concept_groups"]["paper2_ewa"] = ["paper2_ewa"] + sorted(set(CATEGORY_CONCEPT.values()))
    concepts_data["concept_count"] = len(concept_map)
    concepts_path.write_text(json.dumps(concepts_data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    csv_path = KG_DIR / "papers.csv"
    with csv_path.open("w", encoding="utf-8-sig", newline="") as handle:
        fields = [
            "key", "type", "title", "first_author", "all_authors", "year", "venue", "volume", "number", "pages", "doi", "eprint", "category", "concepts", "has_pdf", "pdf_path", "cited_count"
        ]
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for paper in papers_data["papers"]:
            key = paper["key"]
            local = PDF_DIR / f"{key}.pdf"
            authors = paper.get("authors") or []
            writer.writerow(
                {
                    "key": key,
                    "type": paper.get("type", ""),
                    "title": paper.get("title", ""),
                    "first_author": authors[0] if authors else "",
                    "all_authors": "; ".join(authors),
                    "year": paper.get("year", ""),
                    "venue": paper.get("venue", ""),
                    "volume": paper.get("volume", ""),
                    "number": paper.get("number", ""),
                    "pages": paper.get("pages", ""),
                    "doi": paper.get("doi", ""),
                    "eprint": paper.get("eprint", ""),
                    "category": paper.get("category", ""),
                    "concepts": "; ".join(paper.get("concepts") or []),
                    "has_pdf": str(bool(paper.get("has_pdf"))).lower(),
                    "pdf_path": str(local.relative_to(ROOT)) if local.exists() else "",
                    "cited_count": len(paper.get("cited_in") or []),
                }
            )

    paper_count = papers_data["paper_count"]
    concept_count = concepts_data["concept_count"]
    category_count = category_data["category_count"]
    for name in ("README.md", "README_RUN.md"):
        path = KG_DIR / name
        raw = path.read_text(encoding="utf-8")
        raw = re.sub(r"\b120 篇\b", f"{paper_count} 篇", raw)
        raw = re.sub(r"\b302 个概念\b", f"{concept_count} 个概念", raw)
        raw = re.sub(r"\b15 个(?:主)?类别\b", f"{category_count} 个主类别", raw)
        raw = re.sub(r"\b15 类别\b", f"{category_count} 类别", raw)
        raw = re.sub(r"完整元数据（\d+ 篇）", f"完整元数据（{paper_count} 篇）", raw)
        raw = re.sub(r"概念 → 论文映射（\d+ 个概念）", f"概念 → 论文映射（{concept_count} 个概念）", raw)
        raw = re.sub(r"类别 → 论文映射（\d+ 个类别）", f"类别 → 论文映射（{category_count} 个类别）", raw)
        path.write_text(raw, encoding="utf-8")


def main() -> None:
    records = json.loads(META_PATH.read_text(encoding="utf-8"))
    summaries = json.loads(SUMMARIES_PATH.read_text(encoding="utf-8"))
    for item in records.values():
        key = item["bib_key"]
        local = PDF_DIR / f"{key}.pdf"
        if local.exists():
            item["pdf"] = {
                **(item.get("pdf") or {}),
                "status": "existing",
                "path": str(local),
                "bytes": local.stat().st_size,
                "source_url": (item.get("pdf") or {}).get("source_url") or MANUAL_SOURCE_URLS.get(key, ""),
            }
        else:
            item["pdf"] = {
                **(item.get("pdf") or {}),
                "status": "not_downloaded",
                "path": "",
                "bytes": 0,
                "source_url": "",
            }
    META_PATH.write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding="utf-8")

    added_bib = append_missing_bib(records)
    changed_md = update_source_markdown(records)
    make_navigation(records, summaries)
    make_collection_files(records, summaries, added_bib)
    update_library_docs(records)
    update_knowledge_graph(records, summaries)
    print(f"Added BibTeX entries: {added_bib}")
    print(f"Updated source Markdown files: {changed_md}")
    print(f"Navigation: {NAV_PATH}")


if __name__ == "__main__":
    main()
