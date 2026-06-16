# AI与行为经济学顶刊综述框架

日期：2026-06-15

## 一、总引言：为什么 AI-human interaction 不应只被理解为“信任问题”

过去关于算法与人类判断的经典研究，往往以 `algorithm aversion`、`algorithm appreciation`、`automation bias` 和 `trust in AI` 为中心。这一传统当然重要，因为它回答了一个基础问题：当机器给出建议时，人到底愿不愿意接受。然而，从生成式 AI 扩散之后，顶刊与行为经济学期刊的研究前沿已经明显往前走了一步。现在更重要的问题，不再只是“人信不信 AI”，而是“AI 介入之后，人如何重新分配原本属于自己的搜索、判断、控制、责任与学习工作”。

这一变化来自生成式 AI 与传统算法的根本差异。传统算法多半提供预测、打分、排序或推荐，用户面对的仍然是若干离散的信息入口；生成式 AI 则常常直接给出一个已经综合、解释、压缩过的不确定性判断。换句话说，它不是单纯减少信息获取成本，而是提前替用户完成了一部分认知劳动：筛选证据、组织冲突、建构叙事、压缩模糊性，并在许多场景中暗示“主要证据已经看过了”。因此，AI 的行为后果不仅体现在答案采纳上，更体现在人类如何调整自己的行为规则。

从这个角度看，AI-human interaction 在行为经济学里至少触及四个层面。第一，AI 会不会改变人们把多少控制权让渡给机器，以及这种让渡是否被风险、激励和框架效应系统性扭曲。第二，AI 会不会改变人们的证据搜索、信息权重和信念更新，从而不仅改变结论，还改变形成结论的过程。第三，AI 会不会改变责任、道德成本与社会约束，使人更容易不诚实、甩锅或把“不舒服的决定”外包出去。第四，AI 会不会在更长时间尺度上改变人的学习、技能积累与独立判断能力。

因此，如果只把这条文献写成“信任 AI 的研究综述”，会显得过窄，也会错过当前顶刊最关心的问题。更合适的综述写法是：AI 并不只是一个需要被人类信任或拒绝的建议来源，它还是一个会重写人类认知分工与行为激励结构的交互对象。下面的综述将围绕四条主线展开：`Reliance and Ceding Control`、`Bias Amplification, Search, and Belief Distortion`、`Responsibility, Dishonesty, and Moral Distance`、`Learning, Skill Retention, and Long-run Adaptation`。

## 二、Reliance and Ceding Control：AI如何改变控制权让渡

### 1. 这条文献线的核心问题

这一支文献研究的不是 AI 准不准本身，而是：当 AI 进入决策流程之后，人愿意把多少控制权交给它，什么情况下会依赖它，什么情况下会抗拒它，以及这种 reliance 到底是不是被“校准”了。行为经济学真正关心的不是抽象态度，而是 `willingness to cede control`、override behavior、delegation under risk 和 reliance under incentives。

### 2. 顶刊和行为经济学期刊已经回答了什么

目前最重要的高层结论来自 Vaccaro et al. 在 `Nature Human Behaviour` 2024 的元分析《When combinations of humans and AI are useful》。这篇研究表明，人机组合平均并不稳定优于最佳的人或最佳的 AI，尤其在“决策类任务”中，人机协作经常拿不到理论上应有的互补收益。这个结论很重要，因为它直接否定了“加上 human-in-the-loop 就会自然更好”的朴素想法。

与之对应，行为经济学与管理学期刊进一步解释了 reliance 为什么常常失准。`Management Science` 2025 的《Incentives, Framing, and Reliance on Algorithmic Advice》显示，激励合同和叙述框架可以显著改变对算法建议的依赖程度；同一算法，在不同激励与 framing 下，采纳率可以明显变化。`Management Science` 2025 的《Humans' Use of AI Assistance: The Effect of Loss Aversion on Willingness to Delegate Decisions》则把 loss aversion 带进来，说明人们之所以抗拒 AI，并不只是因为不信任其能力，也可能是因为更害怕“把决定交给机器之后出错”。

在更贴近行为经济学的期刊里，`JBEE` 2024 的《Measuring preferences for algorithms》尤其关键，因为它把“算法厌恶”从态度层面的表达，推进成了可行为化测量的“愿意让渡多少控制权”。`JEBO` 2025 的 beauty contest 研究《How do individuals interact with an AI advisor in strategic reasoning?》进一步说明，AI 不只是提供一个静态建议，它会进入个体的 beliefs、learning 和 higher-order reasoning 过程。也就是说，reliance 的问题在战略互动里会变得更复杂：人可能不是简单采纳 AI，而是在猜“其他人会不会也采纳 AI”。

