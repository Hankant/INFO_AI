# When Using AI Pays: Action-Contingent Incentives and Motivated Trust in AI

**Research fields:** Behavioral economics and decision analysis; human–AI decision-making; management control  
**Target journal:** *Management Science*  
**Umbrella topic:** Formation and governance of miscalibration between human trust and actual AI ability  
**Document type:** Research proposal  
**Version:** 2026-08-02

---

## Abstract

Organizations can encourage employees to use AI through bonuses, performance metrics, or procedural rules. However, the private benefits of using AI do not necessarily convey new information about AI ability. Existing research on algorithmic advice has mainly examined performance incentives aligned with decision accuracy and has found that such incentives can increase the uptake of algorithmic advice. It therefore answers whether incentives change AI use, but not whether they change people's judgments of AI ability (Greiner et al., 2026). Research on trust in AI further distinguishes actual trustworthiness, perceived trustworthiness, trust attitudes, and trusting behavior, and identifies strategic motivation as an underexplored principle (Everett et al., 2026). Against this background, the present study asks a concise question: **Do rewards for using AI cause people to overestimate AI ability?**

The study pits standard belief updating directly against motivated reasoning. If a reward is statistically independent of the AI's actual ability, then, conditional on participants receiving the same performance evidence, the reward can rationally change their decision to use the AI but should not change their judgment of its ability. Motivated reasoning and payoff-based belief distortion instead predict that the benefits of using AI will change how people process evidence about its ability, causing them to place less weight on AI errors and form upwardly biased ability judgments (Kunda, 1990; Epley & Gilovich, 2016; Jiao, 2020).

The research plan comprises two preregistered online experiments. Study 1 compares accuracy-based pay, an additional reward for adopting AI advice, and an equally sized reward unrelated to AI adoption, while holding AI performance and feedback identical across conditions. This design identifies whether the reward changes both reliance behavior and ability judgments. Study 2 manipulates whether participants receive a standardized summary of AI performance and continues observation after the reward is removed. It tests whether explicit ability evidence constrains belief distortion and whether the effect of the reward extends beyond immediate strategic use. The primary dependent variable is an incentive-compatible estimate of the AI's task accuracy. The AI's objective accuracy provides a fixed benchmark, and the difference between the two is defined as ability-judgment bias. Trust attitudes and actual reliance are measured separately; AI use is not treated as a proxy for trust. The theoretical contribution is to move strategic motivation upstream, from the conversion of trust into behavior to the formation of perceived ability from actual ability, and to distinguish rational use induced by incentives from overtrust caused by distorted beliefs.

## 1. Research Question and Scope

### 1.1 Main Research Question

> **RQ: Do rewards for using AI cause people to overestimate AI ability?**

The question contains only three necessary elements: the reward, the judgment of AI ability, and overestimation. Experimental conditions, feedback formats, and measurement occasions are part of the identification strategy and therefore do not appear in the research question.

### 1.2 Object of Study

The object of study is **an individual decision-maker's judgment of the ability of a particular AI system on a particular task**. The unit of analysis is the individual. The organization provides the applied setting for the incentive system but is not itself the unit of analysis. The study therefore requires no organization-level dynamic model, and findings from the individual experiment will not be directly extrapolated to organizational behavior.

### 1.3 What This Study Does Not Examine

The objective of this study is not to increase AI use. Greater use improves decisions only when the AI's actual ability warrants reliance; when trust exceeds the level supported by actual ability, increased use may instead amplify errors (Lee & See, 2004; Mehrotra et al., 2024). The study also does not examine responsibility shifting, AI accountability, or moral delegation, which are separate theoretical questions. Algorithm aversion and algorithm appreciation are neighboring streams of phenomenon-based research rather than the primary theories of this study.

## 2. Core Constructs

Mayer et al. (1995) define trust as a party's willingness to accept vulnerability based on the expectation that another party will perform actions important to the trustor. In the AI context, Everett et al. (2026) further distinguish actual trustworthiness, perceived trustworthiness, trust, and trusting behavior. Lee and See (2004) likewise emphasize that trust influences reliance, but that trust cannot be inferred simply by equating it with reliance behavior. The study therefore adopts the following definitions.

