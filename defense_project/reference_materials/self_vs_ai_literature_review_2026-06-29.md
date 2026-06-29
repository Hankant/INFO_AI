# 文献文档库：Self Error, Advice Taking, Self-Reliance 与 AI Reliance

> 入库日期：2026-06-29
> 来源：用户提供综述（22 篇文献 + 3 段可嵌入 RP 的理论整合段落 + LLM 读取规则）

## 使用目的

本文献库用于支撑以下研究计划中的关键理论判断：

> Self-generated error 可以作为一种 human baseline，但它不同于 external human advisor error。
> 因此，本文研究的不是 AI error vs external human advisor error，而是 AI-generated error vs self-generated error 在 repeated feedback 中对后续 reliance choice 的不同影响。

核心逻辑链为：

```text
Advice-taking 文献
    ↓
自己的初始判断与外部建议是不同信息来源

Self-serving attribution 文献
    ↓
人们对自己的成功与失败存在非对称归因

Overconfidence / illusion of control 文献
    ↓
即使自己犯错，人也可能继续偏好自我判断，因为 self 包含控制感、自信和 agency

Algorithm aversion / AI advice 文献
    ↓
AI 错误可能引发特殊的低依赖或回避

综合结论
    ↓
Self error 是 human-generated error 的一种，但不是 external human advisor error；
    Self vs AI 是一个独立且合理的人机依赖研究场景。
```

---

# A. Advice-taking / Judge-Advisor System 文献

## A1. Yaniv & Kleinberger (2000)

**Citation**

Yaniv, I., & Kleinberger, E. (2000). Advice taking in decision making: Egocentric discounting and reputation formation. *Organizational Behavior and Human Decision Processes, 83*(2), 260–281.

**主题标签**

* Advice-taking
* Egocentric discounting
* Advisor reputation
* Own judgment vs external advice
* Negative information asymmetry

**研究问题**

人们在做判断时如何使用他人的建议？他们是否会中性地整合自己的判断和 advisor 的判断？advisor 的声誉如何形成？

**方法与设计**

该研究使用 judge-advisor paradigm。参与者先形成自己的判断，然后看到 advisor 的建议，再决定是否修正自己的判断。研究通过多项实验观察参与者如何权衡自己的意见和外部建议，以及 advisor 的表现如何影响其后续声誉。

**核心发现**

1. 人们倾向于折扣外部建议，即 advice is discounted relative to one's own opinion。
2. advisor 的声誉形成很快。
3. advisor 的声誉具有负面不对称性，即犯错可能比正确表现更快损害 advisor reputation。
4. 决策者不是简单地按准确率整合信息，而是受到自我中心权重和声誉更新影响。

**对本研究的意义**

这篇文献直接支持本文把 self-generated judgment 与 external advice 区分开。它说明个体自己的初始判断不是普通信息源，而是被给予特殊权重的判断来源。

**可嵌入 RP 的写法**

> Advice-taking research has long distinguished decision makers' initial judgments from external advice. In the judge-advisor paradigm, individuals typically discount external advice relative to their own initial opinions, suggesting that self-generated judgments and externally generated recommendations are psychologically distinct information sources.

---

## A2. Bonaccio & Dalal (2006)

**Citation**

Bonaccio, S., & Dalal, R. S. (2006). Advice taking and decision-making: An integrative literature review, and implications for the organizational sciences. *Organizational Behavior and Human Decision Processes, 101*(2), 127–151.

**主题标签**

* Advice-taking review
* Advice utilization
* Advisor characteristics
* Decision-maker confidence
* Judgment revision

**研究问题**

advice-taking 研究有哪些主要发现？个体在什么情况下会采纳或忽视建议？advisor 特征、decision-maker 特征和任务特征如何影响 advice utilization？

**方法与设计**

综述型文章，系统整合 advice-giving 和 advice-taking 文献，整理影响建议采纳的主要因素，包括 advisor expertise、confidence、decision-maker confidence、task difficulty、accountability、decision accuracy 等。

**核心发现**

1. Advice utilization 受到多重因素影响，不仅取决于 advice 的客观质量。
2. 个体的 confidence 会影响其对 advice 的接受程度。
3. Advisor 的 perceived expertise、credibility 和 relationship 会影响 advice weight。
4. Advice-taking 不只是信息整合问题，也是社会判断与责任分配问题。

**对本研究的意义**

这篇综述可以作为理论框架的基础文献，说明 self vs AI 的设计属于 advice-taking 和 AI-assisted decision-making 的交叉领域。

