# AI–Human 非对称错误权重：研究讨论总结

## 1. 研究起点

导师的 PPT 提出 **Asymmetric Tolerance（非对称容忍）**：当人类与 AI 犯下客观严重程度相同的错误时，人们可能对 AI 错误赋予更高权重。

基准模型为：

\[
\tilde L_H=L,\qquad \tilde L_A=(1+\alpha)L
\]

其中：

- \(L\)：同一错误造成的客观损失；
- \(\alpha\)：非对称容忍参数；
- 原模型设定 \(\alpha\ge 0\)。

因此，若忽略 Human 与 AI 的部署成本差异，理性基准为：

\[
e_A<e_H
\]

而存在非对称容忍时，AI 的采用条件变为：

\[
(1+\alpha)e_A<e_H
\]

对应的 AI 可接受错误率阈值为：

\[
e_A^*=\frac{e_H}{1+\alpha}
\]

由观察到的 switching threshold 可以反推：

\[
\alpha=\frac{e_H}{e_A^*}-1
\]

最初的研究想法是：找到一个 **Human 平均错误率可以确定、AI 错误率可以测量或操纵** 的任务，通过 Human–AI 选择测量 \(\alpha\)。

---

## 2. 对原始 Asymmetric Tolerance 模型的主要 critique

### 2.1 \(\alpha\) 的构念问题

仅仅观察到人们对 AI 更严格，并不能证明存在一个独立的 “asymmetric tolerance” 心理机制。

类似的行为结果也可能来自：

- algorithm aversion；
- ambiguity aversion；
- status quo bias；
- omission/commission bias；
- perceived controllability；
- distrust in automation；
- responsibility attribution；
- benchmark selection；
- 对 AI 客观性能的错误认知。

因此，更稳妥的理论定位是把 \(\alpha\) 理解为一个 **source-dependent evaluation wedge / error weight**，而不是预先声称它代表一种全新的心理机制。

---

### 2.2 Human error 与 AI error 的客观损失未必完全相同

原模型假定：

\[
L_H=L_A=L
\]

但现实中 AI 错误可能具有额外的：

- scalability；
- correlated/common-mode failures；
- systemic risk；
- cyber risk；
- opacity；
- responsibility gaps；
- distributional externalities。

因此，现实中更严格的 AI 标准可能部分来自 rational risk premium，而不完全是 behavioral bias。

理论上可以考虑将 observed AI penalty 拆分为：

\[
\text{Observed AI penalty}
=
\text{objective risk premium}
+
\text{behavioral source-dependent wedge}
\]

从而避免把所有 AI–Human 差异都规范性地解释成“过度监管”或“不理性”。

---

### 2.3 “distortion scales with stakes” 不是当前模型下的无条件结论

导师模型中的理性阈值为：

\[
e_A^*
=
e_H-\frac{c_A-c_H}{L}
\]

而非对称容忍下：

\[
\tilde e_A
=
\frac{e_A^*}{1+\alpha}
\]

两者之差为：

\[
D(L)
=
e_A^*-\tilde e_A
=
\left(e_H-\frac{\Delta c}{L}\right)
\frac{\alpha}{1+\alpha}
\]

其中：

\[
\Delta c=c_A-c_H
\]

于是：

\[
\frac{\partial D}{\partial L}
=
\frac{\Delta c}{L^2}
\frac{\alpha}{1+\alpha}
\]

因此 stakes effect 的符号取决于 \(\Delta c\)：

- 若 \(c_A>c_H\)，则 distortion 随 \(L\) 增加；
- 若 \(c_A<c_H\)，则 distortion 可能随 \(L\) 下降；
- 若 \(c_A\approx c_H\)，则该 comparative static 接近 0。

因此，如果未来理论确实要预测“stakes 越高，AI 越不被容忍”，更合理的做法是直接令：

\[
\alpha=\alpha(L),\qquad \alpha'(L)>0
\]

而不是从当前固定 \(\alpha\) 的模型中自动推出。

---

### 2.4 \(\alpha_{\text{regulator}}>\alpha_{\text{public}}\) 需要额外机制

导师 PPT 提出：

\[
\alpha_{\text{regulator}}
>
\alpha_{\text{public}}
\]

并据此提出 democratic-alignment gap。

但模型本身没有解释为什么 regulator 一定更高。

相反，监管者也可能因为：

- 更专业；
- 更熟悉 base rates；
- 更了解 human error；
- 更习惯统计风险；

