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

- 建议 15 页。
- 若讲述时需要更充分方法解释，可扩到 16 页。
- 若与总领引言合并展示，优先压缩到 14–15 页。

## 页面大纲

### Slide 1

- 英文标题建议 Source-dependent evaluation biases and Context-dependent updating biases
这一页先不显示文章标题，指出AI给人带来的困惑，着重描述有了AI之后和AI之前的行为区别。

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
此处要引入一些对具体文献的批判，比如有一些文献简单地得出了AI会减少人类地搜索行为，但是却没有深入思考。
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
  - 这一页的 gap 要服务于当前研究的三层结构，而不是泛泛说“过去研究不够”。还要尽可能引入文献
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
  `AI summaries create a perceived signal structure`
- 中文核心信息：
  - 用户看到的不只是结论，还会推断 summary 背后的信号生成结构：
    - 是否已搜索更多信息
    - 是否已筛选噪音
    - 是否已整合冲突
    - 是否已考虑反方证据
  - 这就是 `perceived signal structure`。
  - 这一页承担从“来源标签”过渡到“信息校准机制”的作用。
- 对应基准稿位置/内容来源：
  - 基准稿“2.3 算法标签、算法权威与来源效应”
  - 基准稿“核心改动”第 5 点 `same-summary source-label design`
- 需要避免的旧口径错误：
  - 不要把 AI summary 只当成普通文本输入
  - 不要忽略用户对 hidden process 的心理推断

### Slide 7

- 英文标题建议：
  `Information calibration asks whether users correctly value additional evidence`
- 中文核心信息：
  - 正式引出全文主线 `information calibration`。
  - 当前研究的问题不是 AI 是否提高平均表现，而是用户是否正确校准：
    - 当前信息是否已足够
    - 额外证据是否仍然有价值
    - 自己是否真的掌握了足够信息
  - 可以给出一句工作定义：
    - `information calibration = alignment between perceived sufficiency and the actual value of further evidence`
- 对应基准稿位置/内容来源：
  - 基准稿“核心改动”
  - 基准稿“研究背景”后半部分
  - 基准稿“RQ1–RQ3”之间的递进逻辑
- 需要避免的旧口径错误：
  - 不要把主线继续叫做 `double distortion`
  - 不要把问题只从 posterior error 来定义

### Slide 8

- 英文标题建议：
  `The study asks three linked questions`
- 中文核心信息：
  - `RQ1`
    - AI-labeled summary 是否降低额外搜索停止阈值？
  - `RQ2`
    - 搜索减少是理性信息压缩，还是有害的信息获取偏离？
  - `RQ3`
    - 主观信息掌握感与客观判断质量是否发生错配？
  - 三个问题必须呈现递进关系：行为变化 → 规范评价 → 元认知校准。
- 对应基准稿位置/内容来源：
  - 基准稿“三、研究问题”全部
- 需要避免的旧口径错误：
  - 不要沿用旧 proposal 的宽泛问题
  - 不要让三个 RQ 彼此并列、没有递进

### Slide 9

- 英文标题建议：
  `A 3 x 2 design separates content, label, and representativeness`
- 中文核心信息：
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
- 需要避免的旧口径错误：
  - 不要提前展开统计策略
  - 不要把设计结构和识别策略混在一页里

### Slide 10

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

### Slide 11

- 英文标题建议：
  `A controlled evidence pool makes Bayesian benchmarks computable`
- 中文核心信息：
  - 公司风险判断任务
  - 固定证据库
  - 每条证据有明确方向和 likelihood ratio
  - 被试报告 posterior probability
  - 研究者因此可以将“看到了哪些证据”与“应当更新到什么程度”对齐
- 对应基准稿位置/内容来源：
  - 基准稿“4.2 实验任务”
  - 基准稿“4.3 证据库与数据生成过程”
- 需要避免的旧口径错误：
  - 不要把任务讲成开放文本世界
  - 必须强调 `controlled evidence pool`

### Slide 12

- 英文标题建议：
  `Bayesian updating provides the normative reference point`
