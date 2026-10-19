# Paper 3 文献检索、下载、归纳与共享库入库计划

执行对象：DeepSeek

工作目录：`E:\Info_AI`

日期：2026-08-11

## 一、任务目标

围绕 Paper 3 的重构开展一次可复核的文献补库。研究问题尚未确定，本任务只完成理论地形、原文归档和共享库更新，不设计实验，不撰写论文 Introduction，不把任何候选方向宣布为正式理论贡献。

本批覆盖三个相互区分的领域：

1. responsibility / blame / moral agency；
2. social preferences / reciprocity / punishment / intergroup bias；
3. geopolitical and intergroup conflict，包括 security dilemma、bargaining、crisis signaling、retaliation 与 escalation。

最终需要回答：

- RQ1：责任、blame 和 punishment 文献分别使用哪些构念，它们之间是什么关系？
- RQ2：哪些 social preference 理论依赖对他人意图、期待、群体身份或道德资格的判断？
- RQ3：国际冲突理论如何解释事故、误判、信号、报复和升级？
- RQ4：AI 进入行动者、建议者、执行者或信号来源的位置后，哪条既有理论预测可能发生改变？普通自动化系统或人类中介能否产生同样预测？

## 二、必须先读的项目文件

开始任何写入前，完整阅读：

1. `E:\Info_AI\AGENTS.md`
2. `E:\Info_AI\主Agent\AGENTS.md`
3. `E:\Info_AI\主Agent\文章项目\03_AIA责任归因\README.md`
4. `E:\Info_AI\主Agent\共享文献库\README.md`
5. `E:\Info_AI\defense_project\reference_materials\README.md`
6. `E:\Info_AI\defense_project\reference_materials\batch_2026-07-06_summary.md`
7. `E:\Info_AI\defense_project\reference_materials\knowledge_graph\README.md`
8. `E:\Info_AI\defense_project\latex\references.bib`
9. `E:\Info_AI\references_new.bib`
10. `E:\Info_AI\references_2026-07-06_batch.bib`

共享库唯一正式 BibTeX 入口为：

`E:\Info_AI\defense_project\latex\references.bib`

不得建立 Paper 3 独立 bib，不得把候选 bib 整份盲目合并进主 bib。

## 三、Phase 0：现状审计与去重

### 3.1 输出审计基线

记录以下数字：

- 主 bib 条目数；
- DOI 唯一数；
- 标题标准化后的唯一数；
- 各 category 数量；
- 本地 PDF 数量；
- `accountability_delegation` 已有条目与 PDF 状态；
- `references_new.bib` 和 `references_2026-07-06_batch.bib` 中哪些条目已存在于主 bib。

### 3.2 三层去重

依次使用：

1. DOI 完全一致；
2. 标题小写、去标点、去 LaTeX 花括号后的标准化一致；
3. 第一作者 + 年份 + 标题高相似度。

已知风险：`KobisBonnefonRahwan2025` 与 `Kobis2025` 很可能指向同一篇 *Nature* 论文。核对 DOI、作者、标题和版本后只保留一个正式 key；修复所有引用和知识图谱映射，禁止保留重复记录。

### 3.3 先识别已有相关锚点

以下条目已经在主 bib 中，优先补全文、补 DOI 或补理论卡，不得重复新增：

- `AleksovskaSchillemansGrimmelikhuijsen2019`
- `HallFrinkBuckley2017`
- `KirchkampStrobel2019`
- `Kobis2025` / `KobisBonnefonRahwan2025`
- `LernerTetlock1999`
- `SteffelWilliamsPerrmannGraham2016`
- `Xu2026`

## 四、Phase 1：检索范围与搜索式

### 4.1 数据源顺序

优先级如下：

1. DOI / 出版社官网；
2. Crossref、OpenAlex、Semantic Scholar，用于元数据交叉核验；
3. Web of Science、Scopus、PsycINFO、EconLit、Google Scholar，如账号权限允许；
4. PubMed / PMC、ACM Digital Library、AIS eLibrary、SSRN、arXiv、OSF、作者机构仓储；
5. 中文来源使用期刊官网、CNKI 或国家哲学社会科学文献中心。

博客、新闻和百科只能用于发现关键词，不能作为理论或实证结论的证据。

### 4.2 四组搜索式