高风险场景中的 trust asymmetry 也已经开始被更细致地讨论。`JBEE` 2022 关于自动驾驶伦理决策的文章《Is Society Ready for AI Ethical Decision Making?》发现，直接问和间接测量会得出不同结果，说明“人不信任高风险 AI”本身也受测量方式影响。`Management Science` 2025 的现场实验《My Advisor, Her AI, and Me》则显示，在更高风险的投资决策中，保留 human-in-the-loop 反而可能提升 trust、采纳率和主观福利。这提示我们，高风险场景下的问题常常不是“AI 还是人”二选一，而是“AI 以什么流程位置出现”。

### 3. 这一支文献的方法偏向与局限

这一领域的文献已经从简单问卷走向行为实验、现场实验与元分析，这是优点。但它仍有几个明显局限。第一，很多研究把 reliance 当作“最终是否采纳建议”的单一结果变量，忽略了 reliance 其实可以分解成 delegation、override、monitoring、verification 和 post-hoc justification。第二，很多研究仍然使用传统算法建议范式，而不是生成式 AI 的解释型输出，因此对“生成式 AI 如何改变控制权让渡”的机制把握还不够。第三，不少研究关注的是 accuracy、framing 或 fairness perception，却较少把 reliance 与信息搜索、后续证据处理和责任归因放在同一框架里。

### 4. 你的题目可以切入的缺口

你的第二篇如果继续做“高风险场景中人对 AI 的不对称信任”，最好不要停留在 trust 的窄口径，而要升级成 `calibrated reliance under risk`。真正值得问的是：高风险情境下，人不是单纯更不信任 AI，而是更不愿意把最后控制权交出去；低风险情境下，问题又不是简单更信任，而是更容易过度委托、减少监控。这样写，你的研究就能与顶刊文献形成更直接的对话：不是重复 algorithm aversion，而是在问控制权让渡何时失准、为什么失准、是否可以通过流程设计来校准。

## 三、Bias Amplification, Search, and Belief Distortion：AI如何改变搜索与更新

### 1. 这条文献线的核心问题

这一支文献关心的是：AI 是否不仅改变人最后信了什么，还改变人如何搜集证据、如何解释证据、如何给新证据赋权。它研究的是 search rules、stopping rules、diagnosticity perception、belief updating 和 bias amplification。

### 2. 顶刊和行为经济学期刊已经回答了什么

`Nature Human Behaviour` 2025 的《How human-AI feedback loops alter human perceptual, emotional and social judgements》是这一支最关键的顶刊论文之一。它表明，人和 AI 反复互动后，不只是暂时受 AI 影响，而可能把 AI 的偏差内化为自己的偏差，并形成反馈回路。这与传统的“建议采纳”研究不同，因为这里真正变化的是人的判断过程。

`PNAS` 2023 的《Human heuristics for AI-generated language are flawed》则从另一个角度补强了这一点：人并不擅长识别 AI 生成语言，而且会依赖错误启发式来判断文本可信度。对于生成式 AI 来说，这一点尤其关键，因为它意味着结构清晰、语气流畅、叙事完整的回答，可能被误读为“来源充分”“证据完整”“已经看过反方信息”。这为你现在 proposal 中“形式完整性被误读为证据完整性”的机制提供了很强支持。

在更广义的人机判断文献里，`Management Science` 2025 的《Human-Algorithm Collaboration with Private Information》指出，人并不会灵活地根据自己 private information 的价值去调整对算法建议的权重，而是容易做机械加权。这正好说明，AI 改变的不只是结论，更是权重分配规则本身。`JEBO` 2025 的 beauty contest 研究也表明，AI advisor 会影响个体的学习路径与信念修正深度。

此外，`PNAS` 2024 的《The consequences of AI training on human decision-making》和 `PNAS` 2025 的《AI assessment changes human behavior》共同指向一个更大的问题：一旦个体意识到自己正在与 AI 共同构成一个反馈系统，行为就会发生系统性变化。这意味着未来关于 belief formation 的研究，不能再只看单轮输入输出，而需要考虑 AI 监督、AI 学习、AI 评估对行为的反向塑造。

### 3. 这一支文献的方法偏向与局限