而具有更低的 \(\alpha\)。

因此，这一关系目前更像 empirical conjecture，而不是从基础模型推出的理论结果。

一个可能的 microfoundation 是 asymmetric political accountability：

\[
Loss_R
=
SocialLoss+\lambda PoliticalBlame
\]

如果 AI failure 的政治责任成本高于 human failure：

\[
B_A>B_H
\]

则监管者可能表现出更高的有效 AI error weight。

---

### 2.5 Public preference 不等于 welfare benchmark

即使：

\[
\alpha_R>\alpha_P
\]

也不能直接推出“监管过度”。

需要至少区分：

\[
\alpha_P,\qquad
\alpha_R,\qquad
\alpha^*
\]

分别对应：

- public preference；
- regulator preference；
- social welfare benchmark。

只有当：

\[
\alpha_R>\alpha^*
\]

时，才有更强依据讨论 over-regulation。

---

### 2.6 Visibility 可能存在内生性

导师模型提出：

\[
\alpha=\alpha(v),\qquad \alpha'(v)>0
\]

其中 \(v\) 为 AI error visibility。

但现实中：

\[
Regulation\rightarrow Visibility
\]

和：

\[
Visibility\rightarrow Regulation
\]

可能同时存在。

因此跨领域比较很难直接识别 visibility 的因果效应。

更干净的方法是实验操纵 aggregability / visibility，同时固定：

- error rate；
- error realization；
- task；
- information。

---

### 2.7 Counterfactual salience 是更有潜力的 moderator

导师模型提出：

\[
\alpha=\alpha(s),\qquad \alpha'(s)<0
\]

其中 \(s\) 为 human counterfactual salience。

核心思想是：

- 只看到 “AI error = 4%” 时，参与者可能隐含地拿 AI 和 perfection 比；
- 同时看到 “Human error = 6%” 后，评价标准可能改变。

这个机制具有较好的实验可操作性。

未来可以比较：

- AI only；
- AI + average human；
- AI + median human；
- AI + best human；
- AI + human performance distribution。

---

## 3. 最初考虑的 \(\alpha\) 测量设计

如果暂时不考虑经济激励，最简实验可固定：

\[
c_A=c_H
\]

以及固定 \(L\)，只操纵 Human 与 AI 的 objective error rates。

例如固定：

\[
e_H=20\%
\]

并让：

\[
e_A\in\{5\%,10\%,12.5\%,15\%,17.5\%,20\%,25\%\}
\]

记录参与者在每个组合下是否选择 AI。

若参与者的 switching threshold 为：

\[
e_A^*=13.75\%
\]

则：

\[
\hat\alpha
=
\frac{0.20}{0.1375}-1
\approx0.455
\]

因此可以把行为选择映射成个体层面的 implied \(\alpha_i\)。

---

## 4. 为什么“简单测 switching point”本身可能不够新

我们随后讨论到一个重要问题：大量已有研究已经表明，人在 AI 与 Human 之间的依赖并不完全由 objective accuracy 决定。

已有相关研究方向包括：

- **Algorithm Aversion**：即使算法客观表现更好，人们仍可能在看到算法犯错后回避算法；
- **Algorithm Appreciation**：在一些任务中，相同建议被标记为 algorithmic source 时反而获得更高权重；
- **Automation Bias**：人在某些环境下可能过度依赖自动化建议；
- 相同 advice / performance、仅操纵 Human vs AI source label 的设计，也已有较多实验。

因此，以下发现本身新颖性有限：

\[
e_A<e_H
\]

但人仍然选择 Human；

或者：

\[
Same\ advice + Same\ accuracy + Human/AI\ label
\]

产生不同的行为反应。

单纯把已有 algorithm aversion 现象重新写成：

\[
\alpha>0
\]

容易被 reviewer 认为只是 **parametric restatement**。

---

## 5. 更有价值的问题：\(\alpha\) 是否真的是稳定的 multiplicative parameter？

导师模型不仅声称存在 source asymmetry，还隐含了更强的 functional-form assumption：

\[
\tilde L_A=(1+\alpha)L
\]

这意味着在不同 Human baseline error rates 下，同一个人的：

\[
\frac{e_H}{e_A^*}
\]

应该近似保持不变。

例如：

\[
\alpha=0.5
\]

意味着：

\[
e_A^*=\frac{2}{3}e_H
\]

因此：

