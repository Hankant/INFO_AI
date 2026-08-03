# 主 Agent 项目级指令

本文件是 `E:\Info_AI` 的主控记忆文件。它的主要作用不是替代各专项 agent，而是记录项目结构、文章映射、已有工作和关键口径，减少长期对话中的记忆破损与重复沟通。

人工导航与 Agent 台账：

- `E:\Info_AI\主Agent\00_项目导航.md`
- `E:\Info_AI\主Agent\01_Agent职责与成果台账.md`

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
| Paper 2 | belief / feedback → action threshold | AI-mediated reliance calibration / early AI error as calibration shock | Calibration shock |
| Paper 3 | action → responsibility | ownership dilution / responsibility sharing | Ownership dilution |

统一性：

- 三篇都研究 AI 如何作为 decision architecture 改变高风险人类决策。
- 三篇共享一个过程链条：信念形成、依赖校准/行动阈值、责任归属。
- 三篇共同回应现有文献常把 AI 效应混成总量结果，而较少区分信息路径、认知依赖路径和责任路径的问题。

独立性：

- 第一篇隔离 evidence-to-belief 机制。
- 第二篇隔离 belief/feedback-to-action-threshold 机制。
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

### 第二篇：AI 授权 / EWA / 重复反馈依赖校准

这是另一篇后续研究，不是第一篇。

当前状态：

- 旧的“重复策略信念任务 / beauty contest / repeated decision game”版本已被判断为与研究问题存在结构性错配，默认不再作为基准设计。
- 第二篇真正要识别的核心不是高阶博弈推理本身，而是：在重复反馈中，即使 AI 与 human source 的总体表现相同，早期 AI 错误是否会引发更强、更持久的后续低依赖 / 低授权。
- 后续版本应优先采用 repeated forecasting / judgment / social prediction with AI advice 的任务框架，而不是默认采用 beauty contest。

当前建议题目与关键词：

- Early AI Errors and Persistent Under-Reliance in Repeated Forecasting with Feedback
- AI early errors
- dynamic reliance calibration
- source-specific learning
- repeated feedback
- reduced-form dynamic analysis
- simplified EWA / experience-weighted reliance updating

用户偏好的 research gap：

1. AI 错误与人类错误的不对称性。
2. 多轮反馈或长期互动中的学习，而不是单轮 trust、advice adoption 或 calibration。

写作注意：

- 不要把这篇带到金融学、行为金融学、投资决策或金融市场框架，除非用户明确要求。
- 不要再把 beauty contest 当作默认任务骨架；除非用户明确要求保留，否则应改写为更干净的 repeated forecasting / judgment 任务。
- 如果保留 EWA，只应保留其 attraction / weight-updating 思想，并尽量写成可估计的简化版本，而不是完整博弈学习模型。
- 不要过度强调“责任”“高责任流程”“治理红线”等，除非明确是在写治理意义。
- 如果实验只有约 20 轮，不要过度使用“长期锁定”或“长期稳态”。更合适的表述是“有限重复窗口”“20 轮窗口内的持续性低授权”。
- 任务设计应尽量减少额外混淆，尤其要避免“参与者自己在学习任务结构”与“参与者在更新对 AI 的依赖”混在一起。

既有主要材料：

- `E:\Info_AI\outputs\真实多Agent重做版`
- `E:\Info_AI\outputs\研究计划执行产出`
- 当前用户修订后的项目内基准文件：
  `E:\Info_AI\outputs\真实多Agent重做版\final\02_研究计划_当前基准版_2026-07-04.pdf`
- 此前用户退回的旧基准附件：
  `C:\Users\69596\.codex\attachments\90d4f461-ff0f-4214-a96b-05861a460641\pasted-text.txt`

这些材料的使用边界：

- 新 PDF 是当前项目内基准；上述其余材料主要作为“被退回版本”和“可回收组件”的来源，而不是直接续写底稿。
- 可保留的成分主要包括：early vs late vs distributed error 思路、AI/human performance parity、reduced-form 主分析、简化 EWA 机制检验。
- 需要整体放弃或重写的成分主要包括：beauty contest 任务骨架、strategic belief game framing、五种复杂协作架构同时并列的设计。

注意：

- 除非用户明确要求，不要继续沿用：
  `E:\Info_AI\outputs\真实多Agent重做版\final\04_研究计划_20轮策略信念任务打磨版.md`
- 默认也不要把 `E:\Info_AI\主Agent\文章项目\02_AI授权_EWA\README.md` 中旧版 strategic belief 口径视为现行设计；应以后续重构版本为准。

### 第三篇：AIA 责任归因

第三篇尚未正式展开，先保留项目空位。

暂定方向：

- AIA / AI agent / AI-assisted action 中的责任归因。
- 可能关注人在 AI 参与决策或行动后，如何归因责任、能力、意图、控制权和过错。
- 后续需要单独确定理论框架、文献边界、实验设计和与前两篇的关系。

当前状态：

- 目录已预留：`E:\Info_AI\主Agent\文章项目\03_AIA责任归因`
- 不要擅自替第三篇确定具体题目或理论主张。可以先建立问题清单和文献入口。

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

## 五、常见禁区

- 不要再把 AI 授权/EWA 那篇称为“第一篇文章”。
- 不要把第一篇继续称为“双重贝叶斯偏离”或把 Double Bayesian Distortion 放进主标题，除非用户明确要求讨论旧稿。
- 不要把第一篇写成简单的“AI 让人少搜索，所以判断更差”。
- 不要把 double Bayesian distortion 当成必然成立的理论预设；当前版本中它只能作为可能经验结果或偏离模式谨慎出现。
- 不要在第二篇中加入金融学、行为金融学或投资决策贡献。
- 不要在第三篇正式确定前，擅自把 AIA 责任归因写成某一个固定理论模型。
- 不要让共享文献库分裂成互相不连通的三套引用系统。