#### A. Responsibility 与 moral agency

```text
("artificial intelligence" OR algorithm* OR robot* OR "human-AI" OR "artificial agent*")
AND
("responsibility attribution" OR blame OR accountability OR "moral agency" OR "perceived moral agency" OR culpability OR punishment)
```

#### B. Social preferences 与群际行为

```text
("artificial intelligence" OR algorithm* OR "artificial agent*" OR automation)
AND
("social preference*" OR reciprocity OR "guilt aversion" OR punishment OR "third-party punishment" OR "ingroup favoritism" OR "outgroup hostility" OR "parochial altruism" OR "group reciprocity")
```

同时检索不含 AI 的理论原文和综述，防止只得到应用论文。

#### C. 地缘冲突、危机与升级

```text
("artificial intelligence" OR "AI decision support" OR "autonomous weapon*" OR algorithm*)
AND
("security dilemma" OR "crisis decision-making" OR "crisis signaling" OR retaliation OR escalation OR deterrence OR "bargaining model of war" OR "inadvertent escalation")
```

#### D. 交叉问题

```text
(AI OR algorithm* OR autonomous)
AND
(accident* OR unintended OR miscalculation OR attribution OR responsibility)
AND
(retaliation OR punishment OR conflict OR military OR interstate)
```

### 4.3 检索覆盖标准

每个理论分支至少包含：

- 1 篇奠基性原文；
- 1 篇高质量综述或 meta-analysis；
- 2 篇直接实证研究；
- 1 篇 2024–2026 年 AI 相关研究。

如果某分支达不到上述覆盖，明确标为 evidence gap，不得用相邻文献填充后假装已经覆盖。

## 五、Phase 2：优先核对的种子文献

下列仅为检索种子。所有作者、年份、DOI、卷期和正式版本都必须由 DeepSeek 独立核验。

### 5.1 直接综述与 meta-analysis

1. Zhou et al. (2026), *A systematic review and meta-analysis of psychological and behavioural responses in human-agent vs. human-human interactions*, DOI `10.1038/s44271-026-00466-z`。
2. Huang & Suang (2024), *A Systematic Review on Responsibility Attribution in AI Service and Human-AI Joint Service*, ECIS 2024 / AIS eLibrary。
3. Tok, Powell, & Guellaï (2026), *A systematic review of moral agency in artificial agents*, DOI `10.1007/s44202-025-00537-y`。
4. Bonnefon, Rahwan, & Shariff (2024), *The Moral Psychology of Artificial Intelligence*, DOI `10.1146/annurev-psych-030123-113559`。
5. Thellman, de Graaf, & Ziemke (2022), *Mental State Attribution to Robots: A Systematic Review of Conceptions, Methods, and Findings*, DOI `10.1145/3526112`。
6. Tang et al. (2026), *The moral impact of delegating to artificial intelligence*, DOI `10.3724/SP.J.1042.2026.1084`。

### 5.2 Responsibility / blame 理论锚点

1. Alicke (2000), *Culpable Control and the Psychology of Blame*, DOI `10.1037/0033-2909.126.4.556`。
2. Burger (1981), *Motivational Biases in the Attribution of Responsibility for an Accident: A Meta-analysis of the Defensive-Attribution Hypothesis*, DOI `10.1037/0033-2909.90.3.496`。
3. 检索并核验 Malle、Guglielmo 与 Monroe 关于 Path Model of Blame / theory of blame 的原始文献；不要只引用二手综述。

### 5.3 Social preferences 与群际冲突锚点

1. Rabin (1993), intention-based fairness / reciprocity。
2. Dufwenberg & Kirchsteiger (2004), sequential reciprocity。
3. Battigalli & Dufwenberg (2007), guilt aversion / *Guilt in Games*。
4. Fehr & Schmidt (1999), inequity aversion。
5. Choi & Bowles (2007), *The Coevolution of Parochial Altruism and War*, DOI `10.1126/science.1144237`。
6. 检索 group reciprocity、intergroup punishment、ingroup favoritism 与 outgroup discrimination 的实证原文和综述。

### 5.4 国际冲突与 AI 锚点

