# 研究计划：经济激励能否纠正 AI 非对称容忍？

## 暂定英文标题

**Can Incentives Correct Asymmetric Tolerance Toward AI? Performance Benchmarks, Belief Calibration, and AI Adoption**

备选标题：

**Paying People to Trust AI? Economic Incentives, Asymmetric Tolerance, and Performance Calibration**

**Correcting AI Under-Adoption or Buying Trust? Economic Incentives under Asymmetric Tolerance**

---

## 一、研究背景与核心问题

随着 AI 被越来越多地用于预测、诊断、招聘和组织决策，一个重要但尚未充分解决的问题是：人们是否使用相同的绩效标准评价 AI 和人类决策者。

Asymmetric Tolerance 框架认为，即使 AI 和人类错误产生相同的客观损失，AI 错误仍可能被赋予更高的主观权重：

\[
\tilde L_H=L,
\qquad
\tilde L_A=(1+\alpha)L,
\qquad
\alpha\geq0.
\]

因此，一个 AI 即使客观表现优于人类，也可能因为 \(\alpha>0\) 而不能达到行为上的采用门槛。

与此同时，现实组织越来越多地通过统一采购、费用报销、AI 使用额度和使用奖金等经济工具促进员工采用 AI。经济激励可以直接改变采用 AI 的私人收益，但它是否真正纠正了对 AI 的非对称容忍尚不清楚。更重要的是，经济利益还可能反过来改变使用者对 AI 能力的判断，从而产生新的 trust miscalibration。

本研究因此提出：

> **RQ：当 AI 与人类的客观能力可以直接比较时，个体是否表现出针对 AI 的非对称容忍？经济激励是在纠正这种非对称容忍，还是仅仅通过支付购买 AI 使用，甚至进一步扭曲个体对 AI 能力的判断？**

---

# 二、理论框架

## 2.1 理性采用基准

考虑一个决策者在 Human advisor \(H\) 与 AI advisor \(A\) 之间选择。

二者错误率分别为：

\[
e_H,\qquad e_A.
\]

每次错误造成损失 \(L\)。

若暂时忽略使用成本，则理性决策者应在：

\[
e_A<e_H
\]

时偏好 AI。

加入 AI 使用的净经济激励 \(g\) 后，理性采用条件可以表示为：

\[
(e_H-e_A)L+g>0.
\]

其中：

\[
g<0
\]

表示使用 AI 需要支付额外成本，

\[
g=0
\]

表示不存在额外使用成本，

\[
g>0
\]

表示采用 AI 可以获得经济奖励。

这是本文的 normative benchmark。

---

## 2.2 Asymmetric Tolerance

若个体对 AI 错误给予额外权重：

\[
\tilde L_A=(1+\alpha)L,
\]

则其感知采用条件变为：

\[
[e_H-(1+\alpha)e_A]L+g>0.
\]

其中：

\[
\alpha>0
\]

表示相同客观错误更难被容忍，只因为错误来源是 AI。

在 \(g=0\) 时，AI 被接受的错误率门槛为：

\[
\tilde e_A^*
=
\frac{e_H}{1+\alpha}.
\]

因此，即使：

\[
e_A<e_H,
\]

个体仍可能拒绝 AI。

例如 Human error rate 为 \(10\%\)，而某个参与者只有在 AI error rate 降至 \(7\%\) 时才愿意使用 AI，则其 implied asymmetric tolerance parameter 约为：

\[
\hat\alpha
=
\frac{0.10}{0.07}-1
=
0.429.
\]

本文因此不只检验“是否喜欢 AI”，而是估计：

\[
\boxed{\alpha_i}
\]

作为个体层面的行为参数。

---

# 三、把经济激励嵌入 Asymmetric Tolerance

经济激励可能存在三种完全不同的作用。

### Channel 1：纯粹的价格效应

激励改变 \(g\)，但不改变：

\[
\alpha
\]

也不改变参与者对：

\[
e_A,e_H
\]

的判断。

此时使用 AI 增加完全是理性的 payoff response。

