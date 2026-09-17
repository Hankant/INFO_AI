# Paper 2：现实场景中的 AI Error-Tolerance Mismatch 候选

> 目的：为 Paper 2 的真实场景扩展筛选候选任务。核心不是简单寻找“AI aversion / AI appreciation”，而是寻找 **人的 AI error tolerance 与 AI 的客观能力发生系统性错配** 的场景。当前判断基于已有文献的快速筛选，最终方向仍应通过独立 screening pilot 验证。

## 核心思路

在抽象任务中先定义并解释 \(\alpha\)，然后在真实任务中寻找两个方向相反的场景：

- **低容忍 / under-reliance 候选**：AI 客观表现已经较强，但人仍要求 AI 达到更高标准，或仍坚持自己的判断。
- **高容忍 / over-reliance 候选**：AI 客观表现并没有想象中可靠，但人仍愿意接受其建议或错误。

现有文献已经充分证明“有些场景存在 AI aversion，有些场景存在 AI appreciation”。Qin et al. (2025) 的 meta-analysis 汇总了 163 项研究、442 个 effect sizes、82,078 名参与者。因此，Paper 2 更值得强调的不是“方向会变化”本身，而是能否用同一个 behavioral threshold / \(\alpha\) 框架识别 **现实中的系统性错配**。

DOI: https://doi.org/10.1037/bul0000477

---

## 可能出现较低 AI error tolerance 的任务

### 1. Phishing / 钓鱼邮件识别 —— 当前最值得优先 pilot

已有实验发现，即使 anti-phishing tool 的准确率很高，用户仍不会完全依赖工具；其 under-reliance 与 distrust、对工具机制缺乏透明理解有关。

这非常接近我们想要的结构：

\[
AI\text{ 客观能力较高} + Human\text{ 仍坚持自己的判断}
\]

因此它可能对应较高的 AI error intolerance / 正向 \(\alpha\)。相比自动驾驶，这一方向的行为研究更少，也更意外。

**代表文献**  
*It's not just about accuracy: An investigation of the human factors in users' reliance on anti-phishing tools*, Decision Support Systems, 2022.  
DOI: https://doi.org/10.1016/j.dss.2022.113846

**文献密度判断**：中等。已有直接 under-reliance 证据，但远没有自动驾驶、医疗 AI 那么拥挤。

### 2. 自动驾驶 —— 很典型，但 novelty 较弱

Shariff, Bonnefon, and Rahwan 的三项 preregistered studies（N = 4,566）显示，人们要求 autonomous vehicles 达到比 human drivers 更高的安全水平，而且这种要求与人们高估自身驾驶能力有关。

**代表文献**  
Shariff, A., Bonnefon, J.-F., & Rahwan, I. (2021). *How safe is safe enough? Psychological mechanisms underlying extreme safety demands for self-driving cars.*  
DOI: https://doi.org/10.1016/j.trc.2021.103069

**文献密度判断**：高。适合作为 motivating example，不建议作为最主要的新 application。

### 3. 医疗 AI —— 低容忍证据成熟，但非常拥挤

经典研究发现，消费者在医疗决策中往往更抗拒 AI，其中一个重要原因是认为自己的医疗需求具有独特性，而 AI 无法充分 personalization。

**代表文献**  
Longoni, C., Bonezzi, A., & Morewedge, C. K. (2019). *Resistance to Medical Artificial Intelligence.*  
DOI: https://doi.org/10.1093/jcr/ucz013

**文献密度判断**：很高。适合理论背景，不太适合做新的 application。

### 4. 道德、法律裁决、军事决策 —— 低容忍明显，但不利于计算 objective error

Bigman and Gray 的九项研究发现，人们明显排斥机器参与 morally relevant driving、law、medicine、military decisions，即使结果是正面的，这种 aversion 仍然存在。

问题在于这些任务往往缺乏清晰、单一的 objective truth，因此不一定适合直接使用 accuracy threshold 来估计 \(\alpha\)。

**代表文献**  
Bigman, Y. E., & Gray, K. (2018). *People are averse to machines making moral decisions.*  
DOI: https://doi.org/10.1016/j.cognition.2018.08.003

