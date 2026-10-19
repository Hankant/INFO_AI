# 检索记录 Search Log

建立：2026-09-08｜本专题「群体智慧与 Collective Intelligence 英文文献」

---

## 一、检索总述

本次检索分两步：

1. **种子核验**：对综述文件 `outputs/Paper1/literature_review/Paper1_群体智慧理论演进综述_2026-09-07.md`「参考文献」一节的 30 项逐条核验（是否入 bib、是否有本地原文、题名作者是否匹配、版本关系）。
2. **扩展检索**：围绕 wisdom of crowds、collective intelligence 及相邻关键词补充经典理论、测量争议与边界条件文献，定位支持、反驳、复现与边界证据。

检索日期：2026-09-08。核验方式：Crossref REST API（`api.crossref.org/works/{DOI}`）逐条查询；非 DOI 条目走 arXiv / 馆藏 / 出版社记录。**没有对全部数据库做穷尽检索，也没有下载全部 PDF**，故不报告 PRISMA 式筛选数量。

---

## 二、种子清单核验方式与结果

对 30 项种子：先查「是否已在 `references.bib`」，再对不在 bib 的条目查 DOI。

- **已在主 bib（13 项）**：StasserTitus1985、LorenzRauhutSchweitzerHelbing2011、GolubJackson2010、HegselmannKrause2002、DeGroot1974、PerraRocha2019、ChuangEtAl2024、NyhanEtAl2023、FugenerGrahlGuptaKetter2021、DoshiHauser2024、JiangEtAl2025ArtificialHivemind、KleinbergRaghavan2021、Vaccaro2024。这 13 项保留 2026-07-29 / 2026-08-01 批次的核验记录，本次仅核对 key 与题名对应关系。
- **不在主 bib（17 项）**：Condorcet 1785、Häggström 等 2004、Galton 1907、Surowiecki 2004、Larrick & Soll 2006、Hong & Page 2004、Prelec 等 2017、Steinel 等 2010、Woolley 等 2010、Friedkin & Johnsen 1990、Bikhchandani 等 1992、Becker 等 2017、Navajas 等 2018、Becker 等 2019、Schoenegger 等 2025、Abels & Lenaerts 2025、Eriksson 等 2026。这 17 项本次逐条 Crossref/arXiv 核验（结果见下表）。

### 17 项种子核验结果（Crossref，2026-09-08）

| 种子# | 题名（截断） | 核验结果 |
| --- | --- | --- |
| 1 | Condorcet, Essai sur l'application de l'analyse…（1785） | 法语原著，无 DOI；按馆藏（digibug.ugr.es）记录 |
| 2 | Häggström, Kalai & Mossel, A law of large numbers for weighted majority（2004） | arXiv:math/0406509，作者 Olle Haggstrom / Gil Kalai / Elchanan Mossel，2004-06-24 |
| 3 | Galton, Vox Populi（1907） | Nature 75(1949):450–451，DOI 10.1038/075450a0 ✅ |
| 4 | Surowiecki, The Wisdom of Crowds（2004） | 专著，无 DOI；按出版社（Penguin Random House）记录 |
| 5 | Larrick & Soll（2006） | Management Science 52(1):111–127，10.1287/mnsc.1050.0459 ✅ |
| 6 | Hong & Page（2004） | PNAS 101(46):16385–16389，10.1073/pnas.0403723101 ✅ |
| 7 | Prelec, Seung & McCoy（2017） | Nature 541(7638)，10.1038/nature21054 ✅ |
| 8 | Steinel, Utz & Koning（2010） | OBHDP 113(2):85–96，10.1016/j.obhdp.2010.07.001 ✅ |
| 9 | Woolley, Chabris, Pentland, Hashmi & Malone（2010） | Science 330(6004):686–688，10.1126/science.1193147 ✅ |
| 10 | Friedkin & Johnsen（1990） | J. Math. Sociology 15(3–4):193–206，10.1080/0022250X.1990.9990069 ✅ |
| 11 | Bikhchandani, Hirshleifer & Welch（1992） | JPE 100(5):992–1026，10.1086/261849 ✅ |
| 12 | Becker, Brackbill & Centola（2017） | PNAS 114(26)，10.1073/pnas.1615978114 ✅ |
| 13 | Navajas, Niella, Garbulsky, Bahrami & Sigman（2018） | Nature Human Behaviour 2(2):126–132，10.1038/s41562-017-0273-4 ✅ |
| 14 | Becker, Porter & Centola（2019） | PNAS 116(22):10717–10722，10.1073/pnas.1817195116 ✅ |
| 15 | Schoenegger, Park, Karger, Trott & Tetlock（2025） | ACM TIIS 15(1)，10.1145/3707649 ✅ |
| 16 | Abels & Lenaerts（2025） | IJCAI-25, 321–329，10.24963/ijcai.2025/37 ✅ |
| 17 | Eriksson, Karlsson, Vartanova & Strimling（2026） | Communications AI & Computing 1(1)，10.1038/s44488-026-00018-8 ✅（CC-BY） |