这一领域的强项在于，它已经开始把 AI 影响写成动态反馈过程，而不只是单轮 advice adoption。然而它也有两个空白。第一，现有顶刊虽然证明了 AI 会放大偏差，却仍较少把偏差清楚拆成“搜得不够”与“更得不够”两阶段。第二，许多研究展示了 AI 会改变 perception 或 judgment，但对其背后的信息经济学机制，例如 perceived value of information、optimal stopping 和 diagnostic underweighting，仍然展开得不够。

### 4. 你的题目可以切入的缺口

这正是你第一篇最强的地方。你现在 proposal 里的 `double Bayesian distortion` 框架，把 AI 的影响拆成信息获取阶段的 under-sampling 和信息处理阶段的 under-updating，这一点与现有顶刊形成了清晰互补。换句话说，现有高水平文献已经告诉我们 AI 会改变 judgment process，但还没有把“少看”和“少更”作为两个不同的偏差来源严格分离。你完全可以把自己的定位写成：顶刊已证明 AI 会改变人的判断轨迹，而你的研究进一步解释它具体是通过改变 evidentiary sufficiency judgment 和 diagnosticity judgment 来实现的。

## 四、Responsibility, Dishonesty, and Moral Distance：AI如何改变责任与道德成本

### 1. 这条文献线的核心问题

这一支文献讨论的是：当 AI 被引入决策和行动之后，人会不会更容易把“不舒服的决定”交给机器，把责任推给机器，或者在与机器互动时感受到更低的道德成本与社会约束。这里的关键变量包括 responsibility attribution、blame shifting、dishonesty、moral distance、prosociality 和 strategic delegation。

### 2. 顶刊和行为经济学期刊已经回答了什么

`Nature` 2025 的《Delegation to artificial intelligence can increase dishonest behaviour》无疑是目前这一支最重要的研究。它把问题从“事后怪谁”推进到了“事前敢不敢做坏事”：一旦个体可以把行为委托给 AI，不诚实行为就可能上升。这个发现意味着，AI 的道德风险不只是责任归因的再分配，更是道德成本的重新定价。

`Nature Human Behaviour` 2021 的《Bad machines corrupt good morals》虽然是 perspective，但它的重要性在于提出了一个更大的研究议程：AI 不是中性工具，它可以系统性改变伦理行为。行为经济学期刊则把这个议程推进到了可观测实验层面。`JBEE` 2024 的《Would I lie to you?》发现，与 chatbot 互动时，人比与人互动时更不诚实，而且 agency cue 在 human-human 互动中有作用，在 chatbot 条件下却失效。`JBEE` 2025 关于 tax compliance 的文章进一步显示，当审计者是机器而不是人时，遵从行为下降，说明社会评价与道德约束在 machine interaction 中可能被削弱。

但这条文献并不是单向度的。`JBEE` 2019 的《Sharing responsibility with a machine》没有发现机器共同决策会稳定降低责任感或内疚感。`JEBO` 2022 的《Artificial intelligence, ethics, and intergenerational responsibility》甚至表明，在某些条件下，当人知道自己的行为会训练未来影响他人的算法时，反而可能变得更亲社会。也就是说，AI 并不自动导致责任外包；关键在于互动结构、时间维度、是否存在社会评价，以及人是否把 AI 理解为真正承担后果的行动者。

### 3. 这一支文献的方法偏向与局限

这一领域的优点是，已经从伦理讨论走向实验行为度量，例如 private reporting、tax compliance、dictator game 和 delegated decision tasks。局限则在于，很多研究把 outcome 放在诚实/不诚实或 blame attribution 上，但还没有充分把这些行为与生成式 AI 的“解释性输出”和“权威感”联系起来。也就是说，传统 machine interaction 文献能告诉我们机器会削弱社会约束，但还没有完全解释：为什么生成式 AI 这种会说话、会解释、会显得“懂你”的系统，可能比传统自动化工具更适合承接责任外包。

### 4. 你的题目可以切入的缺口

你的第三篇如果只写“事后人会不会把责任推给 AI”，会显得偏窄。更强的写法是把它升级成 `moral distance and delegated responsibility`。你可以研究的不只是 blame allocation，而是：当 AI 被理解为一个已经“判断过”“解释过”“帮我想过”的认知代理时，人是否会更容易在事前外包道德负担，在事中降低内疚约束，在事后更容易说“这是 AI 的建议”。这样，你的研究就能连接顶刊关于 dishonesty 的发现，也能和你自己的算法权威框架形成闭环。

