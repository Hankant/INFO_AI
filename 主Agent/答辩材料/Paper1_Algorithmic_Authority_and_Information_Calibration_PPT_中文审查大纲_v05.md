# 第一篇 PPT 中文审查大纲

对应英文答辩 PPT 主题：
`Algorithmic Authority and Information Calibration: How Generative AI Changes Additional Search and Belief Updating under Uncertainty`

本文件用于审查第一篇英文 PPT 的内容结构。最终 PPT 应为英文；本文件只提供中文说明、英文页标题建议、每页核心信息、对应基准稿位置/内容来源，以及需要避免的旧口径错误。

## 使用原则

- 当前第一篇**唯一优先基准稿**：
  `E:\Info_AI\主Agent\文章项目\01_算法权威与信息校准\当前第一章_算法权威与信息校准_基准稿.md`
- 可以参考但不得覆盖基准稿口径的材料：
  - `E:\Info_AI\修改版本.md`
  - `E:\Info_AI\dd636486-c2c3-485e-a8b5-0ec083e806dd_修改版｜算法权威与信息校准：生成式_AI_如何改变额外搜索与信念更新.pdf`
  - `E:\Info_AI\defense_project\latex\sections\*.tex`
- 当前主线必须是 `information calibration`。
- `double Bayesian distortion` 不得作为标题、总框架或开篇理论预设；它最多只能在后验偏离或预期结果部分谨慎出现，作为可能的经验结果模式。

## 页数建议

- 建议压缩到 13–14 页。
- 当前前半段应进一步压缩，避免在提出核心问题前铺垫过长。
- 当前后半段也应避免在实验介绍完成后继续堆叠过多技术页。
- 若与总领引言合并展示，优先控制在 13–14 页。

## 页面大纲

### Slide 1

- 英文标题建议 Source-dependent evaluation biases and Context-dependent updating biases
这一页先不显示文章标题，指出AI给人带来的困惑

  `Paper 1: Algorithmic Authority and Information Calibration`
- 中文核心信息：
  - 从总领引言进入第一篇。
  - 明确这一篇研究的是 `evidence -> belief`，但当前切入点不是旧版的 `Double Bayesian Distortion`，而是生成式 AI 如何改变额外搜索与信念更新中的 `information calibration`。
  - 需要一句话点明：问题不只是 AI 给了什么答案，而是它是否改变了人判断“还需不需要继续找证据”。
- 对应基准稿位置/内容来源：
  - 基准稿开头“核心改动”
  - 基准稿“研究背景”前两段
  - 基准稿“三、研究问题”总问题段
- 需要避免的旧口径错误：
  - 不要把标题写成 `Double Bayesian Distortion`
  - 不要把第一页讲成 generic algorithm trust 总论

### Slide 2

- 英文标题建议：
  `From searching evidence to receiving an interpreted answer`
- 中文核心信息：
  - 必须保留生活化左右对比。
  - 左侧：`Search engine logic`
    - 用户面对多个来源、多个链接、多个冲突
    - 需要自己打开、比较、筛选、整合，再形成判断
    - 标签：`Evidence first -> interpretation later`
  - 右侧：`AI assistant logic`
    - 用户先收到一个已经组织好的解释、定义、例子和结论
    - 面对的是被筛选、被叙述、被压缩后的信息结构
    - 标签：`Interpreted answer first -> optional verification later`
  - 底部 punchline 应强调：
    - 变化不只在于搜索量，而在于人如何判断继续搜索的价值
- 对应基准稿位置/内容来源：
  - 基准稿“研究背景”第 1–3 段
  - 基准稿“2.2 生成式 AI、总结式回答与信息压缩”
- 需要避免的旧口径错误：
  - 不要抽象理论起手
  - 不要在此页引入 `double Bayesian distortion`
  - 不要把 AI 描述成单纯“更快搜索引擎”

### Slide 3

- 英文标题建议：
  `Less search is not necessarily worse judgment`
- 中文核心信息：
  - AI 后少搜索，不必然代表判断更差。
  - 至少有两条可能路径：
    - `Efficient compression`
      - less search
      - no loss in posterior quality
    - `Harmful under-search`
      - less search
      - more deviation from the full-information benchmark
  - 这一页要切断一个常见误解：关键不是“有没有少搜索”，而是“少搜索之后是否偏离规范判断”。
