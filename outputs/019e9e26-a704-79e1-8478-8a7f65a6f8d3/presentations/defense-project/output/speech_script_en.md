# English Speech Script

This script follows the 20-slide defense deck and is designed for a concise proposal defense presentation.

## Slide 01: Algorithmic Authority and Information Calibration

Good morning, and thank you for the opportunity to present my proposal. My project asks a simple but important question: when people see an AI-generated answer before they inspect the evidence themselves, does that change how much more they want to search, how much they feel they truly know, and how they update when counterevidence arrives? I will show why this question matters, how the revised design improves identification, and where I would still strengthen the experiment before implementation.

## Slide 02: Generative AI may change the order of judgment before it changes the final answer.

The main intuition is that generative AI does more than save time. It can shift the sequence of cognition. Instead of evidence first and judgment later, users often receive a structured answer first and only then decide whether to verify it. That matters because belief formation is not only about which answer we adopt. It is also about whether we think we have seen enough evidence, whether we feel that the knowledge is really ours, and whether we still respond appropriately to disconfirming signals.

## Slide 03: The epistemic sequence is reversed in an answer-first environment.

This slide captures the background in one picture. In a traditional information environment, people usually collect evidence, build an explanation, and then reach a judgment. In a generative AI environment, the user often sees an answer and a coherent narrative first, and verification becomes optional. My argument is that this reversal can reshape the stopping rule for search and the weight assigned to later evidence. That is the basic background from which the entire project starts.

## Slide 04: The project sits at the intersection of three research traditions.

The literature review is organized into three streams. The first is information acquisition, which tells us that search depth and stopping rules matter. The second is belief updating, which tells us that people often underweight or reinterpret counterevidence. The third is algorithmic authority, which shows that human responses to automated systems are complex. My project connects these literatures by asking how generative AI changes both information acquisition and later updating through a new metacognitive layer.

## Slide 05: The missing link is metacognitive calibration, not answer adoption alone.

The gap is not that we know nothing about trust or persuasion. The gap is that we still do not explain cleanly how users recalibrate the information environment itself after receiving an AI answer. My project therefore shifts the question. Instead of asking only whether users accept the answer, I ask whether the label and format of an AI answer change the perceived sufficiency of current evidence, the ownership of knowledge, and the diagnosticity of what comes next.

## Slide 06: The revised proposal organizes the theory as three calibration problems.

A key improvement in the revised version is theoretical discipline. Instead of assuming double Bayesian distortion from the start, the revised proposal reframes the problem as three possible calibration failures. First, users may think the evidence is already sufficient. Second, they may know more than they feel they know because AI compressed the evidence for them. Third, they may assign too little weight to later counterevidence. This makes the theory more testable and less rhetorically overloaded.

## Slide 07: The revised draft asks a cleaner mechanism question.

This slide sorts out the research purpose and the research questions. The broad purpose is to study how answer-first AI changes metacognitive calibration under uncertainty. The more specific mechanism question is this: if the initial summary is the same and additional search cost is held constant, does the AI label itself change how users value more evidence, how much ownership they feel, and how they update later? That is the cleaner empirical question I would emphasize in the defense.

## Slide 08: Why the revised design is stronger than the original draft.

This is the most important revision to explain to the committee. The original design compared AI search and traditional search more directly, but that bundled together too many mechanisms, especially search cost. The revised design narrows the estimand. It asks whether the AI label changes behavior and judgment after the initial answer, when the remaining search environment is held constant. That makes the project more defensible methodologically, and it also makes the theory more precise.

## Slide 09: The same-summary source-label design isolates a plausible AI-specific effect.

The identification strategy is straightforward but powerful. Every participant can face the same prior information, the same initial summary text, the same downstream evidence pool, and the same marginal search cost for additional evidence. The only difference is whether the summary is absent, unlabeled, labeled as AI, or labeled as expert. If the AI label still changes search demand or later updating, then the explanation is no longer just that AI made search objectively cheaper.

## Slide 10: Study 1 tests whether AI labels reduce additional information acquisition.

Study 1 is the first empirical test of the new design. The task is a corporate default-risk judgment. Participants start from the same prior and the same base information. The experimental manipulation occurs at the level of the initial answer. Then everyone enters the same additional evidence pool and faces the same token cost for viewing more evidence. The key outcome is whether the AI label reduces demand for additional evidence, not whether AI search is globally faster than traditional search.

