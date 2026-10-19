# 主 Agent 项目级指令

本文件是 `E:\Info_AI` 的主控记忆文件。它的主要作用不是替代各专项 agent，而是记录项目结构、文章映射、已有工作和关键口径，减少长期对话中的记忆破损与重复沟通。

人工导航与 Agent 台账：

- `E:\Info_AI\主Agent\00_项目导航.md`
- `E:\Info_AI\主Agent\01_Agent职责与成果台账.md`

## 项目分区与 Git 默认规则（2026-10-10）

总入口为 `E:\Info_AI\README.md`，仓库边界及同步步骤见 `E:\Info_AI\docs\REPOSITORY_MANAGEMENT.md`。
实验工程 `projects/paper2-slot-prototype` 已拆为独立本地 Git 仓库，仍保留原路径；研究仓库忽略该目录，不能在根仓库提交实验代码。
用户泛指“同步 Git”时优先检查、验证、提交和同步实验仓库；论文与国自然题目一、题目四按指定范围分别处理，不把研究材料与实验改动混在同一次提交中。
实验仓库远端为 https://github.com/Hankant/paper2-slot-prototype.git（私有），main 跟踪 origin/main；不得推向研究仓库的 main。2026-10-10 已推送拆分历史，工作区未提交改动仍需另行审查和同步。详细状态以实际 Git 检查为准。

会话默认（2026-09-21 用户声明）：用户说"项目进展"时，默认指 **Paper 2 的实验进展**（含研究设计线程与 `projects/paper2-slot-prototype` 工程线程），不是三篇文章的整体盘点；除非用户另行说明。

## 一、项目总结构

当前项目不是单篇论文，而是围绕三篇文章与一套共享文献库、共享答辩材料展开。

主结构如下：

```text
E:\Info_AI
├── 主Agent
│   ├── AGENTS.md                         # 本文件：项目总控记忆
│   ├── 文章项目
│   │   ├── 01_算法权威与信息校准
│   │   ├── 02_AI授权_EWA
│   │   └── 03_AIA责任归因
│   ├── 共享文献库
│   └── 答辩材料
├── defense_project                       # 第一篇与共享文献库的主要既有材料
├── outputs                               # 第二篇及多 Agent 产出
├── docs
└── tmp
```

原则：

- 不要把三篇文章混成一篇。
- 不要把第二篇 AI 授权/EWA 误称为“第一篇文章”。
- 文献库由专门的文献库 agent 负责更新和维护。主 Agent 只记录入口、使用原则和与三篇文章的关系，不直接接管文献库维护。
- 答辩材料是三篇文章一起打包准备，但内部要分成三节。
- 主 Agent 需要持续记录：这个项目做过什么、哪些文件是基准版本、哪些材料已被退回或不应继续使用。

## 二、三篇文章映射

## 二〇、博士课题总框架：AI as Decision Architecture

三篇文章的总领框架是 **AI as Decision Architecture**。

这里的 decision architecture 不应被写成一个已经完全稳定、边界清晰的成熟理论，而应被写成一个整合性分析框架。它用于描述 AI 如何重构高风险决策中的信息流、认知负担、行动阈值、决策权和责任关系。

总命题：

> AI 通过改变人们相信什么、在既有信念与反馈下如何校准依赖和行动阈值，以及如何归属行动后果，重构了高风险人类决策。

英文命题：

> AI reshapes high-risk human decision-making by altering what people believe, how they calibrate reliance and action thresholds conditional on those beliefs, and how they assign ownership over consequential actions.

三篇文章共同识别同一个 AI-mediated decision process 的三个环节：

```text
Belief Formation
→ Risk Appraisal / Reliance Calibration
→ Responsibility
```

对应中文问题：

```text
人相信什么？
在既有信念下，人如何校准依赖并转化为行动？
如果采取行动，后果算谁的？
```

三篇文章的关系：

| 论文 | 核心映射 | 核心机制 | 记忆点 |
| --- | --- | --- | --- |
| Paper 1 | evidence → belief | answer-first belief anchoring / 信息充分性感知与贝叶斯更新偏离 | Belief anchoring |
| Paper 2 | comparable performance evidence → comparative trust | Asymmetric Trust across Human and AI | Asymmetric Trust |
| Paper 3 | action → responsibility | ownership dilution / responsibility sharing | Ownership dilution |

统一性：

- 三篇都研究 AI 如何作为 decision architecture 改变高风险人类决策。
- 三篇共享一个过程链条：信念形成、来源评价与行动选择、责任归属。
- 三篇共同回应现有文献常把 AI 效应混成总量结果，而较少区分信息路径、认知依赖路径和责任路径的问题。

