# Paper 3：作者原文 Gap、局限、未来方向与前文批评

生成时间（UTC）：2026-08-12T03:32:59+00:00

## 证据规则

- 仅收录作者在全文中明确写出的内容。
- 每条英文引文已由程序在对应 PDF 页内反向匹配。
- 模型推断、无法定位的引文和类别不合格项均不进入本文件。
- `processing_status.csv` 记录缺失全文、损坏 PDF、无可提取文本和 API 错误。

## 全文处理覆盖

| 状态 | 篇数 |
|---|---:|
| missing_full_text | 26 |
| skipped_completed | 4 |

## 理论展望优先索引

### VanBaarEtAl2019: The computational and neural substrates of moral strategies in social decision-making

> Second, do decision strategies inferred from behavior correspond to participants' subjective experiences? Although there is evidence that participants are generally unable to accurately report their internal cognitive processes, it would be interesting to explore the subjective reasoning of participants whose strategy lacks internal consistency (e.g., moral opportunists).

- 类型：construct_refinement
- 位置：PDF p. 10；section: Discussion
- 原始理论/构念：moral opportunism
- 作者指出的理论不足：当前研究仅从行为和神经层面推断道德策略，未考察参与者对自身策略的主观体验和推理。
- 作者提出的理论推进：通过比较行为推断的策略与主观报告，检验道德策略构念是否具有主观对应物，并探索道德机会主义者的主观推理。
- 待检验关系/命题：检验行为推断的道德策略与主观体验之间的一致性。

> Third, what leads to the development of a mix of moral strategies in a population? In many human social interactions, moral opportunism may be the most adaptive strategy, as it allows participants to maximize payoff while still being able to justify their decision to others—a key goal of moral reasoning. However, there may be psychological or cultural boundary conditions to this strategy that drive some individuals toward moral consistency.

- 类型：boundary_condition
- 位置：PDF p. 10；section: Discussion
- 原始理论/构念：moral opportunism; moral consistency
- 作者指出的理论不足：当前研究未解释为何群体中会同时存在多种道德策略，也未识别道德机会主义与道德一致性的边界条件。
- 作者提出的理论推进：识别导致个体采用道德机会主义或道德一致性的心理或文化边界条件。
- 待检验关系/命题：检验心理或文化因素如何调节道德策略的选择（机会主义 vs. 一致性）。

> The low prevalence of pure guilt aversion in our sample may be helpful for improving psychological game theory as it suggests that some guilt-averse behavior in past research may in fact have been motivated by inequity aversion, and that guilt-averse preferences may be context-dependent (e.g., for moral opportunists in our task).

- 类型：theory_extension
- 位置：PDF p. 9；section: Discussion
- 原始理论/构念：psychological game theory; guilt aversion; inequity aversion
- 作者指出的理论不足：心理博弈理论可能未充分区分 guilt aversion 和 inequity aversion 的动机，且未考虑 guilt-averse 偏好的情境依赖性。
- 作者提出的理论推进：通过揭示 guilt-averse 行为可能由 inequity aversion 驱动且具有情境依赖性，扩展心理博弈理论中关于社会偏好的假设。
- 待检验关系/命题：检验 guilt-averse 行为是否可被 inequity aversion 解释，以及 guilt-averse 偏好如何随情境变化。

### Joo2024: It is the AI fault not mine: Mind perception increases blame attribution to AI

> Since affective responses are often triggered by cognitive blame, future research should explore how emotional reactions fluctuate depending on mind perception.

- 类型：mechanism_specification
- 位置：PDF p. 12；section: General discussion
- 原始理论/构念：mind perception; blame; affective responses
- 作者指出的理论不足：当前研究仅关注责备的认知过程，未考察情感反应。
- 作者提出的理论推进：探索心智感知如何影响情感反应，从而扩展责备归因的机制理解。
- 待检验关系/命题：检验心智感知与情感反应（如愤怒、敌意）之间的关系。

> Future studies should further investigate the relationship between cognitive and affective components of blame, particularly in the context of AI moral transgressions.