## Slide 11: Study 1 traces a mechanism from source label to search stopping.

The logic of Study 1 is a mediation chain. The AI label should first increase perceived sufficiency. That should lower the felt value of one more piece of evidence. And that lower value should lead users to stop sooner or buy less additional evidence. Importantly, the design lets me test whether the behavior operates through subjective valuation rather than through objective cost. That is why the revised version is much sharper than a general AI-versus-search comparison.

## Slide 12: Study 2 asks whether AI compression creates an ownership mismatch.

Study 2 is conceptually important because it adds something the original draft did not emphasize enough: epistemic ownership. The same underlying information can be delivered in two ways. In one condition, AI compresses it into a structured answer. In another, the participant searches through it directly. My expectation is that AI compression may help participants reach a better posterior more efficiently, but they may still feel that the knowledge is not fully their own. That mismatch is theoretically and practically important.

## Slide 13: Study 3 uses a yoked design to isolate belief updating.

Study 3 preserves one of the best ideas from the original proposal: the yoked control. Once participants enter the updating stage with equal information sets, any remaining difference in reaction to a high-likelihood-ratio disconfirming shock is harder to explain by saying that one group simply saw less. This is where the project can most cleanly test whether an AI-labeled initial answer changes the diagnostic weight assigned to later counterevidence.

## Slide 14: The design keeps a computable Bayesian benchmark while staying behaviorally meaningful.

Methodologically, I would emphasize that the project still keeps a normative benchmark. The evidence-generating process is controlled, the likelihood ratios are known, and the shock in the updating stage is measurable in log-odds terms. That allows me to distinguish between two different problems: not acquiring enough evidence and not giving enough weight to evidence that is already available. I would also clearly state that the AI answer is modeled as a lossy compression of the evidence environment, not as an independent signal.

## Slide 15: The project contributes on theory, design, and governance.

These are the contributions I would emphasize in the defense. Theoretically, the project treats generative AI as answer-first epistemic infrastructure. Mechanistically, it separates three calibration problems. Empirically, it offers a cleaner identification strategy than the original draft. And from a governance perspective, it argues that we should design information architectures that improve calibration under different levels of risk rather than simply telling everyone to verify more.

## Slide 16: Governance should match risk, not maximize verification in every context.

This slide speaks to the research meaning of the project. The practical implication is not that every AI system should force exhaustive verification. That would often be wasteful. The implication is that different risk environments need different information architectures. In low-risk contexts, gentle prompts may be enough. In medium-risk contexts, conflict-first or uncertainty-calibrated summaries may improve calibration. In high-risk contexts, stronger friction may be justified because the cost of error is much larger.

## Slide 17: What the revised version already solves well.

If I were answering a committee question about whether the revision was worthwhile, I would say yes for four reasons. First, it resolves the largest identification issue. Second, it keeps the Bayesian benchmark that gives the project rigor. Third, it decomposes authority effects more carefully with AI, unlabeled, and expert conditions. Fourth, it adds epistemic ownership, which makes the paper more original and more relevant to contemporary debates about human-AI judgment.

## Slide 18: What I would still update before the defense or pre-registration.

The revised draft is stronger, but there are still upgrades I would recommend. The most important is a manipulation pretest, because label-based designs can unintentionally import assumptions about quality or competence. I would also diversify the scenario set, add objective ownership measures, collect moderator variables, and pre-register robustness outcomes such as Brier score or log score. Finally, I would consider one more naturalistic follow-up task to strengthen external validity after the cleaner identification test.

## Slide 19: The central claim is about calibration under AI, not blind hostility to AI.

My final message would be that this project is not anti-AI. It is about calibration. AI may improve efficiency and even improve posterior quality in some contexts. But it can also shift the stopping rule for search, weaken ownership of understanding, and alter responses to counterevidence. The revised version is stronger because it asks a narrower and more credible causal question while preserving the broader theoretical ambition about how answer-first systems reshape human judgment.

## Slide 20: Thank you.

Thank you very much. I welcome questions especially on the identification strategy, the way I distinguish perceived ownership from confidence, and the conditions under which governance friction is justified.

