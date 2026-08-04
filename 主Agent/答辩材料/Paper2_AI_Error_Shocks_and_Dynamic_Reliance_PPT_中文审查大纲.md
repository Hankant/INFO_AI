# Paper 2 PPT 中文审查大纲

对应英文 section deck 标题建议：
`AI Error Shocks and Dynamic Reliance in Repeated Human-AI Decision Tasks`

对应中文标题建议：
`AI 错误冲击与重复人机决策中的动态依赖：一项基于 EWA 启发的实验研究`

当前唯一优先基准：
- `E:\Info_AI\outputs\真实多Agent重做版\final\02_研究计划_当前基准版_2026-07-04.pdf`

辅助规则与任务来源：
- `E:\Info_AI\主Agent\AGENTS.md`
- `E:\Info_AI\主Agent\答辩材料\README.md`
- `E:\Info_AI\主Agent\答辩材料\Paper2_PPT_任务单_2026-07-05.md`
- `E:\Info_AI\主Agent\答辩材料\PPT_叙事顺序与文献使用总则_2026-07-05.md`
- `E:\Info_AI\主Agent\答辩材料\Paper2_讲稿与口头解释策略_2026-07-05.md`
- `E:\Info_AI\主Agent\答辩材料\Paper2_可视化与复杂实验讲清楚技巧_2026-07-05.md`

总页数建议：
- 11 页
- 仍在允许范围 9–11 页内

## 当前叙事总原则

这套 Paper 2 deck 必须服从统一顺序：

`生活化例子 -> 现有研究 -> 传统理解 -> gap -> RQ -> framing -> 机制 -> 实验原型要求 -> 具体设计 -> 预期结果与贡献`

因此：
- 不要一上来进入 treatment 条件和变量表。
- 不要前 3 页就把方法细节推出来。
- 文献优先服务于 `existing work / traditional view / gap`，而不是只在后面挂 citation。
- `performance parity` 必须作为识别前提，而不是普通控制项。

## 核心口径

- 这篇研究的对象不是 generic trust。
- 当前主线是 `dynamic reliance under repeated feedback`。
- 关键问题不是“AI 会不会犯错”，也不是“人们是否讨厌错误”。
- 关键问题是：在总体表现相同的前提下，`AI error` 是否比 `human error` 更容易被当作关于来源本质的不利信号，因此在后续多轮反馈中引发更持久的低依赖。
- `reduced-form path evidence` 是主证据。
- `EWA-inspired model` 是机制层解释，不抢主位。

## 需要避免的旧口径错误

- 不要把问题讲成“AI 错一次，大家就不想再用”。
- 不要把 `AI-specific asymmetry` 误写成一般性的 error aversion。
- 不要忽略 human error 作为对照来源。
- 不要回到 `beauty contest / strategic belief task`。
- 不要把 EWA 讲得比研究问题本身更重要。
- 不要把有限轮次说成长稳态或长期锁定。

## 页面大纲

### Slide 1

- 英文标题建议：
  `Paper 2: AI Error Shocks and Dynamic Reliance`
- 中文核心信息：
  - 明确这是三篇中的第二篇。
  - 对应链条中的 `belief / feedback -> reliance calibration / action threshold`。
  - 开场页只负责定位，不负责进入方法。
- 对应基准来源：
  - `AGENTS.md` 中 Paper 2 的位置
  - `2026-07-04` PDF 首页摘要
- 需要避免的旧口径错误：
  - 不要把封面副标题写成 generic trust。

### Slide 2

- 英文标题建议：
  `The puzzle is not whether people dislike errors, but how they learn from them over time`
- 中文核心信息：
  - 用具体高风险场景进入，例如医疗辅助判断或自动驾驶监控。
  - 同样一次失误，如果来自 AI，人们可能更容易把它理解为“这个来源本身不可靠”。
  - 如果来自 human colleague，人们更可能把它理解为“这次失误，但后续仍可继续校准”。
  - 这一页要讲清楚：真正的 puzzle 不是单次反应，而是后续多轮依赖路径是否恢复。
