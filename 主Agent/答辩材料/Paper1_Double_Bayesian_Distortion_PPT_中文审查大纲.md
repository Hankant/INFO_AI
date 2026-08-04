# 已废弃说明

本文件对应的是旧口径，**不要再作为第一篇正式 PPT 大纲继续使用**。

当前第一篇应改用：
`算法权威与信息校准：生成式 AI 如何改变额外搜索与信念更新`

新的正式审查大纲见：
`E:\Info_AI\主Agent\答辩材料\Paper1_Algorithmic_Authority_and_Information_Calibration_PPT_中文审查大纲.md`

---

# 第一篇 PPT 中文审查大纲

对应英文答辩 PPT 主题：
`Paper 1: Algorithmic Authority and Double Bayesian Distortion`

本文件用于审查第一篇英文 PPT 的内容结构。最终 PPT 应为英文；本文件只提供中文说明、英文页标题建议、每页核心信息与执行提醒。

## 总体口径

- 这一篇研究的是 `evidence -> belief` 的映射如何被生成式 AI 重构。
- 不要把问题写成简单的 “AI makes people search less, therefore they judge worse.”
- 必须区分三件事：
  - 用户是否看得更少
  - 用户是否对已看到的信息更新不足
  - 用户是否误判自己已经掌握了多少信息
- `Double Bayesian distortion` 在当前版本里是待检验的经验模式，不是理论预设。
- 设计可信度的核心是 `same-summary source-label design`：
  - AI-labeled summary 与 unlabeled summary 看到完全相同的 summary 文本
  - 唯一差别是是否标注为 AI 来源

## 页数建议

- 独立展示时：16 页
- 若与总领引言合并：可压到 15 页左右，但当前建议先按 16 页规划

## 页面大纲

### Slide 1

- 英文标题：
  `Paper 1: Algorithmic Authority and Double Bayesian Distortion`
- 页面任务：
  从总领引言进入第一篇，明确这一篇识别的是 `evidence -> belief` 机制。
- 核心信息：
  - 第一篇不讨论责任归属，也不讨论长期依赖校准
  - 它聚焦生成式 AI 如何改变证据接触、搜索停止与后验形成
- 视觉建议：
  - 作为 section title slide，延续旧英文 deck 的深色章节页风格
- 需要避免的旧版错误：
  - 不要一上来进入 Study 1 / Study 2 / Study 3 叙述
  - 不要把第一篇讲成泛泛的 algorithm aversion / authority 研究

### Slide 2

- 英文标题：
  `From searching evidence to receiving an interpreted answer`
- 页面任务：
  用生活化例子讲清楚 search engine logic 与 AI assistant logic 的顺序差异。
- 核心信息：
  - 左侧：Search engine logic
    - 用户面对的是多个来源、多个链接、多个冲突
    - 需要自己打开、比较、筛选、整合，再形成判断
    - 标签：`Evidence first -> interpretation later`
  - 右侧：AI assistant logic
    - 用户先收到一个已经组织好的定义、例子、框架和结论
    - 面对的是被筛选、被叙述、被压缩后的信息结构
    - 标签：`Interpreted answer first -> optional verification later`
  - 页面底部 punchline：
    - `This reversal creates two possible distortions: users may stop searching too early, and the AI's coherent narrative may make the concept feel more settled than the evidence actually warrants.`
- 视觉建议：
  - 必须做成清晰的左右对比图
  - 左边用多来源分散信息，右边用单一整合回答
- 需要避免的旧版错误：
  - 不要直接用抽象理论起手
  - 不要用 “虚数性” 之类不稳定表述
  - 英文尽量使用 `narrative coherence`、`fluency`、`apparent completeness`、`coherent explanation`

### Slide 3

- 英文标题：
  `Less search is not necessarily worse judgment`
- 页面任务：
  先切断一个错误直觉：AI summary 之后少搜索，不必然代表更差判断。
- 核心信息：
  - 分成两个分支：
    - `Efficient compression`
      - less search
      - no loss in posterior quality
    - `Harmful deviation`
      - less search
      - higher full-information deviation
  - 这一页要明确：
    - AI 的核心功能本来就是降低检索、筛选、整合成本
    - 所以问题不是 “有没有少搜索”，而是 “少搜索之后是否偏离规范判断”
- 视觉建议：
  - 一个中间问题框，往下分出两条路径
- 需要避免的旧版错误：
  - 不要把 “search reduction” 直接翻译成 “search laziness”
  - 不要在这里提前断言 distortion 已经存在

### Slide 4

- 英文标题：
  `Existing work rarely separates evidence acquisition from belief updating`
- 页面任务：
  界定 research gap，不是说别人没研究 AI，而是说现有研究较少把三个层次拆开。
- 核心信息：
  - 现有工作常研究：
    - trust
    - adoption
    - automation bias
    - advice-taking
  - 但较少严格区分：
    1. 用户是否看得少
    2. 用户是否看到了但没有正确更新
    3. 用户是否主观上误判自己掌握了多少信息
