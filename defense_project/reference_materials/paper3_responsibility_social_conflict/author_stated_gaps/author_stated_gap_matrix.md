# Paper 3：作者原文 Gap、局限、未来方向与前文批评

生成时间（UTC）：2026-08-12T02:44:57+00:00

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

## VanBaarEtAl2019: The computational and neural substrates of moral strategies in social decision-making

- Year: 2019
- DOI: 10.1038/s41467-019-09161-6
- Source PDF: `E:\Info_AI\defense_project\reference_materials\papers_originals\social_preferences_intergroup_conflict\VanBaarEtAl2019.pdf`

### 作者用于说明本研究必要性的既有研究缺口

> several important questions remain open. First, in most laboratory paradigms, guilt aversion and inequity aversion yield the same behavioral predictions, obfuscating which prosocial motivation was at play in the decision-maker’s mind (as noted by Nihonsugi et al. 14 and Hein et al. 15). Therefore, one important outstanding question is whether these two motivations can be uncoupled behaviorally. Second, the stability of moral strategies is largely unknown. Do people behave consistently across different instances of moral dilemmas or is their decision-making a product of the particular context they are facing? Finally, and crucially, previous neuroimaging studies have averaged measurements across participants, potentially masking individual differences in implicit moral reasoning, and hence obscuring strategy-specific features of the moral brain.

- 位置：PDF p. 2；section: Introduction
- 忠实释义：作者指出几个重要问题尚未解决：首先，在多数实验室范式中，内疚厌恶和不公平厌恶产生相同的行为预测，难以区分决策者的亲社会动机；其次，道德策略的稳定性尚不清楚；最后，以往的神经影像研究对参与者进行平均，可能掩盖了个体差异，从而模糊了道德大脑的策略特异性特征。
- 原文校验：通过

### 作者承认的本研究局限、边界或仍未解决的问题

> An obvious downside of this approach is that we could not control the relative frequencies of moral strategies in our dataset, which contained a relatively low number of purely guilt-averse participants.

- 位置：PDF p. 9；section: Discussion
- 忠实释义：作者承认该方法的一个明显缺点是，他们无法控制数据集中道德策略的相对频率，其中纯粹内疚厌恶的参与者数量相对较少。
- 原文校验：通过
> It is important to note that smaller groups have less power.

- 位置：PDF p. 12；section: Cluster strength analysis
- 忠实释义：作者指出，较小的组统计效力较低。
- 原文校验：通过

### 作者对既有文献、理论、方法或证据的明确批评

> previous neuroimaging studies have averaged measurements across participants, potentially masking individual differences in implicit moral reasoning, and hence obscuring strategy-specific features of the moral brain.

- 位置：PDF p. 2；section: Introduction
- 忠实释义：作者批评以往的神经影像研究：对参与者进行平均测量，可能掩盖了内隐道德推理的个体差异，从而模糊了道德大脑的策略特异性特征。
- 批评对象：previous neuroimaging studies on moral decision-making
- 原文校验：通过
> in most laboratory paradigms, guilt aversion and inequity aversion yield the same behavioral predictions, obfuscating which prosocial motivation was at play in the decision-maker’s mind (as noted by Nihonsugi et al. 14 and Hein et al. 15).

- 位置：PDF p. 2；section: Introduction
- 忠实释义：作者批评以往实验室范式：内疚厌恶和不公平厌恶产生相同的行为预测，混淆了决策者真正的亲社会动机。
- 批评对象：prior laboratory paradigms for guilt aversion and inequity aversion
- 原文校验：通过

## IgweEtAl2024: Analyzing Social Exchange Motives With Theory-Driven Data and Machine Learning

- Year: 2024
- DOI: 10.1109/ACCESS.2023.3348755
- Source PDF: `E:\Info_AI\defense_project\reference_materials\papers_originals\social_preferences_intergroup_conflict\IgweEtAl2024.pdf`

### 作者用于说明本研究必要性的既有研究缺口

> predicting motive from interaction traces presents a new challenge: While intent predominantly anticipates ‘what’ actions people or artificial agents will take [8], motives explore the ‘why’ behind these actions, revealing the underlying reason.

- 位置：PDF p. 2；section: Introduction
- 忠实释义：作者指出，从交互轨迹预测动机是一个新挑战，因为意图主要预测“什么”行动，而动机探究行动背后的“为什么”。
- 原文校验：通过
> only a limited body of literature has focused on the ‘why’ based intent.

