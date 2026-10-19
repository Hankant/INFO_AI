# 对《Asymmetric Tolerance》的评语

## 总体评价

这套模型的核心贡献是非常清楚的：作者试图把一种 **source-dependent evaluation** 正式引入 AI adoption 和 regulation 的分析框架。也就是说，即使 AI 与人类造成的客观损失相同，人们也可能因为错误来自 AI，而给予该错误更高的主观权重。

模型通过

\[
\tilde L_H=L,\qquad \tilde L_A=(1+\alpha)L,\qquad \alpha\ge 0
\]

来刻画这种 **asymmetric tolerance**。这一设定的优点是十分简洁，而且理论识别很干净。作者还假设决策者能够准确观察 AI 与人类的客观错误率 \(e_A\) 和 \(e_H\)，因此可以把“人们误判 AI 的准确率”这一机制排除出去，把注意力集中在“同样的错误因为来源不同而被不同评价”这一行为偏差上。

这一点使模型能够非常直接地得到一个有吸引力的结果：即使

\[
e_A<e_H,
\]

也就是说 AI 客观上比人类表现更好，AI 仍然可能因为更高的主观错误权重而无法达到采用门槛。这为 AI 的 under-adoption 以及 AI 相对于人类受到更严格监管提供了一个统一解释。

---

## 主要问题：模型目前只考虑了“对 AI 不够宽容”这一侧

我认为目前模型最需要进一步解释的问题，是为什么参数被限制为

\[
\alpha\ge 0.
\]

这个设定意味着，AI 错误的主观损失只能等于或者高于人类错误的损失。因此模型从一开始就只允许两种情况：

- \(\alpha=0\)：对 AI 和人类错误完全同等评价；
- \(\alpha>0\)：对 AI 错误更加不宽容。

但现实中的人与 AI 互动并不总是表现为 algorithm aversion。大量实际场景中也存在相反方向的行为：人们可能过度相信 AI、自动接受 AI 建议、忽视 AI 可能犯错的事实，或者因为 AI 输出显得精确、系统化、权威而给予其过高的可信度。

换句话说，现实中不仅存在：

\[
\text{AI intolerance},
\]

还可能存在：

\[
\text{AI over-trust / automation bias / overreliance}.
\]

如果论文希望提出的是一个比较一般性的 **behavioural theory of AI adoption and regulation**，那么当前单边的 \(\alpha\ge0\) 设定会限制模型的解释范围。

---

## “过度相信 AI”和“对 AI 犯错不宽容”其实不是同一个维度

这里需要特别区分两个不同的行为机制。

### 1. 对 AI 错误概率的认知

一个人可能低估 AI 的真实错误率：

\[
\tilde e_A<e_A.
\]

例如，用户看到一个非常自信、表达流畅的 AI 输出，会认为：

> “AI 既然这么确定，应该不会错。”

这种行为更接近 automation bias 或 overreliance。

它影响的是对错误发生概率的判断。

### 2. 对 AI 已经发生的错误的评价

另一个完全不同的问题是：在错误已经发生、或者客观错误率已经明确给出的情况下，人是否认为 AI 的错误“更加不可接受”。

这才是当前模型的 \(\alpha\)：

\[
\tilde L_A=(1+\alpha)L.
\]

这里改变的不是错误发生概率，而是对错误后果的主观权重。

作者通过“决策者准确观察 \(e_A,e_H\)”的假设，实际上有意把第一种机制排除掉了。这使模型内部逻辑很清楚，但也意味着 \(\alpha\) 不应该被解释成一般意义上的“对 AI 的信任”。

更准确地说，\(\alpha\) 描述的是：

> **conditional on knowing the objective error rate, how much additional disutility is attached to an error because its source is AI.**

因此，我建议论文在概念上把这一点说得更明确。

---

## 一个很有意思的现实可能性：事前过度信任，事后过度惩罚

这两种偏差甚至可能同时存在于同一个人身上。

在 AI 使用之前或决策发生之前，个体可能表现出：

\[
\tilde e_A<e_A,
\]

也就是低估 AI 犯错概率，从而形成 **ex ante overreliance**。

但是一旦 AI 真正犯错，个体又可能认为：

\[
\tilde L_A>L,
\]

也就是对 AI 犯错表现出更强烈的负面反应，形成 **ex post intolerance**。

因此，一个人完全可能同时具有：

> **事前过度相信 AI，事后又过度惩罚 AI。**

这并不是矛盾的，反而可能非常符合现实中的 AI 使用行为。