- 若 Human error = 30%，AI threshold 应约为 20%；
- 若 Human error = 15%，AI threshold 应约为 10%；
- 若 Human error = 6%，AI threshold 应约为 4%。

这提供了一个比“是否 algorithm averse”更强的可证伪预测。

---

## 6. Multiplicative \(\alpha\) 与 additive penalty 的 horse race

另一个关键问题是：即使存在 AI penalty，它为什么一定是 multiplicative？

导师模型：

\[
e_A^*
=
\frac{e_H}{1+\alpha}
\]

意味着 AI 所需的 performance advantage 按比例变化。

但另一种可能是固定百分点要求：

\[
e_A^*
=
e_H-\delta
\]

其中 \(\delta\) 为 additive AI penalty。

因此可以比较至少三类模型：

### Model 0：Source-neutral rational benchmark

\[
e_A^*=e_H
\]

### Model 1：Additive penalty

\[
e_A^*=e_H-\delta
\]

### Model 2：Multiplicative asymmetric weighting

\[
e_A^*
=
\frac{e_H}{1+\alpha}
\]

### Model 3：Flexible / nonlinear model

\[
e_A^*
=
f(e_H)
\]

或：

\[
\alpha=\alpha(e_H)
\]

实验可以通过构造多个：

\[
(e_H,e_A)
\]

组合，估计完整的 Human–AI indifference frontier，并比较：

- likelihood；
- AIC/BIC；
- out-of-sample predictive performance；
- hierarchical Bayesian fit。

这样真正要回答的是：

> **Human–AI source-dependent evaluation 的 functional form 是什么？**

而不只是：

> **是否存在 algorithm aversion？**

---

## 7. 最重要的新质疑：为什么 \(\alpha\) 必须非负？

这是讨论中形成的最重要修正。

导师原模型直接限定：

\[
\alpha\ge0
\]

意味着理论预设所有 source-dependent asymmetry 都指向 AI error overweighting。

但已有 algorithm appreciation 与 automation-bias 文献说明，在部分任务中，人可能反而：

- 更愿意相信 AI；
- 给 AI advice 更高权重；
- 在 AI 错误时仍过度依赖系统。

因此没有充分理由先验地排除：

\[
\alpha<0
\]

---

## 8. 将模型扩展为双向 Source-Dependent Error Weight

保留：

\[
\tilde L_A=(1+\alpha)L
\]

但将参数空间扩展为：

\[
\boxed{\alpha\in(-1,\infty)}
\]

此时存在三个理论区域：

\[
\alpha>0
\]

表示：

**AI error overweighting / AI intolerance**

即同样的错误，因为来自 AI 而受到更高权重。

---

\[
\alpha=0
\]

表示：

**source-neutral evaluation**

Human 与 AI 的错误受到相同权重。

---

\[
-1<\alpha<0
\]

表示：

**AI error underweighting / AI over-tolerance**

即同样的错误，因为来自 AI 而被赋予更低权重。

注意：negative \(\alpha\) 与 algorithm appreciation / automation bias 相关，但并不等价。

\(\alpha\) 是模型中的 **error-weighting parameter**；

algorithm appreciation / automation bias 是行为现象或已有理论构念。

---

## 9. 更中性的参数化方式：\(\lambda_A\)

为避免 “tolerance” 本身带来的方向性预设，可以重新定义：

\[
\lambda_A=1+\alpha
\]

并 normalize：

\[
\lambda_H=1
\]

于是：

\[
\tilde L_H=\lambda_HL=L
\]

\[
\tilde L_A=\lambda_AL
\]

其中：

\[
\lambda_A>1
\]

AI error overweighting；

\[
\lambda_A=1
\]

source neutrality；

\[
0<\lambda_A<1
\]

AI error underweighting。

这个名称可以叫：

- **Source-Dependent Error Weight**
- **AI Error Weighting Parameter**
- **Relative AI Error Weight**

这种参数化比 “Asymmetric Tolerance” 更中性，也允许理论同时容纳 aversion 与 appreciation。

---

## 10. 新的核心研究问题

因此研究问题可以从：

> How intolerant are people toward AI errors?

改成：

> **Do people apply symmetric performance standards to humans and AI, and if not, in which direction does the asymmetry run?**

更进一步：

> **Can Human–AI source-dependent evaluation be represented by a stable error-weighting parameter, and when does its sign reverse?**

对应三个基础问题：

### RQ1：Direction

\[
\alpha<0,\quad\alpha=0,\quad\alpha>0?
\]