| Construct | Definition in this study | Operationalization |
|---|---|---|
| Actual AI ability \(q\) | The AI's objective accuracy on a prespecified task distribution; a task-specific component of the AI's performance trustworthiness | Fixed in advance using an independent item pool and held constant across all experimental conditions |
| Perceived AI ability \(\hat q_i\) | Individual \(i\)'s subjective estimate of the AI's accuracy on the same task distribution | A 0–100% probability estimate, rewarded according to its proximity to the true value |
| Performance trust | An attitude reflecting an individual's willingness to accept vulnerability under outcome uncertainty based on judgments of the AI's ability and reliability | A multi-item scale measuring willingness to rely on the AI in future tasks of the same type; reported separately from behavioral measures |
| Actual reliance | The behavior of accepting AI advice or revising an initial judgment toward that advice in a specific decision | Adoption rate and weight of advice on trials in which the participant and AI disagree |
| Ability-judgment bias \(G_i\) | The difference between perceived and actual ability | \(G_i=\hat q_i-q\); \(G_i>0\) indicates overestimation and \(G_i<0\) indicates underestimation |

Here, “overestimation” does not mean liking AI or using it frequently. It is a judgment error that can be compared directly with an objective benchmark. Because actual AI ability may differ across tasks, the study's conclusions apply only to the task distribution defined in the experiment. A single accuracy rate will not be presented as the AI's general ability.

## 3. Literature Base and Theoretical Gap

### 3.1 Trust in AI: The Construct Chain from Ability to Behavior

Classic research on trust in automation argues that trust guides reliance when users cannot fully understand a complex system and defines the objective as reliance appropriately matched to system capability rather than reliance maximization (Lee & See, 2004). Subsequent reviews show that trust is shaped jointly by system characteristics, individual differences, and situational conditions (Hoff & Bashir, 2015; Kaplan et al., 2023). A recent review further distinguishes actual trustworthiness, perceived trustworthiness, trust attitudes, and trusting behavior, and proposes that trust in AI is strategically motivated: the same individual may display different levels of trust in the same AI because their goals and interests differ across contexts (Everett et al., 2026).

This literature provides the construct structure for the present study, but it does not separately explain whether a reward that carries no information about AI ability can enter the judgment of that ability. **Synthesis by the present study: Existing frameworks generally place strategic motivation near trust or trusting behavior. This study tests whether it enters earlier, at the link between evidence of actual ability and perceived ability.**

### 3.2 Algorithmic Advice and Incentives: Use Has Been Explained, but Belief Distortion Has Not Been Identified

Research on algorithm aversion and algorithm appreciation shows that advice source, experience of errors, and control over an algorithm can change the uptake of algorithmic advice (Dietvorst et al., 2015, 2018; Logg et al., 2019). Recent studies in *Management Science* further show that capability-irrelevant cues—including human-involvement framing, voice similarity, and payment framing—can alter advice adoption or trusting behavior even when AI performance is unchanged (Yang et al., 2025; Bockstedt & Buckman, 2025; Schanke et al., 2024). These studies demonstrate that behavior can change while ability remains constant, but behavioral change alone does not establish that beliefs about ability have changed.

Greiner et al. (2026) provide the closest precedent. They compare fixed compensation, individual performance incentives, and tournament incentives, finding that performance incentives increase reliance on a better-performing algorithm without reducing task performance. Because the incentives reward more accurate final judgments, greater reliance on the superior algorithm can be consistent with standard utility maximization. Their study does not manipulate a reward that is triggered simply by adopting AI advice while providing no information about AI ability, nor does it compare subjective estimates of AI ability with an objective ability benchmark.

The existing evidence therefore leaves a specific gap: **Does a reward for adopting AI merely change the payoff to action, or does it also change people's beliefs about AI ability?** The present search of motivated reasoning, trust in AI, rewards, and ability judgments did not identify a study that simultaneously satisfies the following three conditions: (1) the reward is triggered solely by adopting AI advice; (2) evidence of AI ability is identical across conditions; and (3) subjective overestimation is measured against an objective ability benchmark. This gap statement is bounded by the scope of the present search and does not claim exhaustive coverage of all relevant literature.

### 3.3 Motivated Reasoning: Why Rewards May Change Ability Judgments

Kunda (1990) distinguishes accuracy motivation from directional motivation. Accuracy motivation leads people to use reasoning strategies they consider appropriate, whereas directional motivation makes evidence and interpretations supporting a desired conclusion more accessible, subject to the constraint that the conclusion must remain justifiable. Epley and Gilovich (2016) further summarize the influence of motivation on belief in terms of evidence search, evidence evaluation, and memory. Economic models of motivated beliefs likewise allow beliefs to trade off accuracy against psychological or behavioral benefits (Brunnermeier & Parker, 2005; Bénabou & Tirole, 2016).

Jiao's (2020) account of payoff-based belief distortion is the closest mechanism. Even when experienced payoffs contain no information about the state of the world, they may change subsequent information processing: beneficiaries relatively underweight negative signals and form more optimistic beliefs. Transposed to human–AI decision-making, a reward for adopting AI advice not only raises the immediate payoff from adoption but may also make “the AI is capable” a more desirable conclusion. Participants may consequently treat AI errors more leniently and AI successes more favorably, ultimately overestimating its ability.