1. Jervis (1978), *Cooperation under the Security Dilemma*, DOI `10.2307/2009958`。
2. Fearon (1995), *Rationalist Explanations for War*, DOI `10.1017/S0020818300033324`。
3. Horowitz & Lin-Greenberg (2022), *Algorithms and Influence: Artificial Intelligence and Crisis Decision-Making*, DOI `10.1093/isq/sqac069`。
4. Goldfarb & Lindsay (2022), *Prediction and Judgment: Why Artificial Intelligence Increases the Importance of Humans in War*, DOI `10.1162/isec_a_00425`。
5. Houghton (2021), *Inadvertent Escalation in the Age of Intelligence Machines*, DOI `10.1017/eis.2021.23`。
6. Croco (2011), *The Decider's Dilemma: Leader Culpability, War Outcomes, and Domestic Punishment*；核验 DOI。
7. 检索 2024–2026 年 AI、retaliation、crisis signaling、nuclear escalation 和 military decision support 的同行评审实证研究。

## 六、Phase 3：原文下载与真实性核验

### 6.1 合法下载顺序

1. 出版社 OA PDF；
2. PubMed Central / ACM OA / AIS eLibrary；
3. arXiv、SSRN、OSF；
4. 作者机构仓储或作者主页的 accepted manuscript；
5. 只有元数据和付费墙时，保留 DOI / 官方页面，不伪造 PDF，不使用来路不明的全文站点。

### 6.2 PDF 验证要求

每个下载文件必须同时通过：

- 文件头为 `%PDF`；
- 文件可解析，页数大于 0；
- 抽取文本中的标题、第一作者和年份与元数据一致；
- 正文不是出版社登录页、错误页、补充材料或另一篇论文；
- 记录下载来源 URL 和核验日期。

只检查文件大小不算完成核验。

### 6.3 文件目录与命名

继续使用同一个共享库，在 `papers_originals` 下新增或使用以下目录：

```text
E:\Info_AI\defense_project\reference_materials\papers_originals\
├── accountability_delegation\
├── responsibility_moral_agency\
├── social_preferences_intergroup_conflict\
└── ai_geopolitical_conflict\
```

文件名必须与最终 BibTeX key 完全一致：`<bib_key>.pdf`。

状态枚举只能使用：

- `local_verified_pdf`
- `official_fulltext_html`
- `doi_only_paywalled`
- `metadata_only`
- `unverified`

付费墙不等于 unverified；只要 DOI 与官方元数据已核验，可以标记 `doi_only_paywalled`。

## 七、Phase 4：逐篇理论卡片

每篇入选文献必须填写以下字段，不允许凭标题或摘要推断全文结论：

```text
bib_key:
完整引文:
DOI / 官方链接:
全文状态:
研究类型: 理论 / 综述 / meta-analysis / 实验 / 调查 / 其他

1. 原始术语：文献实际使用的英文名称和中文译名
2. 理论来源：该构念来自哪篇原始理论
3. 理论定义：具体包含什么，不包含什么
4. 分析层级：个人 / 群体 / 组织 / 国家 / 国际体系 / 技术系统
5. 模型位置：前因 / 机制 / 结果 / 调节 / 研究情境
6. 经验对应：使用什么操控、量表或行为指标
7. 理论区分力：能够区分哪两种竞争性解释
8. 研究设计与样本：不得只写结论
9. 主要发现：标明效应方向、效应量或统计证据；没有报告则明确写无
10. 边界与限制：作者原文限制 + 本文归纳
11. AI 非替代性：替换为人类建议者、普通工具或规则自动化后，命题是否仍成立
12. 对 Paper 3 的作用：理论锚点 / 直接证据 / competing mechanism / 方法借鉴 / 仅背景
13. 证据定位：页码、章节、表格或图号
```

任何没有全文的条目只能制作“元数据卡”或“摘要卡”，并明确标记 `尚未逐页核对全文`。

## 八、Phase 5：跨文献归纳

输出一个理论矩阵，禁止按论文逐篇堆砌。矩阵至少包含：

| 理论 | 核心主体 | 核心构念 | 分析层级 | 标准预测 | 常用测量 | AI 进入位置 | 与传统预测的张力 | AI 可替代性 | 证据强度 |
|---|---|---|---|---|---|---|---|---|---|

归纳时必须分开：