- 视觉建议：
  - 上半部分列 existing work
  - 下半部分列 what remains conflated
- 需要避免的旧版错误：
  - 不要把 gap 写成 “nobody has studied this”
  - 不要把第一篇简单并入 general AI trust literature

### Slide 5

- 英文标题：
  `AI summaries create a perceived signal structure`
- 页面任务：
  引出当前版本最关键的 conceptual move。
- 核心信息：
  - 用户看到的不只是一个结论
  - 用户还会推断：
    - AI 是否已经搜索过更多信息
    - 是否已经筛选过噪音
    - 是否已经整合过冲突证据
    - 是否已经处理过反方信息
  - 这就是 `perceived signal structure`
- 视觉建议：
  - 可做成 “visible answer” 与 “inferred hidden process” 两层结构
- 需要避免的旧版错误：
  - 不要把 AI summary 写成单纯内容输入
  - 不要忽略用户对 summary 背后信息结构的心理推断

### Slide 6

- 英文标题：
  `Path 1: AI may reduce the perceived value of additional evidence`
- 页面任务：
  展开第一条机制路径：信息获取偏离。
- 核心信息：
  - AI summary 看起来已经很完整
  - 用户因此高估信息充分性
  - 额外证据的边际价值在主观上下降
  - 搜索停止阈值前移
  - 机制关键词：
    - `illusion of algorithmic exhaustiveness`
    - `sufficiency illusion`
- 视觉建议：
  - 从 `AI summary` 指向 `perceived sufficiency`，再指向 `lower search willingness`
- 需要避免的旧版错误：
  - 不要写成 “AI makes people lazy”
  - 要保留“这可能是心理机制，不是道德评价”

### Slide 7

- 英文标题：
  `Path 2: AI may reduce updating on later counterevidence`
- 页面任务：
  展开第二条机制路径：后续更新偏离。
- 核心信息：
  - AI 的流畅叙事把模糊性和冲突压缩成连贯解释
  - 后续反向证据更容易被看成局部例外
  - 结果是后验更新不足
  - 机制关键词：
    - `ambiguity compression`
    - `narrative anchoring`
    - `under-updating`
- 视觉建议：
  - 先有 coherent initial answer，再出现 later counterevidence，但 counterevidence 权重被压低
- 需要避免的旧版错误：
  - 不要把机制写成 generic anchoring bias 就结束
  - 这里强调的是 AI narrative 对 diagnosticity perception 的影响

### Slide 8

- 英文标题：
  `Double Bayesian distortion is a testable pattern, not an assumption`
- 页面任务：
  正式定义论文名里的核心概念，同时降调，避免像先验结论。
- 核心信息：
  - `information-acquisition distortion`
  - `belief-updating distortion`
  - 这两者可以同时出现，也可以只出现其中之一
  - 当前论文把它作为可检验经验模式，而不是理论预设
- 视觉建议：
  - 用双路径结构汇总 slide 6 和 slide 7
- 需要避免的旧版错误：
  - 不要把 double Bayesian distortion 写成必然成立的理论事实

### Slide 9

- 英文标题：
  `The study asks three linked questions`
- 页面任务：
  把研究问题清晰列出来，为后面实验设计服务。
- 核心信息：
  - `RQ1`
    - Does an AI-labeled summary change the stopping threshold for additional search?
  - `RQ2`
    - Is reduced search efficient compression or Bayesian information-acquisition distortion?
  - `RQ3`
    - Do subjective information mastery and objective judgment quality become misaligned?
- 视觉建议：
  - 三条编号问题，保持简洁
- 需要避免的旧版错误：
  - 不要再沿用旧版 proposal 的宽泛问题设定
  - 三个问题必须表现为递进关系

### Slide 10

- 英文标题：
  `A 3 x 2 design separates content, label, and evidence representativeness`
- 页面任务：
  给出实验设计总体结构。
- 核心信息：
  - 三个呈现条件：
    - `no-summary control`
    - `unlabeled summary`
    - `AI-labeled summary`
  - 两种 summary / evidence representativeness：
    - `representative summary`
    - `incomplete summary`
  - 这一页的任务是让听众先看懂 design matrix
- 视觉建议：
  - 明确的 3 x 2 表格或矩阵图
- 需要避免的旧版错误：
  - 不要塞进太多流程细节
  - 这一页先讲结构，不先讲统计

### Slide 11

- 英文标题：
  `The same-summary source-label design isolates the AI label effect`
- 页面任务：
  强调识别策略，这是方法可信度的核心页。
- 核心信息：
  - AI-labeled 与 unlabeled 组看到完全相同的 summary 正文
  - 唯一差别是是否标注 “generated by AI”
  - 因而两组差异不能归因于内容本身，只能归因于来源标签与算法权威效应