- 类型：construct_refinement
- 位置：PDF p. 12；section: General discussion
- 原始理论/构念：blame; cognitive component; affective component
- 作者指出的理论不足：责备的认知与情感成分之间的关系尚不清楚。
- 作者提出的理论推进：明确责备的认知与情感成分之间的区别与联系，以完善责备构念。
- 待检验关系/命题：检验责备的认知成分与情感成分在AI道德违规情境中的关系。


## 逐篇完整证据


## VanBaarEtAl2019: The computational and neural substrates of moral strategies in social decision-making

- Year: 2019
- DOI: 10.1038/s41467-019-09161-6
- Source PDF: `E:\Info_AI\defense_project\reference_materials\papers_originals\social_preferences_intergroup_conflict\VanBaarEtAl2019.pdf`

### 作者承认的本研究局限、边界或仍未解决的问题

> our inferences about moral strategies required the use of a task in which different social preference models yield different behavioral predictions (i.e., The Hidden Multiplier Trust Game).

- 位置：PDF p. 8；section: Discussion
- 忠实释义：作者承认，他们对道德策略的推断依赖于一个特定的任务设计，即隐藏乘数信任博弈，该任务使得不同的社会偏好模型产生不同的行为预测。
- 原文校验：通过（normalized_exact）
> An obvious downside of this approach is that we could not control the relative frequencies of moral strategies in our dataset, which contained a relatively low number of purely guilt-averse participants.

- 位置：PDF p. 9；section: Discussion
- 忠实释义：作者承认其方法的一个明显缺点是，无法控制数据集中不同道德策略的相对频率，导致纯粹 guilt-averse 参与者数量较少。
- 原文校验：通过（normalized_exact）

### 作者明确提出的未来研究方向

> Second, do decision strategies inferred from behavior correspond to participants' subjective experiences? Although there is evidence that participants are generally unable to accurately report their internal cognitive processes, it would be interesting to explore the subjective reasoning of participants whose strategy lacks internal consistency (e.g., moral opportunists).

- 位置：PDF p. 10；section: Discussion
- 忠实释义：作者提出未来研究可探讨从行为推断的决策策略是否与参与者的主观体验相对应，尤其是探索缺乏内部一致性的策略（如道德机会主义者）的主观推理过程。
- 展望类型：construct_refinement
- 原始理论/构念术语：moral opportunism
- 分析层级：individual
- 作者指出的理论不足：当前研究仅从行为和神经层面推断道德策略，未考察参与者对自身策略的主观体验和推理。
- 作者提出的理论推进：通过比较行为推断的策略与主观报告，检验道德策略构念是否具有主观对应物，并探索道德机会主义者的主观推理。
- 待检验关系/命题：检验行为推断的道德策略与主观体验之间的一致性。
- 原文校验：通过（exact_word_sequence_typography_normalized）
> Third, what leads to the development of a mix of moral strategies in a population? In many human social interactions, moral opportunism may be the most adaptive strategy, as it allows participants to maximize payoff while still being able to justify their decision to others—a key goal of moral reasoning. However, there may be psychological or cultural boundary conditions to this strategy that drive some individuals toward moral consistency.

- 位置：PDF p. 10；section: Discussion
- 忠实释义：作者提出未来研究应探讨导致群体中出现混合道德策略的原因，并指出可能存在心理或文化边界条件，使得某些个体倾向于道德一致性而非机会主义。
- 展望类型：boundary_condition
- 原始理论/构念术语：moral opportunism; moral consistency
- 分析层级：individual
- 作者指出的理论不足：当前研究未解释为何群体中会同时存在多种道德策略，也未识别道德机会主义与道德一致性的边界条件。
- 作者提出的理论推进：识别导致个体采用道德机会主义或道德一致性的心理或文化边界条件。
- 待检验关系/命题：检验心理或文化因素如何调节道德策略的选择（机会主义 vs. 一致性）。
- 原文校验：通过（exact_word_sequence_typography_normalized）

### 作者对既有文献、理论、方法或证据的明确批评

> in most laboratory paradigms, guilt aversion and inequity aversion yield the same behavioral predictions, obfuscating which prosocial motivation was at play in the decision-maker’s mind (as noted by Nihonsugi et al. 14 and Hein et al. 15).

