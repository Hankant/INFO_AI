# Paper 3 文献补库总结 — 2026-08-11 批次

> 批次日期：2026-08-11
> 源：四组结构化搜索（responsibility/moral agency, social preferences/intergroup conflict, geopolitical conflict, cross-cutting AI questions）
> 核验：CrossRef / Semantic Scholar / 出版社官网 DOI 交叉核验

---

## 一、审计基线

| 指标 | 入库前 | 说明 |
|------|--------|------|
| 主 bib 条目数 | 166 | `references.bib` |
| 唯一 DOI 数 | 146 | 20 条无 DOI |
| 本地 PDF 数 | 49 | `papers_originals/` |
| accountability_delegation 已有条目 | 11 | 全部来自 2026-07-06 批次 |
| accountability_delegation 本地 PDF | 0 | 全付费墙 |
| `references_new.bib` 未合并条目 | 0 | 全部 19 条已入库 |
| `references_2026-07-06_batch.bib` 未合并条目 | 0 | 全部 11 条已入库 |

### Kobis 重复确认

`KobisBonnefonRahwan2025`（3 作者，无 DOI）与 `Kobis2025`（8 作者，DOI `10.1038/s41586-025-09505-x`）指向同一篇 *Nature* 论文。`Kobis2025` 保留为正式 key，`KobisBonnefonRahwan2025` 待移除。

---

## 二、本批新增条目

本批共检索并核验 **30 条**新文献，覆盖三个理论领域。

### 2.1 Responsibility / Blame / Moral Agency（12 条）

| Bib key | 类型 | 状态 |
|---------|------|------|
| `ZhouEtAl2026` | 综述 + meta-analysis | DOI verified |
| `HuangSuang2024` | 综述（ECIS） | AISeL verified |
| `TokPowellGuellai2026` | 综述 | DOI verified |
| `BonnefonRahwanShariff2024` | 综述（ARP） | DOI verified |
| `ThellmanDeGraafZiemke2022` | 综述（ACM THRI） | DOI verified |
| `TangEtAl2026_MoralDelegation` | 综述（心理科学进展） | DOI verified |
| `Alicke2000` | 理论（Culpable Control Model） | DOI verified |
| `Burger1981` | meta-analysis（defensive-attribution） | DOI verified |
| `MalleGuglielmoMonroe2014` | 理论（Path Model of Blame） | DOI verified |
| `Joo2024` | 实验（PLOS ONE） | DOI verified |
| `TsumuraYamada2026` | 实验（Scientific Reports） | DOI verified |
| `Franklin2025` | 博士论文（UCL） | DOI verified |

### 2.2 Social Preferences / Reciprocity / Punishment / Intergroup Bias（7 条）

| Bib key | 类型 | 状态 |
|---------|------|------|
| `Rabin1993` | 理论（intention-based reciprocity） | AER, confirmed |
| `DufwenbergKirchsteiger2004` | 理论（sequential reciprocity） | DOI verified |
| `BattigalliDufwenberg2007` | 理论（guilt aversion） | DOI verified |
| `FehrSchmidt1999` | 理论（inequity aversion） | DOI verified |
| `ChoiBowles2007` | 理论 + ABM（parochial altruism） | DOI verified |
| `IgweEtAl2024` | 机器学习 + social preferences | DOI verified |
| `VanBaarEtAl2019` | 计算建模（moral strategies） | DOI verified |

### 2.3 Geopolitical / Intergroup Conflict + AI（11 条）

| Bib key | 类型 | 状态 |
|---------|------|------|
| `Jervis1978` | 理论（security dilemma） | DOI verified |
| `Fearon1995` | 理论（bargaining model of war） | DOI verified |
| `HorowitzLinGreenberg2022` | 实验（ISQ） | DOI verified |
| `GoldfarbLindsay2022` | 理论 + 分析（IS） | DOI verified |
| `Johnson2021` | 分析（EJIS） | DOI verified |
| `Croco2011` | 实证（APSR） | DOI verified |
| `Payne2026` | 实验（war-game simulation） | arXiv verified (DOI `10.48550/arXiv.2602.14740`) — ⚠ 已从KCL report更正为arXiv |
| `RiveraEtAl2024` | 实验（ACM FAccT） | DOI verified |
| `SIPRI2025` | 政策分析 | SIPRI DOI verified (DOI `10.55163/FZIW8544`) — ⚠ Chernavskikh & Palayer; 标题已更正 |
| `Larsen2024` | 博弈论分析（JCR） | DOI verified (DOI `10.1177/00220027231185154`) — ⚠ 作者/标题/DOI已更正 |
| `Johnson2026` | 分析（EJIS） | DOI verified (DOI `10.1017/eis.2026.10063`) — ⚠ 原LinGreenberg2025; 作者/年份/DOI已更正 |

---

## 三、检索覆盖评估

按照计划要求的覆盖标准（每分支 1 奠基 + 1 综述 + 2 实证 + 1 AI 2024-2026），各分支状态：