## 五、Learning, Skill Retention, and Long-run Adaptation：AI如何改变长期能力

### 1. 这条文献线的核心问题

这一支文献关心的是更长时间尺度上的行为后果：当 AI 成为稳定存在的认知工具之后，人会不会减少技能投资、削弱 experiential learning、改变培训激励，甚至逐渐把独立思考本身视为不再值得投入的能力。

### 2. 顶刊和行为经济学期刊已经回答了什么

虽然这条线在行为经济学里还没有像 trust 文献那样成熟，但已经出现了非常有力的信号。`Organization Science` 2025 的《Algorithmic Recommendation Tools and Experiential Learning in Clinical Care》显示，算法推荐工具可能削弱 experiential learning，尤其在低难度、低多样性的任务环境中更明显。也就是说，当系统替人做了足够多的判断工作，人对自己通过重复经验学习的依赖可能下降。

`JEBO` 2025 的《Artificial intelligence adoption and workplace training》则从组织层面提供外部效度：AI adoption 与培训投入变化有关，但收益更偏向高技能者。这意味着 AI 带来的不是简单的“少学”，而可能是学习机会与技能积累路径的重新分配。`JEBO` 2026 关于创意任务的实验也提示，生成式 AI 提高表现不代表一定带来人机互补，它可能在帮助一部分人的同时，改变人们对自身能力的评估和对 AI 的依赖方式。

此外，`PNAS` 2024 的《The consequences of AI training on human decision-making》说明，即使不直接使用 AI，只要知道自己的行为会被 AI 吸收和学习，人就会改变决策方式。这使长期适应问题变得更复杂：未来需要研究的不只是“用了 AI 之后能力会不会退化”，还包括“在 AI 存在的制度环境中，人是否会提前改变努力配置与技能投资”。

### 3. 这一支文献的方法偏向与局限

这一领域最大的不足是，现有文献虽然已经看到 AI 与学习、培训、经验积累之间的关系，但大多数研究仍然停留在组织层面或短期行为层面。真正关于“认知卸载是否削弱独立判断能力”“生成式 AI 是否改变 effort investment”的实验行为经济学研究仍然较少。也就是说，这条线已经有外部效度和邻近证据，但还没有形成像 algorithm aversion 那样成熟的实验传统。

### 4. 你的题目可以切入的缺口

这恰恰是你未来第四篇最好的扩展位点。相比继续围绕 trust 或 blame 打转，转向 `cognitive offloading and skill investment` 可以明显降低同质化，而且仍然与你当前项目高度连贯。你的总体叙事可以从“AI 如何扭曲一次判断”扩展到“AI 如何改变长期认知资本形成”。在 dissertation 结构上，这会让你的研究从短期行为偏差走向长期能力配置，层次会更完整。

## 六、综合比较：这些文献共享的机制、方法与空白

从顶刊和行为经济学期刊合起来看，当前文献已经形成三个相对稳定的共识。

第一，AI 的影响不是单纯准确率问题，而是交互结构问题。无论是 reliance、更新偏差还是责任外包，决定行为结果的往往不是 AI 本身有多准，而是它在流程中如何出现、以什么话语形式出现、是否保留 human-in-the-loop、是否允许验证、是否让用户感觉自己仍保有控制权。

第二，AI 的影响越来越被理解为过程性影响，而不是结果性影响。现在的顶刊文献已经不满足于问“最后选了什么”，而更关注“之前搜了多少”“中间怎么加权”“事后怪谁”“长期还学不学”。这为行为经济学提供了一个非常自然的切口，因为这些问题都可以被写成 choice under uncertainty、delegation under incentives 或 moral cost allocation。

第三，生成式 AI 的特殊性在于，它把解释、叙事和社会性线索一起带入了交互过程。传统算法更多改变 exposure 和 recommendation；生成式 AI 则更容易改变 evidentiary sufficiency judgment、mind perception、social expectation 和 epistemic authority。这也是为什么简单沿用传统 algorithm aversion 框架已经不够。

但与此同时，这些文献也共享几个空白。第一，很多研究仍然各自研究一个 outcome，例如 reliance、dishonesty、bias 或 training，却较少把它们放进统一的行为经济学框架里。第二，尽管顶刊开始重视 feedback loops 和 longer-run effects，但“少搜”和“少更”这样更细致的信息经济学拆分仍然不足。第三，长期学习与技能投资这一支仍然偏弱，尤其缺少生成式 AI 条件下的重复实验设计与行为激励设计。第四，程序正义、自主性感知与控制权让渡之间的连接虽然在邻近领域已有信号，但在行为经济学中还没有被充分吸收。