- 位置：PDF p. 2；section: Introduction
- 忠实释义：作者批评以往实验室范式的一个缺陷：内疚厌恶和不公平厌恶产生相同的行为预测，导致无法区分决策者背后的亲社会动机。
- 批评对象：prior laboratory paradigms
- 原文校验：通过（exact_word_sequence_typography_normalized）
> previous neuroimaging studies have averaged measurements across participants, potentially masking individual differences in implicit moral reasoning, and hence obscuring strategy-specific features of the moral brain.

- 位置：PDF p. 2；section: Introduction
- 忠实释义：作者批评以往神经影像研究对参与者进行平均，可能掩盖了个体在道德推理上的差异，从而模糊了策略特异性的脑特征。
- 批评对象：previous neuroimaging studies
- 原文校验：通过（normalized_exact）

### 作者明确提出的理论含义、理论延伸或未来理论工作

> The low prevalence of pure guilt aversion in our sample may be helpful for improving psychological game theory as it suggests that some guilt-averse behavior in past research may in fact have been motivated by inequity aversion, and that guilt-averse preferences may be context-dependent (e.g., for moral opportunists in our task).

- 位置：PDF p. 9；section: Discussion
- 忠实释义：作者指出，样本中纯粹 guilt aversion 的低发生率可能有助于改进心理博弈理论，因为它表明过去研究中的某些 guilt-averse 行为实际上可能由 inequity aversion 驱动，且 guilt-averse 偏好可能是情境依赖的。
- 展望类型：theory_extension
- 原始理论/构念术语：psychological game theory; guilt aversion; inequity aversion
- 分析层级：individual
- 作者指出的理论不足：心理博弈理论可能未充分区分 guilt aversion 和 inequity aversion 的动机，且未考虑 guilt-averse 偏好的情境依赖性。
- 作者提出的理论推进：通过揭示 guilt-averse 行为可能由 inequity aversion 驱动且具有情境依赖性，扩展心理博弈理论中关于社会偏好的假设。
- 待检验关系/命题：检验 guilt-averse 行为是否可被 inequity aversion 解释，以及 guilt-averse 偏好如何随情境变化。
- 原文校验：通过（exact_word_sequence_typography_normalized）

## IgweEtAl2024: Analyzing Social Exchange Motives With Theory-Driven Data and Machine Learning

- Year: 2024
- DOI: 10.1109/ACCESS.2023.3348755
- Source PDF: `E:\Info_AI\defense_project\reference_materials\papers_originals\social_preferences_intergroup_conflict\IgweEtAl2024.pdf`

### 作者用于说明本研究必要性的既有研究缺口

> The prediction of “why” based intent using interaction traces like the clickstream and interaction network, however, remains relatively unexplored.

- 位置：PDF p. 3；section: Literature Review
- 忠实释义：作者指出，利用点击流和交互网络等交互痕迹来预测“为什么”类意图（即动机）的研究相对未被探索。
- 原文校验：通过（exact_word_sequence_typography_normalized）
> While Bolle et al. [28] analyzed motives in a game context that relied on explicitly defined reward values, the open social exchange used in our study has no defined reward for actions. Also, there was no indication of whether the utility function can predict the players’ ‘unseen’ motives.

- 位置：PDF p. 4；section: Literature Review
- 忠实释义：作者指出，Bolle等人的研究依赖于明确定义的奖励值，而本研究使用的开放社会交换没有定义奖励；此外，尚不清楚效用函数能否预测玩家“未见的”动机。
- 原文校验：通过（normalized_exact）

### 作者承认的本研究局限、边界或仍未解决的问题

> This is an oversimplification because each allocation may be informed by multiple motives.

- 位置：PDF p. 4；section: The Present Study
- 忠实释义：作者承认，将每次分配视为仅由单一动机驱动是一种过度简化，因为每次分配可能受到多种动机的影响。
- 原文校验：通过（normalized_exact）
> a critique that can be made of this study is whether the ground truth is accurate. Self-reporting introduces inherent biases, including impression management, such as faking and lying [68]. This raised the question: why should we place trust in individuals’ self-disclosures? Consequently, self-reporting does not serve as a benchmark for accurately identifying motives. In our study, we combined previous moves and the knowledge of well-established theories on social exchanges to identify motives signaled by the recipient’s identity. While this approach mitigated the trust issues associated with self-reporting, it introduced a dependency on, and necessitated trust in, psychological theories about motives in social exchanges.