- 对应基准来源：
  - `2026-07-04` PDF 的研究动机部分
  - `Paper2_讲稿与口头解释策略_2026-07-05.md`
- 需要避免的旧口径错误：
  - 不要写成“AI 回复错了，所以大家以后不用 AI”。
  - 不要把例子写成只针对 AI、自身没有 human 对照。

### Slide 3

- 英文标题建议：
  `Most existing work is still built around one-shot trust or one-shot advice use`
- 中文核心信息：
  - 现有研究主要看：
    - algorithm aversion
    - advice taking
    - trust in automation
    - appropriate reliance
  - 但大量研究仍是单轮或近似单轮反应。
  - 它们更擅长回答“这次错误后是否少采纳”，不擅长回答“后续多轮依赖路径如何更新”。
- 对应基准来源：
  - `2026-07-04` PDF 文献综述部分
  - `PPT_叙事顺序与文献使用总则_2026-07-05.md`
- 需要避免的旧口径错误：
  - 不要把这一页做成作者姓名堆砌。
  - 不要过早进入 shock timing。

### Slide 4

- 英文标题建议：
  `A symmetric learning view would predict similar updating from similar errors`
- 中文核心信息：
  - 传统理解是：如果 AI 和 human 的总体表现相同，那么理性学习者应当对相似错误作出相似更新。
  - 也就是说，错误只是 performance signal，而不是 source-specific signal。
  - 如果后续观察到 AI error 带来更持久的低依赖，就说明错误不只是“错了”，而是被赋予了更强的来源诊断意义。
- 对应基准来源：
  - `2026-07-04` PDF 中关于 parity 与识别逻辑的部分
- 需要避免的旧口径错误：
  - 不要把传统 benchmark 写成“AI 错了以后理应完全恢复信任”这种过强表述。
  - 这里讲的是对称更新基准，不是空泛的理性人设定。

### Slide 5

- 英文标题建议：
  `The gap has two parts: existing work is rarely multi-round, and it rarely isolates AI-specific diagnostic asymmetry`
- 中文核心信息：
  - 明确讲出两个 gap：
  - `Gap 1: multi-round gap`
    - 很多研究不是多轮，无法观察早期错误如何持续影响后续依赖路径。
  - `Gap 2: asymmetry gap`
    - 很少有研究在总体表现相同的条件下，直接比较 `AI error` 与 `human error` 是否具有不同诊断权重。
  - 这一页要形成一句 punchline：
    - 本文研究的不是 generic distrust，而是 `dynamic asymmetry under repeated feedback`。
- 对应基准来源：
  - `2026-07-04` PDF 中研究 gap 与问题提出部分
- 需要避免的旧口径错误：
  - 不要把 gap 写成一句泛泛的“较少研究”。
  - 不要漏掉 human comparison。

### Slide 6

- 英文标题建议：
  `These gaps lead to one framing: dynamic reliance after source-specific error shocks`
- 中文核心信息：
  - 由 gap 引出研究问题：
    - 在 repeated feedback 中，依赖是否随相对表现更新？
    - early AI error 是否比 early human error 更容易压低后续 adoption path？
    - 这种效应是否取决于 timing？
  - 再明确 framing：
    - 不是静态 trust
    - 而是 repeated-feedback 条件下的 dynamic reliance updating
- 对应基准来源：
  - `2026-07-04` PDF 中 RQ / H 部分
- 需要避免的旧口径错误：
  - 不要让 RQ 先于 gap 出现。
  - 不要把 RQ 直接写成方法语言。

### Slide 7

- 英文标题建议：
  `A local failure can become a calibration shock`
- 中文核心信息：
  - 机制链条：
    - local miss
    - negative updating of source attractiveness
    - lower later adoption
    - persistent under-reliance
  - 机制维度要点明两条：
    - timing heterogeneity
    - source asymmetry
  - 这里可以自然引出为什么后面要做 early / mid / distributed shock。
- 对应基准来源：
  - `2026-07-04` PDF 中机制与假设部分
- 需要避免的旧口径错误：
  - 不要直接贴 EWA 参数。
  - 不要让机制页抢过 framing 页。

### Slide 8