独立性：

- 第一篇隔离 evidence-to-belief 机制。
- 第二篇隔离 comparative-performance-to-source-choice 机制。
- 第三篇隔离 action-to-responsibility 机制。
- 三篇在任务结构、行为数据、因变量和识别策略上应明显不同，避免变成同质化 vignette experiments。

### 第一篇：算法权威与信息校准

用户所说的“第一篇文章”指的是这一篇。

Paper 1“群体智慧”候选重构方向的主问题与行动约束见：

- `E:\Info_AI\主Agent\文章项目\01_算法权威与信息校准\Paper1_群体智慧方向_主问题锁定与行动约束_2026-07-31.md`
- `E:\Info_AI\主Agent\文章项目\01_算法权威与信息校准\Paper1_群体智慧方向_研究计划存档_2026-07-31.md`

处理该候选方向时必须先读该文件。其唯一锁定主问题为“**大语言模型会削弱群体智慧吗？**”。该文件不覆盖下述“算法权威与信息校准”现有基准稿。

核心题目与关键词：

- Algorithmic Authority and Information Calibration
- 算法权威与信息校准：生成式 AI 如何改变额外搜索与信念更新
- 生成式 AI、证据抽样、信念更新
- additional information acquisition after an initial answer
- same-summary source-label design
- epistemic ownership
- information calibration mismatch
- conditional Bayesian deviation
- full-information deviation

核心理论口径：

- 生成式 AI 不是简单提供建议，而是通过 answer-first synthesis 改变人在不确定性下的信息获取和信念更新。
- 当前版本已经不再把“双重贝叶斯偏离”作为标题或理论预设。
- 当前主线是 information calibration：在初始 summary 内容相同、额外搜索成本相同的条件下，AI 来源标签是否改变用户对额外证据价值、主观信息获得感、epistemic ownership 和后续信念更新的判断。
- “双重贝叶斯偏离”最多作为可能被观察到的经验结果或后验偏离模式出现，不能作为开篇理论框架。
- 不要把“搜索减少”直接等同于“判断质量下降”。第一篇的关键是区分理性信息压缩、有害的信息获取偏离和主观—客观信息校准错配。

既有主要材料：

- `E:\Info_AI\主Agent\文章项目\01_算法权威与信息校准\当前第一章_算法权威与信息校准_基准稿.md`
- `E:\Info_AI\修改版本.md`
- `E:\Info_AI\dd636486-c2c3-485e-a8b5-0ec083e806dd_修改版｜算法权威与信息校准：生成式_AI_如何改变额外搜索与信念更新.pdf`
- `E:\Info_AI\defense_project\latex\main.tex`
- `E:\Info_AI\defense_project\latex\sections\01_intro_lit_review.tex`
- `E:\Info_AI\defense_project\latex\sections\02_framework_questions_hypotheses.tex`
- `E:\Info_AI\defense_project\latex\sections\03_research_design_and_studies.tex`
- `E:\Info_AI\defense_project\latex\sections\04_empirics_contributions_governance.tex`

注意：`defense_project/latex` 中仍有旧标题与旧表述，例如 Double Bayesian Distortion。制作 PPT 或讲稿时，应优先采用 `主Agent\文章项目\01_算法权威与信息校准\当前第一章_算法权威与信息校准_基准稿.md`，其次参考 `修改版本.md` 和上述“算法权威与信息校准”PDF 的新口径。

### 第二篇：Asymmetric Trust

这是另一篇后续研究，不是第一篇。

截至 2026 年 8 月 23 日，当前优先推进的新方向为：

- RP 构造思路：`E:\Info_AI\主Agent\文章项目\02_AI授权_EWA\研究计划构造思路_人类与AI错误的非对称权重_2026-08-23.md`
- 项目进展说明：`E:\Info_AI\主Agent\文章项目\02_AI授权_EWA\Paper2_项目进展说明_2026-08-23.md`
- 最新讨论总结：`E:\Info_AI\主Agent\文章项目\02_AI授权_EWA\AI_Human_Asymmetric_Error_Weighting_Discussion_Summary.md`
- 最新评语：`E:\Info_AI\主Agent\文章项目\02_AI授权_EWA\Asymmetric_Tolerance_评语_2026-08-23.md`
- 核心概念档案：`E:\Info_AI\主Agent\文章项目\02_AI授权_EWA\AI信任核心概念_Everett等2026_原文定义与文献来源_2026-08-22.md`
- 导师 PPT 想法存档：`E:\Info_AI\主Agent\文章项目\02_AI授权_EWA\导师PPT_Asymmetric_Tolerance_想法存档_2026-08-18.md`