**文献密度判断**：高，且主要属于 moral machine / algorithm aversion 路线。

### 5. 招聘 / HR algorithm —— 有 algorithm aversion，但 benchmark 较难

Recruiter 研究发现，人类招聘者往往更偏好 human expert recommendation，而不是 digital hiring algorithm。

问题是“谁招对了人”的真实结果通常需要长期绩效才能验证，因此 objective accuracy benchmark 不够干净。

**代表文献**  
*Recruiters prefer expert recommendations over digital hiring algorithm: a choice-based conjoint study in a pre-employment screening scenario.*  
DOI: https://doi.org/10.1108/MRR-06-2020-0356

**文献密度判断**：中高。适合 algorithm aversion，不是最干净的 \(\alpha\) 场景。

### 6. 个性化服务 / 主观信息咨询 —— 对 AI 容忍度较低，但更像 preference 问题

近期 customer-service 研究发现，在披露 subjective information 时，人更偏好 human agent；在 objective information 情况下，则更偏好 AI。

**代表文献**  
Dai, X., Zhang, L., Huang, Z., & Wang, L. (2026). *AI or human: How the type of information to be disclosed alters customer service agent preferences.*  
DOI: https://doi.org/10.1016/j.jretconser.2025.104621

**文献密度判断**：中高，而且正在快速增长。

### 7. Deepfake detection —— 值得保留为 screening 候选

Deepfake detection 有明确 ground truth，也可以做 Human → AI advice → final choice 的统一流程。当前更适合作为 exploratory candidate，因为“人究竟系统性低估还是高估 AI detector”的方向需要 pilot 决定。

**文献密度判断**：技术性能研究很多，但与 behavioral acceptance threshold 直接对应的研究相对少。

---

## 可能出现较高 AI error tolerance 的任务

### 8. LLM citation / reference verification —— 当前最值得优先 pilot

相比“AI 帮你改英文论文”，更干净的任务是：

- 这篇论文是否真的存在？
- 这个 DOI / 作者 / 年份是否正确？
- 这篇文献是否真的支持某个 claim？

这些任务有明确 ground truth，而且 LLM 的 citation hallucination 已经有大量技术证据。2026 年的一项研究使用 9 个 LLM 生成了 74,196 条 bibliographic references，并系统分析 fabricated references，同时在真实发表文献中发现了虚假引用进入 scientific record 的案例。

这提供了一个很好的 over-tolerance 候选：

\[
AI\text{ 的真实可靠性有限，但用户可能因为输出流畅、格式完整而过度接受}
\]

需要强调的是：现有文献已经证明“LLM citation 会错”，但还没有充分证明“普通用户一定系统性高估它”。因此它非常适合 screening pilot。

**代表文献**  
Picazo-Sanchez, P., & Ortiz-Martin, L. (2026). *Evaluating the Integrity of LLM-Generated Citations: Prevalence and Risks of Fabricated References in Scientific Literature.*  
DOI: https://doi.org/10.3390/data11050122

**文献密度判断**：技术 hallucination 文献很多，但“行为阈值 / 用户愿意容忍多少错误”这一问题明显更少。

### 9. 法律案例 / 法条 / citation verification —— 和学术引用核验属于同一个好家族

法律任务同样可以构造明确的 ground truth，例如某案例是否真实存在、某判例是否支持该命题、某法条是否被正确引用。

已有研究显示，即便是专业 legal AI research tools，hallucination 仍然存在。

**代表文献**  
Magesh, V., Surani, F., Dahl, M., Suzgun, M., Manning, C. D., & Ho, D. E. (2025). *Hallucination-Free? Assessing the Reliability of Leading AI Legal Research Tools.*  
DOI: https://doi.org/10.1111/jels.12413

**文献密度判断**：模型可靠性研究正在快速增加，但 behavioral tolerance threshold 仍然相对空。

### 10. 财务风险 / AI advice —— 已有较直接的 overreliance 证据

实验研究发现，人会在 financially risky decisions 中 overrely on AI advice，甚至当 AI 建议与已有 contextual information 和自己的判断冲突时仍跟随 AI，进而产生低效率结果。