**可嵌入 RP 的写法**

> Advice utilization is shaped by advisor characteristics, decision-maker confidence, task features, and perceived responsibility. Therefore, AI reliance should be treated as a behavioral choice embedded in a broader advice-taking process rather than as a simple response to predictive accuracy.

---

## A3. Sniezek & Buckley (1995)

**Citation**

Sniezek, J. A., & Buckley, T. (1995). Cueing and cognitive conflict in judge-advisor decision making. *Organizational Behavior and Human Decision Processes, 62*(2), 159–174.

**主题标签**

* Judge-advisor system
* Cognitive conflict
* Advice cueing
* Role differentiation
* Decision-maker vs advisor

**研究问题**

当 judge 面对 advisor 的建议时，信息线索和 cognitive conflict 如何影响判断？judge 和 advisor 的角色如何在决策过程中区分？

**方法与设计**

使用 judge-advisor system 范式，考察参与者在自我判断和他人建议之间如何处理冲突。该范式强调 judge 与 advisor 的角色分化：judge 拥有最终决策权，advisor 提供外部信息。

**核心发现**

1. Judge-advisor system 为研究分工角色下的判断修正提供了标准实验范式。
2. Decision maker 的自我判断和 advisor 的建议构成不同信息来源。
3. 当两者冲突时，参与者需要处理 cognitive conflict，并决定是否调整自己的判断。

**对本研究的意义**

这篇文献可用于说明 self vs AI 的实验流程是有经典范式基础的：先做 self prediction，再看 AI advice，然后选择最终采用 self 或 AI。

**可嵌入 RP 的写法**

> The current design builds on the judge-advisor paradigm, in which decision makers first form their own judgments and then decide how to use external advice. This structure allows the study to separate self-generated judgments from externally generated recommendations.

---

## A4. Harvey & Fischer (1997)

**Citation**

Harvey, N., & Fischer, I. (1997). Taking advice: Accepting help, improving judgment, and sharing responsibility. *Organizational Behavior and Human Decision Processes, 70*(2), 117–133.

**主题标签**

* Advice-taking
* Judgment improvement
* Responsibility sharing
* Self vs advice
* Weight of advice

**研究问题**

人们为什么接受建议？建议是否改善判断？接受建议是否与责任分担有关？

**方法与设计**

实验研究，考察参与者在判断任务中如何使用外部建议，以及建议是否提高判断准确性。文章也讨论 advice-taking 与 responsibility sharing 的关系。

**核心发现**

1. 外部建议通常可以提高判断准确性，但参与者并不总是充分使用建议。
2. 接受建议不仅是为了改善判断，也可能涉及责任分担。
3. 人们对外部建议的使用程度受到任务、建议来源和自身判断信心影响。

**对本研究的意义**

这篇文献支持"采用 AI"不只是准确率最大化，也涉及责任和控制权转移。与 self 相比，AI 是外部来源，因此采用 AI 可能意味着放弃部分控制或转移责任。

**可嵌入 RP 的写法**

> Advice-taking can serve not only to improve judgment accuracy but also to redistribute responsibility. Therefore, adopting AI advice may differ psychologically from relying on one's own judgment, even when both are evaluated against the same feedback.

---

## A5. Soll & Larrick (2009)

**Citation**

Soll, J. B., & Larrick, R. P. (2009). Strategies for revising judgment: How and how well people use others' opinions. *Journal of Experimental Psychology: Learning, Memory, and Cognition, 35*(3), 780–805.

**主题标签**

* Judgment revision
* Advice weighting
* Averaging vs choosing
* PAR model
* Wisdom of crowds

**研究问题**

当人们看到他人的意见后，如何修正自己的判断？他们是平均自己的判断和他人建议，还是在二者之间选择？

**方法与设计**

多项实验研究量化判断任务中的 advice use。参与者先给出自己的估计，再看到他人的估计，并做出最终判断。研究比较不同 revision strategies 的效果。

**核心发现**

1. 人们常用两类策略：averaging 和 choosing。
2. 从准确性角度看，合理整合他人意见通常有助于提高判断质量。
3. 但人们往往不能最优地使用外部意见。
4. 个体经常在自己的判断和外部建议之间进行非最优权衡。

**对本研究的意义**

这篇文献非常适合支撑你的两项设计：参与者在 self prediction 和 AI prediction 之间选择，正是一个 judgment revision / advice use 问题。

**可嵌入 RP 的写法**