当前状态：`FRAMING AND RESEARCH-QUESTION DEVELOPMENT`。经济激励已退出 Paper 2 主线；当前核心概念为 `Asymmetric Trust`，优先确认研究问题、理论冲突与贡献边界，不展开具体 Study 架构。

当前核心问题：

> Do people trust humans and AI differently under equivalent performance evidence?

当前理论结构：

1. `Asymmetric Trust` 暂定义为：可比任务绩效证据下，个体对 Human 与 AI 表现出的系统性信任差异。
2. Human 表示人类总体来源类别，不是参与者本人，也不是必须存在的单一专家。
3. 分开 objective task performance、perceived trustworthiness、attitudinal trust 与 trusting behaviour；不得把选择差异自动称为信任差异。
4. “同一绩效标准”是诊断问题；`relative AI error weight lambda_A` 是候选机制；两者都不取代 `Asymmetric Trust` 的核心位置。
5. 当前先回答差异出现在哪一层、由什么形成以及边界在哪里；函数形式和具体检验程序后置。

当前必须遵守的术语：

- Human 与 AI 的实验表现称为 `objective aggregate human error rate` 与 `objective AI error rate`；不得直接称为 `actual trustworthiness`。
- 参与者估计双方错误率称为 `perceived human/AI error rate`；它们是能力信念，不是信任构念。
- Human–AI 选择称为 `source choice`；不得自动称为 trust 或 trusting behaviour。
- `performance trust` 是独立量表构念，只用于 construct validity。
- `relative AI error weight lambda_A` 与 `alpha=lambda_A-1` 是待识别结构参数，不是成熟 AI 信任构念。

进入研究设计前的 framing 门：

1. 确认 Asymmetric Trust 的核心结果优先落在 perceived trustworthiness、attitudinal trust，还是 trusting behaviour。
2. 确认 trust calibration 与 algorithm aversion / appreciation 在 framing 中的主次关系。
3. 确认绩效判断与来源依赖评价是必须区分的解释层次。
4. 确认任务差异与 AI 特异性是当前论文的组成部分还是理论边界。
5. 确认标题中的 theory、adoption 与 regulation 各自需要达到的证据边界；之后再讨论具体研究设计。

历史方向边界：

- 早期 AI 错误、重复反馈和 EWA 路线目前暂缓，不再作为当前候选 RP 的直接设计。
- `E:\Info_AI\outputs\真实多Agent重做版\final\02_研究计划_当前基准版_2026-07-04.pdf` 变更为历史基准。
- Beauty contest、strategic belief game 和五种复杂协作架构继续列为已退回设计。
- `研究计划：经济激励能否纠正 AI 非对称容忍？.md` 与 `RP_AI使用经济激励与性能信任校准_正式稿_2026-08-03.md` 均变更为历史稿；其中术语分离与参数识别审计可以回收。

### 第三篇：AIA 责任归因

当前正式 Research Proposal 基准（用户于 2026-08-27 确认）：

- `E:\Info_AI\主Agent\文章项目\03_AIA责任归因\Paper3_加入群体后的新实验推进稿_2026-08-17.md`

当前研究围绕群体利益冲突中的 AI 决策代理、冲突升级与责任归因展开。后续修改默认在上述文件上推进；其他 proposal、实验笔记、材料地图、PPT 源稿和对话总结仅作为来源材料，不得被误称为现行基准。

“当前正式基准”表示项目内唯一现行 RP，仍保留 `UNVERIFIED DESIGN` 状态；不得据此声称实验已经验证、通过伦理审查或完成预注册。

### 候选 IDEA 档案：AI 错误不对称容忍与采用阈值

当前入口：

- `E:\Info_AI\主Agent\候选IDEA\01_AI错误不对称容忍与采用阈值\README.md`
- 原始 PPT：`E:\Info_AI\主Agent\候选IDEA\01_AI错误不对称容忍与采用阈值\00_原始材料\Asymmetric_Tolerance_July30.pptx`

当前状态与边界：

- 该目录的核心模型已于 2026 年 8 月 18 日进入 Paper 2 的当前整合候选 RP。
- 该目录继续保存导师原始 PPT、文献审计、实验草案和参数识别讨论，不单独称为 Paper 4。
- 原 PPT 的 `asymmetric tolerance parameter α` 仍是自定义结构参数；并入 Paper 2 不等于其已成为成熟理论构念。
- 必须继续分开：能力信念、固定来源折价 `delta`、来源依赖风险斜率 `alpha`、错误相关性、可纠正性、可追责性和一般算法来源效应。
- 核心 AI 非替代性检验仍为 human / rules-based algorithm / AI 三方对照。若 AI 与规则算法无差异，只能报告一般算法或自动化来源效应。

