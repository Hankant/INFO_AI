# AI与人类交互：20篇核心论文、研究方法、gap、逻辑链路与理论发展进程

日期：2026-06-15

## 一、怎么理解这份清单

这份清单不是“只要带 AI 关键词就都算”，而是围绕你当前研究主轴反推出来的 20 篇核心论文。筛选标准有三个：

1. 期刊层级优先 `Nature Human Behaviour`、`PNAS`、`Nature`、`JEBO`、`JBEE`，并保留最关键的 `Management Science` 和 `Organization Science`。
2. 主题必须与以下至少一条高度相关：
   - AI 与控制权让渡、reliance、algorithm delegation
   - AI 与搜索、更新、判断偏差、反馈回路
   - AI 与责任、道德成本、不诚实、亲社会行为
   - AI 与长期学习、技能保留、组织适应
3. 优先保留实验、现场实验、元分析、系统综述和能推动理论演化的代表性论文。

如果一句话概括，这 20 篇共同描述的是这样一条研究路径：

`从“人信不信AI” -> 到“人把多少控制权交给AI” -> 到“AI如何改变搜索与更新过程” -> 到“AI如何改变责任与道德成本” -> 再到“AI如何重塑长期学习与能力配置”。`

## 二、20篇核心论文矩阵

| 编号 | 论文 | 期刊/年份 | 研究方法 | 主题位置 | 关键发现 | 该文留下的gap | 与你研究的关系 | 在理论链条中的位置 |
|---|---|---|---|---|---|---|---|---|
| 1 | [Sharing responsibility with a machine](https://ideas.repec.org/a/eee/soceco/v80y2019icp25-33.html) | JBEE, 2019 | 改造版 dictator game 实验 | 责任归因 | 与机器共同决策未必显著降低责任感、内疚或实际选择。 | 使用的是较静态的机器情境，不是会解释、会互动的生成式 AI；外部效度有限。 | 是你第三篇的重要反例，提醒你不能预设“AI 一定导致责任外包”。 | 早期基线文献，说明“责任外包”不是自动发生的。 |
| 2 | [Artificial intelligence, ethics, and intergenerational responsibility](https://ideas.repec.org/a/eee/jeborg/v203y2022icp284-317.html) | JEBO, 2022 | 在线行为实验，当前选择会训练未来算法 | 责任与伦理 | 当参与者知道自己的选择会训练未来影响他人的算法时，在某些条件下会更亲社会。 | 研究的是算法训练外部性，不是日常 AI 互动，也未直接研究甩锅或道德外包。 | 对你第三篇有用，因为它把责任问题从事后 blame 推到跨期责任。 | 把责任问题从“当前决策”推进到“训练未来算法”的跨期责任。 |
| 3 | [Is Society Ready for AI Ethical Decision Making? Lessons from a Study on Autonomous Cars](https://ideas.repec.org/a/eee/soceco/v98y2022ics2214804322000556.html) | JBEE, 2022 | 两个伦理场景实验，比较直接与间接测量 | 高风险接受 | 自动驾驶伦理任务中，直接问与间接测量会得到不同的 AI 接受结果。 | 更像伦理态度研究，离生成式 AI 和真实行为还远；机制拆解不够细。 | 对你第二篇有直接价值，尤其是“高风险 AI 不信任”不能只靠显性态度题来测。 | 提醒我们高风险场景中的 AI aversion 本身就受测量方式影响。 |
| 4 | [Algorithm-Augmented Work and Domain Experience](https://pubsonline.informs.org/doi/10.1287/orsc.2021.1554) | Organization Science, 2022 | 组织环境中的实证/实验结合研究 | 异质性与组织适应 | 经验与算法增强的收益呈非线性关系，能力提升与算法厌恶并存。 | 不是生成式 AI 场景；心理机制更多是推断而非直接测量。 | 对你第四篇特别重要，因为它说明 AI 效果存在明显 expertise heterogeneity。 | 早期说明“谁受益、谁抗拒”是一个异质性问题。 |
| 5 | [Psychological factors underlying attitudes toward AI tools](https://www.nature.com/articles/s41562-023-01734-2) | Nature Human Behaviour, 2023 | 高层综述/理论整合 | 总体理论 | 对 AI 工具态度并不只由准确率决定，还受多种心理因素影响。 | 是高层综述，不够机制化，也没把生成式 AI 的特殊性完全展开。 | 可作为你整套研究的开篇总引文，用来说明不要把问题只写成 trust。 | 从单一 trust 视角过渡到多心理机制视角的概念桥梁。 |
| 6 | [Human heuristics for AI-generated language are flawed](https://www.pnas.org/doi/10.1073/pnas.2208839120) | PNAS, 2023 | 多实验，测试人类识别 AI 文本的启发式 | 语言与判断 | 人类难以识别 AI 生成文本，并依赖错误启发式判断其可信度。 | 研究的是文本识别，并未直接连接到搜索停止或更新不足。 | 对你第一篇非常关键，它支撑“形式流畅性被误读为证据充分性”。 | 为“形式流畅性被误读为证据充分性”提供基础。 |
| 7 | [When combinations of humans and AI are useful](https://www.nature.com/articles/s41562-024-02024-1) | Nature Human Behaviour, 2024 | 系统综述 + 元分析，106 个实验、370 个效应量 | 人机协作总评估 | 人机组合平均不稳定优于最佳的人或最佳的 AI，尤其在决策任务中协同收益有限。 | 是元分析，回答了“是否有效”，但对“为什么失效”还不够细。 | 是你第二篇最重要的总背景文献之一，能避免你把 human-in-the-loop 写得过于乐观。 | 奠定“人机协作并非天然最优”的总背景。 |
| 8 | [Measuring preferences for algorithms - How willing are people to cede control to algorithms?](https://ideas.repec.org/a/eee/soceco/v112y2024ics2214804324001071.html) | JBEE, 2024 | 实验 + menu-based 行为测量 | 控制权让渡 | 提出行为化测量 `willingness to cede control` 的方法。 | 主要是测量工具，尚未连接到后续搜索、责任和学习结果。 | 对你第二篇很关键，你可以借它把 trust 转成可行为化的 control delegation。 | 把 trust/aversion 变成可度量的 control delegation。 |
| 9 | [Would I lie to you? How interaction with chatbots induces dishonesty](https://ideas.repec.org/a/eee/soceco/v112y2024ics2214804324001162.html) | JBEE, 2024 | 随机数私报实验 | 不诚实行为 | 人在 chatbot 条件下比在人类条件下更不诚实，agency cue 对 chatbot 无效。 | 任务较简单，未触及生成式 AI 的解释权威或高风险场景。 | 是你第三篇的直接邻近文献，说明 social image constraint 在 AI 互动中会变弱。 | 说明 AI 互动会削弱一部分社会约束。 |
| 10 | [The consequences of AI training on human decision-making](https://www.pnas.org/doi/10.1073/pnas.2408731121) | PNAS, 2024 | 行为实验，操纵“行为是否被用于训练 AI” | 反馈系统 | 当人知道自己的行为会被用于训练 AI 时，会改变自己的行为，且效应持续。 | 更多是“被 AI 学习”的反应性行为，还未分解其认知机制。 | 对你第一篇和第四篇都很有用，因为它把 AI 影响扩展到长期反馈和制度反应。 | 把文献从“用 AI”推进到“与 AI 共同构成反馈系统”。 |
| 11 | [Incentives, Framing, and Reliance on Algorithmic Advice](https://pubsonline.informs.org/doi/10.1287/mnsc.2022.02777) | Management Science, 2025 | 大样本控制实验，操纵激励与 framing | reliance 校准 | 激励合同和 framing 会显著影响人们对算法建议的依赖。 | 更关注采纳率，尚未进入证据搜索和信念更新的内部过程。 | 对你第二篇特别关键，因为它告诉你 reliance 不能脱离激励结构来谈。 | 把 reliance 明确嵌入行为经济学的激励与框架效应。 |
| 12 | [Humans' Use of AI Assistance: The Effect of Loss Aversion on Willingness to Delegate Decisions](https://pubsonline.informs.org/doi/10.1287/mnsc.2024.05585) | Management Science, 2025 | 多实验，操纵收益/损失框架 | 风险不对称 | loss aversion 会系统性影响是否愿意把决定委托给 AI。 | 聚焦单一机制，对生成式 AI 的解释性特征触及不多。 | 是你第二篇“高风险不愿让渡控制权”的核心机制文献。 | 为“高风险不愿让渡控制权”提供行为机制。 |
| 13 | [Human-Algorithm Collaboration with Private Information: Naive Advice-Weighting Behavior and Mitigation](https://pubsonline.informs.org/doi/10.1287/mnsc.2022.03850) | Management Science, 2025 | 控制实验，观察 private information 与 algorithm advice 的整合 | 信息整合 | 人在整合自身 private information 与算法建议时，经常机械加权，而非灵活调整。 | 控制环境较强，离自然生成式 AI 交互还有距离。 | 对你第一篇极其重要，因为它正好说明“看到信息”不等于“正确赋权”。 | 解释了为什么 human-in-the-loop 未必能带来规范性改进。 |
| 14 | [How human-AI feedback loops alter human perceptual, emotional and social judgements](https://www.nature.com/articles/s41562-024-02077-2) | Nature Human Behaviour, 2025 | 多实验，n=1,401，研究重复互动后的偏差内化 | 偏差放大 | 与 AI 反复互动会让人内化并放大 AI 偏差。 | 证明了反馈放大，但没有严格拆成“少搜”与“少更”两类偏差。 | 是你第一篇最接近的顶刊文献，能帮助你强调 process distortion 而非单次采纳。 | 把研究推进到动态反馈回路阶段。 |
| 15 | [Delegation to artificial intelligence can increase dishonest behaviour](https://www.nature.com/articles/s41586-025-09505-x) | Nature, 2025 | 13 个研究、8000+ 被试的多实验设计 | 道德外包 | 将任务委托给 AI 会提高不诚实行为。 | 识别效应很强，但边界条件、不同 AI 形态差异仍需继续展开。 | 这是你第三篇必须正面回应的核心文献，因为它已把问题推进到 ex ante moral outsourcing。 | 把文献从 blame shifting 推到 ex ante unethical delegation。 |
| 16 | [How gender and prosociality affect machine interaction in tax compliance](https://ideas.repec.org/a/eee/soceco/v116y2025ics2214804325000369.html) | JBEE, 2025 | 税收遵从博弈实验，比较人类审计员与机器审计员 | 社会约束异质性 | 面对机器审计员时，合规性下降，且性别与亲社会性存在异质影响。 | 语境较窄，尚未完全分离 deterrence、mind perception 与 social distance。 | 对你第三篇有帮助，因为它说明 AI 道德效应具有明显异质性。 | 说明 moral distance 的效应是异质性的，不是一刀切。 |
| 17 | [How do individuals interact with an AI advisor in strategic reasoning? An experimental study in beauty contest](https://ideas.repec.org/a/eee/jeborg/v237y2025ics0167268125002781.html) | JEBO, 2025 | beauty contest 实验，引入 ChatGPT advisor | 战略推理 | AI advisor 会影响 beliefs、learning 与 backward induction 深度。 | 战略实验较干净，但离真实高风险生成式 AI 场景仍有距离。 | 对你第二篇有用，因为它把 reliance 问题拓展到 strategic reasoning。 | 把 AI 依赖问题从普通判断扩展到战略互动。 |
| 18 | [My Advisor, Her AI, and Me: Evidence from a Field Experiment on Human-AI Collaboration and Investment Decisions](https://pubsonline.informs.org/doi/10.1287/mnsc.2022.03918) | Management Science, 2025 | 金融顾问场景现场实验 | 高风险现场证据 | 在金融顾问场景中，保留 human-in-the-loop 能提升 trust、采纳与福利，尤其在高风险投资中。 | 主要是金融场景，能否外推到医疗、法律、公共决策仍待检验。 | 对你第二篇非常贴合，因为它直接对应“高风险依赖谁、为什么”的问题。 | 是“高风险 reliance 与流程设计”最重要的现场证据之一。 |
| 19 | [Algorithmic Recommendation Tools and Experiential Learning in Clinical Care](https://pubsonline.informs.org/doi/10.1287/orsc.2022.16738) | Organization Science, 2025 | 医疗组织面板研究 | 长期学习 | 算法推荐工具会削弱 experiential learning，尤其在低难度低多样性任务中。 | 主要是组织面板证据，个体层面的认知卸载机制仍需实验补强。 | 对你第四篇极其重要，因为它已经把 AI 使用与 learning cost 连起来了。 | 把文献从一次判断推进到长期学习代价。 |
| 20 | [Artificial intelligence adoption and workplace training](https://ideas.repec.org/a/eee/jeborg/v238y2025ics0167268125003257.html) | JEBO, 2025 | 企业面板数据研究 | 人力资本配置 | AI adoption 会改变培训投入与机会分配，且更偏向高技能者。 | 更多是组织层面证据，难以直接识别个体心理机制。 | 对你第四篇有用，因为它把认知卸载问题接到了 training incentives 和 skill inequality。 | 把 AI-human interaction 接到技能投资与不平等问题上。 |

## 三、20篇论文的研究方法详解

### 1. Sharing responsibility with a machine

这篇文章的方法核心是一个改造过的 dictator game。研究者把“分配决策”设置成几种不同条件，例如由参与者独自决定、由机器给出建议后参与者决定，或者由人机共同形成结果，再比较参与者在不同条件下的责任感、内疚感和最终分配行为是否变化。它的方法优势在于识别逻辑很干净，因为通过随机分组把“是否与机器共同决策”单独抽出来；但弱点也很明显：机器在这里更像一个静态决策对象，而不是今天这种会对话、会解释、会形成权威感的生成式 AI，所以它能识别“机器参与”本身，却不太能识别“解释型 AI”带来的责任转移。

### 2. Artificial intelligence, ethics, and intergenerational responsibility

这篇文章采用的是在线行为实验设计，但它最特别的地方在于把“当前决策会训练未来算法”这一层加入了实验结构。参与者并不是只面对一次性的伦理分配，而是被告知他们现在的选择会影响后续算法如何对待别人，因此研究者可以观察：一旦人意识到自己不只是做一个即时决定，而是在塑造未来机器行为时，是否会表现得更亲社会。方法上，它把 AI 训练外部性内生进了实验任务，这是很强的设计；不足之处是场景仍较抽象，离真实生成式 AI 的日常使用情境较远。

### 3. Is Society Ready for AI Ethical Decision Making? Lessons from a Study on Autonomous Cars

这篇文章的方法重点不在复杂操纵，而在测量设计。作者围绕自动驾驶伦理判断设置了两个实验，一方面直接询问受试者是否愿意让 AI 作出道德决策，另一方面通过更间接的方式观察其偏好，从而比较显性态度和隐含偏好是否一致。这个方法很重要，因为它说明“AI aversion”可能部分是一个测量产物：同一个人，在直接表态时会说自己不信任 AI，但在更间接的任务里未必表现出同样程度的拒绝。方法上的强项是把显性与隐性测量分开，弱点是场景仍偏伦理判断题，不够接近真实交互。

### 4. Algorithm-Augmented Work and Domain Experience

这篇文章采用的是组织场景中的算法增强工作研究方法，核心是比较不同经验水平的工作者在引入算法工具后的表现变化。它不是单纯看平均效应，而是把 domain experience 作为关键异质性变量，去识别“经验高的人是否更能用好算法”“经验低的人是否更依赖算法”“中等经验者是否最容易出现矛盾反应”。方法上的价值在于，它把 AI 研究从标准在线实验推进到了真实工作环境中的异质性识别；但局限在于，很多心理机制仍然是通过绩效差异来反推，而非在实验中直接测量信任、控制感或认知负荷。

### 5. Psychological factors underlying attitudes toward AI tools

这篇并不是单一实验，而是高层次的理论整合与文献综述。它的方法不是通过一个新实验识别单一效应，而是系统梳理不同研究中影响 AI 态度的心理因素，例如能力感知、威胁感、控制感、公平感、身份威胁等，再把分散证据组织成一个可供后续研究使用的分析框架。它的优势是能在概念层面清楚告诉我们，为什么“准确率越高越信任”这种线性直觉不够；弱点则是不能直接解决识别问题，也很难告诉你生成式 AI 在机制上和传统算法究竟差了多少。

### 6. Human heuristics for AI-generated language are flawed

这篇文章采用的是多实验文本判断设计。参与者会读到不同来源的文本，再判断文本是否出自 AI、是否可信、为什么这样判断。研究者由此提取出人类在识别 AI 文本时依赖的启发式规则，例如是否更流畅、是否更正式、是否更像模板化表达，并进一步检验这些启发式到底准不准。方法上的强项是它非常适合研究“语言形式线索如何误导判断”；局限则在于，它识别的是文本判断过程，而不是更复杂的决策链条，因此还没有直接进入搜索停止、信息加权或更新不足这些更深层的行为后果。

### 7. When combinations of humans and AI are useful

这篇文章的方法是系统综述与元分析，而不是原始实验。作者把大量人机协作研究按任务类型、协作结构、绩效比较对象等维度编码，然后在统一效应量框架下比较：人机组合相对人类单独、AI 单独以及最佳单方的表现究竟如何。这个方法的价值在于，它能把原本看起来互相矛盾的单篇研究整合成更稳定的总体结论，特别适合回答“human-AI collaboration 是否普遍有效”这种总问题。它的限制也很清楚：元分析能告诉你平均规律，但对机制解释和场景细节的把握，始终不如专门设计的单项实验。

### 8. Measuring preferences for algorithms - How willing are people to cede control to algorithms?

这篇文章的方法创新主要在测量工具上。作者不是简单问“你信不信算法”，而是设计出一套更行为化的测量方式，让参与者在不同控制权配置、不同收益结构和不同决策主体之间做选择，由此推导出其 `willingness to cede control`。这种方法非常适合行为经济学，因为它把抽象态度转成了可比较、可量化的选择行为。它的优点是操作化非常清楚，能够为后续实验提供统一测量框架；但局限在于，它更像一个测量平台，本身并不解释这些控制权偏好为何形成，也还没和搜索、责任或长期学习结果真正打通。

### 9. Would I lie to you? How interaction with chatbots induces dishonesty

这篇文章使用的是典型的不诚实测量实验，通常是私报随机结果或类似信息不对称任务，然后把互动对象设置为人类或 chatbot，并进一步加入 agency cue 等条件。研究者比较不同互动对象下，参与者是否更愿意夸大、隐瞒或误报结果。这个方法的强项在于，对 dishonesty 的度量很成熟，识别也相对直接；而且因为随机分配互动对象，能较干净地检验“机器对社会约束的削弱作用”。不足在于任务仍较简化，更像基础道德行为实验，对生成式 AI 的解释能力、角色定位和高风险情境涉及较少。

### 10. The consequences of AI training on human decision-making

这篇文章的方法核心是操纵一个很新的变量：参与者是否知道自己的选择会被拿去训练 AI。研究者并不只是比较“有 AI vs 无 AI”，而是让个体在一个行为实验里意识到自己正处在 AI 训练流程中，从而观察他们的行为是否因此变化，以及这种变化在后续回合或后续任务中是否持续。这个设计很有方法创新性，因为它把 AI 的存在从“使用工具”扩展成“被工具学习”的制度环境。局限在于，这类设计更容易识别反应性行为，却不一定能细致拆开究竟是 reputational concern、战略适应，还是认知框架变化在起作用。

### 11. Incentives, Framing, and Reliance on Algorithmic Advice

这篇文章的方法是大样本控制实验，重点操纵两个变量：激励结构和 advice 的 framing。参与者在面对算法建议时，所处的报酬规则、竞争环境和建议呈现方式会被系统改变，研究者据此比较他们对算法建议的采纳率、依赖程度以及最终决策表现。方法上的强项在于，它把 reliance 放进了行为经济学最擅长的激励框架里来识别，而不是只当成心理态度；不足则在于，它更侧重最终采纳行为，对个体在采纳前是否验证、采纳后如何整合证据，触及得还不够深。

### 12. Humans' Use of AI Assistance: The Effect of Loss Aversion on Willingness to Delegate Decisions

这篇文章采用多实验设计，通过在收益框架和损失框架之间切换，识别 loss aversion 是否会影响人们把决策交给 AI 的意愿。换句话说，它并不是简单比较“AI 条件和非 AI 条件”，而是研究同一个决策任务在 gain frame 和 loss frame 下，delegation 的心理门槛如何变化。这个方法的优点是非常适合识别风险不对称背后的行为机制，也能很好地和 prospect theory 对话；不足在于它把焦点放在一个机制上，因此对生成式 AI 特有的叙事性、解释性和来源权威感覆盖得不够。

### 13. Human-Algorithm Collaboration with Private Information: Naive Advice-Weighting Behavior and Mitigation

这篇文章的方法是很经典也很强的控制实验：让参与者同时拥有自己的 private information，并收到算法建议，然后观察他们到底如何整合两类信息。研究者通常可以明确知道 private signal 的质量和算法建议的质量，因此能够把参与者的实际加权方式与规范性加权基准直接比较，再测试一些 mitigation 处理是否能让他们更合理地整合两种来源。这个方法对识别“看到了信息但没有给够权重”特别有效。它的局限是环境仍偏理想化，离自然生成式 AI 会话中的复杂证据整合还有一定距离。

### 14. How human-AI feedback loops alter human perceptual, emotional and social judgements

这篇文章的方法前沿性很强，因为它研究的是 repeated interaction 而不是单次判断。研究者让参与者在多个回合中不断接触 AI 的判断，再作出自己的判断，比较偏差是否会在反复互动中被内化、放大和反馈回去。它的优势在于能识别动态 feedback loop，而不是只测 advice uptake；而且因为任务跨感知、情绪和社会判断多个领域，结果的外延也更广。局限在于，虽然它抓住了“偏差放大”，但并没有进一步拆解这个过程究竟是因为更早停止搜索、对反方证据赋权不足，还是两者同时发生。

### 15. Delegation to artificial intelligence can increase dishonest behaviour

这篇文章的方法非常强，采用的是 13 个研究组成的多实验证据链。它不是只用一个任务来证明 AI 会提高不诚实，而是通过多个场景、不同操纵方式和不同被试群体，系统比较“自己做”与“委托 AI 做”时不诚实行为是否变化。方法上的强项是外部效度和稳健性都较强，因为单一任务特异性不太可能解释全部结果；同时它也把 delegation 而不是单纯使用 AI 作为核心识别变量。局限则在于，虽然效应识别很强，但不同 AI 形态、不同任务道德性质、不同责任结构下的边界条件仍值得继续细化。

### 16. How gender and prosociality affect machine interaction in tax compliance

这篇文章采用税收遵从博弈实验，把审计者设定为人类或机器，再观察纳税申报行为如何变化，并进一步考察性别和亲社会性差异。方法上的价值在于，它把 AI 互动放进了一个既有经典行为经济学传统、又天然带有道德张力的场景里，因此可以同时测合规、风险和社会约束。它的强项是能识别异质性，不是只给出平均效应；不足在于，这类任务更多表现的是“面对机器的社会距离变化”，仍然没有完全进入生成式 AI 那种会解释、会对话、会显得有判断能力的复杂互动。

### 17. How do individuals interact with an AI advisor in strategic reasoning? An experimental study in beauty contest

这篇文章的方法是在 beauty contest 这种经典战略推理实验中引入 ChatGPT advisor。参与者不只是收到一个数字建议，而是在战略环境中面对一个可能影响其 beliefs 和 learning 的 AI 顾问，因此研究者可以观察 AI 是否改变了参与者的层级推理深度、对他人行为的预期，以及随回合推进的学习轨迹。这个方法的长处在于，它把 AI reliance 从简单判断扩展到了 strategic reasoning，这是很有行为经济学味道的推进；局限是 beauty contest 依然是高度抽象环境，对真实高风险生成式 AI 场景的外推需要谨慎。

### 18. My Advisor, Her AI, and Me: Evidence from a Field Experiment on Human-AI Collaboration and Investment Decisions

这篇文章的方法是现场实验，这也是它最有价值的地方。研究者在真实金融顾问与投资决策场景中比较不同的人机协作安排，例如是否保留 human-in-the-loop、AI 在流程中的位置如何、客户面对的是纯人类建议还是人机结合建议，然后观察采纳、信任和福利后果。现场实验的好处是生态效度很高，尤其适合检验高风险决策中的真实反应；缺点则是机制识别通常不如实验室那么干净，而且金融场景中的信任结构未必能直接复制到医疗、法律或公共治理中。

### 19. Algorithmic Recommendation Tools and Experiential Learning in Clinical Care

这篇文章主要使用临床照护场景中的组织/面板数据方法，比较算法推荐工具引入前后，医生或相关决策者的 experiential learning 轨迹是否发生变化。换句话说，它不是直接测“这次判断准不准”，而是观察长期经验积累是否因为工具介入而被削弱。这个方法的优势是能抓住长期后果，并且场景本身高度真实；不足是组织数据的识别依赖较多模型设定与控制变量，难以像随机实验那样直接观测个体的认知卸载过程。因此它非常适合提出问题，但还需要实验方法进一步补足机制。

### 20. Artificial intelligence adoption and workplace training

这篇文章的方法主要是企业层面的面板数据研究，通过追踪 AI adoption 与培训投入、培训对象、技能结构变化之间的关系，来识别 AI 是否改变了人力资本配置。它的方法强项在于能把问题放进更宏观、更真实的组织决策环境中，因此对外部效度很有帮助；但局限也很明确：这种设计能观察 adoption 与 training 的关联，却不容易直接识别个体层面的心理机制，例如人是不是因为认知卸载而减少学习，还是因为组织重新分配培训资源才出现差异。因此它更像长期趋势证据，而不是机制识别的终点。

## 四、这些论文的共同 logic chain 是什么

如果把这 20 篇不是当成零散论文，而是当成一条理论发展链条来看，它们大致组成了下面这条 `logic chain`：

### 第一步：从“信不信 AI”出发

早期与中期文献首先回答的是最基础的问题：人是不是愿意接受机器的判断。这里的关键词是 `AI attitudes`、`algorithm aversion`、`acceptance` 和 `trust`。代表论文如 `Psychological factors underlying attitudes toward AI tools`、`Is Society Ready for AI Ethical Decision Making?`。这一步告诉我们，AI 接受度本身就不是稳定的，而是受风险、测量方式、心理框架和社会语境影响。

### 第二步：从信任转向“让不让控制权”

接下来，文献开始意识到，仅讨论信任过于粗糙。真正重要的是，人愿不愿意把决策权交出去，以及交出去多少。这时研究重心从 attitude 走向 `ceding control`、`delegation`、`override`、`reliance under framing and incentives`。代表论文包括 `Measuring preferences for algorithms`、`Incentives, Framing, and Reliance on Algorithmic Advice`、`Humans' Use of AI Assistance`。这一步的理论升级在于：AI 不再只是一个被评价的对象，而成为一个可能接管部分认知控制权的代理。

### 第三步：从最终采纳转向过程性失真

再往前，研究不再满足于问“最后听没听 AI 的”，而开始问“AI 如何改变搜索、加权、更新和反馈回路”。代表论文包括 `Human heuristics for AI-generated language are flawed`、`Human-Algorithm Collaboration with Private Information`、`How human-AI feedback loops alter...`。这一阶段的关键变化是，AI 被理解为一个会重写判断过程的交互系统，而不只是一个单次 advice provider。

### 第四步：从认知后果延伸到道德与责任后果

一旦 AI 被看作可以承接判断与行动的代理，行为经济学自然会继续追问：那人会不会把不舒服的决定也交给它？这就进入 `dishonesty`、`moral distance`、`strategic delegation`、`responsibility attribution`。代表论文是 `Would I lie to you?` 和 `Delegation to artificial intelligence can increase dishonest behaviour`。这一步最重要的理论推进是：AI 不仅影响认知准确性，还可能重新定价道德成本。

### 第五步：从单次行为走向长期能力配置

最后，最新一波研究开始追问 AI 的长期后果：它会不会改变学习、经验积累、培训投入和技能保留。代表论文如 `Algorithmic Recommendation Tools and Experiential Learning in Clinical Care`、`Artificial intelligence adoption and workplace training`。这一步把文献从短期行为偏差，推进到了 `human capital` 与 `organizational adaptation`。

如果一句话概括整条逻辑链，那就是：

`AI研究正在从“是否接受机器建议”走向“人类是否正在把原本属于自己的认知、控制、责任与学习工作重新分配给机器”。`

## 五、理论的发展进程：2019-2025 大致经历了四个阶段

### 阶段一：2019-2022
**主题：从机器接受到责任与伦理的基础问题**

这一阶段的研究还没有完全进入生成式 AI 时代，更多是在讨论“机器参与决策之后，责任感、伦理接受度和人与机器的差异会不会变化”。代表论文是 `Sharing responsibility with a machine`、`Artificial intelligence, ethics, and intergenerational responsibility`、`Is Society Ready for AI Ethical Decision Making?`。

这一阶段的理论特征是：

- AI 主要被当作“非人格化工具”而非解释性代理。
- 研究重点是接受度、责任归因、伦理直觉。
- 结果变量多为态度或简单行为。

这一阶段留下的核心 gap 是：

- 没有真正处理生成式 AI 的解释能力和语言能力。
- 没有把责任、控制权和搜索更新放到同一个框架里。
- 很少研究动态反馈与长期后果。

### 阶段二：2023-2024
**主题：从 trust/aversion 转向生成式 AI 的线索与控制权问题**

这一阶段开始显著受生成式 AI 扩散影响。研究不再只问“机器建议准不准”，而开始问：人如何识别 AI 文本、如何对 AI 标签反应、是否愿意把控制权让给 AI。代表论文包括 `Human heuristics for AI-generated language are flawed`、`Psychological factors underlying attitudes toward AI tools`、`Measuring preferences for algorithms`、`When combinations of humans and AI are useful`。

这一阶段的理论推进是：

- AI 从工具变成带有来源线索和语言线索的交互对象。
- `trust` 被逐渐拆解成 delegation、control、framing、label effects。
- 文献开始意识到 human-AI collaboration 不是天然互补。

这一阶段的核心 gap 是：

- 仍偏重静态接受和单轮判断。
- 对搜索、更新和道德后果的系统拆解还不充分。
- 对长期学习和能力变化几乎还没有成体系的解释。

### 阶段三：2024-2025
**主题：从单轮采纳到反馈回路、行为改变与道德外包**

这一阶段是目前最重要的转折点。顶刊和高水平期刊开始集中研究 AI 如何改变判断过程，而不是只改变最终选择。代表论文包括 `The consequences of AI training on human decision-making`、`How human-AI feedback loops alter...`、`Human-Algorithm Collaboration with Private Information`、`Delegation to artificial intelligence can increase dishonest behaviour`。

这一阶段的理论特征是：

- AI 被明确理解为一个反馈系统，而不是单次建议者。
- 人机交互被放进激励、风险、反馈和社会约束中来理解。
- 道德外包、不诚实和责任转移开始成为核心议题。

这一阶段的核心 gap 是：

- 仍然缺少一个统一框架，把 control、search、updating、responsibility 串起来。
- 大量研究只解释单个 outcome，还没有做机制整合。
- 长期能力和人力资本问题刚刚起步。

### 阶段四：2025 以后
**主题：从短期行为后果走向长期学习与能力配置**

随着组织与现场证据出现，研究进一步开始从“AI 会不会让你这次选错”转向“AI 会不会让你以后不再自己学”。代表论文是 `Algorithmic Recommendation Tools and Experiential Learning in Clinical Care`、`Artificial intelligence adoption and workplace training`，以及可补充参考的创意任务和技能卸载文献。

这一阶段的理论推进是：

- AI 与 human capital、experiential learning、training incentives 建立了直接联系。
- 行为后果被放到更长时间尺度上理解。
- AI 的分配效应和能力极化效应开始进入视野。

这一阶段仍然缺的，是：

- 个体层面的重复实验，对“认知卸载 -> 技能退化/技能重配”做更干净识别。
- 把长期学习和短期 reliance 放进同一个统一模型中。
- 把生成式 AI 的解释型、会话型特征正式纳入能力变化理论。

## 六、研究方法的发展进程与方法 gap

如果从方法上看，这批文献也经历了一个很清楚的演进过程。

### 1. 早期方法：态度测量与小型实验

2019-2022 年的很多研究，主要依赖小规模实验、伦理判断任务、改造版博弈实验或 attitude-style 设计。优点是机制识别较干净，缺点是外部效度偏弱，而且机器常被设定为比较静态、低互动的对象。

### 2. 中期方法：行为化 delegation 测量与多实验设计

到了 2023-2024 年，研究开始从单纯态度题走向更行为化的 delegation 与 reliance 测量。典型方法包括：

- menu-based control delegation measurement
- 多实验并行复现
- AI label / framing manipulation
- 比较 human source 与 AI source 的文本实验

这一阶段的方法进步在于，研究不再只问“你怎么看 AI”，而开始问“你愿不愿意把决定真的交给 AI”。

### 3. 当前前沿方法：反馈回路、现场实验、组织面板与元分析

2024-2025 的前沿研究显著更丰富：

- 元分析：例如 `When combinations of humans and AI are useful`
- 多实验、大样本：例如 `Delegation to artificial intelligence can increase dishonest behaviour`
- 现场实验：例如 `My Advisor, Her AI, and Me`
- 组织/临床面板：例如 `Algorithmic Recommendation Tools and Experiential Learning in Clinical Care`
- 动态反馈实验：例如 `How human-AI feedback loops alter...`

这说明方法上的前沿已经不再满足于单轮实验，而是开始追求：

- 更强的外部效度
- 更动态的 interaction process
- 更长期的行为后果
- 更接近真实制度环境的识别

### 4. 当前方法上的四个主要空缺

#### 方法 gap 1：缺少把“少搜”和“少更”拆开的实验设计

现有文献已经证明 AI 会影响判断，但很少有研究能严格区分：

- 是在搜索阶段提前停了，
- 还是在更新阶段权重给少了，
- 还是二者同时发生。

这恰好是你第一篇最有方法贡献的地方，因为你已经在往 sequential sampling + updating decomposition 这个方向走。

#### 方法 gap 2：缺少生成式 AI 的解释型输出与标准算法 advice 的正面对照

很多 algorithm advice 文献研究的是数字预测、规则建议或静态 recommendation，而不是会说话、会解释、会制造“证据已经处理过”印象的生成式 AI。未来最需要的方法设计，是把：

- 传统 advice
- 生成式 AI answer-first
- human expert answer-first
- source/evidence-first

这些条件放进一个统一框架中比较。

#### 方法 gap 3：缺少长期重复任务实验

学习、技能保留和认知卸载这一支，现在主要依赖组织面板和邻近证据。真正缺的是 repeated-task behavior experiments，例如：

- 前几轮允许用 AI，后几轮禁止用 AI
- 比较 direct answer、scaffold、question prompting 三种 AI 介入方式
- 测长期表现而不仅是当轮表现

这正对应你未来第四篇。

#### 方法 gap 4：缺少将责任外包与认知委托放在同一实验里的设计

现有研究常常把 honesty、blame 和 reliance 分开测。真正有前沿价值的方法，是在一个实验里同时测：

- 愿不愿意把判断交给 AI
- 交给 AI 后是否减少监控和验证
- 结果不佳时如何归责
- 是否因此更敢做道德风险更高的行为

这会把你的第二篇和第三篇更紧地连在一起。

## 七、现有文献最大的五个总 gap

结合这 20 篇论文，可以把当前文献最大的总 gap 概括成五条：

### 1. 缺少统一框架

现有研究常常分开讨论 trust、reliance、dishonesty、learning，但很少用一个统一的行为经济学框架解释：AI 其实是在重写人类对 `搜索、控制、责任、学习` 的分配。

### 2. 对生成式 AI 的“解释性权威”还不够重视

很多研究仍以传统 algorithm advice 为原型，但生成式 AI 的关键差异并不只是更准，而是它会用自然语言给出完整叙事，让人误以为“它已经看过、想过、整合过”。这一块还没有被充分理论化。

### 3. 缺少对信息获取与信息处理的分阶段拆解

当前文献已经看到 AI 会放大偏差、改变判断，但仍少有研究像信息经济学那样清楚区分：

- AI 是让人 `少搜` 了？
- 还是让人 `少更` 了？
- 还是两者同时发生？

这正是非常值得进入的 gap。

### 4. 道德与责任研究仍偏碎片化

已有研究说明 AI 可能让人更不诚实、也可能不自动导致责任转移，但还缺少一个能同时解释 `事前外包、事中道德约束减弱、事后责任归因变化` 的连贯框架。

### 5. 长期学习与技能投资这一支还在早期

组织和现场证据已经提示 AI 可能削弱 experiential learning、改变培训结构，但实验行为经济学还没有形成足够成熟的 `cognitive offloading -> skill investment` 研究传统。

## 八、对你最有用的结论

如果把这 20 篇论文用在你的研究上，最重要的不是记住每一篇讲了什么，而是看到一个更大的转向：

早期文献把问题写成：

`人是否信任AI？`

而前沿文献越来越把问题写成：

`AI是否正在让人把本来属于自己的认知、控制、道德与学习工作委托出去？`

这也是为什么你的项目最适合放在下面这个总框架中：

- `delegated cognition`
- `delegated control`
- `delegated responsibility`

在这个框架下，你当前和未来的研究最容易形成系统性贡献：

- 第一篇进入：AI 如何改变证据搜索与信念更新
- 你的方法优势：可以用 sequential sampling + updating decomposition 补上“少搜 / 少更”的识别空缺

- 第二篇进入：AI 如何改变风险下的 reliance 与控制权让渡
- 你的方法优势：可以把高风险/低风险、final override 权、verification requirement 放进统一实验设计

- 第三篇进入：AI 如何改变责任、道德成本与不诚实行为
- 你的方法优势：可以把 delegation、monitoring、blame attribution 和 dishonesty 放到同一个实验链条里

- 第四篇可扩：AI 如何改变长期学习、技能投资与认知卸载
- 你的方法优势：可以设计 repeated-task experiment，直接补长期能力变化的实验缺口

如果只保留一句最重要的话，那就是：

**这条文献的发展进程说明，AI-human interaction 研究正在从“是否听AI的话”，走向“人类是否正在重新分配原本属于自己的判断工作”。**