> Prior work on judgment revision shows that people often choose between their own estimates and others' estimates, or average the two. The present study focuses on the choosing case, asking whether early AI errors shift participants away from AI-generated judgments and back toward self-generated judgments.

---

## A6. Bailey et al. (2022/2023)

**Citation**

Bailey, P. E., et al. (2022/2023). A meta-analysis of the weight of advice in decision-making. *Current Psychology.*

**主题标签**

* Weight of advice
* Meta-analysis
* Advice discounting
* Judgment revision
* Advice utilization

**研究问题**

跨大量 advice-taking 研究，人们平均会给外部建议多大权重？哪些因素影响 weight of advice？

**方法与设计**

元分析，整合大量关于 advice-taking 和 weight of advice 的实验研究。

**核心发现**

1. 人们通常不会完全采纳外部建议。
2. Advice weight 受到 advisor expertise、task difficulty、decision-maker confidence、advice timing 等因素影响。
3. 该文献进一步确认 advice-taking 中存在系统性折扣现象。

**对本研究的意义**

这篇元分析可以作为 advice-taking 领域的综合证据，支持"self vs external advice 是一个成熟研究结构"。

**可嵌入 RP 的写法**

> The dependent variable, AI reliance, can be interpreted as a behavioral form of advice weighting. Instead of measuring the numerical weight assigned to advice in a single judgment, the current study observes whether participants choose the AI-generated prediction across repeated feedback.

> ⚠️ **入库状态**：本条作者字段写为 "Bailey, P. E., et al."，年份模糊（"2022/2023"），期刊给定（*Current Psychology*）。暂不入 bib，待用户确认具体作者列表、年份、卷期后再补。

---

# B. Self-serving Attribution / Self Error 文献

## B1. Miller & Ross (1975)

**Citation**

Miller, D. T., & Ross, M. (1975). Self-serving biases in the attribution of causality: Fact or fiction? *Psychological Bulletin, 82*(2), 213–225.

**主题标签**

* Self-serving bias
* Attribution
* Success and failure
* Responsibility
* Self-protection

**对本研究的意义**

Self error 不是单纯性能信号，而是触发自我保护归因的事件，可能不会削弱 self-reliance。

---

## B2. Bradley (1978)

**Citation**

Bradley, G. W. (1978). Self-serving biases in the attribution process: A reexamination of the fact or fiction question. *Journal of Personality and Social Psychology, 36*(1), 56–71.

**主题标签**

* Self-serving attribution
* Success-failure asymmetry
* Defensive attribution

**对本研究的意义**

与 Miller & Ross 搭配，给出更直接的 self-serving attribution 经验证据。

---

## B3. Weiner (1985)

**Citation**

Weiner, B. (1985). An attributional theory of achievement motivation and emotion. *Psychological Review, 92*(4), 548–573.

**主题标签**

* Attribution theory
* Locus, stability, controllability

**对本研究的意义**

错误反馈本身不直接决定后续依赖；关键在于参与者如何归因（内部/外部、稳定/不稳定、可控/不可控）。

---

## B4. Campbell & Sedikides (1999)

**Citation**

Campbell, W. K., & Sedikides, C. (1999). Self-threat magnifies the self-serving bias: A meta-analytic integration. *Review of General Psychology, 3*(1), 23–43.

**主题标签**

* Self-threat
* Self-serving bias
* Meta-analysis

**对本研究的意义**

Self error 是 self-threatening event，可能触发自我保护性归因；外部 advisor 错误则是 reliability evaluation。

---

## B5. Mezulis et al. (2004)

**Citation**

Mezulis, A. H., Abramson, L. Y., Hyde, J. S., & Hankin, B. L. (2004). Is there a universal positivity bias in attributions? *Psychological Bulletin, 130*(5), 711–747.

**主题标签**

* Self-serving attribution
* Positivity bias
* Meta-analysis (266 studies, 503 effect sizes)

**对本研究的意义**

大型元分析，作为 self-serving attribution 的强证据。

---

## B6. Shepperd, Malone, & Sweeny (2008)

**Citation**

Shepperd, J., Malone, W., & Sweeny, K. (2008). Exploring causes of the self-serving bias. *Social and Personality Psychology Compass, 2*(2), 895–908.

**主题标签**

* Self-serving bias
* Motivated reasoning
* Self-enhancement
* Self-presentation

**对本研究的意义**

Self-serving bias 来自认知、动机、自我呈现多重机制；self error 的特殊性是多机制叠加。

