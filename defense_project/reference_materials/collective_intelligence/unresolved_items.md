# 待核查条目与需要人工解决的问题

建立：2026-09-08｜本专题「群体智慧与 Collective Intelligence 英文文献」

> 以下条目**不进入正式结论**，需人工二次核查或补齐。无法确认的条目已在这里隔离，不在综述正文当作已核实事实使用。

---

## 一、元数据待补（页码等）

Crossref 对少数条目未返回页码字段（`page` 为空），以下页码来自综述参考文献列表或通行书目，**未逐页校勘出版社页**，撰写正文引用时需回原文确认：

| BibTeX key | 缺失项 | 现状 | 待做 |
| --- | --- | --- | --- |
| `BeckerBrackbillCentola2017` | 页码 | Crossref 未返回；综述记录 E5070–E5076 | 核对 PNAS 官方页 |
| `PrelecSeungMcCoy2017` | 页码 | Crossref 未返回；综述记录 532–535 | 核对 Nature 官方页 |
| `SchoeneggerEtAl2025` | 页码/文章号 | Crossref 未返回页码（v15 i1） | 核对 ACM 官方页（文章号） |
| `ErikssonEtAl2026` | 文章号 | Crossref 未返回页码；综述记录 article 15 | 核对 Communications AI & Computing 官方页 |
| `AbelsLenaerts2025` | 卷期 | Crossref 无 volume/issue（IJCAI 论文集 321–329） | 已按会议记录处理，无需卷期 |

## 二、无 DOI 条目（图书 / arXiv）

| BibTeX key | 类型 | 官方入口 | 待做 |
| --- | --- | --- | --- |
| `Condorcet1785` | 法语原著（书） | 馆藏 https://digibug.ugr.es/handle/10481/57153 | 如需核对经典多数决定理，用 `HaggstromKalaiMossel2004` 的数学表述交叉核对，不逐页校勘十八世纪原文 |
| `Surowiecki2004` | 专著（书） | 出版社 https://www.penguinrandomhouse.com/books/175380/ | 无 PDF 要求；保留馆藏/出版社入口 |
| `HaggstromKalaiMossel2004` | arXiv 预印本 | https://arxiv.org/abs/math/0406509 | 作者已核验（Haggstrom/Kalai/Mossel）；arXiv 元数据 API 返回 503，标题以综述记录「A law of large numbers for weighted majority」为准，需在撰写时回 arXiv 确认标题精确串 |

## 三、全文获取待办（付费墙 / 版本）

截至 2026-09-09，已通过 PMC 开放存档、galton.org 公共领域扫描件、作者自存档、arXiv 等合法渠道获取 **17 篇全文**（清单与哈希见 [manifest.csv](manifest.csv)；PDF 存于 `papers_originals/collective_intelligence/`）。以下 **13 篇仍未获得全文**，只核验到元数据/摘要，**不能标记「全文已读」**：

### 3.1 订阅闭源（无合法 OA 副本，需机构 / 校园网下载）

| BibTeX key | 官方入口（DOI） | 状态 / 失败原因 |
| --- | --- | --- |
| `LarrickSoll2006` | 10.1287/mnsc.1050.0459 | INFORMS 付费墙 |
| `PrelecSeungMcCoy2017` | 10.1038/nature21054 | Nature 付费墙 |
| `SteinelUtzKoning2010` | 10.1016/j.obhdp.2010.07.001 | Elsevier 付费墙 |
| `WoolleyEtAl2010` | 10.1126/science.1193147 | Science 付费墙（MIT 作者副本可另寻） |
| `MannesSollLarrick2014` | 10.1037/a0036677 | APA 付费墙 |
| `WoolleyAggarwalMalone2015` | 10.1177/0963721415599543 | SAGE 付费墙 |
| `Centola2022` | 10.1016/j.tics.2022.08.009 | Elsevier 付费墙 |
| `StasserTitus1985` | 10.1037/0022-3514.48.6.1467 | APA 付费墙（既有 bib，无本地 PDF） |
| `DeGroot1974` | 10.1080/01621459.1974.10480137 | JASA 付费墙（既有 bib，无本地 PDF） |

### 3.2 有 OA 副本但反爬 / 受限（可用浏览器手动下载）