**代表文献**  
Klingbeil, A., Grützner, C., & Schreck, P. (2024). *Trust and reliance on AI — An experimental study on the extent and costs of overreliance on AI.*  
DOI: https://doi.org/10.1016/j.chb.2024.108352

**文献密度判断**：中高。和 overreliance 很契合，但没有 citation verification 那么意外。

### 11. 医学影像中的 AI assistance —— 专业人员也可能出现过度依赖

患者面对医疗 AI 时可能出现 aversion，但专业人员使用 AI assistance 时可能出现相反方向的 automation bias。

Mammography 实验显示，当 AI 给出错误建议时，不同经验水平的 radiologists 都会受到影响，尤其 inexperienced readers 更容易跟随错误 AI 建议。

**代表文献**  
Dratsch, T. et al. (2023). *Automation Bias in Mammography: The Impact of Artificial Intelligence BI-RADS Suggestions on Reader Performance.*  
DOI: https://doi.org/10.1148/radiol.222176

**文献密度判断**：中高。现象很有意思，但需要专业样本，实验实施成本较高。

### 12. 数值预测 / forecasting —— AI appreciation 很明确，但未必是“错配”

Logg, Minson, and Moore 的经典研究发现，人会对 algorithmic advice 赋予比 human advice 更高的权重，涵盖 numeric estimation、歌曲流行度、romantic attraction forecasting 等任务。

但这里的问题是 algorithm 很多时候客观上确实更好，因此“高容忍”未必等于“过度容忍”。

**代表文献**  
Logg, J. M., Minson, J. A., & Moore, D. A. (2019). *Algorithm appreciation: People prefer algorithmic to human judgment.*  
DOI: https://doi.org/10.1016/j.obhdp.2018.12.005

**文献密度判断**：高，属于经典 algorithm appreciation 路线。

### 13. 一般性的 GenAI factual advice / research assistance —— 方向重要，但任务需要进一步收窄

一般的“ChatGPT 给建议，人会不会相信”已经比较拥挤。Microsoft 2024 的 research synthesis 汇总了约 50 篇 GenAI appropriate-reliance 文献；2022 年 overreliance review 汇总了约 60 篇相关研究。

因此，如果使用这一方向，更适合收窄到 citation verification、source checking、legal fact checking 等客观任务。

**代表综述 / 技术报告（无 DOI）**

- Passi, S., Dhanorkar, S., & Vorvoreanu, M. (2024). *Appropriate Reliance on Generative AI: Research Synthesis.* Microsoft Technical Report MSR-TR-2024-7.  
  https://www.microsoft.com/en-us/research/publication/appropriate-reliance-on-generative-ai-research-synthesis/

- Passi, S., & Vorvoreanu, M. (2022). *Overreliance on AI: Literature Review.* Microsoft Technical Report MSR-TR-2022-12.  
  https://www.microsoft.com/en-us/research/publication/overreliance-on-ai-literature-review/

---

## 当前优先级

第一轮 screening pilot 最值得优先考虑四个场景：

1. **Phishing detection**：低容忍 / under-reliance 候选。
2. **Deepfake detection**：低容忍方向的 exploratory candidate。
3. **Citation / reference verification**：高容忍 / over-reliance 候选。
4. **Legal / factual verification**：高容忍方向的第二候选。

其中目前最有潜力的一对是：

\[
\boxed{\text{Phishing detection}}
\]

对

\[
\boxed{\text{Citation verification}}
\]

前者可能代表：**AI 已经相当可靠，但人仍然不愿完全交给它。**

后者可能代表：**AI 明明仍会犯大量可验证错误，但人仍可能因为输出的流畅性和权威感而过度接受。**

如果未来能在同一套 threshold-elicitation procedure 下得到：

\[
\alpha_{phishing}>0,\qquad \alpha_{citation}<0
\]

那么 Paper 2 的现实意义就不只是“不同 context 中 AI aversion / appreciation 不一样”，而是：

> **同一个可比较的行为参数可以识别现实任务中方向相反的 AI error-tolerance mismatch。**

这可能是相较已有 AI aversion / appreciation 文献更有辨识度的 contribution。