- 英文标题建议：
  `The experimental prototype must satisfy five identification requirements`
- 中文核心信息：
  - 这一页先讲为什么这种实验原型合理，再讲设计。
  - 原型必须满足：
    - repeated rounds
    - observable updating path
    - full feedback after each round
    - abstract standardized environment
    - parity-controlled source usefulness
  - 回答的问题是：
    - 为什么必须用这种 task prototype
    - 它隔离了什么机制
- 对应基准来源：
  - `2026-07-04` PDF 的设计逻辑部分
- 需要避免的旧口径错误：
  - 不要把这一页写成变量清单。

### Slide 9

- 英文标题建议：
  `Hypotheses, manipulations, comparisons, and parity standards align cleanly`
- 中文核心信息：
  - 这是硬性表格页。
  - 建议列：
    - `RQ / Hypothesis`
    - `Experimental Manipulation`
    - `Key Comparison`
    - `Parity Standard`
    - `What the Comparison Identifies`
  - 要让老师一眼看到：
    - `RQ / H -> manipulation -> comparison -> parity -> identification`
- 对应基准来源：
  - `2026-07-04` PDF 的假设、设计、分析部分
- 需要避免的旧口径错误：
  - 不要把整段假设原文塞进表里。

### Slide 10

- 英文标题建议：
  `Now the design becomes simple: vary timing, match performance, observe later reliance`
- 中文核心信息：
  - 这是实验流程可视化页。
  - 上层讲条件逻辑：
    - Balanced Error
    - Early Shock
    - Mid Shock
    - 用时间条和红块位置差异表达
  - 中间明确 `performance parity`：
    - same total payoff
    - same average performance
    - same overall error burden
    - same later recovery level
  - 下层讲单个受试者的一轮体验：
    - see task
    - make own judgment
    - observe source output
    - choose / allocate reliance
    - receive full feedback
    - update for next round
- 对应基准来源：
  - `2026-07-04` PDF 设计部分
  - `Paper2_可视化与复杂实验讲清楚技巧_2026-07-05.md`
- 需要避免的旧口径错误：
  - 不要把 30 轮完全展开。
  - 不要把 parity 放成脚注。

### Slide 11

- 英文标题建议：
  `We first expect a visible path effect and then explain why it persists`
- 中文核心信息：
  - 先讲预期结果，再讲分析层级。
  - 推荐层级：
    - visible reliance path
    - reduced-form identification
    - EWA-inspired mechanism
  - 核心 punchline：
    - 先证明路径变了；
    - 再证明这是 source-specific treatment effect；
    - 最后解释为什么恢复不完全。
- 对应基准来源：
  - `2026-07-04` PDF 分析与预期结果部分
- 需要避免的旧口径错误：

### Slide 12

- 英文标题建议：
  `The contribution is to identify path-dependent under-reliance after AI errors`
- 中文核心信息：
  - 理论贡献：
    - 从单轮 algorithm aversion 推进到 repeated dynamic reliance
  - 设计贡献：
    - 用 parity-controlled timing design 识别路径效应
  - 机制贡献：
    - 连接 reduced-form path effect 与 asymmetric learning
  - 与 dissertation 的关系：
    - Paper 1 研究 belief formation
    - Paper 2 研究 feedback 后的 reliance calibration
- 对应基准来源：
  - `2026-07-04` PDF 摘要与总结
  - `AGENTS.md` 三篇映射
- 需要避免的旧口径错误：
  - 不要空泛喊治理口号收尾。

## 版式与执行要求

- 英文字体优先 `Times New Roman`。
- 视觉保持与总领、Paper 1 同一家族：
  - 深色封面
  - 米白正文
  - 细线分区
  - 低饱和铜色 / 橄榄色强调
- 最值钱的方法页必须优先可读：
  - 表格页
  - 双层流程页
- 技术细节一律节制，只保留防误解与识别关键内容。

## 当前正式基准说明

- 本大纲以 `2026-07-04` PDF 为当前 Paper 2 正式内容基准。
- 旧 `beauty contest / strategic belief` 口径不再作为本 deck 的主线。