不同任务中 source-dependent asymmetry 的方向是否相同？

### RQ2：Magnitude

\[
|\alpha|
\]

在不同个体与不同任务之间有多大差异？

### RQ3：Stability

同一个人在不同：

\[
(e_H,e_A)
\]

组合下，是否可以用一个稳定的 \(\alpha_i\) 描述？

### RQ4：Functional Form

Human–AI performance threshold 更符合：

- source-neutral；
- additive penalty；
- multiplicative weighting；
- nonlinear weighting；

中的哪一种？

---

## 11. 一个更有潜力的理论观点：\(\alpha\) 可能是 task-dependent，而不是 trait

一个重要推论是：

\[
\alpha_i
\]

可能不是稳定的人格或一般 AI attitude。

更合理的形式可能是：

\[
\alpha_{id}=f(i,d)
\]

其中：

- \(i\)：individual；
- \(d\)：domain / task。

同一个人可能在不同任务中表现出不同符号：

- arithmetic / calculation：可能 \(\alpha<0\)；
- statistical forecasting：可能 \(\alpha\le0\)；
- image classification：可能接近 0；
- medical diagnosis：可能 \(\alpha>0\)；
- hiring：可能 \(\alpha>0\)；
- moral judgment：可能 \(\alpha>0\)；
- creative evaluation：可能 \(\alpha>0\)。

这些只是有待检验的理论方向，而非预设结果。

核心可能是：

\[
\boxed{\text{When does asymmetric weighting reverse?}}
\]

---

## 12. Population average 可能掩盖双向异质性

仅报告：

\[
E[\alpha]
\]

可能会误导。

例如：

\[
50\%\quad \alpha=+0.5
\]

以及：

\[
50\%\quad \alpha=-0.5
\]

总体：

\[
E[\alpha]=0
\]

但这并不代表人们 source-neutral。

相反，它意味着 population 中存在明显的双向 source-dependent distortion。

因此未来应同时报告：

\[
P(\alpha>0)
\]

\[
P(\alpha\approx0)
\]

\[
P(\alpha<0)
\]

以及完整的：

\[
F(\alpha)
\]

分布。

---

## 13. 推荐的基础实验结构

如果研究目标是建立 \(\alpha\) / \(\lambda_A\) 的 measurement map，一个合适的基础设计是让参与者面对大量 Human–AI performance pairs：

\[
(e_H,e_A)
\]

例如：

| Human error | AI error |
|---:|---:|
| 5% | 2% |
| 5% | 3% |
| 5% | 5% |
| 10% | 5% |
| 10% | 8% |
| 10% | 10% |
| 20% | 10% |
| 20% | 15% |
| 20% | 20% |
| 30% | 15% |
| 30% | 20% |
| 30% | 30% |

每次记录：

\[
Choose\ AI / Choose\ Human
\]

从而估计：

\[
P(AI\mid e_H,e_A)
\]

以及 participant-level indifference frontier。

---

## 14. 实验中应尽可能固定的因素

为了把选择差异解释成 source-dependent error weighting，基础测量实验中最好固定：

\[
c_A=c_H
\]

避免 cost difference 混入 \(\alpha\)。

同时固定：

\[
L_H=L_A
\]

以及：

- task；
- available information；
- payoff consequences；
- advice format；
- error severity；
- feedback structure。

如果可能，Human 与 AI 的 advice/error realization 也应 performance-match。

---

## 15. 应保留的 belief measurement

即使 objective error rates 已知，也建议测量：

\[
\hat e_H,\qquad \hat e_A
\]

因为观察到 participant 选择 Human，可能来自：

1. 真正的 source-dependent error weighting；
2. 对 AI performance 的错误认知。

因此可以区分：

### Objective-implied \(\alpha\)

根据实验给出的 objective performance：

\[
\alpha_i^O
=
\frac{e_H}{e_{A,i}^*}-1
\]

### Belief-adjusted \(\alpha\)

根据 participant 自己相信的 performance：

\[
\alpha_i^B
=
\frac{\hat e_H}{\hat e_{A,i}^*}-1
\]

如果控制主观 performance belief 后仍存在稳定 source effect，对 source-dependent weighting 的解释更强。

---

## 16. 推荐的研究程序

### Study 1：Measurement and Functional Form

目标：

- 估计 Human–AI indifference frontier；
- 检验 \(\alpha\) 是否存在稳定的单参数表示；
- 比较 multiplicative、additive 与 flexible model；
- 检验 negative \(\alpha\) 是否存在。