- responsibility attribution、blame、punishment、retaliation；
- individual social preferences 与 state-level strategic interaction；
- moral judgment 与 deterrence / threat response；
- AI 作为建议来源、执行代理、武器系统、互动对象和归责对象；
- AI 特有效应与一般 automation / delegation 效应。

最后只提交：

1. 已有理论一致解释的关系；
2. 文献中真正存在的矛盾；
3. 最多 3 个值得 Paper 3 继续核查的理论问题；
4. 每个问题的致命替代解释；
5. 仍缺哪些证据。

不得在本批次直接确定正式 RQ 或实验设计。

## 九、Phase 6：正式入库

### 9.1 必须更新的源文件

1. `E:\Info_AI\defense_project\latex\references.bib`
2. `E:\Info_AI\defense_project\reference_materials\to_collect.md`
3. `E:\Info_AI\defense_project\reference_materials\verified_links.md`
4. `E:\Info_AI\export_bib.py` 中的 `CATEGORY_MAP` 和 `CONCEPT_TAGS`

不要直接手工编辑生成物来代替源文件更新。

### 9.2 重新生成知识图谱

运行：

```powershell
$env:PYTHONIOENCODING='utf-8'
py -3 E:\Info_AI\export_bib.py
```

然后核对：

- `knowledge_graph/papers.json`
- `knowledge_graph/papers.csv`
- `knowledge_graph/concepts.json`
- `knowledge_graph/categories.json`
- `knowledge_graph/data_integrity_report.md`
- `knowledge_graph/validation_report.md`

新增 concept 使用原始文献术语的 snake_case，例如：

- `responsibility_attribution`
- `culpable_control`
- `perceived_moral_agency`
- `intention_based_reciprocity`
- `guilt_aversion`
- `parochial_altruism`
- `group_reciprocity`
- `security_dilemma`
- `bargaining_model_of_war`
- `crisis_signaling`
- `retaliation`
- `inadvertent_escalation`

不得自行发明组合概念。

## 十、交付文件

DeepSeek 最终必须交付：

1. `E:\Info_AI\defense_project\reference_materials\paper3_responsibility_social_conflict\manifest.csv`
2. `E:\Info_AI\defense_project\reference_materials\paper3_responsibility_social_conflict\batch_2026-08-11_summary.md`
3. `E:\Info_AI\主Agent\文章项目\03_AIA责任归因\Paper3_理论文献导航_2026-08-11.md`
4. 已核验 PDF，放入对应 `papers_originals` 子目录
5. 更新后的主 `references.bib`
6. 更新后的知识图谱全部生成物

`manifest.csv` 至少包含：

```text
bib_key,title,year,doi,domain,theory,analysis_level,study_type,verification_status,fulltext_status,local_pdf,official_url,source_url,card_anchor,paper3_role,ai_substitutability,notes
```

## 十一、验收标准

全部满足才算完成：

- [ ] 报告入库前后条目数和去重结果；
- [ ] 每条新文献至少有 DOI 或官方永久链接；
- [ ] 所有 DOI 均与标题、作者、年份匹配；
- [ ] 所有本地 PDF 均完成标题级全文核验；
- [ ] 没有重复 DOI、重复标题或同文多 key；
- [ ] 没有把摘要卡写成全文精读卡；
- [ ] 没有把 responsibility、blame、punishment、retaliation 混为同一构念；
- [ ] 没有把个人层级 social preferences 直接当成国家层级理论；
- [ ] 每个理论都写明原始术语、来源、定义、层级、模型位置、测量和区分力；
- [ ] 每个 AI 贡献判断都完成 human / ordinary tool / rule-based automation 替代性审查；
- [ ] 主 bib 可解析，`export_bib.py` 成功运行；
- [ ] 知识图谱条目数与主 bib 一致；
- [ ] 未修改无关论文正文、PPT 或其他项目文件。

## 十二、遇阻处理

- 数据库限流：记录 API、时间和错误，不把限流写成 not found。
- 付费墙：保留 DOI 与出版社页，标记 `doi_only_paywalled`。
- 版本冲突：优先正式发表版本，保留 preprint 对应关系，不重复入库。
- DOI 或标题不一致：进入 `_unverified`，在批次总结中列出，禁止进入正式理论归纳。
- 无法访问本地工作区：停止写入，只返回阻塞说明和待执行清单。