## 4. Theoretical Framework

### 4.1 Standard Benchmark: Rewards May Change Action but Should Not Change Ability Beliefs

Let \(q\) denote the AI's true accuracy on the target task distribution, \(S=(s_1,\ldots,s_T)\) the performance evidence observed by an individual, and \(R\) the additional reward available for adopting AI advice. The experiment explicitly stipulates and randomly assigns \(R\), so that:

\[
R \perp q, S.
\]

Under the standard Bayesian benchmark:

\[
p(q\mid S,R)=p(q\mid S),
\]

and therefore, when priors and performance evidence are identical, the reward should not change the posterior judgment of AI ability:

\[
E(q\mid S,R)=E(q\mid S).
\]

The reward nevertheless enters the payoff from adopting AI advice. If \(A_i=1\) denotes adoption, an individual may choose \(A_i=1\) more frequently when \(R>0\), even if their belief about the AI's ability remains completely unchanged. **An increase in AI use caused by a reward therefore does not, by itself, demonstrate overtrust or irrationality.**

### 4.2 Motivated Beliefs: Rewards May Enter the Interpretation of Evidence

The study uses a simplified, testable expression for motivated beliefs without presenting it as a new general theory:

\[
\hat q_i=B(S_i)+\delta R_i+\varepsilon_i,
\]

where \(B(S_i)\) is the baseline ability judgment formed solely from identical performance evidence, and \(\delta\) captures whether the reward causes the ability judgment to depart systematically from that baseline. Standard belief updating predicts \(\delta=0\), whereas motivated reasoning predicts \(\delta>0\). When \(q\) is held constant across all conditions:

\[
G_i=\hat q_i-q.
\]

A larger \(G_i\) in the reward condition than in both control conditions constitutes the ability overestimation examined in this study.

If the reward operates by reducing the weight assigned to AI errors, the reward group should revise its ability judgment downward by less after receiving the same negative feedback. A standardized summary of the AI's correct and incorrect predictions reduces the scope for selective interpretation and should therefore attenuate this difference. This prediction follows specifically from the motivated-reasoning requirement that a desired conclusion remain justifiable, rather than from a generic claim that more information is always better (Kunda, 1990; Jiao, 2020).

### 4.3 From Belief to Behavior

Actual reliance is jointly determined by ability beliefs and current action payoffs:

\[
P(A_{it}=1)=f(\hat q_{it},\; \hat q^{self}_{it},\; R_{it},\; stakes_t).
\]

The total effect of the reward on reliance may therefore contain two pathways:

1. **Strategic use:** The reward directly raises the payoff from adopting AI advice but does not change \(\hat q\). The difference in use disappears after the reward is removed.
2. **Motivated trust:** The reward changes \(\hat q\) and thereby increases subsequent trust and reliance through an upwardly biased ability judgment. The difference may persist after the reward is removed.

The theoretical contribution depends on identifying the second pathway. If the experiments find only the first, the proposition that rewards cause overestimation of AI ability must be rejected, and the conclusion must be limited to strategic use.

## 5. Hypotheses

**H1 (Immediate use):** Relative to accuracy-based pay and an equally sized unconditional bonus, an additional reward for adopting AI advice will increase reliance on AI while the reward is available.

H1 is a manipulation check for the change in action payoffs rather than the paper's primary theoretical contribution.

**H2 (Ability overestimation):** Holding actual AI performance and performance evidence constant, an additional reward for adopting AI advice will increase perceived AI ability and enlarge the positive discrepancy between perceived and actual ability.

**H3 (Discounting negative evidence):** After observing the same AI error, participants in the AI-use reward condition will revise their ability judgments downward by less.

**H4 (Evidence constraint):** A standardized presentation of the AI's cumulative accuracy and error record will attenuate the effect of the AI-use reward on ability overestimation.

**H5 (Persistence after reward removal):** If the reward has changed ability judgments, the reward group will continue to exhibit higher performance trust and unrewarded reliance than the control group after the reward is removed. If the effect reflects only strategic use, this difference should disappear when the reward is removed.

## 6. Overview of the Research Method

### 6.1 Why an Experiment Is Appropriate

The study seeks to identify whether a reward changes ability judgments when ability evidence is held constant. In organizational observational data, rewards for AI use are likely to covary with management's assessment of AI quality, the actual quality of the adopted system, employee selection, and job tasks. It is therefore difficult to determine whether a reward truly carries no information about ability. A randomized experiment can hold AI outputs, accuracy, feedback order, and task difficulty constant while varying only the reward rule, directly matching the theoretical claim.

### 6.2 Task