---

# C. Overconfidence / Control Preference / Illusion of Control 文献

## C1. Langer (1975)

**Citation**

Langer, E. J. (1975). The illusion of control. *Journal of Personality and Social Psychology, 32*(2), 311–328.

**主题标签**

* Illusion of control
* Choice, familiarity, involvement
* Perceived control

**对本研究的意义**

Self option 不是普通来源，而是包含 agency 和 perceived control。即使 self 表现不佳，参与者可能因控制感继续选择 self。

---

## C2. Thompson, Armstrong, & Thomas (1998)

**Citation**

Thompson, S. C., Armstrong, W., & Thomas, C. (1998). Illusions of control, underestimations, and accuracy: A control heuristic explanation. *Psychological Bulletin, 123*(2), 143–161.

**主题标签**

* Illusion of control
* Control heuristic
* Intentionality, connection

**对本研究的意义**

Self option 具有 intentionality 和 connection 成分，采用 AI 降低 agency。

---

## C3. Moore & Healy (2008)

**Citation**

Moore, D. A., & Healy, P. J. (2008). The trouble with overconfidence. *Psychological Review, 115*(2), 502–517.

**主题标签**

* Overestimation
* Overplacement
* Overprecision

**对本研究的意义**

Overconfidence 三种形式都可解释 self error 不一定削弱 self attraction。

---

## C4. Larrick, Burson, & Soll (2007)

**Citation**

Larrick, R. P., Burson, K. A., & Soll, J. B. (2007). Social comparison and confidence. *Organizational Behavior and Human Decision Processes, 102*(1), 76–94.

**主题标签**

* Better-than-average effect
* Overplacement

**对本研究的意义**

参与者可能不仅根据自身绝对表现决定是否用 AI，也根据"我是否比 AI 更懂这个任务"决定。

---

## C5. Goodie (2003)

**Citation**

Goodie, A. S. (2003). The effects of control on betting. *Journal of Experimental Psychology: Learning, Memory, and Cognition, 29*(4), 598–610.

**主题标签**

* Control
* Betting
* Calibration

**对本研究的意义**

Confidence 和 perceived control 可以导致非最优选择坚持。

---

# D. Algorithm Aversion / AI Advice 桥接文献

## D1. Dietvorst, Simmons, & Massey (2015)  ⏩ 已在 bib 中（`Dietvorst2015`）

## D2. Logg, Minson, & Moore (2019)  ⏩ 已在 bib 中（`Logg2019`）

## D3. Prahl & Van Swol (2017)

**Citation**

Prahl, A., & Van Swol, L. M. (2017). Understanding algorithm aversion: When is advice from automation discounted? *Journal of Forecasting, 36*(6), 691–702.

**主题标签**

* Algorithm aversion
* Automation advice
* Advice discounting
* Perceived similarity

**对本研究的意义**

AI advice discounting 可能来自 source identity，而非单纯准确率。支撑 self error 与 AI error 不对称。

---

## D4. Longoni, Bonezzi, & Morewedge (2019)

**Citation**

Longoni, C., Bonezzi, A., & Morewedge, C. K. (2019). Resistance to medical artificial intelligence. *Journal of Consumer Research, 46*(4), 629–650.

**主题标签**

* Resistance to AI
* Medical AI
* Uniqueness neglect

**对本研究的意义**

AI resistance 反映 AI 是否适合某类判断任务，不只是准确率。

---

## D5. Vodrahalli, Daneshjou, Gerstenberg, & Zou (2021)

**Citation**

Vodrahalli, K., Daneshjou, R., Gerstenberg, T., & Zou, J. (2021). Do humans trust advice more if it comes from AI? An analysis of human-AI interactions. arXiv preprint.

**主题标签**

* Human-AI advice
* Activation-integration model

**对本研究的意义**

Human-AI advice use 可拆分为 activation（是否采用）和 integration（如何整合）两阶段。本研究聚焦 activation 阶段。

---

# E. 用于 RP 的整合性理论段落

## E1. 版本一（中文）

本文不将 external human advisor 放入主实验，而是将 self-generated judgment 作为 human baseline。这样处理并不意味着 self 与 external human advisor 在心理机制上完全等同。相反，advice-taking 文献通常区分 decision maker 的 initial judgment 与外部 advisor 的 advice，并发现个体往往会相对于自己的判断折扣外部建议。与此同时，self-serving attribution、overconfidence 和 illusion of control 等研究表明，个体对自身错误的解释可能受到自我保护、控制感和自信偏差影响。因此，self error 虽然可以被视为 human-generated error 的一种，但它不同于 external human advisor error。