## 三、共享文献库入口与边界

三篇文章应尽量共享一个文献库，使引用关系、理论关系和知识图谱可以被统一管理。但共享文献库本身由单独的文献库 agent 负责更新，主 Agent 不负责日常入库、核查、下载 PDF 或重建知识图谱。

当前共享文献库主要在：

- `E:\Info_AI\defense_project\reference_materials`
- `E:\Info_AI\defense_project\latex\references.bib`
- `E:\Info_AI\references_new.bib`

文献库应至少覆盖以下方向：

1. 双重贝叶斯偏离相关文献：Bayesian updating、information acquisition、rational inattention、information design、non-Bayesian persuasion、AI summary、epistemic ownership。
2. 分离/来源标签/人机区分相关文献：same-summary source-label design、self vs AI、algorithmic authority、AI label effect、人类与 AI 来源效应。
3. EWA 与重复学习相关文献：EWA、reinforcement learning、belief learning、repeated games、beauty contest、human-AI delegation learning。
4. AIA 责任归因相关文献：AI agency、responsibility attribution、moral agency、control、intentionality、blame、accountability。该方向待补。

主 Agent 的职责：

- 记录共享文献库在哪里。
- 在写作、讲稿和评审时，知道三篇文章共用同一文献库。
- 如果发现某篇文章需要新文献，只提出“需要补文献”的任务说明，不擅自替代文献库 agent 的入库流程。
- 不制造第二套孤立 bib 或 PDF 目录。
- 当用户要求更新文献库时，应提醒或交给专门的文献库 agent 处理。

不属于主 Agent 的职责：

- 日常文献入库。
- 引用存在性核查。
- PDF 下载与归档。
- 文献知识图谱重建。
- 维护 `references.bib` 的完整性。

## 四、答辩材料原则

答辩材料应作为三篇文章的统一组合来准备，而不是孤立准备。

结构建议：

1. 总开场：整体研究主题、三篇文章之间的共同问题意识。
2. 第一节：双重贝叶斯偏离。
3. 第二节：AI 授权 / EWA / 重复策略信念任务。
4. 第三节：AIA 责任归因。
5. 总结：三篇文章如何共同构成一个关于生成式 AI、判断、授权和责任的研究计划。

当前答辩材料既有来源：

- `E:\Info_AI\outputs\019e9e26-a704-79e1-8478-8a7f65a6f8d3\presentations\defense-project`
- `E:\Info_AI\outputs\研究计划执行产出\AgentA_监管与答辩材料`
- `E:\Info_AI\outputs\真实多Agent重做版\final`

写讲稿时：

- 要明确当前讲的是第几篇。
- 讲稿要能直接开口讲。
- 不要把讲稿写成摘要、文献综述或审稿意见。

## 五〇、学术术语与表达禁令

- 禁止把 Agent 临时组合的词语当作理论概念、构念、机制或变量。尤其禁止使用“规范行为线索”这类没有明确原始术语、理论定义和文献来源的表达。
- 提出任何术语前，必须能够给出：文献使用的原始英文、来源论文、原文定义、分析层级、模型位置和经验测量。缺少其中任何一项时，不得将其写入研究问题、假设、理论模型、control 设计或论文正文。
- 文献没有稳定概念时，直接使用普通句子描述可观察事实。例如写“AI 拒绝有害指令并解释拒绝理由”，不得自行概括为一个新的“线索”“机制”“效应”或“能力”。
- 如果为了讨论方便必须使用临时描述，必须当场标明“这是描述性说法，不是文献构念”，并且不得沿用到正式研究材料。
- 优先使用本领域读者能够直接理解的常用术语。生僻术语只有在原始理论确实使用、且它能区分竞争性解释时才能保留；首次出现必须用普通语言解释。

## 五、常见禁区

- 不要再把 AI 授权/EWA 那篇称为“第一篇文章”。
- 不要把第一篇继续称为“双重贝叶斯偏离”或把 Double Bayesian Distortion 放进主标题，除非用户明确要求讨论旧稿。
- 不要把第一篇写成简单的“AI 让人少搜索，所以判断更差”。
- 不要把 double Bayesian distortion 当成必然成立的理论预设；当前版本中它只能作为可能经验结果或偏离模式谨慎出现。
- 不要在第二篇中加入金融学、行为金融学或投资决策贡献。
- 不要在第三篇正式确定前，擅自把 AIA 责任归因写成某一个固定理论模型。
- 不要让共享文献库分裂成互相不连通的三套引用系统。