- 位置：PDF p. 13；section: Conclusion
- 忠实释义：作者承认，本研究对动机的识别依赖于社会交换理论，这引入了对心理学理论的依赖和信任问题，即动机的“真实值”可能不准确。
- 原文校验：通过（normalized_exact）

### 作者明确提出的未来研究方向

> An improvement would be to incorporate a search strategy that penalizes the algorithm when it is biased toward a class.

- 位置：PDF p. 13；section: Conclusion
- 忠实释义：作者建议未来改进C-HMM算法，加入一种搜索策略，当算法偏向某一类别时对其进行惩罚，以缓解类别不平衡的影响。
- 展望类型：method_or_measurement_only
- 方法性内容：改进C-HMM算法，加入惩罚偏向某一类别的搜索策略。
- 原文校验：通过（normalized_exact）

### 作者对既有文献、理论、方法或证据的明确批评

> While questionnaires and surveys have been traditional tools for investigating motives, they have inherent self-report biases and are expensive and time-consuming, particularly in repeated interactions where motives evolve over time.

- 位置：PDF p. 3；section: Literature Review
- 忠实释义：作者批评传统问卷和调查方法存在自我报告偏差，且在动机随时间演变的重复互动中成本高、耗时。
- 批评对象：traditional questionnaire and survey methods for investigating motives
- 原文校验：通过（normalized_exact）
> While Bolle et al. [28] analyzed motives in a game context that relied on explicitly defined reward values, the open social exchange used in our study has no defined reward for actions. Also, there was no indication of whether the utility function can predict the players’ ‘unseen’ motives.

- 位置：PDF p. 4；section: Literature Review
- 忠实释义：作者批评Bolle等人的研究依赖于明确定义的奖励值，且未表明效用函数能否预测未见的动机。
- 批评对象：Bolle et al. [28] study
- 原文校验：通过（normalized_exact）

## Joo2024: It is the AI fault not mine: Mind perception increases blame attribution to AI

- Year: 2024
- DOI: 10.1371/journal.pone.0314559
- Source PDF: `E:\Info_AI\defense_project\reference_materials\papers_originals\responsibility_moral_agency\Joo2024.pdf`

### 作者用于说明本研究必要性的既有研究缺口

> comparatively little attention has been given to explicit moral transgressions instigated by AIs.

- 位置：PDF p. 2；section: Introduction
- 忠实释义：作者指出，现有研究主要关注自动驾驶汽车事故或AI道德困境，而对AI引发的明确道德违规关注较少。
- 原文校验：通过（normalized_exact）
> they did not manipulate the mind perception, and only included mind-perception as a covariate along with other manipulations, obscuring the clear causal path between mind perception and blame attribution.

- 位置：PDF p. 3；section: Introduction
- 忠实释义：作者指出，Shank等人的研究未操纵心智感知，仅将其作为协变量，因此未能明确心智感知与责备归因之间的因果关系。
- 原文校验：通过（normalized_exact）

### 作者承认的本研究局限、边界或仍未解决的问题

> the study provides weak support for a causal relationship, as the data were correlational.

- 位置：PDF p. 6；section: Discussion
- 忠实释义：作者承认，研究1的数据是相关性的，因此对因果关系的支持较弱。
- 原文校验：通过（normalized_exact）
> One limitation of Studies 1 and 2 was that only the AI was explicitly referenced as an agent within the scenario, in contrast to others (e.g., the programmer). Consequently, an alternative explanation may emerge, wherein the influence of mind perception on individuals’ tendency to attribute moral culpability to AI becomes confounded with their exclusive presence as agents within the scenario.

- 位置：PDF p. 8；section: Discussion
- 忠实释义：作者承认研究1和2的一个局限：场景中只有AI被明确提及为行动者，而其他方（如程序员）未被提及，这可能导致对AI的归责受到其作为唯一行动者的混淆。
- 原文校验：通过（normalized_exact）
> Despite these speculations, given the sensitivity of our results to how blame was measured, caution should be exercised in interpreting the findings.