例如，一个用户在使用生成式 AI 时，因为模型的语气非常确定而直接采纳答案；但当后来发现答案是错误的，又会产生比面对普通人的错误更强烈的失望，并迅速降低对整个 AI 系统的信任。

如果能够把这两个阶段区分开来，理论会比现在更加丰富。

---

## 作者目前有没有回答这个问题？

从现有 PPT 来看，作者并没有真正把“过度相信 AI”纳入模型。

作者确实在后面的理论定位中强调，这个模型与 **trust-in-automation** 文献不同。作者认为传统 trust-in-automation 研究更多讨论 miscalibrated reliance，以及这种错误依赖是否可以通过经验、学习和暴露得到校准；而当前模型关注的是一种附着于“AI 作为错误来源”的 source-specific penalty。

因此，可以理解为作者有意把研究边界划在：

> “为什么 AI 的错误会受到额外惩罚？”

而不是：

> “人在什么情况下会正确、过度或不足地信任 AI？”

这种限定本身是可以成立的。

但是，如果采取这种解释，那么论文最好更加明确地说明：

1. 为什么理论上主要关注 \(\alpha\ge0\) 的情形；
2. 哪些领域中这种假设最合理；
3. 哪些领域中 automation bias 或 algorithm appreciation 可能占主导，因此当前模型并不适用；
4. 论文究竟想提出一个“AI error intolerance theory”，还是更广义的“AI adoption behavioral theory”。

如果不做这一限定，那么标题所声称的理论范围可能略大于模型实际覆盖的行为范围。

---

## 一个简单扩展：允许 \(\alpha\) 为负

最直接的扩展是允许：

\[
\alpha\in(-1,\infty).
\]

于是：

### 当 \(\alpha>0\)

\[
\tilde L_A>L,
\]

表示 AI intolerance / algorithm aversion。

### 当 \(\alpha=0\)

表示 source-neutral benchmark。

### 当 \(-1<\alpha<0\)

\[
\tilde L_A<L,
\]

表示个体对 AI 错误反而更加宽容。

这种处理的优点是非常简单，可以让现有模型自然覆盖正负两个方向的 source-dependent weighting。

但我认为，这个扩展虽然数学上方便，行为解释上并不是最理想的，因为“过度相信 AI”通常并不等同于“AI 犯错以后我觉得损失比较小”。

---

## 更好的扩展：区分 probability bias 和 tolerance bias

一个更有解释力的模型可以同时引入两个 behavioral wedges。

设：

\[
\tilde e_A=(1-\beta)e_A,
\]

其中 \(\beta\) 描述对 AI 错误概率的认知偏差。

如果：

\[
\beta>0,
\]

说明个体低估 AI 错误率，即存在 over-trust 或 automation bias。

同时保留：

\[
\tilde L_A=(1+\alpha)L,
\]

其中 \(\alpha\) 描述个体对 AI 错误本身的额外惩罚。

那么 AI 的主观预期成本变为：

\[
\tilde C_A
=
(1-\beta)e_A(1+\alpha)L+c_A.
\]

这时最终采用决策取决于：

\[
(1-\beta)(1+\alpha).
\]

这个框架的好处是，它允许两个方向相反的行为机制同时存在：

- \(\beta>0\)：提高 AI adoption，表现为过度相信 AI；
- \(\alpha>0\)：降低 AI adoption，表现为对 AI 犯错不宽容。

两者可能相互抵消，也可能由其中一个机制占主导。

这样一来，原来的 asymmetric tolerance 就不再是唯一的 behavioral distortion，而是一个更一般的 source-dependent AI evaluation framework 中的一个组成部分。

---

## 这个扩展还会带来新的实证预测

如果区分 \(\alpha\) 和 \(\beta\)，就可以研究很多原模型无法处理的问题。

### 1. 不同阶段的偏差可能方向相反

在 adoption 前：

\[
\beta \text{ 可能较大},
\]

人们因为 AI 的权威感、自动化程度或者输出形式而过度依赖。

在 failure 发生以后：

\[
\alpha \text{ 可能迅速上升},
\]

人们又对 AI 犯错产生 disproportionate punishment。

因此可以研究：

> **ex ante trust 与 ex post tolerance 是否是两个独立维度？**

### 2. 不同任务可能对应不同的 \((\alpha,\beta)\)

例如：

- 自动驾驶：可能是高 \(\alpha\)、低 \(\beta\)；
- 医疗 AI：可能同时存在较高 \(\alpha\) 和一定程度的 \(\beta\)；
- 生成式 AI：在普通用户中可能出现较高 \(\beta\)，但在一次严重 hallucination 以后 \(\alpha\) 快速上升；
- 算法推荐：用户可能长期形成 automation complacency，从而表现出较大的 \(\beta\)。

