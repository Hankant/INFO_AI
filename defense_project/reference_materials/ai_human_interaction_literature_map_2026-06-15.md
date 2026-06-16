# AI-human interaction literature map

Date: 2026-06-15

## Scope

This note curates papers that are directly useful for a dissertation on:

- AI and human information search / belief updating
- trust, calibrated reliance, and ceding control to AI
- responsibility attribution, dishonesty, moral distance, and prosocial behavior
- longer-run learning, skill retention, and adaptation to AI

Sources prioritized in this round:

- `Nature Human Behaviour`
- `PNAS`
- `Nature`
- `Journal of Economic Behavior & Organization (JEBO)`
- `Journal of Behavioral and Experimental Economics (JBEE)`
- adjacent top journals: `Management Science`, `Organization Science`

This is not a keyword dump. It is a filtered map of papers that are most likely to matter for your current project.

## A. Top-tier behavior science

### 1. Human-AI collaboration and decision quality

- [When combinations of humans and AI are useful](https://www.nature.com/articles/s41562-024-02024-1)
  Journal: `Nature Human Behaviour`, 2024
  Design: systematic review and meta-analysis of 106 experiments and 370 effect sizes.
  Use for you: strongest high-level evidence that human-AI combinations do not automatically outperform the best human or the best AI. Very useful for your second paper on calibrated reliance.

- [Does AI help humans make better decisions? A statistical evaluation](https://www.pnas.org/doi/10.1073/pnas.2505106122)
  Journal: `PNAS`, 2025
  Design: statistical evaluation framework for AI-assisted decision experiments.
  Use for you: useful as a methodological reference for how to evaluate whether AI actually improves human judgment rather than merely changes it.

- [Superhuman artificial intelligence can improve human decision-making](https://www.pnas.org/doi/10.1073/pnas.2214840120)
  Journal: `PNAS`, 2023
  Design: behavioral / strategic experiments.
  Use for you: important balancing citation so your project does not assume AI is always harmful.

### 2. Bias amplification, feedback loops, and belief distortion

- [How human-AI feedback loops alter human perceptual, emotional and social judgements](https://www.nature.com/articles/s41562-024-02077-2)
  Journal: `Nature Human Behaviour`, 2025
  Design: multiple experiments, n = 1,401.
  Core finding: repeated interaction with AI can make people internalize and amplify AI biases.
  Use for you: very close to your first paper. It supports the idea that AI changes the updating process itself, not just the final answer.

- [Human heuristics for AI-generated language are flawed](https://www.pnas.org/doi/10.1073/pnas.2208839120)
  Journal: `PNAS`, 2023
  Design: experiments on human detection of AI-generated text.
  Core finding: people are poor at detecting AI-generated language and rely on flawed heuristics.
  Use for you: strong support for your “formal completeness misread as evidentiary completeness” argument.

- [The consequences of AI training on human decision-making](https://www.pnas.org/doi/10.1073/pnas.2408731121)
  Journal: `PNAS`, 2024
  Design: behavioral experiments.
  Core finding: when people know their actions will train AI, they change their behavior, and the effect persists after training ends.
  Use for you: useful if you want to move from “using AI” to “being observed / learned by AI.”

- [AI assessment changes human behavior](https://www.pnas.org/doi/10.1073/pnas.2425439122)
  Journal: `PNAS`, 2025
  Design: behavioral experiments.
  Use for you: directly useful for a side branch on AI supervision, AI monitoring, or evaluation-induced behavior change.

### 3. Persuasion, labels, and attitudes to AI

- [On the conversational persuasiveness of GPT-4](https://www.nature.com/articles/s41562-025-02194-6)
  Journal: `Nature Human Behaviour`, 2025
  Design: preregistered persuasion experiments.
  Use for you: important if you expand toward AI persuasion, preference shaping, or personalized influence.

- [Psychological factors underlying attitudes toward AI tools](https://www.nature.com/articles/s41562-023-01734-2)
  Journal: `Nature Human Behaviour`, 2023
  Design: review / theoretical synthesis.
  Use for you: good top-level citation for why attitudes toward AI are not reducible to accuracy alone.

- [AI can help people feel heard, but an AI label diminishes this impact](https://www.pnas.org/doi/10.1073/pnas.2319112121)
  Journal: `PNAS`, 2024
  Design: behavioral experiments.
  Core finding: AI-generated responses can have positive effects, but explicit AI labeling reduces them.
  Use for you: very useful for separating content effects from source-label effects in your own experiments.

- [Thinking about God increases acceptance of artificial intelligence in decision-making](https://www.pnas.org/doi/10.1073/pnas.2218961120)
  Journal: `PNAS`, 2023
  Design: multiple experiments.
  Use for you: useful evidence that acceptance of AI depends on deeper worldviews and mindsets, not only on risk level or measured accuracy.

- [Evidence of a social evaluation penalty for using AI](https://www.pnas.org/doi/10.1073/pnas.2426766122)
  Journal: `PNAS`, 2025
  Design: behavioral experiments.
  Core finding: people who use AI can be socially penalized in others’ evaluations.
  Use for you: opens a new angle on the social reputation cost of AI use.

### 4. Morality, dishonesty, and responsibility

- [Delegation to artificial intelligence can increase dishonest behaviour](https://www.nature.com/articles/s41586-025-09505-x)
  Journal: `Nature`, 2025
  Design: 13 studies with more than 8,000 participants.
  Core finding: delegating tasks to AI can increase dishonest behavior.
  Use for you: must-read for your third paper. It moves the conversation from blame shifting to ex ante moral outsourcing.

- [Bad machines corrupt good morals](https://www.nature.com/articles/s41562-021-01128-2)
  Journal: `Nature Human Behaviour`, 2021
  Design: perspective / agenda-setting piece.
  Use for you: helpful theoretical anchor for the broader claim that AI can reshape moral behavior.

## B. Behavior economics core pool

### 1. JEBO

- [Artificial intelligence, ethics, and intergenerational responsibility](https://ideas.repec.org/a/eee/jeborg/v203y2022icp284-317.html)
  Journal: `JEBO`, 2022
  Design: online experiment with a dictator-game-style setting where present choices train future algorithms.
  Core finding: when participants know their current choices train future algorithms affecting others, prosociality can increase under some conditions.
  Use for you: highly relevant for responsibility and moral externalities of AI training.

- [How do individuals interact with an AI advisor in strategic reasoning? An experimental study in beauty contest](https://ideas.repec.org/a/eee/jeborg/v237y2025ics0167268125002781.html)
  Journal: `JEBO`, 2025
  Design: beauty contest experiment with a ChatGPT advisor.
  Core finding: AI advice changes beliefs, learning, and depth of strategic reasoning.
  Use for you: strong paper for your second line on reliance in uncertain or strategic settings.

- [How scary is the risk of automation? Evidence from a large-scale survey experiment](https://ideas.repec.org/a/eee/jeborg/v235y2025ics0167268125001532.html)
  Journal: `JEBO`, 2025
  Design: large survey experiment with nearly 6,000 participants.
  Use for you: helpful if you want to connect reliance to automation anxiety and perceived labor-market risk.

- [Artificial intelligence adoption and workplace training](https://ideas.repec.org/a/eee/jeborg/v238y2025ics0167268125003257.html)
  Journal: `JEBO`, 2025
  Design: German establishment panel data.
  Core finding: AI adoption is associated with some increase in training, but training benefits tilt toward more skilled workers.
  Use for you: strong external-validity support for a fourth paper on skill investment and longer-run adaptation.

- [Lie against AI: Revealing private information through AI in an economic experiment](https://ideas.repec.org/a/eee/jeborg/v245y2026ics0167268126001332.html)
  Journal: `JEBO`, 2026
  Design: buyer-seller experiment with lie detection and AI information revelation.
  Use for you: relevant at the intersection of information acquisition, overconfidence, and algorithm aversion.

- [Generative AI adoption in human creative tasks: Experimental evidence](https://ideas.repec.org/a/eee/jeborg/v242y2026ics0167268126000028.html)
  Journal: `JEBO`, 2026
  Design: preregistered experiment with 302 students using ChatGPT.
  Core finding: ChatGPT improves creative performance, but effects vary by baseline ability and there is no simple human-AI complementarity story.
  Use for you: very useful for a future paper on cognitive offloading, skill heterogeneity, and creative effort.

### 2. JBEE

- [Sharing responsibility with a machine](https://ideas.repec.org/a/eee/soceco/v80y2019icp25-33.html)
  Journal: `JBEE`, 2019
  Design: modified dictator game.
  Core finding: sharing decisions with a machine did not significantly change responsibility, guilt, or actual choice in that setup.
  Use for you: important counterexample. Responsibility outsourcing does not arise automatically.

- [We and It: An interdisciplinary review of the experimental evidence on how humans interact with machines](https://ideas.repec.org/a/eee/soceco/v99y2022ics2214804322000714.html)
  Journal: `JBEE`, 2022
  Design: interdisciplinary review of 138 experimental studies.
  Use for you: best broad review entry point inside the behavior-econ / experimental-econ neighborhood.

- [Is Society Ready for AI Ethical Decision Making? Lessons from a Study on Autonomous Cars](https://ideas.repec.org/a/eee/soceco/v98y2022ics2214804322000556.html)
  Journal: `JBEE`, 2022
  Design: two experiments in autonomous-car ethics settings.
  Core finding: direct questioning shows AI aversion, but indirect measurement can look different.
  Use for you: highly relevant for your high-risk-trust line and a good warning that measurement format itself changes the answer.

- [When do robo-advisors make us better investors? The impact of social design elements on investor behavior](https://ideas.repec.org/a/eee/soceco/v103y2023ics2214804323000101.html)
  Journal: `JBEE`, 2023
  Design: two induced-value experiments.
  Core finding: robo-advisors can improve investment decisions, and the effect depends on social design elements.
  Use for you: useful for risky decisions, financial contexts, and interface design as a moderator.

- [Do people trust humans more than ChatGPT?](https://ideas.repec.org/a/eee/soceco/v112y2024ics2214804324000776.html)
  Journal: `JBEE`, 2024
  Design: experiment comparing trust in statements from humans versus ChatGPT.
  Use for you: direct trust paper, but best treated as only one layer of the story.

- [Measuring preferences for algorithms - How willing are people to cede control to algorithms?](https://ideas.repec.org/a/eee/soceco/v112y2024ics2214804324001071.html)
  Journal: `JBEE`, 2024
  Design: experimental measurement approach.
  Core finding: proposes a way to quantify willingness to cede control to algorithms.
  Use for you: extremely important if you want to move beyond attitude items to a behavioral measure of control delegation.

- [Would I lie to you? How interaction with chatbots induces dishonesty](https://ideas.repec.org/a/eee/soceco/v112y2024ics2214804324001162.html)
  Journal: `JBEE`, 2024
  Design: random-number private-report experiment.
  Core finding: people are more dishonest with chatbots than with humans; agency cues help in human settings but not with chatbots.
  Use for you: direct support for the idea that social constraints weaken in AI interaction.

- [How gender and prosociality affect machine interaction in tax compliance](https://ideas.repec.org/a/eee/soceco/v116y2025ics2214804325000369.html)
  Journal: `JBEE`, 2025
  Design: tax-compliance game with human or machine auditor.
  Core finding: compliance is lower with machine auditors, especially for some groups.
  Use for you: useful evidence that changing the social nature of the interaction changes moral behavior.

- [Chatbot or humanaut? How the source of advice impacts prosocial behavior](https://ideas.repec.org/a/eee/soceco/v121y2026ics2214804326000017.html)
  Journal: `JBEE`, 2026
  Design: three classic social-preference games.
  Core finding: both human and genAI advice can increase prosocial behavior, but human advice remains more valued and more norm-oriented.
  Use for you: very useful nuance paper for your responsibility / prosociality line.

## C. Adjacent top management / organization journals

### 1. Management Science

- [Incentives, Framing, and Reliance on Algorithmic Advice](https://pubsonline.informs.org/doi/10.1287/mnsc.2022.02777)
  Journal: `Management Science`, 2025
  Design: large-scale experiments with around 1,500 participants.
  Core finding: incentives and framing significantly affect reliance on algorithmic advice; emphasizing that AI also embodies human expertise can increase use.
  Use for you: one of the best papers for your second project.

- [Human-Centered Artificial Intelligence: A Field Experiment](https://pubsonline.informs.org/doi/10.1287/mnsc.2022.03849)
  Journal: `Management Science`, 2025
  Design: field experiment in a multinational pharmaceutical company.
  Core finding: matching AI-supported workflows to workers’ cognitive styles improves performance.
  Use for you: supports the view that interaction design matters as much as algorithm quality.

- [Humans' Use of AI Assistance: The Effect of Loss Aversion on Willingness to Delegate Decisions](https://pubsonline.informs.org/doi/10.1287/mnsc.2024.05585)
  Journal: `Management Science`, 2025
  Design: multiple experiments.
  Core finding: changing task framing can reduce reluctance to delegate to AI.
  Use for you: very important for a risk-asymmetry framing of reliance.

- [Human-Algorithm Collaboration with Private Information: Naive Advice-Weighting Behavior and Mitigation](https://pubsonline.informs.org/doi/10.1287/mnsc.2022.03850)
  Journal: `Management Science`, 2025
  Design: controlled experiments.
  Core finding: people combine their own private information with algorithmic advice too mechanically instead of adjusting weights flexibly.
  Use for you: directly relevant to your first and second papers because it shows why human-in-the-loop does not automatically yield good updating.

- [Algorithm Reliance: Fast and Slow](https://pubsonline.informs.org/doi/10.1287/mnsc.2023.01989)
  Journal: `Management Science`, 2025
  Design: experiments.
  Core finding: reliance on algorithms can be driven by separable fast and slow psychological processes.
  Use for you: good reason not to model reliance with a single trust scale.

- [Till Tech Do Us Part: Betrayal Aversion and Its Role in Algorithm Use](https://pubsonline.informs.org/doi/10.1287/mnsc.2022.03510)
  Journal: `Management Science`, 2025
  Design: experiments.
  Core finding: betrayal aversion is an important mechanism behind resistance to algorithms.
  Use for you: strong theoretical support for why high-risk settings may produce asymmetrical reluctance.

- [My Advisor, Her AI, and Me: Evidence from a Field Experiment on Human-AI Collaboration and Investment Decisions](https://pubsonline.informs.org/doi/10.1287/mnsc.2022.03918)
  Journal: `Management Science`, 2025
  Design: field experiment in financial advising.
  Core finding: keeping humans in the loop can preserve trust and improve adoption, especially in higher-risk investments.
  Use for you: directly relevant to your proposed high-risk / low-risk asymmetry question.

- [When Will Workers Follow an Algorithm? A Field Experiment with a Retail Business](https://pubsonline.informs.org/doi/10.1287/mnsc.2020.3599)
  Journal: `Management Science`, 2020
  Design: retail field experiment.
  Core finding: workers resist algorithmic advice less when their own input is incorporated into the algorithm.
  Use for you: useful for any human-in-the-loop ownership or participation mechanism.

### 2. Organization Science

- [Algorithm-Augmented Work and Domain Experience](https://pubsonline.informs.org/doi/10.1287/orsc.2021.1554)
  Journal: `Organization Science`, 2022
  Design: organizational experiment.
  Core finding: experience has a nonlinear relationship with gains from algorithm augmentation because ability gains and aversion coexist.
  Use for you: very useful if you want heterogeneous treatment effects by expertise.

- [Algorithmic Recommendation Tools and Experiential Learning in Clinical Care](https://pubsonline.informs.org/doi/10.1287/orsc.2022.16738)
  Journal: `Organization Science`, 2025
  Design: panel evidence from clinical care.
  Core finding: algorithmic recommendation tools can weaken experiential learning, especially under lower task difficulty and lower task variety.
  Use for you: one of the strongest neighboring papers for a fourth project on cognitive offloading and skill erosion.

## D. How to use this map for your dissertation

### 1. If paper 1 remains about information search and belief updating

Read first:

- `How human-AI feedback loops alter human perceptual, emotional and social judgements`
- `When combinations of humans and AI are useful`
- `Human heuristics for AI-generated language are flawed`
- `Human-Algorithm Collaboration with Private Information`
- `Incentives, Framing, and Reliance on Algorithmic Advice`

Why:

- these papers justify a process view rather than a static trust view
- they show that updating failures can arise from interaction structure, weighting, and feedback loops

### 2. If paper 2 remains about high-risk trust / reliance asymmetry

Read first:

- `When combinations of humans and AI are useful`
- `Thinking about God increases acceptance of artificial intelligence in decision-making`
- `Is Society Ready for AI Ethical Decision Making?`
- `Measuring preferences for algorithms`
- `Humans' Use of AI Assistance`
- `Till Tech Do Us Part`
- `My Advisor, Her AI, and Me`

Why:

- these papers show that reliance depends on framing, betrayal risk, legitimacy, and delegation preferences

### 3. If paper 3 remains about responsibility and blame

Read first:

- `Delegation to artificial intelligence can increase dishonest behaviour`
- `Bad machines corrupt good morals`
- `Sharing responsibility with a machine`
- `Would I lie to you?`
- `How gender and prosociality affect machine interaction in tax compliance`
- `Chatbot or humanaut?`

Why:

- these papers move the discussion from abstract ethics to measurable behavior
- they also show that responsibility externalization is conditional, not automatic

### 4. If you want a fourth paper on long-run adaptation

Read first:

- `Artificial intelligence adoption and workplace training`
- `Algorithmic Recommendation Tools and Experiential Learning in Clinical Care`
- `Generative AI adoption in human creative tasks`
- `The consequences of AI training on human decision-making`

Why:

- together these papers support a shift from one-shot judgment bias to dynamic human-capital and cognitive-capital questions

## E. My bottom-line diagnosis

The literature frontier has already moved beyond the simple formula:

- `AI = trust problem`

The stronger framing now is:

- `AI changes how humans allocate search, control, responsibility, reputation, and learning`

For your project, that means your most defensible umbrella is not simply “trust in AI,” but something closer to:

- `delegated cognition`
- `delegated control`
- `delegated responsibility`

That is the language that best connects your current ideas to top-tier and behavior-economics literatures.