- 中文核心信息：
  - 放核心公式：
    - `logit(posterior) = logit(prior) + sum log(LR_j)`
  - 这一页要强调：
    - 本文不只看点击了多少证据
    - 更看最终后验是否接近规范贝叶斯基准
- 对应基准稿位置/内容来源：
  - 基准稿“2.4 贝叶斯信念更新与后验判断质量”
  - 基准稿“4.7 贝叶斯后验计算”
- 需要避免的旧口径错误：
  - 不要做成纯 technical dump
  - 不要让公式脱离 normative benchmark 的解释

### Slide 13

- 英文标题建议：
  `Two deviation measures distinguish “searching less” from “updating worse”`
- 中文核心信息：
  - `Conditional Bayesian deviation`
    - 用户是否正确吸收了自己实际看到的信息？
  - `Full-information deviation`
    - 最终判断距离完整证据基准有多远？
  - 这两个指标一起区分：
    - 看得少但更新准
    - 看得多但更新差
    - 看得少且信息不足
  - 如果后面要谨慎提到 `double Bayesian distortion`，只能放在这里或预期结果部分，把它作为可能出现的 combined deviation pattern，而不是前置理论框架。
- 对应基准稿位置/内容来源：
  - 基准稿“2.4 贝叶斯信念更新与后验判断质量”
  - 基准稿“4.6 核心变量与操作化”
  - 基准稿“4.7 贝叶斯后验计算”
- 需要避免的旧口径错误：
  - 不要把 deviation 简化成 generic judgment error
  - 不要把 `double Bayesian distortion` 再抬回主标题或总框架

### Slide 14

- 英文标题建议：
  `AI may improve information access while weakening epistemic ownership`
- 中文核心信息：
  - 自主搜索者可能：
    - 查阅更多
    - subjective mastery 更高
    - 但未必更准确
  - AI summary 使用者可能：
    - posterior 更接近规范基准
    - 但 `epistemic ownership` 与 perceived information acquisition 更低
  - 这一页要把主观—客观信息校准错配讲清楚。
- 对应基准稿位置/内容来源：
  - 基准稿“研究背景”关于反直觉现象的段落
  - 基准稿“2.5 主观信心、信息掌握感与校准错配”
  - 基准稿“4.8 主观—客观校准指标”
- 需要避免的旧口径错误：
  - 不要把 ownership 误写成 responsibility / blame
  - 这里讨论的是知识掌握感，不是责任归属

### Slide 15

- 英文标题建议：
  `Expected patterns separate efficient compression from harmful under-search`
- 中文核心信息：
  - 在 `representative summary` 条件下：
    - search less
    - but no worse full-information performance
    - 说明可能是 efficient compression
  - 在 `incomplete summary` 条件下：
    - search less
    - and larger full-information deviation
    - 说明可能是 harmful under-search
  - 同时可能出现：
    - objective performance 较好
    - subjective mastery 较低
    - 即 information calibration mismatch
- 对应基准稿位置/内容来源：
  - 基准稿“4.9 统计分析策略”
  - 基准稿“4.10 预期结果模式”
- 需要避免的旧口径错误：
  - 不要把预期结果直接命名为 `Double Bayesian Distortion`
  - 结果模式必须保持待检验语气

## 与旧口径切割说明

- 不再使用 `Double Bayesian Distortion / 双重贝叶斯偏离` 作为第一篇标题或开篇理论框架。
- 旧的 `defense_project/latex` 中仍含有旧标题、旧表述和旧的 Study 1/2/3 结构，不能直接作为 PPT 主线。
- 旧文件
  `E:\Info_AI\主Agent\答辩材料\Paper1_Double_Bayesian_Distortion_PPT_中文审查大纲.md`
  不应继续作为正式大纲。

## 下一步建议

- 若用户认可这版 15 页结构，再进入英文可视化版 PPT 制作。
- 后续做英文 PPT 时，三张最关键的识别页应优先保证清晰：
  - Slide 2：搜索引擎 vs AI assistant
  - Slide 10：same-summary source-label design
  - Slide 13：two deviation measures