这不能被解释成 trust increase。

---

### Channel 2：纠正 Asymmetric Tolerance

某些经济激励可能降低个体实际表现出的：

\[
\alpha.
\]

例如经济成本促使参与者更认真地比较 AI 和 Human 的真实表现，从而减少单纯因为 source identity 而产生的 AI penalty。

此时：

\[
\alpha_{Incentive}
<
\alpha_{Baseline}.
\]

这种变化才可以被解释为：

> economic incentives attenuate asymmetric tolerance。

---

### Channel 3：Payoff-induced belief distortion

经济激励还可能改变参与者认为 AI 正确的主观概率：

\[
\hat e_A
\]

或

\[
\hat q_A=1-\hat e_A.
\]

例如，如果采用 AI 可以获得额外奖金，参与者可能逐渐形成：

\[
\hat q_A>q_A
\]

的能力高估。

此时 AI adoption 也会上升，但并不是 asymmetric tolerance 得到纠正，而是产生了新的 belief miscalibration。

因此：

\[
\boxed{
More\ AI\ adoption
\neq
Better\ calibration
}
\]

这是本文区别于传统 technology adoption 和 incentive research 的关键。

---

# 四、研究设计总体结构

建议采用三个互相衔接的实验，而不是让一个复杂的 \(2\times3\times2\times2\) 实验承担所有问题。

三个实验分别回答：

\[
\text{Does }\alpha\text{ exist?}
\]

\[
\text{Can incentives change }\alpha\text{?}
\]

\[
\text{Why does }\alpha\text{ change?}
\]

---

# Study 1：识别 Asymmetric Tolerance

## 研究目的

首先证明，在 Human 与 AI：

- 完成相同任务；
- 具有相同 objective performance；
- 具有相同 error realization；

的情况下，仅仅改变建议来源是否足以改变采用标准。

---

## 实验任务

采用具有明确 ground truth 的重复判断任务。

优先考虑：

**视觉分类任务 / 概率判断任务 / 简单预测任务。**

正式实验前进行大型 pre-study，获得每道题的人类平均正确率：

\[
q_{H,k}.
\]

同时对 AI 进行相同测试，获得：

\[
q_{A,k}.
\]

正式实验中不依赖在线生成建议，而是冻结 Human 与 AI advisor 的建议序列。

---

## 核心 manipulation

随机分配：

\[
Source\in\{Human,AI\}.
\]

两个条件实际看到的 advice sequence 完全相同。

例如 100 轮中：

\[
90\ Correct,\quad10\ Wrong.
\]

Human condition 被告知：

> 建议来自此前完成该任务的一组人类参与者。

AI condition 被告知：

> 建议来自一个 AI system。

但错误发生的位置完全一致。

因此：

\[
Performance_H=Performance_A
\]

且：

\[
ErrorRealization_H=ErrorRealization_A.
\]

唯一差异为：

\[
SourceIdentity.
\]

---

## Performance threshold elicitation

进一步改变 advisor 的 objective error rate，例如：

\[
e_j\in
\{2\%,4\%,6\%,8\%,10\%,12\%,14\%\}.
\]

让参与者在 advisor 与一个固定 Human benchmark 之间选择。

估计每个参与者的 switching point：

\[
\tilde e_{A,i}^*.
\]

进而计算：

\[
\hat\alpha_i
=
\frac{e_H}{\tilde e_{A,i}^*}-1.
\]

---

## H1：Asymmetric Tolerance

在控制实际绩效后，AI advisor 的采用门槛高于 performance-equivalent Human advisor。

即：

\[
\alpha>0.
\]

换句话说：

> AI 必须比 Human 更准确，才能获得与 Human 相同的采用概率。

---

# Study 2：经济激励是在纠正 \(\alpha\)，还是在购买 adoption？

## 核心问题

在已经确认 asymmetric tolerance 后，引入原研究计划中的经济激励。

采用：

\[
2\times3
\]

设计：

### Advisor Source