- 对应基准稿位置/内容来源：
  - 基准稿“研究背景”关于“AI 的核心功能之一正是降低信息检索、筛选和整合成本”
  - 基准稿“2.1 信息搜索、搜索成本与停止规则”
  - 基准稿“RQ2”
- 需要避免的旧口径错误：
  - 不要把 `search reduction` 直接等同 `judgment decline`
  - 不要把这页写成对 AI 的道德批评

### Slide 4

- 英文标题建议：
  `Existing work rarely separates search, updating, and subjective mastery`
- 中文核心信息：
  - 现有研究常看：
    - trust
    - adoption
    - automation bias
    - advice-taking
  - 但较少严格区分三件事：
    1. 用户是否继续查找额外证据
    2. 用户是否对已接触证据正确更新
    3. 用户是否误判自己已经掌握了多少信息
  - 这一页的 gap 要服务于当前研究的三层结构，而不是泛泛说“过去研究不够”。
- 对应基准稿位置/内容来源：
  - 基准稿“2.1 信息搜索、搜索成本与停止规则”
  - 基准稿“2.3 算法标签、算法权威与来源效应”
  - 基准稿“2.5 主观信心、信息掌握感与校准错配”
- 需要避免的旧口径错误：
  - 不要把 gap 写成 “没人研究 AI”
  - 不要重新并回 generic trust literature

### Slide 5

- 英文标题建议：
  `Algorithmic authority changes judgments of evidentiary sufficiency`
- 中文核心信息：
  - 当前版本中的 `algorithmic authority` 不是简单的 “the AI answer is correct”。
  - 它更具体地指向用户对如下问题的判断变化：
    - AI 是否已经搜索得足够多
    - 是否已经整合了主要信息
    - 是否已经处理了反向证据
  - 所以算法权威首先改变的是用户对 `evidentiary sufficiency` 的判断。
- 对应基准稿位置/内容来源：
  - 基准稿“2.3 算法标签、算法权威与来源效应”
  - 基准稿“三、研究问题”总问题段
- 需要避免的旧口径错误：
  - 不要把 authority 简化成 blind obedience
  - 不要把这一页讲成普通 trust 定义

### Slide 6

- 英文标题建议：
  `Core question: How do generative AI answers change users' stopping thresholds, Bayesian posterior quality, and subjective information mastery?`
- 中文核心信息：
  - 这一页应合并原先第 7、8 页的功能，不再分成“framing”与“mechanism”两页。
  - 开门见山给出本文总问题：
    - 生成式 AI 回答如何影响用户的搜索停止阈值、贝叶斯后验更新质量和主观信息掌握感？
  - 明确本文的 framing：
    - 本文不把生成式 AI 使用者减少原始证据查阅直接视为 `search laziness`
    - 而是把这一行为放回 `Bayesian belief updating` 框架下重新评估
  - 这一页要把主线说得足够尖锐：
    - 关键不是 AI 是否让人少搜
    - 而是 AI 是否通过改变 `perceived evidentiary sufficiency`，把搜索停止阈值向前推
  - 建议页面结构改成一条清晰链条，而不是三个并列小框：
    - `AI answer / AI label`
    - `inferred hidden search-and-integration process`
    - `perceived sufficiency rises`
    - `value of additional evidence falls`
    - `stopping threshold shifts`
  - 可以保留一句简短工作定义：
    - `information calibration = alignment between perceived sufficiency and the actual value of further evidence`
- 对应基准稿位置/内容来源：
  - 基准稿“核心改动”
  - 基准稿“研究背景”后半部分
  - 基准稿“2.3 算法标签、算法权威与来源效应”
  - 基准稿“RQ1–RQ3”之间的递进逻辑
- 需要避免的旧口径错误：
  - 不要再先讲“not generic trust”再慢慢绕回总问题
  - 不要把主线继续叫做 `double distortion`
  - 不要把机制做成松散的三条推断清单，缺少行为落点

### Slide 7

- 英文标题建议：
  `The study asks three linked questions`
- 中文核心信息：
  - 在第 6 页明确总问题和 framing 后，这一页应迅速进入研究问题，不再做额外过渡。
  - `RQ1`
    - AI-labeled summary 是否改变额外搜索停止阈值？
  - `RQ2`
    - 搜索减少是理性信息压缩，还是有害的信息获取偏离？
  - `RQ3`
    - 主观信息掌握感与客观判断质量是否发生错配？
  - 三个问题必须呈现递进关系：
    - `behavioral threshold change`
    - `normative evaluation of posterior quality`
    - `metacognitive calibration`