- 位置：PDF p. 10；section: General discussion
- 忠实释义：作者指出，由于结果对责备测量方式敏感，解释发现时需谨慎。
- 原文校验：通过（normalized_exact）
> Firstly, the stimuli utilized may not fully encompass the diverse array of scenarios found in real-world AI-related moral violations.

- 位置：PDF p. 11；section: General discussion
- 忠实释义：作者承认所用刺激材料可能未完全涵盖现实世界中AI相关道德违规的多样性场景。
- 原文校验：通过（normalized_exact）
> Secondly, as inherent in vignette studies, there remains uncertainty regarding the extent to which participants’ judgments reflect their reactions in actual situations involving AI.

- 位置：PDF p. 11；section: General discussion
- 忠实释义：作者承认，由于是情境研究，参与者的判断在多大程度上反映其在真实AI情境中的反应仍不确定。
- 原文校验：通过（normalized_exact）
> Also, this study focuses on blame as a cognitive process rather than as a negative affective response, such as anger or hostility.

- 位置：PDF p. 12；section: General discussion
- 忠实释义：作者指出，本研究关注的是作为认知过程的责备，而非愤怒或敌意等负面情感反应。
- 原文校验：通过（normalized_exact）
> We asked participants to distribute responsibility among various agents using a numerical scale based on previous studies [6,22]. However, this approach risks oversimplifying the complexities of the responsibility attribution process.

- 位置：PDF p. 12；section: General discussion
- 忠实释义：作者承认，使用数字量表分配责任可能过度简化了责任归因过程的复杂性。
- 原文校验：通过（normalized_exact）
> Moreover, the non-nationally representative sample used in the experiment may limit the generalizability of the findings, especially considering that online samples tend to comprise individuals with a certain level of technological literacy and comfort.

- 位置：PDF p. 12；section: General discussion
- 忠实释义：作者承认，实验使用的非全国代表性样本可能限制发现的普遍性，尤其在线样本往往由具备一定技术素养和舒适度的个体组成。
- 原文校验：通过（normalized_exact）

### 作者明确提出的未来研究方向

> in Study 2, we manipulated the levels of perceived AI mind in scenarios to directly assess their impact on the attribution of moral responsibility.

- 位置：PDF p. 6；section: Discussion
- 忠实释义：作者提出，在研究2中通过操纵AI心智感知水平来直接评估其对道德责任归因的影响，以建立因果关系。
- 展望类型：method_or_measurement_only
- 方法性内容：在研究2中，通过实验操纵AI心智感知水平，以直接评估其对道德责任归因的因果影响。
- 原文校验：通过（normalized_exact）
> future studies should aim to address this limitation by employing more comprehensive stimuli. For example, employing situational sampling techniques could facilitate the collection and categorization of a broader range of such incidents.

- 位置：PDF p. 11；section: General discussion
- 忠实释义：作者建议未来研究采用更全面的刺激材料，例如使用情境抽样技术来收集和分类更广泛的AI道德违规事件。
- 展望类型：method_or_measurement_only
- 方法性内容：采用情境抽样技术收集和分类更广泛的AI道德违规事件。
- 原文校验：通过（normalized_exact）
> Since affective responses are often triggered by cognitive blame, future research should explore how emotional reactions fluctuate depending on mind perception.

- 位置：PDF p. 12；section: General discussion
- 忠实释义：作者建议未来研究探索情感反应如何随心智感知而波动，因为情感反应常由认知责备触发。
- 展望类型：mechanism_specification
- 原始理论/构念术语：mind perception; blame; affective responses
- 分析层级：individual
- 作者指出的理论不足：当前研究仅关注责备的认知过程，未考察情感反应。
- 作者提出的理论推进：探索心智感知如何影响情感反应，从而扩展责备归因的机制理解。
- 待检验关系/命题：检验心智感知与情感反应（如愤怒、敌意）之间的关系。
- 原文校验：通过（normalized_exact）
> Future studies should further investigate the relationship between cognitive and affective components of blame, particularly in the context of AI moral transgressions.

