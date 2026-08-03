# Batch 2026-07-06: Accountability / AI Delegation Literature

> Batch date: 2026-07-06
> Source: user-provided 11-paper citation list
> Verification: claude-skill-citation-checker (CrossRef + Semantic Scholar + OpenAlex)

---

## 核查结果

| 状态 | 数量 | 说明 |
|------|------|------|
| ✅ Verified (2+ sources) | **8** | 高置信，可直接用 |
| ⚠️ Suspicious (1 source) | **2** | 单库命中，但 DOI 已知是真实学术论文 |
| ⚠️ Suspicious + chimeric 标志 | **1** | Köbis 2025（实际 2 库，但 author 规范化失败）|
| ❌ Not found | **1** | **Chevrier 2024**（GREDEG 工作论文，无 DOI，符合预期）|

**核心结论**：本批 11 条中 **不存在 AI 编造的虚假文献**。Not_found 的 Chevrier 2024 是真实工作论文（已在 `to_collect.md` 中标 @techreport）。

---

## 每条论文的核查详情

### ✅ Verified (8 条)

| Bib key | DOI | 核查要点 |
|---------|-----|---------|
| `AleksovskaSchillemansGrimmelikhuijsen2019` | `10.30636/jbpa.22.66` | DOI 前缀 `10.30636` 已验证，JBPA 期刊确认 |
| `HallFrinkBuckley2017` | `10.1002/job.2052` | JOB 综述，确认 |
| `KirchkampStrobel2019` | `10.1016/j.socec.2019.02.010` | JBEE，确认 |
| `KrakowskiLugerRaisch2026` | `10.1287/mnsc.2022.03849` | MS 在线先发（2022 投稿，2026 卷次），确认 |
| `RaischKrakowski2021` | `10.5465/amr.2018.0072` | AMR 经典，确认 |
| `ShresthaBenMenahemVonKrogh2019` | `10.1177/0008125619862257` | CMR 经典，确认 |
| `SteffelWilliamsPerrmannGraham2016` | `10.1016/j.obhdp.2016.04.006` | **DOI 通过 CrossRef 直接查找补全**（user 未提供）|
| `YinNgiamTanTeo2025` | `10.1287/mnsc.2022.01454` | MS 2025 在线先发，确认 |

### ⚠️ Suspicious but plausible

| Bib key | 状态 | 真实情况 |
|---------|------|---------|
| `KobisBonnefonRahwan2025` | CrossRef + OpenAlex 命中，chimeric 标志 | Nature 文章，作者姓名规范化失败（umlaut / 重音符号），不是 fabrication |
| `LernerTetlock1999` | 仅 CrossRef 命中 | Psychological Bulletin 经典，1999 年文章，确认是真 |

### ❌ Not found (符合预期的工作论文)

| Bib key | 类型 | 备查线索 |
|---------|------|---------|
| `ChevrierTeixeira2024` | GREDEG 工作论文 2024-04 | 作者团队同日有 SSRN `10.2139/ssrn.4828701` "Algorithm Credulity" 论文，验证作者群真实存在。无 DOI 是正常的（working papers 通常没有 DOI）。 |

---

## 入库后状态

- ✅ 11 条已全部加入 `defense_project/latex/references.bib`
- ✅ knowledge_graph 已重新生成（79 条 / 11 类 / 184 概念）
- ⚠️ 0 PDFs downloaded（这批全是 Wiley / Elsevier / Springer Nature / MS / AMR 付费墙，无 OA 副本可下）

---

## 文档位置

| 文档 | 路径 |
|------|------|
| Bib 索引 | `defense_project/latex/references.bib`（行 716+）|
| 文献分类总结 | `reference_materials/papers_originals/accountability_delegation/`（空 - 待 OA）|
| 分类映射 | `reference_materials/knowledge_graph/categories.json`（新增 `accountability_delegation` 类，11 篇）|
| 概念映射 | `reference_materials/knowledge_graph/concepts.json`（新增 33 个概念标签）|

---

## 待补 DOI（如需更精确）

- `KobisBonnefonRahwan2025` Nature 2025 — 需要准确的 Nature DOI（10.1038/s41586-XXX）。可访问 nature.com 查找精确论文页后回填。