Participants complete a demand-forecasting task framed as a managerial decision. Using simplified product information and historical market data, they judge whether demand in the next period will exceed a prespecified threshold. In each round, participants first answer independently and report confidence, then observe advice labeled as coming from an AI forecasting system, and finally submit a final judgment. Once the outcome is revealed, the interface displays the true outcome, whether the participant's initial judgment was correct, and whether the AI advice was correct.

AI outputs are generated from an item–advice sequence fixed before the experiment. The main experiment prespecifies an imperfect but informative accuracy level and ensures that all conditions receive the same advice, error locations, and outcome sequence. The exact accuracy and number of trials will be fixed after the pilot and preregistered. Actual AI ability is defined by its accuracy on the complete item pool, which is not disclosed to participants, thereby avoiding the treatment of a small number of chance successes as ability.

### 6.3 Common Measurement Occasions

- **T0:** Before the reward rule is introduced, measure initial judgments of AI ability, performance trust, and general attitudes toward AI.
- **T1:** After the reward rule is randomly assigned and explained but before the first decision, measure ability judgments again to identify changes triggered by reward information alone.
- **T2:** After participants have observed the common evidence of AI performance, measure ability judgments, performance trust, and reliance.
- **T3:** After the AI-use reward is removed, administer new tasks drawn from the same distribution and measure ability judgments and reliance without the reward.

Each ability estimate is rewarded according to its proximity to the prespecified true accuracy, giving participants an economic incentive to report accurately. The reward instructions explicitly state that the rule was randomly assigned by the experiment and is unrelated to the AI's developer or actual quality. Comprehension questions confirm this distinction and reduce the likelihood that participants interpret the reward as organizational endorsement of AI quality.

## 7. Study 1: Does the Reward Change Ability Judgments?

### 7.1 Design

Study 1 uses a three-condition between-subjects randomized design:

1. **Accuracy-pay condition:** Participants are paid for correct final judgments and receive no additional benefit from adopting AI advice.
2. **AI-use reward condition:** The same accuracy-based pay is retained. Participants receive an additional fixed reward whenever their final judgment adopts the AI advice, regardless of whether that judgment is correct.
3. **Matched unconditional bonus condition:** The same accuracy-based pay is retained. Each participant is paired with a preceding participant in the AI-use reward condition and receives exactly the same additional payment in each round as that matched participant, but the additional payment is unrelated to the recipient's own choice.

The third condition rules out changes in ability evaluations caused by total income, positive affect from receiving money, or a perception that the experiment is more generous. The AI advice and feedback sequence are identical across all three conditions. Participants see whether the AI was correct in each round regardless of whether they adopted its advice, so differences in AI use do not produce differences in exposure to ability evidence.

### 7.2 Primary Dependent Variable

The primary dependent variable is perceived AI accuracy at T2, \(\hat q_i\). The ability-judgment bias, \(G_i=\hat q_i-q\), is reported alongside it. The key comparisons contrast the AI-use reward condition with the accuracy-pay condition and the matched unconditional bonus condition. The result will be interpreted as ability overestimation caused by an AI-use-contingent reward only if both comparisons support a positive difference.

Secondary dependent variables include the T1 ability judgment, round-level adoption of AI advice, weight of advice, performance trust, and reliance at T3 after reward removal. Distinguishing T1 from T2 helps determine whether the effect arises immediately after the reward is introduced or only after participants repeatedly adopt the advice and observe outcomes.

### 7.3 Sample Planning

The preliminary sample plan is 1,050 participants, with 350 per condition. This figure is a planning value based on the available budget and the need to detect small effects; it is not the result of a completed power analysis. The final sample size will be determined after a small pilot using a preregistered simulation-based power analysis focused on the two primary contrasts for H2. Data collection will not be stopped early based on interim significance.

### 7.4 Diagnostic Outcomes for Study 1

| Result pattern | Permissible interpretation |
|---|---|
| The reward increases reliance but not \(\hat q_i\), and the difference disappears after reward removal | Strategic use; reject the ability-overestimation proposition |
| The reward increases both \(\hat q_i\) and \(G_i\) relative to both control conditions | Supports reward-induced distortion of ability beliefs |
| The matched unconditional bonus produces the same effect as the AI-use reward | General gain or affect effect; does not support an effect specific to the AI-use-contingent reward |
| No difference appears at T1, but one emerges at T2 | May reflect biased interpretation of feedback or post-adoption rationalization; Study 2 is needed to distinguish them |
| A difference is already present at T1 | The reward itself changes ability judgments; post-adoption cognitive dissonance alone cannot explain the effect |

## 8. Study 2: Negative Evidence and a Governance Mechanism

### 8.1 Design