结论：17 项种子题名/作者/年份/刊物/DOI 与综述参考文献列表一致，无编造条目。少数条目的页码 Crossref 未返回（如 Becker 2017 为 E5070–E5076、Prelec 2017 为 532–535），以出版社/综述记录为准，未逐页校勘。

---

## 三、扩展检索

### 检索关键词

英文：

- `wisdom of crowds`
- `collective intelligence`、`collective intelligence factor`、`c-factor`
- `group intelligence`
- `judgment aggregation`、`group decision making`
- `information pooling`、`shared/unshared information`
- `social influence`、`social learning`、`opinion dynamics`
- `human–AI collective intelligence`、`hybrid human-LLM`

相邻用语（`swarm intelligence`、`crowdsourcing`、`distributed cognition`）**未单独纳入关联区**，因与综述问题（判断聚合、群体信息加工、社会学习、人机协作）的直接关系未在原文中说明。

### 检索式与数据库

- Crossref REST API `works/{DOI}`：核验候选 DOI。
- 未对 Scopus / Web of Science / PubMed 做全库检索式检索；本次扩展以综述已有的引用关系为锚，向后追踪「支持、反驳、复现、测量争议、边界条件」文献，属**叙述性补充**而非系统检索。

### 纳入扩展（10 项，已逐条 Crossref 核验）

| BibTeX key | 题名（截断） | 类别（相对种子的作用） | DOI |
| --- | --- | --- | --- |
| VulPashler2008 | Measuring the Crowd Within | 判断聚合（单人心内聚合） | 10.1111/j.1467-9280.2008.02136.x |
| HerzogHertwig2009 | The Wisdom of Many in One Mind | 判断聚合（辩证自助） | 10.1111/j.1467-9280.2009.02271.x |
| ListPettit2002 | Aggregating Sets of Judgments: An Impossibility Result | 判断聚合（命题聚合不可能定理） | 10.1017/S0266267102001098 |
| MannesSollLarrick2014 | The Wisdom of Select Crowds | 判断聚合（选择性子集聚合） | 10.1037/a0036677 |
| DavisStoberEtAl2014 | When Is a Crowd Wise? | 判断聚合的边界条件 | 10.1037/dec0000004 |
| EngelEtAl2014 | Reading the Mind in the Eyes or Reading between the Lines? | 概念定义与测量（c-factor 的 ToM 机制复现） | 10.1371/journal.pone.0115212 |
| WoolleyAggarwalMalone2015 | Collective Intelligence and Group Performance | 概念定义与测量（c-factor 综述） | 10.1177/0963721415599543 |
| JaylesEtAl2017 | How Social Information Can Improve Estimation Accuracy in Human Groups | 社会影响（正面证据） | 10.1073/pnas.1703695114 |
| RiedlEtAl2021 | Quantifying Collective Intelligence in Human Groups | 概念定义与测量（c-factor 再测量） | 10.1073/pnas.2005737118 |
| Centola2022 | The Network Science of Collective Intelligence | 社会影响与网络（理论综述） | 10.1016/j.tics.2022.08.009 |

> 更正记录：Centola 2022 的正确 DOI 为 `10.1016/j.tics.2022.08.009`；初次按 `…/2022.08.002` 查询命中另一篇 Sporns 论文，已纠正。

### 筛选理由（纳入 vs 不纳入）

- **纳入**：直接回答「聚合为何/何时准确」「c-factor 如何测量与复现」「社会影响如何双向作用」，且能对种子形成支持、反驳或边界对照。
- **不纳入**：`crowdsourcing` 平台机制、`swarm intelligence` 优化算法、组织管理学的团队绩效量表（未说明与综述问题的关系）暂不入库，避免以相邻术语凑数。
- **已由既有 bib 覆盖、不重复纳入**：Burton et al. 2024（LLM 重塑集体智慧）、Bommasani et al. 2022（算法单一化结果同质化）、Ashkinaze et al. 2025 等，均已在 `collective_intelligence_homogeneity`。

---

## 四、未覆盖范围（诚实声明）

1. 未对中文文献（如「群体智慧」「集体智慧」的中文综述与实证）做检索，故 [concept_boundaries.md](concept_boundaries.md) 的「中文概念混用表」只列出**待核查问题**，未判定中文作者错误。
2. 未做撤稿数据库专项审计；未逐篇核对补充材料。
3. 未对预测市场（prediction markets）、民主审议（deliberative democracy）、组织集体智力测量的完整争论做穷尽覆盖。
4. 近期（2025–2026）人机集体智慧证据受模型版本与任务范围限制，仅纳入已核验到的条目。
5. 扩展检索是叙述性补充，不是系统性综述；「未检出某类研究」不能作为「该类研究不存在」的证据。