\[
Human
\quad vs\quad
AI
\]

### Economic condition

\[
Cost,\quad Neutral,\quad Bonus.
\]

其中：

**Cost**

采用 advisor 时：

\[
g=-c.
\]

**Neutral**

使用成本得到完全返还：

\[
g=0.
\]

**Bonus**

采用 advisor 时获得额外奖励：

\[
g=b>0.
\]

Human 与 AI advisor 在每个绩效条件下采用完全相同的 advice sequence 和 error realization。

---

# 五、Study 2 的关键识别

这一步必须把三件事区分开。

## 5.1 Objective economically optimal choice

根据实际绩效与支付规则：

\[
A_{it}^{O}
=
\mathbf 1
\left\{
w(p_{it}^{Advisor}-p_{it}^{Self})+g>0
\right\}.
\]

它回答：

> 给定真实能力和支付结构，一个 expected-payoff-maximizing individual 应该选择什么？

---

## 5.2 Subjectively optimal choice

利用参与者报告的主观概率：

\[
A_{it}^{B}
=
\mathbf 1
\left\{
w(\hat p_{it}^{Advisor}-\hat p_{it}^{Self})+g>0
\right\}.
\]

它回答：

> 如果参与者真正相信自己报告出来的概率，他应该做什么？

---

## 5.3 Actual choice

\[
A_{it}.
\]

比较：

\[
A^O,\qquad A^B,\qquad A
\]

可以继续保留原研究最有价值的分解：

\[
A-A^O
=
(A^B-A^O)
+
(A-A^B).
\]

即：

\[
D^{Total}
=
D^{Belief}
+
D^{Choice}.
\]

但新版中，这一分解属于**机制识别工具**，不再与 \(\alpha\) 竞争理论中心。

---

# 六、Study 2 的主要假设

## H2：Pure Price Effect

如果经济激励只是改变 payoff，则控制实际支付后：

\[
\hat q_A
\]

以及结构估计得到的 source-specific：

\[
\alpha
\]

不应发生变化。

AI 使用率可以上升，但：

\[
D^{Belief}
\]

不应系统变化。

---

## H3：Correction of Asymmetric Tolerance

如果经济激励迫使参与者更加关注 AI 与 Human 的真实相对表现，则 AI-specific source penalty 应下降：

\[
\alpha_{Neutral}
<
\alpha_{Cost}
\]

或：

\[
\alpha_{Bonus}
<
\alpha_{Neutral}.
\]

关键证据不是 adoption 上升，而是：

\[
AI-Human\ adoption\ gap
\]

在控制 objective performance 和 payoff 后缩小。

---

## H4：Payoff-induced Belief Distortion

若正向奖金使参与者更倾向相信 AI 有能力，则：

\[
\hat q_A-q_A
\]

会随着 Bonus 增加。

尤其当 AI 实际能力较低时，这将产生：

\[
D^{Belief}>0
\]

以及过度 AI adoption。

于是可能出现一个具有管理意义的结果：

\[
\text{Bonus lowers observed AI aversion}
\]

但同时：

\[
\text{Bonus increases AI overestimation}.
\]

因此“纠正 algorithm aversion”与“制造 automation bias”可能同时发生。

---

# 七、重新加入 AI actual ability

建议保留原实验中的：

\[
High\ AI
\quad vs\quad
Low\ AI.
\]

但它现在的理论角色应该更加明确。

例如：

\[
q_H=90\%,
\qquad
q_L=70\%.
\]

Human benchmark 可以设为：

\[
q_{Human}=80\%.
\]

这样就出现两个特别有意义的条件：

### High AI

\[
q_A>q_H.
\]

规范上应该采用 AI。

如果仍拒绝 AI，就是最重要的：

\[
\boxed{AI\ under-adoption}
\]

---

### Low AI

\[
q_A<q_H.
\]

规范上应该保留 Human。

如果 Bonus 导致大量采用 AI，就是：

\[
\boxed{AI\ over-adoption}
\]

这样 economic incentive 会产生一个非常漂亮的 asymmetric welfare test：