Study 2 uses a 2 × 2 between-subjects randomized design:

- Reward: AI-use reward vs. matched unconditional bonus;
- Performance information: round-level raw feedback vs. round-level feedback plus a standardized cumulative performance summary.

The raw-feedback condition is identical to Study 1. In the performance-summary condition, the interface displays the AI's cumulative number of correct predictions, number of errors, and accuracy after each task block, without explanatory or persuasive language. All groups receive the same underlying evidence; the only difference is whether the observed outcomes are organized into a statistical summary that is less open to selective interpretation.

After the reward phase, all participants enter the unrewarded T3 phase. T3 uses new items from the same target distribution, and adopting AI advice no longer yields an additional reward. This design measures whether the reward effect persists and whether clearer performance information prevents upwardly biased beliefs from continuing to translate into reliance.

### 8.2 Mechanism Measures

After each block, participants estimate the AI's cumulative accuracy. This directly measures how much participants revise their estimate of AI ability downward when a block contains more AI errors. If the reward group revises its estimate downward by less after observing the same number of errors, and the standardized summary attenuates this difference, the result is consistent with the mechanism of underweighting negative evidence.

### 8.3 Sample Planning

The preliminary sample plan is 1,200 participants, with 300 in each cell. The final sample size will be jointly determined by the pilot estimates of variance, within-person correlation, and the minimum detectable reward × information interaction, and will be fixed through preregistration.

## 9. Analysis Plan

### 9.1 Primary Models

Study 1 estimates the T2 ability-judgment bias as follows:

\[
G_i=\alpha+\beta_1 AIReward_i+\beta_2 MatchedBonus_i+\gamma G_{i,T0}+X_i'\eta+\varepsilon_i.
\]

The accuracy-pay condition is the reference group. H2 requires \(\beta_1>0\), and the preregistered linear contrast between the AI-use reward condition and the matched unconditional bonus condition must also be significantly positive. \(X_i\) contains only prespecified baseline variables; post-reward attitudes, reliance, and performance will not be included as controls.

Study 2 estimates:

\[
G_i=\alpha+\beta_1 AIReward_i+\beta_2 Summary_i+\beta_3(AIReward_i\times Summary_i)+\gamma G_{i,T0}+\varepsilon_i.
\]

H4 predicts \(\beta_3<0\). Ability judgments and reliance at T3 will be analyzed using the same interaction structure.

### 9.2 Block-Level Responses to Evidence

Block-level ability estimates will be analyzed using an individual random-intercept model. Predictors include the cumulative numbers of correct and incorrect AI predictions before the relevant block, the reward condition, and their interactions. The critical test for H3 is the cumulative errors × AI-use reward interaction. If the reward group responds less to errors, this interaction should reduce the absolute magnitude of the negative adjustment in ability estimates. Because the cumulative numbers of correct and incorrect predictions jointly determine cumulative accuracy, the exact parameterization and functional form of the time trend will be preregistered before the results are observed.

### 9.3 Behavioral Outcomes

Reliance will be analyzed separately using a binary adoption model and a weight-of-advice model. The models will report both the total effect of the reward on reliance and the conditional association after accounting for baseline ability judgments. A mediation analysis using post-treatment ability judgments will not be interpreted directly as identifying a causal mechanism. Behavioral differences after reward removal provide more direct evidence for distinguishing immediate action payoffs from persistent ability beliefs.

### 9.4 Inference Rules

- The two planned contrasts for H2 are the primary tests and will be subject to preregistered familywise error-rate control.
- H1 and H3–H5 are mechanism and boundary tests. Effect sizes, confidence intervals, and raw means will be reported for each.
- Exclusion criteria are limited to repeat participation, noncompletion, failure of the reward-rule comprehension questions, and technical failures. They will be preregistered before condition differences are examined.
- Both full-sample intention-to-treat results and results for the comprehension-check sample will be reported; the primary conclusion will be based on the intention-to-treat analysis.
- For null results, the range of effect sizes ruled out by the data will be reported; nonsignificance will not be described as evidence of no effect whatsoever.

## 10. Competing Explanations and Identification Strategies

### 10.1 Purely Strategic Use

This is the most important competing explanation. The reward makes AI adoption more profitable, so increased reliance can be a rational change in action. Distortion of ability beliefs is supported only if the reward also raises incentive-compatible ability estimates and continues to affect trust or reliance after the reward is removed.

### 10.2 Income or Positive Affect

Through paired payments, the matched unconditional bonus condition holds the distribution of additional income constant while removing the condition that participants must adopt AI advice to benefit. If the two reward conditions produce the same ability judgments, the proposed mechanism is not supported.

### 10.3 Rewards as Organizational Endorsement