基于这一点，本文的核心比较不是 AI error versus external human advisor error，而是 AI-generated error versus self-generated error。本文关注的问题是：当 AI 和自己都会犯错时，人们是否更容易原谅自己的错误，而更严厉地惩罚 AI 的错误？

## E2. 版本二（学术英文）

The present study treats self-generated judgment as a human baseline, but not as a direct substitute for an external human advisor. In the advice-taking literature, decision makers' initial judgments and advisors' recommendations are typically treated as psychologically distinct information sources. People often discount external advice relative to their own opinions, suggesting that self-generated judgments carry privileged weight in subsequent revision. In addition, attribution theory and self-serving bias research suggest that self-generated errors are self-relevant events that may be interpreted through self-protective mechanisms. Overconfidence and illusion-of-control research further indicate that individuals may preserve self-reliance because it maintains agency and perceived control. Therefore, self-generated error is a form of human-generated error, but it is not equivalent to error made by an external human advisor. This distinction motivates the present focus on AI-generated error versus self-generated error in repeated reliance decisions.

## E3. 版本三（回应导师质疑）

如果导师问"self 为什么可以作为 human baseline，但又不是 human advisor"，可以回答：

本文不是把 self 等同于 external human advisor，而是将 self 作为一个更基础的人类判断基准。Advice-taking 研究本身就区分 decision maker 的 own judgment 和 external advice；self-serving attribution 研究说明人们对自己的错误有特殊归因；overconfidence 和 illusion of control 研究说明 self option 包含控制感和自我能力感。因此，self error 是 human-generated error 的一种，但不是 external human advisor error。本文的主问题也相应收窄为 AI-generated judgment 与 self-generated judgment 的动态依赖差异，而不是 AI 与外部人类专家的来源比较。

---

# F. 文献清单 + 入库状态

## A. Advice-taking / Judge-advisor system
| key | 状态 |
|-----|------|
| `YanivKleinberger2000` | 待核查 |
| `BonaccioDalal2006` | 待核查 |
| `SniezekBuckley1995` | 待核查 |
| `HarveyFischer1997` | 待核查 |
| `SollLarrick2009` | 待核查 |
| `Bailey2022` | ⚠️ **作者/年份不全，待用户确认** |

## B. Self-serving attribution / Attribution theory
| key | 状态 |
|-----|------|
| `MillerRoss1975` | 待核查 |
| `Bradley1978` | 待核查 |
| `Weiner1985` | 待核查 |
| `CampbellSedikides1999` | 待核查 |
| `MezulisEtAl2004` | 待核查 |
| `ShepperdMaloneSweeny2008` | 待核查 |

## C. Overconfidence / Control / Self-reliance
| key | 状态 |
|-----|------|
| `Langer1975` | 待核查 |
| `ThompsonArmstrongThomas1998` | 待核查 |
| `MooreHealy2008` | 待核查 |
| `LarrickBursonSoll2007` | 待核查 |
| `Goodie2003` | 待核查 |

## D. Algorithm aversion / Human-AI advice
| key | 状态 |
|-----|------|
| `Dietvorst2015` | ⏩ 已在 bib 中 |
| `Logg2019` | ⏩ 已在 bib 中 |
| `PrahlVanSwol2017` | 待核查 |
| `LongoniBonezziMorewedge2019` | 待核查 |
| `VodrahalliEtAl2021` | 待核查（arXiv preprint） |

---

# G. 给 LLM 的读取指令

1. 不要把 self error 简单等同于 external human advisor error。
2. 应表述为：self-generated error is a human baseline, but psychologically distinct from external human advisor error。
3. 理论支撑来自三条线：
   * advice-taking：self judgment 与 external advice 是不同信息来源；
   * attribution/self-serving bias：self error 会触发自我归因和自我保护；
   * overconfidence/control：self option 包含 agency、control 和 self-confidence。
4. AI 文献用于说明 AI error 可能引发 algorithm aversion，但不要声称本文直接比较 AI error 与 external human advisor error。
5. 本文的主研究对象应写成：
   * AI-generated error vs self-generated error；
   * dynamic AI reliance vs self-reliance；
   * repeated feedback 中的 reliance updating。
6. External human advisor 应作为 future extension 或 reference-option extension，而不是主实验核心。
7. EWA 应作为机制模型，不应替代 reduced-form 主分析。