这比单纯比较不同领域的 \(\alpha\) 更丰富。

### 3. 信息干预对两个参数的影响可能相反

原模型认为提高 human counterfactual salience 会降低 \(\alpha\)。

但如果同时向用户展示“AI 平均表现优于人类”，这种信息还可能进一步降低主观的 \(\tilde e_A\)，从而增加 overreliance。

因此，同一个 benchmark intervention 可能：

\[
\alpha\downarrow
\]

但同时：

\[
\beta\uparrow.
\]

这意味着一个旨在减少 algorithm aversion 的政策设计，理论上可能产生新的 automation bias。

这是一个非常有意思的 welfare trade-off。

---

## 对论文定位的建议

我认为作者有两种比较清晰的选择。

### 路径一：维持现有简洁模型，但缩窄理论主张

作者可以明确说：

> 本文并不是试图建立一个完整的 AI trust theory，而是识别并形式化一种特定的 behavioral distortion：conditional on objective performance being known, AI-generated errors receive greater negative weight than equivalent human-generated errors.

如果这样定位，那么 \(\alpha\ge0\) 是一个有意识的研究范围选择，而不是模型遗漏。

这种做法的优点是保持模型简单、理论机制突出。

### 路径二：把 asymmetric tolerance 扩展成更一般的 source-dependent evaluation framework

如果作者希望保留更宏大的标题和理论定位，则可以考虑允许多个 source-specific distortions：

\[
\text{perceived probability}
\times
\text{perceived loss}.
\]

这样既可以解释：

- algorithm aversion，
- automation bias，
- algorithm appreciation，
- under-adoption，
- over-adoption，
- 以及事故发生后的 trust collapse。

这种方向理论上更完整，但模型复杂度也会明显增加。

---

## 我会直接问作者的几个问题

### 问题1

为什么模型限制

\[
\alpha\ge0
\]

而不允许人们在某些情况下对 AI 错误更加宽容？

这是一个理论假设、经验事实，还是为了简化模型？

### 问题2

作者如何区分：

\[
\text{misperception of } e_A
\]

和

\[
\text{source-dependent weighting of } L_A?
\]

换句话说，如何实证识别一个人是在“过度相信 AI 不会犯错”，还是“知道 AI 会犯错，但对 AI 犯错特别不能容忍”？

### 问题3

现实中可能同时存在：

> ex ante automation bias

和

> ex post algorithm aversion。

当前模型是否有办法解释同一个个体在不同阶段表现出的这种方向反转？

### 问题4

如果提高 human-counterfactual salience 可以降低 \(\alpha\)，这种信息干预是否同时可能导致用户过度依赖 AI？

也就是说：

> 减少 algorithm aversion 的 intervention，会不会增加 automation bias？

如果会，那么政策目标应该是最小化 asymmetric tolerance，还是实现 calibrated reliance？

---

## 总结

我认为这套模型当前最大的优点，是把一个非常具体的行为偏差——**AI 错误受到比人类错误更大的主观惩罚**——以极简方式引入 adoption 和 regulation 的理论框架，并且可以直接推导 AI under-adoption、监管门槛扭曲以及 stakeholder heterogeneity 等结果。

但与此同时，目前模型明显只覆盖了人与 AI 互动中的一个方向。现实中同样存在 automation bias、overreliance 和 algorithm appreciation。因此，作者需要更加明确地回答：

> **为什么非对称一定表现为对 AI 更不宽容，而不是也可能表现为对 AI 更宽容或更加信任？**

如果作者只希望研究 AI error intolerance，那么建议明确缩窄理论边界，并解释 \(\alpha\ge0\) 的适用条件。

如果作者希望提出一个更加一般性的 AI adoption behavioral theory，那么一个自然的下一步，是把“对 AI 错误概率的认知偏差”和“对 AI 错误后果的容忍偏差”分开建模，例如分别使用 \(\beta\) 和 \(\alpha\)。

我认为最有潜力的扩展不是简单地允许 \(\alpha<0\)，而是研究一个更有行为含义的问题：

> **为什么人们可能在事前过度相信 AI，却在 AI 真正犯错以后又对它表现出过度惩罚？**

这会把当前的 asymmetric tolerance 理论进一步连接到 automation bias、trust calibration 和动态 AI adoption 文献，也可能产生比单向 algorithm aversion 更丰富的理论与实证预测。