- 位置：PDF p. 12；section: General discussion
- 忠实释义：作者建议未来研究进一步探讨责备的认知成分与情感成分之间的关系，特别是在AI道德违规情境中。
- 展望类型：construct_refinement
- 原始理论/构念术语：blame; cognitive component; affective component
- 分析层级：individual
- 作者指出的理论不足：责备的认知与情感成分之间的关系尚不清楚。
- 作者提出的理论推进：明确责备的认知与情感成分之间的区别与联系，以完善责备构念。
- 待检验关系/命题：检验责备的认知成分与情感成分在AI道德违规情境中的关系。
- 原文校验：通过（normalized_exact）
> Future studies should incorporate more comprehensive measures that capture the multidimensional nature of responsibility attribution, such as qualitative analyses of the reasons and amounts of blame assigned, as well as behavioral measures [10].

- 位置：PDF p. 12；section: General discussion
- 忠实释义：作者建议未来研究采用更全面的测量方法，如定性分析责备的原因和数量，以及行为测量，以捕捉责任归因的多维性。
- 展望类型：method_or_measurement_only
- 方法性内容：采用定性分析责备的原因和数量，以及行为测量。
- 原文校验：通过（normalized_exact）
> Therefore, future studies should strive to recruit more diverse and representative samples, such as through in-person community recruitment.

- 位置：PDF p. 12；section: General discussion
- 忠实释义：作者建议未来研究招募更多样化和有代表性的样本，例如通过线下社区招募。
- 展望类型：method_or_measurement_only
- 方法性内容：通过线下社区招募更多样化和有代表性的样本。
- 原文校验：通过（normalized_exact）

### 作者对既有文献、理论、方法或证据的明确批评

> they did not manipulate the mind perception, and only included mind-perception as a covariate along with other manipulations, obscuring the clear causal path between mind perception and blame attribution.

- 位置：PDF p. 3；section: Introduction
- 忠实释义：作者批评Shank等人的研究未操纵心智感知，仅将其作为协变量，导致心智感知与责备归因之间的因果关系不明确。
- 批评对象：Shank et al., [23]
- 原文校验：通过（normalized_exact）
> existing studies have predominantly focused on moral dilemmas involving AIs [27].

- 位置：PDF p. 3；section: Introduction
- 忠实释义：作者批评现有研究主要关注涉及AI的道德困境，而忽视了明确的道德违规。
- 批评对象：existing studies [27]
- 原文校验：通过（normalized_exact）
> Prior research in the literature predominantly centered on moral dilemmas or accidents, scenarios lacking deliberate violations of moral norms by any party involved [4–7].

- 位置：PDF p. 10；section: General discussion
- 忠实释义：作者批评先前研究主要关注道德困境或事故，这些场景缺乏任何一方故意违反道德规范。
- 批评对象：prior research [4–7]
- 原文校验：通过（normalized_exact）
> Even though mind perception has been examined in correlational studies [23], no prior study manipulated mind perception in the context of AI transgression.

- 位置：PDF p. 11；section: General discussion
- 忠实释义：作者指出，尽管心智感知已在相关研究中被检验，但尚无研究在AI违规情境中操纵心智感知。
- 批评对象：prior correlational studies [23]
- 原文校验：通过（normalized_exact）

## SIPRI2025: Impact of Military Artificial Intelligence on Nuclear Escalation Risk

- Year: 2025
- DOI: 10.55163/FZIW8544
- Source PDF: `E:\Info_AI\defense_project\reference_materials\papers_originals\ai_geopolitical_conflict\SIPRI2025.pdf`

### 作者用于说明本研究必要性的既有研究缺口

> This raises the fundamental question of whether AI introduces new risks, exacerbates existing ones or fundamentally alters the nature of nuclear escalation.

- 位置：PDF p. 2；section: Introduction
- 忠实释义：作者提出一个根本性问题：人工智能是引入了新的风险，加剧了现有风险，还是从根本上改变了核升级的性质。
- 原文校验：通过（normalized_exact）

### 作者承认的本研究局限、边界或仍未解决的问题

> This paper initiates a deeper exploration of this fundamental question.

