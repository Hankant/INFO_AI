# Knowledge Graph Data Integrity Report

**Generated:** 2026-06-30
**Scope:** `e:\Info_AI\defense_project\reference_materials\knowledge_graph\`
**Files inspected:** `papers.json`, `concepts.json`, `categories.json`, `edges_cocitation.csv`
**Verdict:** PASS with minor cleanup items (1 paper missing concepts, 7 duplicate cocitation edges).

---

## 1. Executive Summary

| Metric | Value |
|---|---|
| Total papers (`papers.json`) | **68** |
| Papers with `has_pdf: true` | **10** (14.7%) |
| Papers with `has_pdf: false` | 58 (85.3%) |
| Categories in `category_to_papers` | **10** (matches expected) |
| Average concepts per paper | **2.96** (min 0, max 4) |
| Papers missing required fields | **0** |
| Papers with empty title / year / category | **0** |
| Concepts in `concept_to_papers` | **184** |
| Concept groups | **129** |
| Orphan concepts (in papers, missing from concepts.json) | **0** |
| Dead concepts (in concepts.json, no paper) | **0** |
| Cocitation edge rows | **23** |
| Broken cocitation references | **0** |
| Self-loops in cocitation | **0** |
| Duplicate cocitation pairs | **7** |
| Categories used in papers not in declared set | **0** |

Overall the dataset is **structurally consistent** and ready for the HTML viewer.

---

## 2. `papers.json`

### 2.1 Counts

- **Total papers:** 68 (matches `paper_count` in JSON header)
- **`has_pdf: true`:** 10 papers
  - `Vaswani2017`, `Brown2020`, `Ouyang2022`, `Bender2021`, `QiPan2026`, `BommasaniEtAl2021`, `HicksHumphriesSlater2024`, `Shanahan2024`, `PrahlVanSwol2017`, `VodrahalliEtAl2021`
- **`has_pdf: false`:** 58 papers

NOTE: README claims "9 PDFs"; actual count is **10** (`VodrahalliEtAl2021` is the extra). README is stale.

### 2.2 Categories used (10/10)

| Category | Papers |
|---|---:|
| `newly_added_candidates` | 13 |
| `algorithms_trust_hci` | 12 |
| `recommender_genai` | 11 |
| `information_acquisition` | 7 |
| `self_serving_attribution` | 6 |
| `advice_taking` | 5 |
| `overconfidence_control` | 5 |
| `foundational_theory` | 4 |
| `narrative_epistemic` | 3 |
| `algorithm_aversion` | 2 |
| **Total** | **68** |

All 10 categories are used. Every paper's `category` value matches one of the declared 10.

### 2.3 Concepts per paper

- **Average:** 2.96
- **Min:** 0 (`deClippelZhang2020` — the 2020 working paper version; the published 2022 version has its own entry with concepts)
- **Max:** 4 (`HicksHumphriesSlater2024`, `Brown2020`, `Ouyang2022`, `PuringtonEtAl2017`, `Bender2021`, `Vaswani2017`, `Shanahan2024`, etc.)

### 2.4 Missing / empty fields

No paper is missing any of the required fields (`key`, `type`, `title`, `authors`, `year`, `venue`, `category`, `concepts`, `has_pdf`, `cited_in`).

No paper has an empty title, year, or category.

### 2.5 Issues

| Severity | Issue | Detail |
|---|---|---|
| **Minor** | `deClippelZhang2020` has empty `concepts: []` | Working paper version. Concepts (`non_bayesian_persuasion`, `distortion_function`, `signal_design`) exist on `deClippelZhang2022` (the published version). Either populate or accept as a deliberate duplicate stub. |
| **Minor** | Several `venue` and `booktitle` fields are empty strings | Expected for preprints / unpublished types — not a bug. |
| **Minor** | `AlonsoCamara2016` author rendering shows `["Alonso, Ricardo", "C{\\^a"]` (LaTeX escape truncated) | Bib parsing issue — author name was cut off after `\^`. Same problem appears in `authors_raw`. Viewer should render the raw string and tolerate LaTeX escapes. |
| **Minor** | `PuringtonEtAl2017` title rendered as `"{``Alexa Is My New BFF''"` | Bib source has stray quote/brace characters. Viewer should display the raw title or apply light cleanup. |
| **Minor** | `GuzmanLewis2020` venue contains `New Media \\& Society` (LaTeX-escaped `&`) | Display layer should unescape. |
| **Info** | DOI / `pdf_size_kb` fields occasionally missing or `""` | Acceptable for preprints / unpublished entries. |

---

## 3. `concepts.json`

### 3.1 Counts

- **Total concepts in `concept_to_papers`:** 184 (matches `concept_count` in header)
- **Total concept groups:** 129
- **Concepts referenced across `papers.json`:** 184
- **Orphans (in papers, missing from concepts.json):** 0
- **Dead (in concepts.json, never used):** 0
- **Concepts in groups but not in `concept_to_papers`:** 0
- **Concepts in `concept_to_papers` but not in any group:** 0

All 184 concepts are bidirectionally consistent between papers and concept index.

### 3.2 Concept groups (129)

Group names (used as the first-token grouping convention):

`AI`, `Alexa`, `CASA`, `ChatGPT`, `GPT`, `HCI`, `InstructGPT`, `LLM`, `NLG`, `RLHF`, `Science`, `achievement`, `activation`, `adaptive`, `advice`, `advisor`, `algorithm`, `algorithmic`, `anthropomorphism`, `appropriate`, `attention`, `attitude`, `attribution`, `automation`, `averaging`, `bayes`, `bayesian`, `behavioral`, `belief`, `better`, `betting`, `biased`, `bullshit`, `calibration`, `choice`, `closed`, `cognitive`, `collaborative`, `confirmation`, `confirmatory`, `conservatism`, `control`, `correlation`, `costly`, `decision`, `defensive`, `distortion`, `egocentric`, `emergence`, `entropy`, `epistemic`, `exposure`, `facebook`, `factuality`, `few`, `filter`, `first`, `forecast`, `foundation`, `freezing`, `hallucination`, `heterogeneous`, `homogenization`, `human`, `ideological`, `illusion`, `in`, `inattention`, `individual`, `information`, `instruction`, `intentionality`, `intuitive`, `judge`, `judgment`, `knowledge`, `language`, `linguistic`, `locus`, `media`, `medical`, `meta`, `mind`, `mindlessness`, `motivated`, `narrative`, `next`, `non`, `optimal`, `overconfidence`, `overestimation`, `overplacement`, `overprecision`, `perceived`, `personalization`, `personification`, `persuasion`, `philosophy`, `positivity`, `posterior`, `prediction`, `prior`, `probabilistic`, `rational`, `recommender`, `representativeness`, `responsibility`, `revealed`, `review`, `role`, `self`, `signal`, `simple`, `smart`, `social`, `source`, `stochastic`, `subjective`, `success`, `task`, `three`, `transfer`, `transformer`, `trust`, `unified`, `uniqueness`, `urn`, `weight`, `wisdom`.

### 3.3 Issues

None. Concept-to-paper mapping is internally consistent and exactly matches the concepts used in `papers.json`.

---

## 4. `categories.json`

### 4.1 Counts

- **Categories in `category_to_papers`:** 10 (matches expected)
- **Categories declared at top level (`categories` array):** 10 — same set, alphabetical order.
- **Categories used in papers:** 10 — same set.

### 4.2 Full category list (10)

1. `advice_taking` — 5 papers
2. `algorithm_aversion` — 2 papers
3. `algorithms_trust_hci` — 12 papers
4. `foundational_theory` — 4 papers
5. `information_acquisition` — 7 papers
6. `narrative_epistemic` — 3 papers
7. `newly_added_candidates` — 13 papers
8. `overconfidence_control` — 5 papers
9. `recommender_genai` — 11 papers
10. `self_serving_attribution` — 6 papers

### 4.3 Cross-check

For each category, the set of paper keys in `category_to_papers` was compared against the set of paper keys whose `category` field matches. No mismatches were found.

### 4.4 Issues

None. Every paper's `category` resolves to one of the 10 declared categories.

---

## 5. `edges_cocitation.csv`

### 5.1 Counts

- **Rows (excluding header):** 23
- **Unique undirected pairs:** 16 (7 are duplicates — see below)
- **Self-loops:** 0
- **Broken references (source or target not in `papers.json`):** 0
- **Distinct tex files referenced:** 1 — `defense_project\latex\sections\01_intro_lit_review.tex` (all 23 rows)

### 5.2 Duplicate cocitation pairs (7)

The same paper pair appears in two different `\cite{...}` groups within the same file. Either intentional (the pair was co-cited in two paragraphs) or a deduplication opportunity.

| Pair | Occurrences |
|---|---:|
| `AdomaviciusTuzhilin2005` ↔ `ResnickVarian1997` | 2 (lines 19, 89) |
| `Bozdag2013` ↔ `ResnickVarian1997` | 2 (lines 19, 89) |
| `AdomaviciusTuzhilin2005` ↔ `Bozdag2013` | 2 (lines 19, 89) |
| `Brown2020` ↔ `Vaswani2017` | 2 (lines 21, 91) |
| `Ouyang2022` ↔ `Vaswani2017` | 2 (lines 21, 91) |
| `Brown2020` ↔ `Ouyang2022` | 2 (lines 21, 91) |
| `NassMoon2000` ↔ `ReevesNass1996` | 2 (lines 77, 97) |

All duplicates are intra-file and reflect the same conceptual cluster being co-cited in two paragraphs (recommender trio and CASA pair). This is a **legitimate repeated co-citation** but the CSV should be either:
- Deduplicated by (source, target) pair to avoid double-counting edge weight, or
- Kept as-is and have a `weight` column aggregated by the viewer.

### 5.3 Issues

None blocking. Both reference endpoints exist in `papers.json`.

---

## 6. Cross-file Consistency

| Check | Result |
|---|---|
| Every `papers.json` category is in `categories.json` | PASS |
| Every `categories.json` category has at least one paper | PASS |
| Every concept referenced in a paper is in `concepts.json` | PASS (0 orphans) |
| Every concept in `concepts.json` is used by at least one paper | PASS (0 dead) |
| Every concept group contains only known concepts | PASS |
| Every cocitation `source_key` / `target_key` is a known paper | PASS |

---

## 7. Recommendations for Cleanup

### Required before viewer ships
None — the data is structurally valid.

### Recommended (low effort, improves UX)

1. **Populate concepts on `deClippelZhang2020`** (or drop the entry if the 2022 published version supersedes it). It currently has `concepts: []`, so any concept-level search will miss it.

2. **Deduplicate `edges_cocitation.csv`** by (source_key, target_key) pair, OR add a `weight` column aggregating occurrences so the viewer can render thicker edges for repeatedly co-cited pairs. Right now the same edge appears twice and a naive viewer will render two parallel lines.

3. **Unescape LaTeX sequences** in display layer (or sanitize at ingest) for:
   - `AlonsoCamara2016` — `C{\\^a` (should be `Câmara` or similar)
   - `GuzmanLewis2020` — `New Media \\& Society`
   - `PuringtonEtAl2017` — title has stray `"{``Alexa Is My New BFF''"`
   - `HicksHumphriesSlater2024` — title fine, but keep `&` handling consistent
   - DOI `10.1126/science.aaa1160` (Bakshy 2015) — `science.` prefix is real per Science's URL scheme but looks suspicious; verify.

4. **Update README claim of "9 PDFs"** — actual count is **10** (added `VodrahalliEtAl2021`).

5. **Verify PDF files actually exist** at the paths listed for the 10 papers with `has_pdf: true`. The `pdf_path` values use Windows-style backslashes and point under `defense_project\reference_materials\papers_originals\<category>\<key>.pdf` — viewer should pre-check existence and gracefully handle 404s. One mismatch to flag: `HicksHumphriesSlater2024.pdf` is filed under `algorithms_trust_hci\` but the paper's `category` is `recommender_genai`. Same for `Shanahan2024.pdf` (filed under `narrative_epistemic\` but `category=recommender_genai`).

6. **Add an `id` field for Author nodes** — currently author identity is the raw display string, which means `Kamenica, Emir` and `Kamenica, E.` will be treated as different people (as the README already warns).

### Nice to have

7. **Concept grouping has 129 groups**, many of which are singletons (e.g. `Alexa`, `GPT`, `InstructGPT`, `RLHF`, `ChatGPT`, `bullshit`, `calibration`, etc.). Consider whether the "first token" grouping heuristic is helpful for the viewer, or whether a manual top-level taxonomy (e.g., 8-12 thematic clusters) would render better.

8. **Year range sanity check:** papers span 1965–2026. The 2026 entries (`WoodruffHewitt2026`, `QiPan2026`) have future years but the README/markdown is dated 2026-06-30, so they are valid in-context. Viewer should treat years as strings to avoid JS Date parsing surprises.

---

## 8. Verdict

**Status: GREEN — viewer can ship against this data.**

- Zero structural errors.
- Zero broken cross-references.
- Zero orphan or dead concepts.
- One paper has empty `concepts` array (`deClippelZhang2020`).
- Seven duplicated cocitation edge pairs (intentional or dedup as preferred).
- README PDF count is stale (9 → 10).
- Two PDF path/category mismatches in on-disk storage (cosmetic).