- 位置：PDF p. 2；section: Introduction
- 忠实释义：作者指出，只有有限的文献关注了基于“为什么”的意图。
- 原文校验：通过
> The prediction of ‘why’ based intent using interaction traces like the clickstream and interaction network, however, remains relatively unexplored.

- 位置：PDF p. 3；section: Literature Review
- 忠实释义：作者指出，使用点击流和交互网络等交互轨迹预测基于“为什么”的意图仍然相对未被探索。
- 原文校验：通过

### 作者承认的本研究局限、边界或仍未解决的问题

> This is an oversimplification because each allocation may be informed by multiple motives.

- 位置：PDF p. 4；section: The Present Study
- 忠实释义：作者承认，将每次分配视为仅由单一动机驱动是一种过度简化，因为每次分配可能受多种动机影响。
- 原文校验：通过
> predicting motives from interaction traces in a social exchange context is relatively unexplored. Thus, it is important to first test well-known basic algorithms.

- 位置：PDF p. 6；section: Method
- 忠实释义：作者承认从社交交换中的互动轨迹预测动机是一个相对未被探索的领域，因此本研究首先测试了基本的机器学习算法。
- 原文校验：通过
> the current study refrained from explicitly interpreting each cluster

- 位置：PDF p. 8；section: Method
- 忠实释义：作者指出本研究未对每个聚类进行明确解释。
- 原文校验：通过
> a critique that can be made of this study is whether the ground truth is accurate. Self-reporting introduces inherent biases, including impression management, such as faking and lying [68]. This raised the question: why should we place trust in individuals’ self-disclosures? Consequently, self-reporting does not serve as a benchmark for accurately identifying motives. In our study, we combined previous moves and the knowledge of well-established theories on social exchanges to identify motives signaled by the recipient’s identity. While this approach mitigated the trust issues associated with self-reporting, it introduced a dependency on, and necessitated trust in, psychological theories about motives in social exchanges.

- 位置：PDF p. 13；section: Conclusion
- 忠实释义：作者承认，本研究的一个可批评之处在于其真实标签的准确性：虽然避免了自我报告带来的印象管理等偏见，但方法依赖于并需要信任关于社会交换动机的心理学理论。
- 原文校验：通过
> its performance indicated that it was susceptible to an imbalanced dataset.

- 位置：PDF p. 13；section: Conclusion
- 忠实释义：作者指出，C-HMM算法的性能表明它对不平衡数据集敏感。
- 原文校验：通过

### 作者明确提出的未来研究方向

> An improvement would be to incorporate a search strategy that penalizes the algorithm when it is biased toward a class.

- 位置：PDF p. 13；section: Conclusion
- 忠实释义：作者建议，未来的改进可以引入一种搜索策略，当算法偏向某一类别时对其进行惩罚。
- 原文校验：通过

### 作者对既有文献、理论、方法或证据的明确批评

> While Bolle et al. [28] analyzed motives in a game context that relied on explicitly defined reward values, the open social exchange used in our study has no defined reward for actions. Also, there was no indication of whether the utility function can predict the players’ ‘unseen’ motives.

- 位置：PDF p. 4；section: Literature Review
- 忠实释义：作者批评Bolle等人的研究依赖于明确定义的奖励值，而本研究使用的开放社会交换没有定义奖励；且未表明效用函数能否预测玩家“未见的”动机。
- 批评对象：Bolle et al. [28]
- 原文校验：通过
> SVC is known to underperform when dealing with imbalanced classes [63].

- 位置：PDF p. 9；section: Preliminary Analysis
- 忠实释义：作者批评支持向量分类器在处理不平衡类别时表现不佳。
- 批评对象：Support Vector Classifier (SVC)
- 原文校验：通过
> Self-reporting introduces inherent biases, including impression management, such as faking and lying [68].

- 位置：PDF p. 13；section: Conclusion
- 忠实释义：作者批评自我报告方法引入固有偏见，包括印象管理，如伪装和说谎。
- 批评对象：self-reporting methods in behavioral studies
- 原文校验：通过

## Joo2024: It is the AI fault not mine: Mind perception increases blame attribution to AI

- Year: 2024
- DOI: 10.1371/journal.pone.0314559
- Source PDF: `E:\Info_AI\defense_project\reference_materials\papers_originals\responsibility_moral_agency\Joo2024.pdf`

### 作者用于说明本研究必要性的既有研究缺口

> Considerable scholarly attention has been paid to responsibility gap caused by accident involving autonomous vehicles (AVs), or moral dilemmas in AI decision-making [4–8]. However, comparatively little attention has been given to explicit moral transgressions instigated by AIs.