- 视觉建议：
  - 左右放同一段 summary
  - 只高亮顶部标签差异
- 需要避免的旧版错误：
  - 不要把 label effect 和 content effect 混在一起
  - 这页要成为 methods credibility 的记忆点

### Slide 12

- 英文标题：
  `A controlled evidence pool makes Bayesian benchmarks computable`
- 页面任务：
  让听众理解为什么这个任务可以算出规范后验。
- 核心信息：
  - 公司风险判断任务
  - 固定证据库
  - 每条证据有明确方向和 likelihood ratio
  - 被试报告 posterior probability
  - 研究者因此可以把 “看到了什么” 与 “应当更新到什么程度” 对齐
- 视觉建议：
  - 证据池示意图 + 风险判断任务框
- 需要避免的旧版错误：
  - 不要把证据结构讲得像开放文本世界
  - 必须强调 “controlled evidence pool”

### Slide 13

- 英文标题：
  `Bayesian updating provides the normative reference point`
- 页面任务：
  给出规范评价基准。
- 核心信息：
  - 放核心公式：
    - `logit(posterior) = logit(prior) + sum log(LR_j)`
  - 解释要点：
    - 论文不只看用户点了多少条证据
    - 更看最终后验是否接近规范贝叶斯基准
- 视觉建议：
  - 公式 + 简短解释
- 需要避免的旧版错误：
  - 不要把公式页做成纯 technical dump
  - 一定要把公式与“normative benchmark”连起来

### Slide 14

- 英文标题：
  `Two deviations distinguish “seeing less” from “updating worse”`
- 页面任务：
  介绍两个偏离指标，这是全文识别逻辑的关键页。
- 核心信息：
  - `Conditional Bayesian deviation`
    - Did the participant correctly absorb the information actually seen?
  - `Full-information deviation`
    - How far is the final judgment from the benchmark under the full evidence pool?
  - 这两个指标一起区分：
    - 看得少但更新准
    - 看得多但更新差
    - 看得少且信息不足
- 视觉建议：
  - 左右双框对比
- 需要避免的旧版错误：
  - 不要把 deviation 只写成 generic judgment error
  - 这页必须让听众记住 “seeing less” 与 “updating worse” 是两回事

### Slide 15

- 英文标题：
  `AI may improve information access while weakening epistemic ownership`
- 页面任务：
  引入主观—客观校准错配，给第一篇增加更强的行为科学贡献。
- 核心信息：
  - 自主搜索者可能：
    - 查阅更多
    - ownership 更强
    - 但未必更准确
  - AI summary 使用者可能：
    - 后验更接近规范基准
    - 但主观掌握感更低
  - 关键词：
    - `epistemic ownership`
    - `calibration gap`
    - `information calibration mismatch`
- 视觉建议：
  - 一个二维图或对照表，区分 objective performance 与 subjective mastery
- 需要避免的旧版错误：
  - 不要把 ownership 误写成责任归属问题
  - 这里讲的是知识掌握感，不是 blame

### Slide 16

- 英文标题：
  `The contribution is to locate where AI distorts belief formation`
- 页面任务：
  总结本篇贡献，并自然为后续 results / empirics 部分预留空间。
- 核心信息：
  - `Theory`
    - 从 AI trust / adoption 转向 evidence-to-belief mechanism
  - `Method`
    - 用可计算贝叶斯基准区分 acquisition distortion 与 updating distortion
  - `Governance`
    - AI governance 不应只要求 “verify more”
    - 更应校准用户对证据充分性的判断
- 视觉建议：
  - 三点贡献结构，简洁有力
- 需要避免的旧版错误：
  - 不要把治理含义写成空泛的 “humans should be careful”
  - 要保留当前版本里对 `perceived sufficiency` 的治理含义

## 与旧英文 PPT 的衔接原则

- 可以参考旧英文 20 页 deck 的美术风格、节奏、章节页、米白正文与低饱和强调色。
- 不能直接沿用旧版内容中与当前文档不一致的部分，尤其是：
  - 旧的 Study 1 / 2 / 3 分法
  - revision review 口径
  - 把搜索减少直接等同于判断劣化的叙述
- 当前第一篇应以这些材料为准：
  - `E:\Info_AI\修改版本.md`
  - `E:\Info_AI\defense_project\latex\sections\01_intro_lit_review.tex`
  - `E:\Info_AI\defense_project\latex\sections\02_framework_questions_hypotheses.tex`
  - `E:\Info_AI\defense_project\latex\sections\03_research_design_and_studies.tex`
  - `E:\Info_AI\defense_project\latex\sections\04_empirics_contributions_governance.tex`

## 下一步建议

- 先审这 16 页结构是否要压到 15 页
- 再进入英文可视化版 PPT 具体制作
- Slide 2、Slide 11、Slide 14 是最关键的三张识别页，后续制作时应优先保证它们最清晰