Participants may interpret an organizational reward for AI use as evidence that the organization possesses private information about the AI's high quality. The main experiment describes the reward as a randomly assigned experimental rule, emphasizes its independence from AI quality, and includes comprehension questions. This treatment increases internal validity, but it also means that the main experiment estimates the effect of an information-irrelevant reward. Policies in actual organizations may combine incentive and endorsement information, and their joint effect requires separate research.

### 10.4 Cognitive Dissonance or Post Hoc Rationalization

Cognitive dissonance theory may explain why people adjust their attitudes after taking an action. Classic forced-compliance research, however, also shows that sufficiently large external rewards can reduce rather than increase internal attitude change because they provide an external justification for the behavior (Festinger & Carlsmith, 1959). Cognitive dissonance is therefore not treated as the primary theory. T1 measures beliefs before the first rewarded adoption. If ability judgments already differ at T1, post-adoption rationalization is insufficient as an explanation. If a difference emerges only at T2, both biased interpretation of feedback and post hoc rationalization must remain viable explanations.

### 10.5 Demand Effects

The experimental materials will not use terms that reveal the purpose of the study, such as trust calibration, overestimation, or motivated reasoning. Ability estimates are rewarded for accuracy, reducing the payoff from accommodating perceived experimenter expectations. At the end of the study, participants will report what they believe the study was testing. These responses will be used in preregistered robustness analyses rather than as a basis for discretionary post hoc exclusions.

## 11. Expected Theoretical Contributions

### 11.1 Contribution to Research on Trust in AI

Everett et al. (2026) distinguish actual trustworthiness, perceived trustworthiness, trust, and trusting behavior and identify strategic motivation as a principle of trust in AI. This study turns that principle into a testable causal question: Does strategic motivation create bias when performance evidence is translated into perceived ability, rather than merely altering reliance after trust is already formed? The contribution therefore concerns the **formation of performance trust**, not generalized AI acceptance.

### 11.2 Contribution to Research on Motivated Beliefs

Research on motivated reasoning and payoff-based belief distortion shows that preferences and payoffs can change information processing (Kunda, 1990; Epley & Gilovich, 2016; Jiao, 2020). This study extends that research to judgments about the ability of an external intelligent agent and provides an objective, repeatable accuracy benchmark against which departures of belief from evidence can be measured directly. This contribution is supported only if the reward changes \(\hat q\), rather than merely changing AI use.

### 11.3 Contribution to Research on Algorithmic Advice and Management Control

Existing research shows that performance incentives aligned with accuracy can increase reliance on algorithmic advice (Greiner et al., 2026). The present study changes a critical feature of the incentive contract: the reward depends not on whether the decision is correct but on whether the employee adopts AI advice. This distinction separates two managerial outcomes—an incentive that encourages employees to make rational use of a superior tool and an incentive that leads employees to believe the rewarded tool is more capable. The former is a behavioral response; the latter is a trust bias.

### 11.4 Relationship to the Umbrella Topic

The umbrella topic examines why human trust becomes misaligned with actual AI ability and how that misalignment can be governed. The present study selects one formation mechanism and one governance lever: a reward for adopting AI advice may raise perceived ability while actual ability remains unchanged, whereas a standardized performance summary may constrain this bias by reducing the scope for selective interpretation of evidence. This focused question directly addresses the umbrella topic without attempting to explain every source of miscalibration in a single paper.

## 12. Managerial Implications

When organizations use AI usage rates, adoption rates, or “AI-first” procedures as performance indicators, the policy may produce two different outcomes. Employees may temporarily use AI to obtain a reward, or they may gradually mistake “the organization rewards it” for “it is more capable.” The former should disappear when the rule is removed; the latter may leave persistent overtrust. Organizations therefore should not evaluate the success of an AI project solely by adoption rates. They should also record task-specific system performance, employees' ability judgments, and the discrepancy between the two.

The governance intervention tested in Study 2 is not generic transparency but a specific organizational practice: while rewarding AI use, regularly show users the AI's cumulative number of correct predictions, number of errors, and accuracy on the same task distribution. A claim that such performance summaries constrain reward-induced trust bias is warranted only if the experiment supports H4. Before results are available, it remains a design proposal to be tested.

## 13. Feasibility, Limitations, and Boundaries

First, an online experiment can cleanly identify the causal effect of an information-irrelevant reward, whereas rewards in organizations often simultaneously communicate managerial endorsement. The main experiment prioritizes identification of the theoretical mechanism; subsequent field research would be required to estimate the combined effect of incentive and endorsement.

Second, actual AI ability is task-specific. Accuracy in the demand-forecasting task cannot represent the overall ability of generative AI, medical AI, or autonomous-driving systems, and the study makes no claim of a universal cross-domain effect.