- 位置：PDF p. 2；section: Introduction
- 忠实释义：作者指出，现有研究多关注自动驾驶汽车事故或AI道德困境中的责任差距，但对AI引发的明确道德违规关注较少。
- 原文校验：通过
> Shank et al., [23] measured mind perception in the context of AI moral transgression to examine the link between mind perception of AI and blame. They found that perceived mind in AI was linked to higher blame in AI. However, they did not manipulate the mind perception, and only included mind-perception as a covariate along with other manipulations, obscuring the clear causal path between mind perception and blame attribution.

- 位置：PDF p. 3；section: Introduction
- 忠实释义：作者指出，Shank等人虽测量了AI道德违规情境中的心智感知与责备的关系，但未操纵心智感知，仅将其作为协变量，未能明确心智感知与责备归因之间的因果关系。
- 原文校验：通过

### 作者承认的本研究局限、边界或仍未解决的问题

> However, the study provides weak support for a causal relationship, as the data were correlational.

- 位置：PDF p. 6；section: Study 1 Discussion
- 忠实释义：作者承认，研究1的数据是相关性的，因此对因果关系的支持较弱。
- 原文校验：通过
> One limitation of Studies 1 and 2 was that only the AI was explicitly referenced as an agent within the scenario, in contrast to others (e.g., the programmer). Consequently, an alternative explanation may emerge, wherein the influence of mind perception on individuals’ tendency to attribute moral culpability to AI becomes confounded with their exclusive presence as agents within the scenario.

- 位置：PDF p. 8；section: Discussion
- 忠实释义：作者承认研究1和2的一个局限是只有AI被明确提及为场景中的行动者，而其他行动者（如程序员）则没有，这可能导致对AI的归因受到其作为唯一行动者的混淆。
- 原文校验：通过
> Despite these speculations, given the sensitivity of our results to how blame was measured, caution should be exercised in interpreting the findings.

- 位置：PDF p. 10；section: General discussion
- 忠实释义：作者指出，由于结果对责备测量方式敏感，在解释发现时应谨慎。
- 原文校验：通过
> Limitations of the current research must be acknowledged. Firstly, the stimuli utilized may not fully encompass the diverse array of scenarios found in real-world AI-related moral violations.

- 位置：PDF p. 11；section: General discussion
- 忠实释义：作者承认当前研究的局限：首先，使用的刺激材料可能无法完全涵盖现实世界中AI相关道德违规的多样化场景。
- 原文校验：通过
> Secondly, as inherent in vignette studies, there remains uncertainty regarding the extent to which participants’ judgments reflect their reactions in actual situations involving AI.

- 位置：PDF p. 11；section: General discussion
- 忠实释义：作者承认，作为情境研究固有的局限，参与者的判断在多大程度上反映他们在实际涉及AI的情境中的反应仍不确定。
- 原文校验：通过
> Also, this study focuses on blame as a cognitive process rather than as a negative affective response, such as anger or hostility.

- 位置：PDF p. 12；section: General discussion
- 忠实释义：作者指出，本研究关注的是作为认知过程的责备，而非愤怒或敌意等负面情感反应。
- 原文校验：通过
> We asked participants to distribute responsibility among various agents using a numerical scale based on previous studies [6,22]. However, this approach risks oversimplifying the complexities of the responsibility attribution process.

- 位置：PDF p. 12；section: General discussion
- 忠实释义：作者承认，使用数字量表让参与者在不同行动者之间分配责任可能过度简化了责任归因过程的复杂性。
- 原文校验：通过
> Moreover, the non-nationally representative sample used in the experiment may limit the generalizability of the findings, especially considering that online samples tend to comprise individuals with a certain level of technological literacy and comfort.

- 位置：PDF p. 12；section: General discussion
- 忠实释义：作者承认，实验使用的非全国代表性样本可能限制了研究结果的普遍性，尤其是在线样本往往由具有一定技术素养和舒适度的个体组成。
- 原文校验：通过

### 作者明确提出的未来研究方向

> Considering the increasing integration of AI into various aspects of our lives, future studies should aim to address this limitation by employing more comprehensive stimuli. For example, employing situational sampling techniques could facilitate the collection and categorization of a broader range of such incidents.

- 位置：PDF p. 11；section: General discussion
- 忠实释义：作者建议未来研究应采用更全面的刺激材料，例如使用情境抽样技术来收集和分类更广泛的AI道德违规事件。
- 原文校验：通过
> Since affective responses are often triggered by cognitive blame, future research should explore how emotional reactions fluctuate depending on mind perception.

