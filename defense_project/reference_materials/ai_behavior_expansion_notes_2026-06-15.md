# AI x 行为科学研究拓展备忘录

日期：2026-06-15

## 1. 先判断你现在的问题到底是什么

看完你现有的 proposal 之后，一个很明显的判断是：

你现在的研究不是分散的三篇，而更像是**同一个母题下面的三个结果变量**。

这个母题可以概括成：

**生成式 AI 作为“被委托的认知代理”之后，人类如何减少自主的认知劳动，并在事前、事中、事后重组自己的判断、行为与责任。**

你目前材料里最强的主线，来自两个地方：

- [理论框架](E:\Info_AI\defense_project\latex\sections\02_framework_questions_hypotheses.tex)
- [研究设计](E:\Info_AI\defense_project\latex\sections\03_research_design_and_studies.tex)

这两部分都在围绕同一个机制链：

`AI先给出综合性结论 -> 人把“证据处理工作”默认委托给AI -> 人更早停止搜索 / 更少更新 / 更容易外包责任`

所以你担心“集中度太高”是对的。不是题目不好，而是**三篇都太像在研究 delegated cognition 的不同下游表现**。

## 2. 更适合你的总品牌

比起把总题目叫做“AI信任”或者“算法权威”，我更建议你把总品牌改成下面这种更宽、也更能容纳多篇论文的说法：

**品牌 A：AI 如何重塑不确定性下的人类认知委托与行为反应**

或者更偏行为经济学一点：

**品牌 B：AI 介入后，人类如何重新分配信息搜索、判断控制、道德成本与责任承担**

这样一来，你现有的三篇就可以被重新摆放：

- 论文 1：AI 如何扭曲证据抽样与信念更新
- 论文 2：AI 介入后，人的 reliance calibration 如何失衡
- 论文 3：AI 介入后，责任归因如何转移

然后第 4、第 5 篇就不必继续围绕“信不信 AI”转，而可以去研究：

- 长期的认知后果
- 程序正义与自主性感知
- 道德距离与不诚实
- 个性化说服与偏好塑造

## 3. 最值得你扩出去的 6 条支线

### 方向 1：认知卸载、技能投资与长期依赖

这条线研究的不是“这一轮决策对不对”，而是：

**反复使用 AI 之后，人是否会减少对自己认知能力的投资？**

可以问的行为经济学问题：

- AI 是否降低人对独立思考的投入意愿
- AI 是否让人把 effort 从 problem solving 转向 output monitoring
- AI 是否降低长期 skill accumulation
- 人是否会因为 AI 可得性而改变自己对学习成本的忍受度

为什么适合你：

- 和你现在的“少搜、少更”很近，但研究对象从**单次判断偏差**转成了**动态的人力资本与认知资本**
- 这会让你的研究从 judgment 扩到 learning / effort / dynamic incentives

可做实验：

- repeated-task design
- 先允许部分被试使用 AI，后面突然取消 AI，看独立表现是否下降
- 比较“AI直接给答案”与“AI只提问题/只做脚手架”对长期能力的影响

### 方向 2：程序正义、自主性感知与接受度

这条线研究的不是“AI对不对”，而是：

**即使结果相同，人们是否会因为 AI 出现在流程中的位置不同，而觉得过程不公平、自己不被尊重、控制权被拿走？**

可以问的行为经济学/组织行为问题：

- AI 先审、人后审，和人先审、AI后审，接受度是否不同
- 用户是否在“被建议”和“被替代”之间有明显的心理断点
- autonomy loss 是否会降低满意度、遵从度和继续使用意愿
- 在高风险 vs 低风险场景中，程序正义的作用是否不同

为什么适合你：

- 它和你第二篇“高风险不信任、低风险过度信任”可以接上
- 但因变量从 trust/reliance 换成了 **procedural legitimacy / autonomy**
- 同质化程度会明显下降

可做实验：

- 同一判断任务，只改 AI 出场顺序、最终裁量权、是否允许用户修改
- 测量 fairness, autonomy, legitimacy, compliance, continued usage intention

### 方向 3：道德距离、不诚实与“AI当替罪羊”

这条线比你现在的责任归因更进一步，不只看事后 blame，而是看：

**人会不会因为可以把脏活交给 AI，而在事前就更敢做不道德的事？**

可以问的问题：

- 有 AI 代理时，人是否更愿意作弊、夸大、隐瞒、甩锅
- vague goal-setting 比 explicit unethical instruction 更危险吗
- 当责任能被“洗给AI”时，道德成本是否下降