Third, the main study does not include a human advisor with matched ability and therefore cannot claim that the effect is unique to AI. AI opacity and users' uncertainty about its ability create conditions for motivated interpretation, but AI nonsubstitutability requires validation in a separate boundary study.

Fourth, a standardized performance summary may both improve memory accuracy and reduce motivated interpretation. Study 2 can establish whether the summary attenuates bias, but the interaction alone cannot identify a unique psychological process. Block-level responses to errors and process measures increase explanatory leverage, but conclusions must remain proportionate to the strength of the data.

Fifth, if the reward increases use without increasing ability judgments, the study can still support a bounded conclusion: organizational incentives can produce strategic behavior characterized by high reliance but low trust. That outcome cannot be relabeled as trust distortion. It would falsify the main hypothesis.

## 14. Implementation Plan

| Stage | Work | Output |
|---|---|---|
| 1. Materials and pilot | Construct the demand-forecasting item pool; fix AI outputs; examine task difficulty, reward comprehension, and the distribution of ability estimates | Item pool, manipulation materials, and pilot report |
| 2. Preregistration | Freeze primary outcomes, contrasts, exclusion rules, power simulations, and analysis code | Study 1 preregistration |
| 3. Study 1 | Conduct the three-condition experiment and test whether strategic use can be separated from ability overestimation | Primary causal results |
| 4. Study 2 | Add the performance summary and observe persistence after reward removal | Mechanism and governance results |
| 5. Robustness and manuscript | Reproduce the analysis, audit construct validity, state boundaries, and prepare the paper | Submission manuscript and public materials |

## 15. Positioning in One Sentence

> This study does not ask whether rewards can make people use AI more. It asks: **When using AI is itself profitable but that benefit provides no evidence that the AI is more capable, do people nevertheless mistake benefit for ability?**

## References

Bénabou, R., & Tirole, J. (2016). Mindful economics: The production, consumption, and value of beliefs. *Journal of Economic Perspectives, 30*(3), 141–164. https://doi.org/10.1257/jep.30.3.141 · [中文总结](./Paper2_EWA_参考文献导航.md#benabou2016) · [官方原文](https://doi.org/10.1257/jep.30.3.141)

Bockstedt, J., & Buckman, J. R. (2025). Humans’ use of AI assistance. *Management Science, 72*(1), 323–342. https://doi.org/10.1287/mnsc.2024.05585 · [中文总结](./Paper2_EWA_参考文献导航.md#bockstedt2026) · [官方原文](https://doi.org/10.1287/mnsc.2024.05585)

Brunnermeier, M. K., & Parker, J. A. (2005). Optimal expectations. *American Economic Review, 95*(4), 1092–1118. https://doi.org/10.1257/0002828054825493 · [中文总结](./Paper2_EWA_参考文献导航.md#brunnermeier2005) · [本地原文](../../../defense_project/reference_materials/papers_originals/paper2_ewa/Brunnermeier2005.pdf)

Dietvorst, B. J., Simmons, J. P., & Massey, C. (2015). Algorithm aversion: People erroneously avoid algorithms after seeing them err. *Journal of Experimental Psychology: General, 144*(1), 114–126. https://doi.org/10.1037/xge0000033 · [中文总结](./Paper2_EWA_参考文献导航.md#dietvorst2015) · [本地原文](../../../defense_project/reference_materials/papers_originals/paper2_ewa/Dietvorst2015.pdf)

Dietvorst, B. J., Simmons, J. P., & Massey, C. (2018). Overcoming algorithm aversion: People will use imperfect algorithms if they can (even slightly) modify them. *Management Science, 64*(3), 1155–1170. https://doi.org/10.1287/mnsc.2016.2643 · [中文总结](./Paper2_EWA_参考文献导航.md#dietvorst2018) · [本地原文](../../../defense_project/reference_materials/papers_originals/paper2_ewa/Dietvorst2018.pdf)

Epley, N., & Gilovich, T. (2016). The mechanics of motivated reasoning. *Journal of Economic Perspectives, 30*(3), 133–140. https://doi.org/10.1257/jep.30.3.133 · [中文总结](./Paper2_EWA_参考文献导航.md#epley2016) · [官方原文](https://doi.org/10.1257/jep.30.3.133)

Everett, J. A. C., Claessens, S., Knöchel, T.-D., & Reinecke, M. G. (2026). Principles for understanding trust in artificial intelligence. *Nature Reviews Psychology, 5*, 388–401. https://doi.org/10.1038/s44159-026-00562-1 · [中文总结](./Paper2_EWA_参考文献导航.md#everett2026) · [官方原文](https://doi.org/10.1038/s44159-026-00562-1)

