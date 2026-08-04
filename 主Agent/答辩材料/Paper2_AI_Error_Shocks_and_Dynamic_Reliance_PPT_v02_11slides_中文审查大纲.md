# Paper 2 PPT 中文审查大纲 v02（11页）

对应英文 deck 标题：
`AI Error Shocks and Dynamic Reliance`

副标题口径：
`Repeated feedback, matched performance, and path-dependent under-reliance`

本版说明：
- 这是按 11 页重收后的版本，不再沿用之前误扩成 15 页的拆分页。
- 核心顺序重新锁定为：
  `具体问题 -> 现有研究 -> 传统基准 -> gap -> RQ / framing -> 机制 -> 原型要求 -> 表格识别 -> 流程设计 -> 预期结果与贡献`
- 强调 `dynamic reliance under repeated feedback`，不讲回 generic trust。

## Slide 1

- 英文标题：`Paper 2: AI Error Shocks and Dynamic Reliance`
- 核心信息：
  - 这是 dissertation 的第二篇。
  - 位置在 `belief / feedback -> reliance calibration`。
  - 开场只做定位，不进入技术细节。

## Slide 2

- 英文标题：`The puzzle is not whether people dislike errors, but how later reliance recovers`
- 核心信息：
  - 用重复高风险任务进入，而不是抽象模型。
  - 真正的 puzzle 不是“一次犯错后会不会讨厌 AI”，而是“后续依赖路径会不会恢复”。
  - 重点是 error shock 是否留下 longer shadow。

## Slide 3

- 英文标题：`Most existing work is still organized around one-shot trust or one-shot advice use`
- 核心信息：
  - 交代 algorithm aversion / advice taking / appropriate reliance 三条现有研究线。
  - 点明它们更擅长解释 immediate reaction，不擅长解释 later path updating。

## Slide 4

- 英文标题：`A symmetric learning view would predict similar updating from similar errors`
- 核心信息：
  - 这是传统 benchmark 页。
  - 如果 AI 与 self 的总体表现已配平，那么相似错误应带来相似更新。
  - 若 AI error 产生更持久惩罚，说明 error 被理解为 source-specific signal。

## Slide 5

- 英文标题：`The gap has two parts: most work is not multi-round, and most work does not isolate AI-specific diagnostic asymmetry`
- 核心信息：
  - Gap 1：缺少 multi-round path evidence。
  - Gap 2：缺少 matched-performance 下的 diagnostic asymmetry identification。
  - 这一页的 punchline 是：研究对象是 `dynamic asymmetry under repeated feedback`。

## Slide 6

- 英文标题：`These gaps lead to one framing: dynamic reliance after source-specific error shocks`
- 核心信息：
  - 提出核心研究问题。
  - 明确 framing：不是 static trust，而是 repeated-feedback reliance updating。
  - reduced-form path evidence 在前，EWA-inspired mechanism 在后。

## Slide 7

- 英文标题：`A local failure can become a calibration shock`
- 核心信息：
  - 机制链条：
    `local miss -> negative updating -> lower later adoption -> persistent under-reliance`
  - 单独强调两条机制维度：
    - timing heterogeneity
    - source asymmetry

## Slide 8

- 英文标题：`The experimental prototype must satisfy five identification requirements`
- 核心信息：
  - 不直接进 treatment，而先说明为什么这种实验原型合理。
  - 五个要求：
    - multi-round learning
    - full and counterfactual feedback
    - matched overall performance
    - nontrivial but manageable task
    - abstract standardized environment

## Slide 9

- 英文标题：`Hypotheses, manipulations, comparisons, and parity standards align cleanly`
- 核心信息：
  - 核心表格页。
  - 至少对齐：
    - `RQ / H`
    - `Experimental Manipulation`
    - `Key Comparison`
    - `Parity Standard`
    - `What It Identifies`
  - 这一页是老师一眼看懂识别逻辑的关键页。

## Slide 10

- 英文标题：`Now the design becomes simple: vary timing, match performance, observe later reliance`
- 核心信息：
  - 双层流程页。
  - 上层：Balanced / Early Shock / Mid Shock 的时间结构。
  - 中层：`performance parity` 卡片，明确 same total payoff / same error count / same average quality / same recovery level。
  - 下层：单个参与者一轮体验流程。

## Slide 11

- 英文标题：`We first expect a visible path effect and then explain why it persists`
- 核心信息：
  - 先展示 expected path shape，再总结贡献。
  - 贡献三点：
    - 从 one-shot aversion 推进到 repeated dynamic reliance
    - 用 parity-controlled timing design 识别 path effect
    - 用 EWA-inspired logic 解释 why recovery remains incomplete
  - 用一句 takeaway 收束：早期 AI miss 可能留下更持久的 under-reliance path。

## 本版相对前版的修正

- 从 15 页收回到 11 页。
- 去掉了此前第 7 页之后多出来的扩写页，不再拆出 `AI Distinctiveness`、`Narrative Authority` 之类的额外页。
- 恢复你确认过的叙事顺序，尤其补回：
  - `traditional benchmark`
  - `gap before RQ`
  - `prototype requirements before detailed design`
- 最后一页合并了 expected results 与 contribution，避免再次越讲越散。