- 对应基准稿位置/内容来源：
  - 基准稿“三、研究问题”全部
- 需要避免的旧口径错误：
  - 不要沿用旧 proposal 的宽泛问题
  - 不要让三个 RQ 彼此并列、没有递进

### Slide 8

- 英文标题建议：
  `An AI summary-assisted evidence search task in a company-risk judgment setting`
- 中文核心信息：
  - 这一页标题不应直接写 `3 x 2`，因为这对答辩听众不够直观。
  - 应先让老师明白“这到底是什么实验”：
    - 本实验的贝叶斯原型是经典的 `urn-drawing / bookbag-and-poker-chip belief-updating task`
    - 我们的创新是将其情境化为公司风险判断，并加入 `AI summary-first` 的信息呈现与后续证据搜索
  - 然后再简洁交代设计结构：
    - 三个呈现条件：
      `no-summary control / unlabeled summary / AI-labeled summary`
    - 两种 representativeness：
      `representative summary / incomplete summary`
  - 这一页的功能应该是：
    - 先建立任务原型
    - 再让听众看到 `3 x 2` 只是这个原型内部的操控结构
  - 三个呈现条件：
    - `no-summary control`
    - `unlabeled summary`
    - `AI-labeled summary`
  - 两种 representativeness：
    - `representative summary`
    - `incomplete summary`
  - 这一页要让听众先明白设计矩阵，而不是陷入流程细节。
- 对应基准稿位置/内容来源：
  - 基准稿“4.1 实验目标与总体设计”
  - 基准稿“4.2 实验任务”
- 需要避免的旧口径错误：
  - 不要提前展开统计策略
  - 不要把设计结构和识别策略混在一页里

### Slide 9

- 英文标题建议：
  `The same-summary source-label design isolates the AI label effect`
- 中文核心信息：
  - AI-labeled 与 unlabeled 组看到完全相同的 summary 正文。
  - 唯一差别是是否标注为 AI 生成。
  - 因此两组差异不能归因于文本内容，而应归因于来源标签及其引发的算法权威/信息充分性感知。
  - 这是方法可信度最核心的一页。
- 对应基准稿位置/内容来源：
  - 基准稿“核心改动”第 5 点
  - 基准稿“2.3 算法标签、算法权威与来源效应”
  - 基准稿“4.4 Summary 操纵”
- 需要避免的旧口径错误：
  - 不要把 label effect 和 content effect 混为一谈
  - 不要把这一页写成泛泛的 manipulation check

### Slide 10

- 英文标题建议：
  `A controlled evidence pool makes Bayesian evaluation possible`
- 中文核心信息：
  - 这一页主要负责把任务原型和固定证据环境讲清楚，不再承担完整的贝叶斯指标定义。
  - 可顺手点明实验原型来源：
    - 贝叶斯规范原型来自经典的 `urn-drawing / bookbag-and-poker-chip` 更新任务
    - 当前设计不是脱离传统 belief-updating paradigm 另起炉灶
    - 而是在这一原型上加入公司风险判断语境、summary-first 呈现和额外证据搜索决策
  - 公司风险判断任务
  - 固定证据库
  - 每条证据有明确方向和 likelihood ratio
  - 被试报告 posterior probability
  - 研究者因此可以将“看到了哪些证据”与“应当更新到什么程度”对齐
- 对应基准稿位置/内容来源：
  - 基准稿“4.2 实验任务”
  - 基准稿“4.3 证据库与数据生成过程”
  - 基准稿“4.7 贝叶斯后验计算”
- 需要避免的旧口径错误：
  - 不要把任务讲成开放文本世界
  - 必须强调 `controlled evidence pool`

### Slide 11

- 英文标题建议：
  `Bayesian updating provides the normative benchmark`
- 中文核心信息：
  - 这一页专门解释为什么本实验不只是看“点了多少证据”，而是能评估后验判断是否接近规范基准。
  - 可用最简洁的 log-odds 形式呈现规范更新：
    - `logit(p_Bayes) = logit(p_prior) + Σ log(LR_j)`
  - 需要点明信息集如何进入计算：
    - summary 中明确提到的证据计入已接触信息集
    - 后续自由搜索中被试点击并阅读的证据同样计入信息集
  - 这一页最好只保留两个核心偏离指标：
    - `Conditional Bayesian Deviation`
      - 被试报告后验与 `p_Bayes observed` 的距离
      - 衡量是否正确处理了自己已经看到的信息
    - `Full-information Deviation`
      - 被试报告后验与 `p_Bayes full` 的距离
      - 衡量最终判断距离完整证据基准有多远
  - 这两个指标的解释必须非常直观：
    - `conditional` 低但 `full-information` 高
      - 说明对已看证据处理较准确，但搜索不足，遗漏了关键证据
    - `conditional` 高
      - 即使看了较多证据，也说明证据加权或后验更新本身存在偏差
  - 这一页的功能是把后面的结果识别逻辑立住：
    - 我们能够区分 under-search 和 under-updating，而不是把两者混成同一种误差