Festinger, L., & Carlsmith, J. M. (1959). Cognitive consequences of forced compliance. *Journal of Abnormal and Social Psychology, 58*(2), 203–210. https://doi.org/10.1037/h0041593 · [中文总结](./Paper2_EWA_参考文献导航.md#festinger1959) · [本地原文](../../../defense_project/reference_materials/papers_originals/paper2_ewa/Festinger1959.pdf)

Greiner, B., Grünwald, P., Lindner, T., Lintner, G., & Wiernsperger, M. (2026). Incentives, framing, and reliance on algorithmic advice: An experimental study. *Management Science, 72*(1), 302–322. https://doi.org/10.1287/mnsc.2022.02777 · [中文总结](./Paper2_EWA_参考文献导航.md#greiner2026) · [官方原文](https://doi.org/10.1287/mnsc.2022.02777)

Hoff, K. A., & Bashir, M. (2015). Trust in automation: Integrating empirical evidence on factors that influence trust. *Human Factors, 57*(3), 407–434. https://doi.org/10.1177/0018720814547570 · [中文总结](./Paper2_EWA_参考文献导航.md#hoff2015) · [官方原文](https://doi.org/10.1177/0018720814547570)

Jiao, P. (2020). Payoff-based belief distortion. *The Economic Journal, 130*(629), 1416–1444. https://doi.org/10.1093/ej/ueaa019 · [中文总结](./Paper2_EWA_参考文献导航.md#jiao2020) · [官方原文](https://doi.org/10.1093/ej/ueaa019)

Kaplan, A. D., Kessler, T. T., Brill, J. C., & Hancock, P. A. (2023). Trust in artificial intelligence: Meta-analytic findings. *Human Factors, 65*(2), 337–359. https://doi.org/10.1177/00187208211013988 · [中文总结](./Paper2_EWA_参考文献导航.md#kaplan2023) · [官方原文](https://doi.org/10.1177/00187208211013988)

Kunda, Z. (1990). The case for motivated reasoning. *Psychological Bulletin, 108*(3), 480–498. https://doi.org/10.1037/0033-2909.108.3.480 · [中文总结](./Paper2_EWA_参考文献导航.md#kunda1990) · [官方原文](https://doi.org/10.1037/0033-2909.108.3.480)

Lee, J. D., & See, K. A. (2004). Trust in automation: Designing for appropriate reliance. *Human Factors, 46*(1), 50–80. https://doi.org/10.1518/hfes.46.1.50_30392 · [中文总结](./Paper2_EWA_参考文献导航.md#leesee2004) · [官方原文](https://doi.org/10.1518/hfes.46.1.50_30392)

Logg, J. M., Minson, J. A., & Moore, D. A. (2019). Algorithm appreciation: People prefer algorithmic to human judgment. *Organizational Behavior and Human Decision Processes, 151*, 90–103. https://doi.org/10.1016/j.obhdp.2018.12.005 · [中文总结](./Paper2_EWA_参考文献导航.md#logg2019) · [本地原文](../../../defense_project/reference_materials/papers_originals/paper2_ewa/Logg2019.pdf)

Mayer, R. C., Davis, J. H., & Schoorman, F. D. (1995). An integrative model of organizational trust. *Academy of Management Review, 20*(3), 709–734. https://doi.org/10.5465/amr.1995.9508080335 · [中文总结](./Paper2_EWA_参考文献导航.md#mayer1995) · [官方原文](https://doi.org/10.5465/amr.1995.9508080335)

Mehrotra, S., et al. (2024). A systematic review on fostering appropriate trust in human-AI interaction: Trends, opportunities and challenges. *ACM Journal on Responsible Computing, 1*(4), Article 26. https://doi.org/10.1145/3696449 · [中文总结](./Paper2_EWA_参考文献导航.md#mehrotra2024) · [官方原文](https://doi.org/10.1145/3696449)

Schanke, S., Burtch, G., & Ray, G. (2024). Digital lyrebirds: Experimental evidence that voice-based deep fakes influence trust. *Management Science, 72*(1), 386–405. https://doi.org/10.1287/mnsc.2022.03316 · [中文总结](./Paper2_EWA_参考文献导航.md#schanke2026) · [官方原文](https://doi.org/10.1287/mnsc.2022.03316)

Yang, C. (L.), Bauer, K., Li, X., & Hinz, O. (2025). My advisor, her AI, and me: Evidence from a field experiment on human–AI collaboration and investment decisions. *Management Science, 72*(1), 242–264. https://doi.org/10.1287/mnsc.2022.03918 · [中文总结](./Paper2_EWA_参考文献导航.md#yang2026) · [官方原文](https://doi.org/10.1287/mnsc.2022.03918)