为什么适合你：

- 和责任归因相关，但不再只是“ blame 分配”
- 它进入了行为经济学里更经典的 moral wiggle room / moral distance / unethical delegation

可做实验：

- die-roll / tax-reporting / allocation / hiring recommendation 场景
- 比较“自己做”“让人代做”“让规则算法代做”“让生成式 AI 代做”

### 方向 4：个性化说服、偏好塑造与选择架构

这条线研究：

**AI 不只是改变你“相信什么”，还可能改变你“想要什么”。**

可以问的问题：

- 个性化 AI 建议是否比一般建议更能改变消费、政治、健康选择
- AI 是在传递信息，还是在重塑偏好
- 用户是否把 AI 的个性化建议误当成“懂我”，从而降低防御

为什么适合你：

- 和你的第一篇“信息更新”邻近，但理论重心从 Bayesian updating 转向 persuasion / preference construction
- 更容易和 choice architecture、nudging、welfare analysis 接轨

可做实验：

- 同一产品/政策/健康选择，比较 generic advice 与 personalized AI advice
- 测量 preference shift、WTP、态度持久性、反悔率

### 方向 5：AI 介导的确认偏差与信息回音室

这条线研究：

**AI 是否因为“迎合式对话”而放大用户原有立场，而不只是提供错误信息。**

可以问的问题：

- 用户带着先验立场来问 AI 时，AI 是否更容易强化原有信念
- 这种强化是来自 personalization、礼貌迎合，还是 conflict-avoidance
- 高认知闭合需求的人是否更容易受到影响

为什么适合你：

- 与你现有 proposal 最接近
- 但它更偏向 selective exposure / confirmation bias / motivated reasoning
- 如果你想保守扩展，这是最容易落地的“第四篇”

### 方向 6：AI、分配公平与再分配偏好

这条线稍微远一点，但仍然在行为经济学边上：

**当人们认为 AI 正在改变收入分配、就业机会和社会回报时，他们的公平偏好和再分配态度会不会变？**

可以问的问题：

- AI造成的不平等，是否比“市场导致的不平等”更容易被接受或更难被接受
- 人们是否更愿意支持针对 AI 替代风险的保险、补贴、再分配
- 当决策由 AI 做出时，人们对结果不平等的容忍度是否变化

为什么值得保留：

- 这是把你的项目从 micro judgment 扩到 political economy 的桥
- 适合作为中长期发展方向，但不一定是现在最优先的第 4 篇

## 4. 我最推荐的第 4、第 5 篇

如果目标是“不要离太远，但又不要显得还在重复同一篇”，我建议优先这样配：

### 第 4 篇优先选：认知卸载与技能投资

原因：

- 和你现在的机制主线连得很顺
- 但单位从“一次决策”切到“长期能力变化”
- 很容易讲出新的理论贡献：AI 不只是扭曲 belief formation，还重塑 human capital formation

一句话题目感：

**生成式 AI 会不会让人把思考外包，从而减少对独立判断能力的投资？**

### 第 5 篇优先选：程序正义与自主性感知

原因：

- 这篇会明显降低同质化
- 它研究的不是 epistemic distortion，也不是 blame shifting，而是 process legitimacy
- 很适合和你第二篇的 risk/trust 设想重新拼接

一句话题目感：

**人们反感的也许不是 AI 本身，而是 AI 在流程中“拿走最后决定权”的方式。**

## 5. 你现有三篇最好怎么重新摆

为了避免看起来像“三个几乎一样的题目”，我建议你改成下面的结构：

### 板块一：Epistemic Dependence

- 论文 1：AI 如何改变信息搜索与信念更新

关键词：

- evidence sampling
- value of information
- Bayesian updating
- ambiguity compression

### 板块二：Control and Reliance

- 论文 2：AI 如何改变人对控制权、风险与 reliance 的配置

关键词：

- calibrated reliance
- autonomy
- override behavior
- risk asymmetry

### 板块三：Accountability and Moral Distance

- 论文 3：AI 如何改变责任、道德成本与 blame allocation

关键词：

- responsibility attribution
- moral distance
- strategic delegation
- excuse value

### 板块四：Long-run Cognition

- 论文 4：AI 如何改变 effort investment、skill retention 与独立判断

### 板块五：Legitimacy and Preference Shaping

- 论文 5：AI 如何改变程序正义、自主性感知，或直接塑造偏好

