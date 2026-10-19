# Paper 2：Asymmetric Trust

## 当前项目状态

截至 2026 年 8 月 23 日，Paper 2 已从经济激励方向转向 **Asymmetric Trust**：可比绩效证据下的 Human–AI 信任差异。

当前工作标题：

> **Asymmetric Trust: A Behavioural Theory of AI Adoption and Regulation**

当前状态为 **FRAMING AND RESEARCH-QUESTION DEVELOPMENT**。经济激励已退出 Paper 2 主线；当前先确认研究问题、理论冲突与贡献边界，不展开具体 Study 架构。

## 当前核心问题

> **Do people trust humans and AI differently under equivalent performance evidence?**

研究分别考察 perceived trustworthiness、attitudinal trust 与 trusting behaviour 上的 Human–AI 差异，并区分这种差异来自感知绩效还是来源依赖评价。“同一绩效标准”是诊断问题；来源依赖错误权重是候选机制。

## 当前理论结构

导师 PPT 中的模型设想为：

\[
\widetilde L_H=L,
\qquad
\widetilde L_A=(1+\alpha)L.
\]

当前采用中性的重新参数化：

\[
\lambda_H=1,
\qquad
\lambda_A=1+\alpha>0.
\]

\(\lambda_A>1\) 表示 AI 错误高权重，\(\lambda_A=1\) 表示来源中性，\(0<\lambda_A<1\) 表示 AI 错误低权重。研究不预设方向。该参数只形式化“是否采用同一绩效标准”，不是成熟的信任构念，也不是当前阶段需要优先决定的完整统计模型。

## 术语边界

- Human 与 AI 的实验表现称为 `objective aggregate human error rate` 与 `objective AI error rate`。
- `perceived human/AI error rate` 是参与者对双方表现的主观判断，不是 trust 构念。
- Human–AI 实际选择称为 `source choice`；不能自动称为 trust 或 trusting behaviour。
- `performance trust` 作为独立量表构念，不承担规范基准功能。
- \(\lambda_A\) 与 \(\alpha\) 是本项目待识别的结构参数，不是成熟 AI 信任构念。
- 固定来源偏好 \(\delta_A\)、主观能力信念、一般风险函数和相对错误权重 \(\lambda_A\) 必须分开。

## 当前 framing 待确认事项

进入研究设计前先确认：

1. Asymmetric Trust 的核心结果应优先落在 perceived trustworthiness、attitudinal trust，还是 trusting behaviour；
2. 论文以 trust calibration 还是 algorithm aversion / appreciation 为首要理论对话对象；
3. 任务差异是当前论文的理论边界，还是必须直接回答的组成部分；
4. 标题中的 theory、adoption 与 regulation 各自需要达到什么证据边界。

## 当前文件入口

- RP 构造思路：`研究计划构造思路_人类与AI错误的非对称权重_2026-08-23.md`
- 项目进展：`Paper2_项目进展说明_2026-08-23.md`
- 最新讨论总结：`AI_Human_Asymmetric_Error_Weighting_Discussion_Summary.md`
- 最新评语：`Asymmetric_Tolerance_评语_2026-08-23.md`
- 核心概念档案：`AI信任核心概念_Everett等2026_原文定义与文献来源_2026-08-22.md`
- 导师 PPT 想法存档：`导师PPT_Asymmetric_Tolerance_想法存档_2026-08-18.md`
- 相关文献导航：`Paper2_EWA_参考文献导航.md`

## 历史方向及使用边界

### 重复反馈 / EWA 方向

早期 AI 错误、AI/human performance parity、动态分析和简化 EWA 曾是 Paper 2 的主线。该方向目前暂缓，不再作为当前候选 RP 的直接设计。相关材料仍可用于未来独立的动态研究。

### 经济激励方向

`研究计划：经济激励能否纠正 AI 非对称容忍？.md` 与 `RP_AI使用经济激励与性能信任校准_正式稿_2026-08-03.md` 均保留为历史稿。经济激励不再是当前 Paper 2 的研究问题；其中“支付反应、能力信念与行为选择应分开”的审计结论继续保留。

### Asymmetric Tolerance 候选目录

原候选目录继续保存导师 PPT、文献审计、实验草案和参数识别讨论。其测量与参数识别内容已进入当前 Paper 2；该目录本身仍是来源与方法档案。

## 当前一句话定位

> 本研究考察同等绩效证据是否在 Human 与 AI 之间产生不同的感知可信性、信任态度与信任行为，并区分这种 Asymmetric Trust 来自绩效判断还是来源依赖评价。
