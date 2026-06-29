# Knowledge Graph Artifacts

> Generated: 2026-06-30
> Purpose: 供其他 agent 直接消费，无需重新解析 LaTeX 或 bib 文件即可构建知识图谱。

---

## 文件清单

| 文件 | 格式 | 内容 |
|------|------|------|
| `papers.json` | JSON | 完整元数据（68 篇），包含 title / authors / year / venue / DOI / category / concepts / has_pdf / cited_in |
| `papers.csv` | CSV | 扁平表格（pandas/spreadsheet 直接可读），18 列 |
| `concepts.json` | JSON | 概念 → 论文映射（184 个概念）+ 概念分组 |
| `categories.json` | JSON | 类别 → 论文映射（10 个类别）+ 类别描述 |
| `citations_in_thesis.csv` | CSV | 论文 → 引用位置（tex 文件 + 行号）|
| `edges_cocitation.csv` | CSV | 共被引边（在同一 `\cite{a,b,c}` 中出现的论文对）|

---

## Schema (papers.json)

每篇论文包含以下字段：

```json
{
  "key": "KamenicaGentzkow2011",          // bib key (唯一标识)
  "type": "article",                      // @article / @inproceedings / @book / @misc
  "title": "Bayesian Persuasion",
  "authors": ["Kamenica, Emir", "Gentzkow, Matthew"],   // 解析后的数组
  "authors_raw": "Kamenica, Emir and Gentzkow, Matthew", // bib 原始字符串
  "year": "2011",
  "venue": "American Economic Review",    // journal 或 booktitle 或 publisher
  "volume": "101",
  "number": "6",
  "pages": "2590--2615",
  "doi": "10.1257/aer.101.6.2590",
  "eprint": "",                            // arXiv ID（如果有）
  "url": "",
  "note": "...",                           // 人工注释（核查状态、入库批次等）
  "category": "foundational_theory",       // 见 categories.json
  "concepts": ["bayesian_persuasion", ...], // 见 concepts.json
  "has_pdf": true,                         // 是否已下载 PDF
  "pdf_path": "defense_project/.../KamenicaGentzkow2011.pdf",
  "pdf_size_kb": 1234,
  "cited_in": [                            // 在 thesis 的 .tex 中被引用的位置
    {"file": "defense_project/latex/sections/01_intro_lit_review.tex", "line": 17}
  ]
}
```

---

## Schema (concepts.json)

```json
{
  "concept_to_papers": {
    "bayesian_persuasion": ["KamenicaGentzkow2011", "AlonsoCamara2016", ...],
    "algorithm_aversion": ["Dietvorst2015", "PrahlVanSwol2017", ...],
    ...
  },
  "concept_groups": {
    "bayesian": ["bayesian_persuasion"],
    "algorithm": ["algorithm_aversion", "algorithm_appreciation"],
    ...
  }
}
```

**约定**：concept 命名用 snake_case；分组按首词（`bayesian_persuasion` → 组 `bayesian`）。

---

## Schema (categories.json)

10 个主类别：

- `foundational_theory` — Bayesian persuasion / information design / rational inattention
- `information_acquisition` — sequential sampling, belief updating
- `algorithms_trust_hci` — algorithm aversion, CASA, anthropomorphism
- `recommender_genai` — recommenders, transformers, LLMs, RLHF
- `narrative_epistemic` — narrative persuasion, epistemic agency
- `advice_taking` — judge-advisor paradigm (2026-06-29 batch)
- `self_serving_attribution` — self-serving bias (2026-06-29 batch)
- `overconfidence_control` — overconfidence, illusion of control (2026-06-29 batch)
- `algorithm_aversion` — AI resistance mechanisms (2026-06-29 batch)
- `newly_added_candidates` — background references

---

## 推荐的知识图谱构建方式

### 节点（Node）

1. **Paper 节点** — `key` 为唯一 ID，属性来自 papers.json
2. **Author 节点** — 从 `authors` 数组构造，节点属性：name, papers
3. **Concept 节点** — 从 `concepts.json.concept_to_papers` 的 keys 构造，属性：name, paper_count
4. **Category 节点** — 从 `categories.json.category_to_papers` 的 keys 构造
5. **Year 节点**（可选）— 时间维度
6. **Venue 节点**（可选）— 期刊/会议维度

### 边（Edge）

| 关系类型 | 来源字段 | 目标 |
|----------|----------|------|
| AUTHORED | papers.authors[i] | Paper.key |
| COVERS_CONCEPT | papers.concepts[i] | Concept |
| IN_CATEGORY | papers.category | Category |
| PUBLISHED_IN | papers.venue | Venue（可选）|
| PUBLISHED_YEAR | papers.year | Year（可选）|
| CITED_IN_FILE | papers.cited_in | .tex file |
| COCITED_WITH | edges_cocitation.csv | Paper |

### Cypher 示例（Neo4j）

```cypher
// 1. 载入论文
LOAD CSV WITH HEADERS FROM 'file:///papers.csv' AS row
CREATE (:Paper {
  key: row.key,
  title: row.title,
  year: toInteger(row.year),
  doi: row.doi,
  category: row.category,
  has_pdf: row.has_pdf = 'True'
});

// 2. 载入作者关系
LOAD CSV WITH HEADERS FROM 'file:///papers.csv' AS row
WITH row, split(row.all_authors, ';') AS authors
UNWIND authors AS author
MATCH (p:Paper {key: row.key})
MATCH (a:Author {name: trim(author)})
MERGE (a)-[:AUTHORED]->(p);

// 3. 载入概念关系（用 papers.json 更方便）
// 详见 ingest_concepts.py

// 4. 查询：算法厌恶相关论文 + 引用了它们的章节
MATCH (p:Paper)-[:COVERS_CONCEPT]->(c:Concept)
WHERE c.name CONTAINS 'algorithm_aversion'
MATCH (p)-[:CITED_IN_FILE]->(f)
RETURN p.title, c.name, f;
```

---

## 重新生成脚本

如果 references.bib 改了，跑：

```bash
PYTHONIOENCODING=utf-8 py -3 e:/Info_AI/export_bib.py
```

脚本会覆盖 knowledge_graph/ 下所有 artifacts。

---

## 数据完整性

- ✅ 68 篇全部有 title / year / authors（部分无 venue / volume / pages 是 bib 本身缺）
- ✅ 9 篇已下载 PDF（位于 `../papers_originals/<category>/<key>.pdf`）
- ✅ 184 个概念标签（来自 to_collect.md、user-provided summaries、人工补充）
- ✅ 29 篇在 thesis 中被实际引用（citations_in_thesis.csv）
- ⚠️ Bailey2022 未入 bib（作者/年份不全，待用户补全）

---

## 已知限制

1. **概念标签是手写的**：来自用户提供的综述文档 + 知识补充；新文献需要手动加 concept。
2. **共被引边**只反映 thesis 内部 `\cite{a,b,c}` 共现，不反映外部文献中的引用关系。
3. **PDF 路径** 用 POSIX 风格（`/` 分隔），Windows 工具读时注意转换。
4. **Author 节点** 没有去重——`Kamenica, Emir` 和 `Kamenica, E.` 会被当成两个作者。需要做 author disambiguation 时再处理。