- 对应基准稿位置/内容来源：
  - 基准稿“4.7 贝叶斯后验计算”
  - 基准稿“4.6 核心变量与操作化”
- 需要避免的旧口径错误：
  - 不要把公式做得过重，变成纯技术推导页
  - 不要只给公式，不解释两个 deviation 指标各自识别什么

### Slide 12

- 英文标题建议：
  `Different result patterns would support different hypotheses`
- 中文核心信息：
  - 到这一页为止，实验已经介绍完毕。
  - 因此这里最重要的不是继续堆指标定义，而是明确：
    - 什么样的结果会支持 `RQ1`
    - 什么样的结果会支持 `RQ2`
    - 什么样的结果会支持 `RQ3`
  - 推荐做成“结果模式 -> 假设支持”的对照页：
    - 若 `AI-labeled summary` 组更少搜索、更早停止、额外证据支付意愿更低
      - 支持 `RQ1`：AI 标签改变搜索停止阈值
    - 若在 `representative summary` 条件下搜索减少，但 `full-information deviation` 不上升
      - 支持 `RQ2` 中的 `efficient compression`
    - 若在 `incomplete summary` 条件下搜索减少，且 `full-information deviation` 上升
      - 支持 `RQ2` 中的 `harmful information acquisition deviation`
    - 若 AI summary 组客观更新质量较高，但 `subjective mastery / epistemic ownership` 较低
      - 支持 `RQ3`：信息校准错配
  - 这一页要把“实验结果如何证明实验假设”说清楚，而不是只解释统计指标本身。
- 对应基准稿位置/内容来源：
  - 基准稿“4.9 统计分析策略”
  - 基准稿“4.10 预期结果模式”
  - 基准稿“4.6 核心变量与操作化”
- 需要避免的旧口径错误：
  - 不要把这一页写成新的技术说明页
  - 不要只定义 `conditional deviation` 和 `full-information deviation`，却不告诉老师这些指标如何对应假设

### Slide 13

- 英文标题建议：
  `Expected contributions`
- 中文核心信息：
  - 这一页不再单独展开新的结果模式，而是收束整篇的预期贡献。
  - 理论贡献：
    - 把问题从 generic trust / automation bias 推进到 `evidence -> belief` 的信息校准机制
  - 方法贡献：
    - 用经典贝叶斯更新原型的情境化扩展，区分搜索行为变化、后验更新质量与主观掌握感
  - 识别贡献：
    - 用 `same-summary source-label design` 分离内容效应与 AI 标签效应
  - substantive contribution：
    - 说明生成式 AI 的关键影响不只是“让人少搜索”，而是改变人对证据充分性的判断
- 对应基准稿位置/内容来源：
  - 基准稿全文主线
  - 基准稿“4.10 预期结果模式”
- 需要避免的旧口径错误：
  - 不要把贡献写成泛泛的 “AI makes people trust less or more”
  - 不要再把 `double Bayesian distortion` 拉回总结页

## 与旧口径切割说明

- 不再使用 `Double Bayesian Distortion / 双重贝叶斯偏离` 作为第一篇标题或开篇理论框架。
- 旧的 `defense_project/latex` 中仍含有旧标题、旧表述和旧的 Study 1/2/3 结构，不能直接作为 PPT 主线。
- 旧文件
  `E:\Info_AI\主Agent\答辩材料\Paper1_Double_Bayesian_Distortion_PPT_中文审查大纲.md`
  不应继续作为正式大纲。

## 下一步建议

- 若用户认可这版压缩后的 13 页结构，再进入英文可视化版 PPT 制作。
- 后续做英文 PPT 时，三张最关键的识别页应优先保证清晰：
  - Slide 2：搜索引擎 vs AI assistant
  - Slide 9：same-summary source-label design
  - Slide 11：Bayesian updating provides the normative benchmark
  - Slide 12：different result patterns would support different hypotheses