因此，现在最值得推进的理论语言，不是“AI 会不会让人做错”，而是“AI 会不会让人重新配置原本属于自己的认知、控制、道德与学习工作”。这比单纯的 trust 叙事更能统摄现有文献，也更能为你的 dissertation 提供总品牌。

## 七、你的研究定位：三篇如何重排，未来两篇如何扩

### 1. 现有三篇分别放在哪个板块

你现在的第一篇最自然地放在 `Bias Amplification, Search, and Belief Distortion`。它的核心贡献不应只表述为“AI 影响信息更新”，而应写成：AI 通过改变用户对证据充分性和冲突诊断性的判断，影响信息获取与信念更新这两个阶段。

你现在的第二篇不应继续停留在“高风险信任、高低风险不对称”这种比较松的说法，而应明确放进 `Reliance and Ceding Control`。更准确的表述是：AI 介入后，人们如何在不同风险环境中配置最终控制权、采纳权与覆核权，以及这种配置何时失去校准。

你现在的第三篇则应放进 `Responsibility, Dishonesty, and Moral Distance`。如果只写责任归因，容易显得是第二篇的后果变量；如果升级为“AI 如何改变道德成本与责任承担”，就会和当前顶刊文献更接轨。

### 2. 现有三篇为什么会显得同质化

你担心三篇太像，判断是对的。问题不在于题目不好，而在于三篇都围绕同一个母机制展开：人把认知工作委托给 AI 之后，分别在事前少搜、事中少更、事后甩锅。也就是说，现在的三篇更像是 `delegated cognition` 的三个 downstream outcomes，而不是三条相互独立的研究线。

因此，真正需要调整的不是推翻现有题目，而是把三篇放回不同层级。第一篇负责“证据与更新”，第二篇负责“控制权与 reliance”，第三篇负责“责任与道德”。只要层级摆正，它们就不再像一个题目的三个因变量，而会更像一个总项目下的三条子线。

### 3. 第四篇和第五篇最自然的扩展位点

最自然的第四篇是 `Learning, Skill Retention, and Long-run Adaptation`。一句话概括，就是研究生成式 AI 会不会让人把思考外包，从而减少对独立判断能力的投资。它与第一篇最接近，但把分析单位从一次判断扩展到了长期能力变化。

最自然的第五篇是围绕程序正义、自主性感知与流程位置展开。虽然它不在你原来的三篇之内，但与第二篇高度相邻。你可以把它写成：人们反感的也许不是 AI 本身，而是 AI 在流程中拿走最后决定权的方式。这会显著降低整体同质化，因为它从 epistemic distortion 转到了 process legitimacy。

### 4. 一个更稳的 dissertation 总体定位

如果要把整套研究写成一个更大的 dissertation 品牌，最稳的总命题不是“AI 是否让人判断失真”，而是：

`生成式 AI 作为被委托的认知代理，如何重塑人类在不确定性下对搜索、控制、责任与学习的配置。`

在这个总框架下，你的五篇可以被重排为：

- 论文一：AI 如何改变证据抽样与信念更新
- 论文二：AI 如何改变风险下的 reliance 与控制权让渡
- 论文三：AI 如何改变责任归因、道德成本与不诚实行为
- 论文四：AI 如何改变认知卸载、技能投资与独立判断
- 论文五：AI 如何改变程序正义、自主性感知与系统接受度

这样写的好处在于，你既没有离开行为经济学，也没有被困在传统 trust 文献里。更重要的是，它能把你当前的 proposal 从“一个很强但偏窄的三篇组合”，升级成“一个围绕 delegated cognition and delegated responsibility 的系统研究计划”。

## 八、结论

从顶刊和行为经济学期刊的现有文献看，AI-human interaction 的研究重心已经明显从“人信不信 AI”转向“AI 如何改变人的行为规则”。最值得保留的不是 trust 这个旧标签，而是背后更大的结构性问题：当生成式 AI 作为解释者、建议者、代理者和评估者进入决策过程之后，人会不会更早停止搜索、更少更新信念、更愿意交出控制权、更容易外包责任，以及更少投资于长期能力。

这正是你的研究最有潜力的地方。你的优势不在于重复 algorithm aversion，而在于把 AI 对人类行为的影响写成一个统一的行为经济学问题：AI 是否正在重新分配原本属于人类自己的认知、控制、道德与学习工作。