- 位置：PDF p. 2；section: Introduction
- 忠实释义：作者承认本文只是对这一根本问题的初步探索，暗示研究尚不完整。
- 原文校验：通过（normalized_exact）
> Assessing the effect of military AI on nuclear escalation risk is highly complex due to the potential for AI to be integrated in various systems and at various levels across the military domain. This complexity is compounded by the variety of drivers of nuclear escalation, sources of nuclear risk and the fragile balance of strategic stability.

- 位置：PDF p. 10；section: Conclusions
- 忠实释义：作者承认，评估军事人工智能对核升级风险的影响非常复杂，因为人工智能可能以多种方式集成到不同军事系统和层级中，且核升级的驱动因素、风险来源和战略稳定性脆弱平衡进一步加剧了这种复杂性。
- 原文校验：通过（normalized_exact）
> the lack of transparency in this system prevents understanding of why it selected the most escalatory options.

- 位置：PDF p. 7；section: Military AI decision-support systems
- 忠实释义：作者指出，由于AI系统缺乏透明度，无法理解其为何选择最升级的选项，这构成了当前研究的一个局限。
- 原文校验：通过（normalized_exact）

### 作者明确提出的未来研究方向

> Section III concludes by summarizing the findings and indicating a potential direction for future policy-oriented research aimed at addressing this risk through existing or novel risk-reduction measures.

- 位置：PDF p. 2；section: Introduction
- 忠实释义：作者指出，未来政策导向的研究方向是通过现有或新的风险降低措施来应对这一风险。
- 展望类型：policy_or_practice_only
- 原文校验：通过（normalized_exact）
> Developing measures to mitigate the risk of nuclear use requires further examination of how military applications of AI can influence nuclear escalation risk in particular contexts and specific crisis scenarios.

- 位置：PDF p. 11；section: Conclusions
- 忠实释义：作者建议未来研究需要进一步考察军事人工智能应用在特定情境和具体危机场景中如何影响核升级风险，以制定风险缓解措施。
- 展望类型：context_or_population_only
- 原文校验：通过（normalized_exact）
> Elaborating on scenarios in which AI influences nuclear escalation can help inform the adaptation of existing risk-reduction measures or the development of new ones at the AI–nuclear nexus.

- 位置：PDF p. 11；section: Conclusions
- 忠实释义：作者建议未来研究应详细阐述人工智能影响核升级的场景，以帮助调整现有风险降低措施或开发新的措施。
- 展望类型：policy_or_practice_only
- 原文校验：通过（normalized_exact）
> These scenarios, for example, could highlight potential approaches to developing training standards for users of military AI. In turn, these approaches could establish redundancies that enable cross-checking of information from multiple sources and systems in order to prevent the deferral of responsibility to AI and ensure that operators are able to critically assess and challenge AI-generated recommendations.

- 位置：PDF p. 11；section: Conclusions
- 忠实释义：作者建议未来研究可通过场景分析，探索制定军事人工智能用户培训标准的方法，建立冗余机制以交叉核对多源信息，防止责任推卸给AI，并确保操作员能够批判性评估和质疑AI建议。
- 展望类型：policy_or_practice_only
- 原文校验：通过（normalized_exact）

### 作者对既有文献、理论、方法或证据的明确批评

> a 2024 study on fictional nuclear escalation scenarios found that large language models (LLMs)—a type of AI—often chose more escalatory options than human participants. This might be due to bias in training data or to the fact that AI lacks human empathy and may more readily make critical escalatory decisions as it is not subject to moral consideration or social norms, such as the nuclear use taboo. However, the lack of transparency in this system prevents understanding of why it selected the most escalatory options.

- 位置：PDF p. 7；section: Military AI decision-support systems
- 忠实释义：作者批评一项2024年的研究，指出其发现LLM在虚构核升级场景中比人类更倾向于选择升级选项，但该研究未能解释原因，因为AI系统缺乏透明度，无法理解其决策逻辑。
- 批评对象：Rivera, J.-P. et al., 'Escalation risks from language models in military and diplomatic decision-making', FAccT '24, 2024.
- 原文校验：通过（exact_word_sequence_typography_normalized）