| BibTeX key | 官方入口（DOI） | 状态 / 失败原因 |
| --- | --- | --- |
| `SchoeneggerEtAl2025` | 10.1145/3707649 | ACM 付费墙；LSE 绿色副本（`researchonline.lse.ac.uk/id/eprint/127059/`）Cloudflare 反爬，程序化抓取 403 |
| `ListPettit2002` | 10.1017/S0266267102001098 | Cambridge 付费墙；LSE 绿色副本（`id/eprint/704/`）Cloudflare 反爬 403 |
| `HerzogHertwig2009` | 10.1111/j.1467-9280.2009.02271.x | SAGE 付费墙；Basel edoc 绿色副本 bitstream 受限（HTTP 401） |

### 3.3 标记为 OA 但实际闭源（bronze 标记失效）

| BibTeX key | 官方入口（DOI） | 状态 / 失败原因 |
| --- | --- | --- |
| `NavajasEtAl2018` | 10.1038/s41562-017-0273-4 | Nature Human Behaviour；OpenAlex 标记 bronze，但 `.pdf` 实际重定向到 HTML 摘要页，非开放全文 |

## 四、版本关系待核

| BibTeX key | 版本问题 | 待做 |
| --- | --- | --- |
| `NavajasEtAl2018` | 预印本（2017）vs 正式发表（2018） | 采用正式发表年份 2018；如存档预印本需标注版本 |
| `JiangEtAl2025ArtificialHivemind` | arXiv v 与 NeurIPS 会议作者列表有差异 | 引用统一用前三作者 + et al.（既有 bib 已按会议版处理） |
| `ChuangEtAl2024` | Findings of NAACL 会议版 vs arXiv 预印本 | 已按 ACL Anthology 会议版入库；预印本版本另存则需标注 |
| `ErikssonEtAl2026` | 2026 新刊（Communications AI & Computing） | 确认卷期与文章号在正式出版后的稳定版 |

## 五、中文文献概念混用核查（未做）

- 本轮**未检索中文文献**，故 [concept_boundaries.md](concept_boundaries.md) 第四节「中文概念混用对照表」只列**候选混用表述**，不指向具体中文文献、不判定任何中文作者错误。
- 撰写中文综述前，需检索并核对中文文献中「群体智慧 / 集体智慧 / 集体智力」的实际用法，回填「中文原句 → 对应原始引文 → 层级/定义差异 → 可支持的修正」表。

## 六、既有 13 项的再核验状态

以下 13 项已在主 bib（2026-07-29 / 08-01 批次核验），本次**未重新逐条 Crossref 核验**，仅核对 key 与题名对应关系：

`StasserTitus1985`、`LorenzRauhutSchweitzerHelbing2011`、`GolubJackson2010`、`HegselmannKrause2002`、`DeGroot1974`、`PerraRocha2019`、`ChuangEtAl2024`、`NyhanEtAl2023`、`FugenerGrahlGuptaKetter2021`、`DoshiHauser2024`、`JiangEtAl2025ArtificialHivemind`、`KleinbergRaghavan2021`、`Vaccaro2024`。

> 若后续需要统一口径，可对这些条目重跑 citation checker；但其 not_found 基线为 0（无编造），元数据已由出版社来源交叉核验。

## 七、本轮已解决

- Centola 2022 的 DOI 已从错误的 `…/2022.08.002`（命中 Sporns 论文）更正为 `10.1016/j.tics.2022.08.009`。
- 17 项种子题名/作者/年份/刊物/DOI 与综述参考文献列表一致，未发现编造条目。
- 2026-09-09 补充获取 **17 篇全文**：7 篇经 PMC 开放存档（`HongPage2004`、`BeckerBrackbillCentola2017`、`BeckerPorterCentola2019`、`KleinbergRaghavan2021`、`Vaccaro2024`、`JaylesEtAl2017`、`RiedlEtAl2021`）；1 篇 galton.org 公共领域扫描件（`Galton1907`）；1 篇 Nature CC-BY 经浏览器抓取（`ErikssonEtAl2026`）；其余 8 篇经 arXiv / 作者自存档 / 出版社 OA（`HaggstromKalaiMossel2004`、`AbelsLenaerts2025`、`EngelEtAl2014`、`BikhchandaniHirshleiferWelch1992`、`DavisStoberEtAl2014`、`FriedkinJohnsen1990`、`LorenzRauhutSchweitzerHelbing2011`、`VulPashler2008`）。
