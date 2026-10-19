# Blueprint: Asymmetric Trust Research Plan

## 论文类型

New problem/setting paper。核心贡献不是首次发现某个来源偏好，也不是发明一个参数，而是把相反方向的 Human–AI 信任差异放入同一个比较校准框架，并把其心理位置与采用后果分开。

## 一句话研究目标

解释人们对 AI 的 performance trust 何时、为何偏离相关 Human alternative 所提供的比较基准，以及这种偏离如何转化为 under-adoption、over-adoption 和部署门槛失准。

## 逻辑链

| 模块 | 内容 |
|---|---|
| 现实背景 | 医疗、自动驾驶等部署问题的真实备选项通常是 Human 与 AI，而不是 AI 与零错误理想系统。 |
| 文献限制 1 | Trust calibration 说明信任应与能力匹配，却通常缺少 Human–AI 的共同比较结构。 |
| 文献限制 2 | Algorithm aversion、appreciation、automation bias 与门槛研究给出负向、正向和零效应，却使用不同因变量和参照。 |
| 文献限制 3 | 观察到来源差异时，现有研究常无法区分能力误判、固定来源偏好与来源依赖错误权重。 |
| 核心目标 | 建立以 human counterfactual 为规范锚点的双向 Asymmetric Trust 框架。 |
| 挑战 1 | 同等来源差异可能发生在感知绩效、信任态度或行为选择的不同环节。 |
| 挑战 2 | 固定来源偏好与随错误风险变化的权重产生相似的平均采用差异。 |
| 挑战 3 | 来源差异的方向可能因任务与比较信息改变，平均零效应可能掩盖双向异质性。 |
| 方法模块 1 | 分列 objective task performance、perceived accuracy/perceived trustworthiness、performance trust 和 source choice。 |
| 方法模块 2 | 通过多水平绩效风险比较估计固定来源项 delta 与来源依赖斜率 tau，并比较替代函数形式。 |
| 方法模块 3 | 用 joint versus separate human benchmark information 检验比较基准能否缩小偏离；报告参数分布和任务异质性。 |

## 核心研究问题

> When and why does trust in AI deviate from the human-counterfactual benchmark?

## 分析问题

1. 在同等绩效证据下，AI 与 Human 是否获得不同的 performance trust？
2. 差异来自 perceived performance、固定来源偏好，还是 source-dependent error weighting？
3. Asymmetric Trust 何时转化为 under-adoption 或 over-adoption？
4. 显示可比较的 Human performance benchmark 能否减少偏离？

## 理论构件

| 构件 | 文献身份 | 模型作用 |
|---|---|---|
| Trust calibration / appropriate reliance | 既有理论框架；Lee & See (2004), Everett et al. (2026), Mehrotra et al. (2024) | 给出“高信任不是目标、匹配才是目标”的规范标准 |
| Algorithm aversion | 既有行为现象；Dietvorst et al. (2015) | 负向来源效应候选区域 |
| Algorithm appreciation / automation bias | 既有行为现象；Logg et al. (2019) 等 | 正向来源效应候选区域 |
| Evaluability hypothesis | 既有理论；Hsee (1996) | 预测共同展示 Human benchmark 提高绩效属性的可评价性 |
| Human counterfactual | 本文规范基准 | 规定 AI 应与哪个现实替代来源比较 |
| Asymmetric Trust | 本文限定的新问题框架 | 描述同等决策相关证据下的 Human–AI performance-trust 差异 |
| tau / delta | 本文简约参数 | 分别表示来源依赖错误权重与固定来源项；不是信任构念 |

## 竞争性预测

1. 来源中立：matched evidence 下，Human 与 AI 的信任和风险斜率相同。
2. Excess intolerance：AI 的 performance trust 更低或 AI 错误权重更高，造成 under-adoption。
3. Excess tolerance：AI 的 performance trust 更高或 AI 错误权重更低，造成 over-adoption。
4. Belief explanation：差异在 perceived performance 被纳入后消失。
5. Fixed preference：来源产生水平差，但来源 × 风险斜率不变。
6. Source-dependent weighting：控制能力信念和固定来源项后，来源 × 风险斜率仍不同。

## 贡献—证据映射

| 预期贡献 | 需要的证据 | 未获得证据时的降级表述 |
|---|---|---|
| Human–AI comparative calibration framing | 构念分离、共同基准与可比任务成立 | 仅称为比较评价框架 |
| 统一 aversion 与 appreciation | signed effect 在同一设计中可估，且方向/异质性可报告 | 仅报告特定场景来源差异 |
| 来源依赖权重机制 | tau 可与 delta、perceived performance 及一般风险函数分离 | 仅报告 reduced-form source effect |
| AI 特异性 | AI 与 Human、rules-based algorithm 均可区分 | 改称算法/自动化来源效应 |
| 监管含义 | 部署/政策阈值与 welfare benchmark 被明确建模或测量 | 仅保留 adoption implication，不把公众偏好称为实际监管 |