> 同一个 AI 使用激励，是不是既能纠正 high-quality AI 的 under-adoption，又可能扩大 low-quality AI 的 over-adoption？

这比简单问：

> subsidy increases AI use?

理论意义强得多。

---

# 八、Study 3：Human Counterfactual Salience

在前两个实验基础上进一步检验导师框架中的核心 moderator。

随机分：

### Low Salience

只显示：

> AI accuracy = 85%.

### High Salience

明确显示：

> AI accuracy = 85%.  
> Human average accuracy = 75%.

两组的信息中 AI 客观能力完全相同。

理论预测：

\[
\alpha_{HighSalience}
<
\alpha_{LowSalience}.
\]

因此：

> 明确呈现 Human counterfactual 可以降低 AI-specific performance penalty。

---

# 九、一个特别重要的扩展：Average Human vs Best Human

进一步随机 manipulation 人类 benchmark：

### Average Human

\[
q_H=75\%.
\]

### Best Human

\[
q_H=90\%.
\]

### Human Distribution

展示：

\[
P_{10},Median,P_{90}.
\]

这样可以区分：

### Asymmetric Tolerance

人们知道正确的人类 benchmark，却仍然：

\[
L_A>L_H.
\]

和：

### Asymmetric Benchmark Selection

人们不是对 AI error 本身更不宽容，而是自动把 AI 与：

\[
Best\ Human
\]

甚至：

\[
Ideal\ Human
\]

进行比较。

后一种机制意味着表面上的：

\[
\alpha>0
\]

其实部分来源于 benchmark selection。

这是一个非常重要的理论边界。

---

# 十、推荐的实验任务

理想任务必须同时满足：

1. ground truth 明确；
2. Human average performance 可以预测试；
3. AI performance 可以精确测量；
4. performance 可以人为匹配；
5. Human 和 AI 可以被赋予相同 error realizations；
6. 任务不能简单到参与者完全不需要 advisor；
7. 任务不能复杂到 participant 无法形成自己的判断。

因此建议优先考虑：

### 第一选择：视觉噪声分类任务

通过调节图像噪声控制难度。

优势是：

- ground truth 完全确定；
- Human accuracy 很容易通过 pre-test 得到；
- AI 可以完成同一任务；
- item difficulty 可以高度控制；
- advisor 错误可以预先冻结；
- 几乎不存在领域知识差异。

---

### 第二选择：概率预测任务

参与者根据多个 probabilistic cues 判断 binary outcome。

例如：

\[
P(Y=1|X).
\]

优势是 objective probability 可以由实验设计直接确定，因此：

\[
p^{Self}
\]

和：

\[
p^{AI}
\]

更容易进入 Bayesian benchmark。

---

### 第三选择：现实化 diagnostic task

作为外部效度 Study。

例如医疗图片、信用风险或商业预测。

但不建议作为第一项实验，因为：

\[
AI-specific objective risk
\]

和 Human/AI error type differences 会严重影响因果识别。

---

# 十一、核心因变量重新排序

新版建议按照以下层级组织。

## Primary theoretical outcome

### Implied Asymmetric Tolerance

\[
\hat\alpha_i.
\]

或者通过 choice model 结构估计 population-level：

\[
\alpha.
\]

这是最接近理论参数的结果。

---

## Primary behavioural outcome

在 AI objectively better than Human 的情况下：

\[
P(Choose\ AI).
\]

以及对应的：

\[
AI-Human\ source\ gap.
\]

---

## Mechanism outcomes

### Perceived performance calibration

\[
D_i^{BeliefPerformance}
=
\hat q_i-q_i.
\]

### Choice decomposition

\[
D^{Total}
=
D^{Belief}
+
D^{Choice}.
\]

---

## Secondary construct

Performance trust scale。

该量表继续用于 construct validity，但不承担 normative benchmark 的功能。

---

# 十二、经验模型

一个基础 choice model 可以写成：

