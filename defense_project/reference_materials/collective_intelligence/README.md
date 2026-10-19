# 群体智慧与 Collective Intelligence 英文文献

> 资料分类名称（非单一理论概念）｜建立：2026-09-08｜维护：文献库 agent

本专题是共享文献库的一个**专题视图**，不是一套独立引用系统。它把分散在既有目录（`collective_intelligence_homogeneity`、`opinion_dynamics_abm`、`llm_social_simulation`）以及尚未归档的经典 wisdom-of-crowds / collective-intelligence 文献，按「理论演进 + 概念边界」重新组织，服务一篇独立的**中文理论综述**（梳理群体智慧理论演进、澄清中文概念混用）。本专题保留与 Paper 1 的关联标签，但不把综述写成仅服务 Paper 1 的研究背景，也不预设 AI 必然损害群体智慧。

---

## 一、定位与边界

- **这不是新 bib**：所有条目共用 `defense_project/latex/references.bib` 的 BibTeX key，不另建互不相通的引用系统。
- **不是单一概念**：本目录标题里的「群体智慧」和「Collective Intelligence」是两个有交集、但操作定义不同的研究对象，详见 [concept_boundaries.md](concept_boundaries.md)。本专题把它们作为「资料分类名称」并列，不宣称为同一理论。
- **不覆盖论文**：本专题负责文献检索、核验与入库，**不修改**三篇论文的研究问题、构念或假设。Paper 1 现行研究问题的边界以 `主Agent/文章项目/01_算法权威与信息校准/` 下的基准稿为准。

---

## 二、可多选的检索标签

分类依据来自原文，允许交叉归属：

| 标签 | 说明 |
| --- | --- |
| 判断聚合 | 多个判断/估计如何聚合为更准结果（Condorcet、Galton、Larrick & Soll、Prelec 等） |
| 群体协作与信息加工 | 群体拥有的信息为何未必被用好（Stasser & Titus、Steinel、Woolley 等） |
| 社会影响与社会学习 | 互动何时带来准确学习、何时仅带来一致（DeGroot、Friedkin & Johnsen、Becker、Jayles 等） |
| 概念定义与测量 | 构念的来源、边界与经验对应（wisdom of crowds、c-factor、judgment aggregation） |
| 人机协作与生成式 AI | 技术如何改变个人表现与群体结果的关系（Kleinberg & Raghavan、Fügener、Doshi & Hauser 等） |

每篇文献的标签见 [manifest.csv](manifest.csv) 的「主题标签」列；交叉归属用 `;` 分隔。

---

## 三、目录内文件

| 文件 | 内容 |
| --- | --- |
| [README.md](README.md) | 本文件：专题入口与导航 |
| [manifest.csv](manifest.csv) | 40 篇（30 种子 + 10 扩展）机器可读清单，含核验/获取/阅读/版本状态 |
| [literature_cards.md](literature_cards.md) | 每篇文献卡片：研究问题、概念定义、分析层级、方法、关键发现、证据边界、推进与遗留 |
| [concept_boundaries.md](concept_boundaries.md) | 核心概念七项记录 + 中文概念混用对照表 |
| [theoretical_development.md](theoretical_development.md) | 理论演进（前一研究回答了什么 → 后续质疑/增加 → 证据如何变化） |
| [search_log.md](search_log.md) | 检索数据库、检索式、日期、筛选理由、未覆盖范围 |
| [unresolved_items.md](unresolved_items.md) | 待核查条目与需要人工解决的问题 |

---

## 四、与既有目录的关系

本专题把以下既有类别的相关论文纳入同一专题视图，**原文维持原路径**，由 manifest 的「本地路径」列引用，避免重复复制：

- `papers_originals/collective_intelligence_homogeneity/` — 现有 19 条（含 StasserTitus1985、Lorenz2011、KleinbergRaghavan2021、DoshiHauser2024、JiangEtAl2025 等）
- `papers_originals/opinion_dynamics_abm/` — 现有 8 条（含 DeGroot1974、GolubJackson2010、HegselmannKrause2002、PerraRocha2019 等）
- `papers_originals/llm_social_simulation/` — 现有 9 条（含 ChuangEtAl2024 等）

**新获取、尚无归档位置的原文**放入 `papers_originals/collective_intelligence/`。

---

## 五、种子来源与核验口径

30 项种子清单取自综述文件：

`E:\Info_AI\outputs\Paper1\literature_review\Paper1_群体智慧理论演进综述_2026-09-07.md` 的「参考文献」一节（编号 1–30）。

核验口径：

- 先查 DOI（Crossref），再查标题与作者；不按文件名认定下载完成。
- 区分预印本、作者接受稿与正式发表版；不擅自覆盖旧文件。
- 状态分开记录：元数据核验状态、全文获取状态、阅读范围、版本状态。
- **没有阅读全文，不标记「全文已读」**。本专题当前对多数条目只核验到「题名/作者/年份/刊物/DOI 与原文摘要」，未做整篇精读。

核验日期：2026-09-08。核验方式：Crossref REST API 逐条查询（`py -3` + urllib），非 DOI 条目（Condorcet 1785 法语原著、Surowiecki 2004 专著、Häggström 等 2004 arXiv）按馆藏/出版社/arXiv 记录核验。

---

## 六、状态概览（2026-09-08）

| 项目 | 数量 |
| --- | --- |
| 种子条目总数 | 30 |
| 已在主 bib（本次未重新逐条核验） | 13 |
| 本次新增入 bib（种子） | 17 |
| 本次新增入 bib（扩展） | 10 |
| 已有本地全文 | 8（种子中既有 PDF） |
| 新获取全文 | 3（HaggstromKalaiMossel2004、AbelsLenaerts2025、EngelEtAl2014） |
| 获取失败（OA 但程序化下载被阻断） | 5（Becker2017、Becker2019、Eriksson2026、Jayles2017、Riedl2021） |
| 只有摘要或元数据（付费墙 / 图书 / 既有无 PDF） | 24 |
| 新增入主 bib 合计 | 27 |

> 精确数字以 [manifest.csv](manifest.csv) 与 [search_log.md](search_log.md) 为准；本表为概览。全部条目「阅读范围」均为「未读全文」，未将任何条目标记为「全文已读」。