核心问题：

\[
\boxed{\text{Does a stable source-dependent error weight exist?}}
\]

---

### Study 2：Cross-Task Sign Reversal

在若干具有理论异质性的任务中重复测量：

\[
\alpha_{id}
\]

目标：

- 检验 task/domain 是否改变 \(\alpha\) 的 magnitude；
- 更重要的是检验其 **sign 是否反转**。

可以使用 multilevel model：

\[
\alpha_{id}
=
\mu+u_i+v_d+\epsilon_{id}
\]

其中：

- \(u_i\)：individual tendency；
- \(v_d\)：domain effect。

关键比较：

\[
Var(u_i)
\]

与：

\[
Var(v_d)
\]

谁更大？

如果：

\[
Var(v_d)\gg Var(u_i)
\]

则意味着 source-dependent AI evaluation 更像 task property，而不是稳定 personality / AI attitude。

---

### Study 3：Mechanisms / Moderators

在基础 measurement 建立后，再研究导师 PPT 提出的两个 moderator：

#### Error Visibility

\[
\alpha=\alpha(v)
\]

#### Human Counterfactual Salience

\[
\alpha=\alpha(s)
\]

这两个机制研究应建立在前两项 measurement 已经清楚之后，而不是一开始就同时加入。

---

## 17. 一个更有潜力的总体理论框架

原模型的故事是：

\[
AI\ Error
\rightarrow
Extra\ Weight
\rightarrow
Under\text{-}adoption
\]

扩展后的框架可以写成：

\[
\boxed{
Source
\times
Task
\times
Performance
\rightarrow
Relative\ Error\ Weight
\rightarrow
Human\text{-}AI\ Choice
}
\]

其中：

\[
\lambda_A
\]

可以：

- 大于 1；
- 等于 1；
- 小于 1。

因此 Algorithm Aversion 和 Algorithm Appreciation 不再被视为两套互相竞争的现象，而可能只是同一个 source-dependent weighting function 的不同参数区域。

---

## 18. 当前最值得继续推进的贡献点

### Contribution 1：从单向 bias 转向双向 behavioral parameter

不是预设：

\[
\alpha\ge0
\]

而是允许：

\[
\alpha\in(-1,\infty)
\]

研究 asymmetry 的 direction 与 magnitude。

### Contribution 2：检验 functional form

已有研究已经大量证明 algorithm aversion / appreciation 的存在。

更有价值的问题是：

\[
\boxed{
\text{这种 Human–AI 差异到底服从什么函数形式？}
}
\]

### Contribution 3：从平均效应转向参数分布

研究：

\[
F(\alpha)
\]

而不只是 average treatment effect。

### Contribution 4：识别 individual vs task heterogeneity

检验：

\[
\alpha
\]

究竟更像：

- stable individual trait；
- task-specific judgment；
- domain-level social norm；
- 或三者共同作用。

### Contribution 5：为导师宏观治理模型提供更可靠的 microfoundation

如果未来要把 \(\alpha\) 用于：

- adoption；
- regulation；
- stakeholder heterogeneity；
- governance；

首先需要证明：

1. 参数是否可测；
2. 是否稳定；
3. 是否一定为正；
4. 是否可跨任务比较；
5. functional form 是否真的是 multiplicative。

---

## 19. 当前最核心的研究命题

研究不应该只问：

> **Are people less tolerant of AI errors?**

而应该问：

> **How do people weight objectively equivalent human and AI errors, and is this source-dependent weighting stable, bidirectional, and task-dependent?**

进一步可以压缩成一句更有辨识度的问题：

> **When does AI have to be better than humans to be accepted, and when are people willing to accept AI even when it is worse?**

这句话同时覆盖：

\[
\alpha>0
\]

与：

\[
\alpha<0
\]

也正是目前讨论后形成的、更开放且更有研究价值的理论方向。

---

## 20. 下一步建议

下一阶段最适合优先解决四个设计问题：

1. 选择什么任务能够同时得到可信的 Human 与 AI objective performance；
2. 如何构造足够密集的 \((e_H,e_A)\) performance grid；
3. 如何用 choice data 估计 individual-level \(\alpha\) / \(\lambda_A\)；
4. 如何做 multiplicative、additive 和 flexible model 的正式比较。

在这四点确定前，暂时不需要加入经济激励、监管者、visibility 或 counterfactual salience 等更复杂机制。