- 位置：PDF p. 12；section: General discussion
- 忠实释义：作者建议未来研究应探索情绪反应如何随心智感知而波动。
- 原文校验：通过
> Future studies should further investigate the relationship between cognitive and affective components of blame, particularly in the context of AI moral transgressions.

- 位置：PDF p. 12；section: General discussion
- 忠实释义：作者建议未来研究应进一步探讨责备的认知和情感成分之间的关系，特别是在AI道德违规的背景下。
- 原文校验：通过
> Future studies should incorporate more comprehensive measures that capture the multidimensional nature of responsibility attribution, such as qualitative analyses of the reasons and amounts of blame assigned, as well as behavioral measures [10].

- 位置：PDF p. 12；section: General discussion
- 忠实释义：作者建议未来研究应采用更全面的测量方法，捕捉责任归因的多维性质，例如对责备原因和数量的定性分析以及行为测量。
- 原文校验：通过
> Therefore, future studies should strive to recruit more diverse and representative samples, such as through in-person community recruitment.

- 位置：PDF p. 12；section: General discussion
- 忠实释义：作者建议未来研究应努力招募更多样化和具有代表性的样本，例如通过面对面的社区招募。
- 原文校验：通过

### 作者对既有文献、理论、方法或证据的明确批评

> Shank et al., [23] measured mind perception in the context of AI moral transgression to examine the link between mind perception of AI and blame. They found that perceived mind in AI was linked to higher blame in AI. However, they did not manipulate the mind perception, and only included mind-perception as a covariate along with other manipulations, obscuring the clear causal path between mind perception and blame attribution.

- 位置：PDF p. 3；section: Introduction
- 忠实释义：作者批评Shank等人的研究未操纵心智感知，仅将其作为协变量，导致心智感知与责备归因之间的因果关系不明确。
- 批评对象：Shank et al. (2020)
- 原文校验：通过

## SIPRI2025: Impact of Military Artificial Intelligence on Nuclear Escalation Risk

- Year: 2025
- DOI: 10.55163/FZIW8544
- Source PDF: `E:\Info_AI\defense_project\reference_materials\papers_originals\ai_geopolitical_conflict\SIPRI2025.pdf`

### 作者用于说明本研究必要性的既有研究缺口

> Developing measures to mitigate the risk of nuclear use requires further examination of how military applications of AI can influence nuclear escalation risk in particular contexts and specific crisis scenarios.

- 位置：PDF p. 11；section: Conclusions
- 忠实释义：作者指出，需要进一步研究军事AI应用在特定情境和具体危机场景中如何影响核升级风险，以制定风险缓解措施。
- 原文校验：通过

### 作者承认的本研究局限、边界或仍未解决的问题

> This paper initiates a deeper exploration of this fundamental question.

- 位置：PDF p. 2；section: Introduction
- 忠实释义：本文启动了对这一根本问题的更深入探索，暗示当前研究仅为初步探讨。
- 原文校验：通过
> Assessing the effect of military AI on nuclear escalation risk is highly complex due to the potential for AI to be integrated in various systems and at various levels across the military domain. This complexity is compounded by the variety of drivers of nuclear escalation, sources of nuclear risk and the fragile balance of strategic stability.

- 位置：PDF p. 10；section: Conclusions
- 忠实释义：作者承认，评估军事AI对核升级风险的影响非常复杂，因为AI可能被整合到军事领域的各种系统和各个层面，且核升级的驱动因素、核风险来源和战略稳定性的脆弱平衡加剧了这种复杂性。
- 原文校验：通过

### 作者明确提出的未来研究方向

> Section III concludes by summarizing the findings and indicating a potential direction for future policy-oriented research aimed at addressing this risk through existing or novel risk-reduction measures.

- 位置：PDF p. 2；section: Introduction
- 忠实释义：作者指出第三节将总结发现并指出未来政策导向研究的潜在方向，旨在通过现有或新的风险降低措施应对这一风险。
- 原文校验：通过
> Elaborating on scenarios in which AI influences nuclear escalation can help inform the adaptation of existing risk-reduction measures or the development of new ones at the AI–nuclear nexus.

- 位置：PDF p. 11；section: Conclusions
- 忠实释义：作者建议，详细阐述AI影响核升级的场景，有助于调整现有风险降低措施或开发AI-核交叉领域的新措施。
- 原文校验：通过
> These scenarios, for example, could highlight potential approaches to developing training standards for users of military AI.

- 位置：PDF p. 11；section: Conclusions
- 忠实释义：作者建议，这些场景可以突出制定军事AI用户培训标准的潜在方法。
- 原文校验：通过