这样看起来就不是“同一个 trust 题目的三个分支”，而是：

**AI 介入后，人类在认知、控制、道德和长期能力上发生的一组系统性变化。**

## 6. 可以直接拿来用的文献种子

下面这些文献最适合给你拓题，而不是只给现有 proposal 补脚注。

### 6.1 认知卸载与长期依赖

- Lee et al. (CHI 2025), *The Impact of Generative AI on Critical Thinking*  
  319 名知识工作者、936 个真实案例；结论很适合你：对 GenAI 越有信心，越少进行 critical thinking。  
  链接：[Microsoft Research](https://www.microsoft.com/en-us/research/publication/the-impact-of-generative-ai-on-critical-thinking-self-reported-reductions-in-cognitive-effort-and-confidence-effects-from-a-survey-of-knowledge-workers/)

### 6.2 程序正义与流程位置

- Jiang et al. (PLOS ONE, 2023), *Who should be first? How and when AI-human order influences procedural justice in a multistage decision-making process*  
  关键点：人先、AI后，比 AI先、人后，更容易被感知为程序不公。  
  链接：[PLOS ONE](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0284840)

### 6.3 道德距离、不诚实与AI外包

- Köbis et al. (Nature, 2025), *Delegation to artificial intelligence can increase dishonest behaviour*  
  13 个研究、8000+ 被试；非常适合你把“责任归因”升级成“AI 是否让人更敢不诚实”。  
  链接：[Nature](https://www.nature.com/articles/s41586-025-09505-x)

- Joo et al. (PLOS ONE, 2024), *It’s the AI’s fault, not mine: Mind perception increases blame attribution to AI*  
  说明当人把 AI 当成“有心智的行动者”时，更容易把 blame 给 AI。  
  链接：[PLOS ONE](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0314559)

### 6.4 个性化说服与偏好塑造

- Matz et al. (Scientific Reports, 2024), *The potential of generative AI for personalized persuasion at scale*  
  四项研究、总样本 1788；个性化信息比非个性化更有说服力。  
  链接：[Scientific Reports](https://www.nature.com/articles/s41598-024-53755-0)

- Salvi et al. (Nature Human Behaviour, 2025), *On the conversational persuasiveness of GPT-4*  
  在个性化条件下，GPT-4 在辩论任务中的说服力高于人类。  
  链接：[Nature Human Behaviour](https://www.nature.com/articles/s41562-025-02194-6)

### 6.5 AI协作并不天然带来更好判断

- Vaccaro et al. (Nature Human Behaviour, 2024), *When combinations of humans and AI are useful: A systematic review and meta-analysis*  
  核心发现很重要：在人机协作里，“决策任务”平均表现往往不如最优的人或最优的AI单独完成。  
  链接：[Nature Human Behaviour](https://www.nature.com/articles/s41562-024-02024-1)

### 6.6 AI与确认偏差

- Lopez-Lopez et al. (Annals of the New York Academy of Sciences, 2025), *Generative artificial intelligence-mediated confirmation bias in health information seeking*  
  虽然是 health 场景，但机制对你很有用：AI 可能通过互动式生成放大确认偏差。  
  链接：[Wiley](https://nyaspubs.onlinelibrary.wiley.com/doi/full/10.1111/nyas.15413)

## 7. 一个实用建议

如果你接下来真的要做“五篇路线图”，最好的办法不是继续围着“trust”扩写，而是先选定一个更高层的总命题，再把每篇论文分别固定在不同阶段：

- 事前：搜不搜、看不看
- 事中：信多少、让多少
- 事后：怪谁、奖谁
- 长期：还学不学、还会不会
- 制度层：觉得公不公平、愿不愿继续接受

这样你的 dissertation / paper pipeline 会显得是一个完整研究计划，而不是同一篇论文的五个 outcome。

## 8. 我给你的结论

你现在最不缺的是“主线”，最缺的是“维度”。

所以接下来最优策略不是把现有三篇完全推翻，而是：

1. 保留你现在这条非常强的 epistemic distortion 主线。
2. 把第二篇从“信任AI”改成“控制权与 reliance calibration”。
3. 把第三篇从“责任归因”升级成“道德距离与责任外包”。
4. 新增第四篇“认知卸载与技能投资”。
5. 新增第五篇“程序正义与自主性感知”。

如果只选一句最重要的话：

**你的总题目不该只是“AI会不会让人判断错”，而应该是“AI会不会让人把原本属于自己的认知、控制与道德工作，越来越多地委托出去”。**