\[
Pr(A_{it}=1)
=
F[
\beta_0
+\beta_1 PerformanceAdvantage_{it}
+\beta_2 AI_i
+\beta_3 Incentive_i
+\beta_4(AI_i\times Incentive_i)
].
\]

其中：

\[
PerformanceAdvantage
=
e_H-e_A.
\]

如果：

\[
\beta_2<0,
\]

表示控制 objective performance 后存在 AI source penalty。

如果：

\[
\beta_4>0,
\]

表示激励缩小 AI-specific penalty。

进一步可以使用结构模型直接估计：

\[
[e_H-(1+\alpha)e_A]L+g.
\]

并令：

\[
\alpha_i
=
\alpha_0
+
\alpha_1Incentive_i
+
\alpha_2Salience_i
+
u_i.
\]

这样理论参数与实验操纵直接对应。

---

# 十三、整篇论文最核心的理论图景

传统技术采用：

\[
Economic\ Incentive
\rightarrow
AI\ Adoption.
\]

原研究计划进一步加入：

\[
Economic\ Incentive
\rightarrow
Belief
\rightarrow
AI\ Adoption.
\]

新版理论则变成：

\[
\boxed{
Objective\ AI-Human\ Performance
\rightarrow
Asymmetric\ Tolerance
\rightarrow
Adoption
}
\]

同时：

\[
Economic\ Incentive
\rightarrow
\begin{cases}
Payoff\ Response\\
Asymmetric\ Tolerance\\
Belief\ Distortion
\end{cases}
\rightarrow
AI\ Adoption.
\]

因此，观察到：

\[
AI\ Adoption\uparrow
\]

本身没有规范意义。

真正的问题是：

\[
\boxed{
\text{What part of the AI adoption gap should incentives correct?}
}
\]

以及：

\[
\boxed{
\text{When does correcting under-adoption turn into over-adoption?}
}
\]

---

# 十四、预期理论贡献

### Contribution 1：从 Algorithm Aversion 到可估计的 Adoption Wedge

研究不只证明人们不喜欢算法，而是用 performance-equivalent Human benchmark 识别一个可量化的：

\[
\alpha.
\]

因此把 individual algorithm aversion 转化成可以进入 adoption model 的 structural behavioural wedge。

### Contribution 2：重新定义 AI Adoption Incentives 的评价标准

传统研究通常关注：

\[
Adoption\uparrow?
\]

本文提出：

\[
Adoption\uparrow
\]

可能分别意味着：

- 纠正 inefficient under-adoption；
- 合理回应经济支付；
- 或制造 inefficient over-adoption。

因此 incentive effectiveness 必须依赖：

\[
AI\ performance
\quad relative\ to\quad
Human\ performance.
\]

### Contribution 3：连接 AI Trust 与 Economic Incentives

本文区分：

\[
Actual\ Trustworthiness,
\]

\[
Perceived\ Trustworthiness,
\]

\[
Trusting\ Behaviour.
\]

经济激励既可能只改变 behaviour，也可能改变 belief。

因此：

\[
Paying\ for\ AI\ use
\neq
Improving\ AI\ trust.
\]

### Contribution 4：为 Asymmetric Tolerance 提供微观实验证据

宏观监管中观察到 AI 比 Human 面临更高标准，并不能直接证明 asymmetric tolerance。

本文通过 performance-matched、error-matched、source-randomized experiment，在个人层面识别：

\[
SourceIdentity
\rightarrow
ToleranceThreshold.
\]

这为后续 regulator/public comparison 和 AI governance 研究建立行为基础。

---

# 十五、最核心的研究命题

整套研究最终可以压缩成一句话：

> **People may require AI to outperform humans before they are willing to rely on it. Economic incentives can close this adoption gap, but closing the gap is socially desirable only when incentives reduce source-dependent intolerance rather than distort beliefs about AI capability.**

因此本文真正研究的不是：

> 如何让人使用更多 AI？

而是：

\[
\boxed{
\text{How much better must AI be than humans before people accept it—and should organizations pay to close that gap?}
}
\]