| 理论分支 | 奠基 | 综述 | 实证 | AI 2024-2026 | 状态 |
|----------|------|------|------|-------------|------|
| responsibility/blame 理论 | Alicke 2000, Malle 2014, Burger 1981 | Zhou 2026, Huang 2024, Tok 2026, Bonnefon 2024, Thellman 2022, Tang 2026 | Joo 2024, Tsumura 2026, Franklin 2025 | ✓ 覆盖 | **完整** |
| social preferences 理论 | Rabin 1993, Dufwenberg 2004, Battigalli 2007, Fehr 1999 | — | Choi 2007, Van Baar 2019 | △ Igwe 2024 部分覆盖 | **缺: 综述、AI-社会偏好交互实验** |
| intergroup conflict 理论 | Jervis 1978, Fearon 1995 | — | Croco 2011 | ✓ Payne 2026, Rivera 2024, Larsen 2024 | **缺: 群际冲突综述** |
| AI + geopolitical | Horowitz 2022, Goldfarb 2022, Johnson 2021 | SIPRI 2025 | Payne 2026, Rivera 2024 | ✓ 覆盖 | **基本完整** |

### 明确证据缺口（按计划标记，不填充）

1. **Social preferences 缺高质量综述**：未找到覆盖 reciprocity/punishment/intergroup bias 的近 5 年系统综述或 meta-analysis。
2. **AI + social preferences 交互实验需进一步检索**：当前已发现 Treiman et al. (AAAI HCOMP) 等 AI-as-social-preferences-game-player 实验，原"完全空白"判断撤回。需专项检索 AI agent 在 ultimatum game / trust game / third-party punishment 中的行为实验。
3. **Intergroup conflict 综述缺**：未找到整合 security dilemma / bargaining / crisis signaling / escalation 的近 5 年系统综述。
4. **Group reciprocity 原文**：计划要求的 group reciprocity、intergroup punishment 原文在本次搜索中未独立命中，需后续专项检索。

---

## 四、全文状态

| 状态 | 数量 | 说明 |
|------|------|------|
| 已有本地 PDF（`papers_originals/`） | 49 | 属于既有 bib |
| 本批已下载 OA PDF | 4 | Joo2024, VanBaarEtAl2019, IgweEtAl2024, SIPRI2025 |
| 本批已删除伪 PDF | 1 | Franklin2025（485字节 401页面，已删除，知识图谱已排除） |
| 本批 OA 但无法自动下载 | ~8 | Nature/Springer/ACM 需浏览器 cookie，curl/Python urllib 均失败 |
| 本批付费墙（`doi_only_paywalled`） | ~15 | Nature / Science / APSR / IS 等 |
| 本批元数据已核验、无 PDF | 2 | 工作论文 / 报告 |

所有 DOI 均与标题、作者、年份交叉核验。3条错误元数据已更正（Larsen2024, LinGreenberg2025→Johnson2026, Payne2026）。1条错误DOI已更正（IgweEtAl2024）。1条错误DOI已更正（SIPRI2025）。

---

## 五、已识别锚点状态

以下计划指定的锚点全部已在主 bib 中，无需重复新增：

| 锚点 | 状态 | 操作 |
|------|------|------|
| `AleksovskaSchillemansGrimmelikhuijsen2019` | 已入库 | 补全文状态标记 |
| `HallFrinkBuckley2017` | 已入库 | 无需操作 |
| `KirchkampStrobel2019` | 已入库 | 无需操作 |
| `Kobis2025` / `KobisBonnefonRahwan2025` | **重复** | 保留 `Kobis2025`，移除 `KobisBonnefonRahwan2025` |
| `LernerTetlock1999` | 已入库 | 无需操作 |
| `SteffelWilliamsPerrmannGraham2016` | 已入库 | 无需操作 |
| `Xu2026` | 已入库 | 无需操作 |

---

## 六、风险与限制

- **Semantic Scholar 限流**：未在本批次运行 citation checker，所有元数据通过 DOI 交叉核验。
- **付费墙比例高**：约 50% 的新增条目无法获取 OA PDF。
- **概念标签手写**：新条目的 concept tags 基于摘要和搜索关键词推断，未经全文精读验证（4篇全文已精读制卡除外）。
- **Phase 4 理论卡片**：已制作 30 张（4 full cards + 26 metadata cards），见 `theory_cards_2026-08-11.md`。**状态：Major revision，暂不入正式理论库。**
- **Phase 5 跨文献归纳**：待理论导航重写后执行。
- **已知元数据错误已修复**：Larsen2024（作者/标题/DOI）、LinGreenberg2025→Johnson2026（作者/年份/DOI/key）、Payne2026（arXiv preprint 非 KCL report）、IgweEtAl2024 DOI、SIPRI2025 DOI/标题/作者。
- **知识图谱**：`export_bib.py` 已修复 concept tag 生成顺序 bug 和 PDF 文件头验证。
