# 共享文献库入口说明

本目录只是主 Agent 视角下的共享文献库入口说明。共享文献库有单独的文献库 agent 负责更新和维护，主 Agent 不接管日常文献入库、引用核查、PDF 下载或知识图谱重建。

## 文献入库 Agent 状态

- 该 Agent 是已经实际执行过任务的专项职责，不只是未来规划。
- 项目未保存统一 Agent ID；应按职责识别，而不是与历史 `Agent A / Lovelace` 混淆。
- 2026-06-29：完成 Self vs AI 等文献批次、健康报告、链接核查和部分 PDF 归档。
- 2026-07-06：完成 accountability / AI delegation 11 条核验与 Bib 入库，并重建知识图谱。详见 `defense_project/reference_materials/batch_2026-07-06_summary.md`。
- 2026-07-21：另有 5 篇行为经济学文献下载到 `behavioral_economics_belief_search_literature/pdf/`，但尚未完成正式并库记录。

当前待办：由文献入库 Agent 核验并合并 2026-07-21 候选批次，处理 `references_new.bib`、`references_2026-07-06_batch.bib` 与主 `references.bib` 的关系，并更新知识图谱。

## 当前主要位置

- `E:\Info_AI\defense_project\reference_materials`
- `E:\Info_AI\defense_project\latex\references.bib`
- `E:\Info_AI\references_new.bib`

## 使用原则

三篇文章应尽量共享一个文献库，这样可以看到引用文献之间的关系，也方便后续做知识图谱、答辩材料和理论整合。

不要让三篇文章各自形成互不相通的文献库。

主 Agent 的作用是：

- 记住共享文献库的位置。
- 在三篇文章写作、讲稿、答辩和评审中引用同一套文献入口。
- 记录某篇文章可能需要补充哪些文献方向。
- 避免因为长期对话导致文献入口、文章映射或基准版本丢失。

主 Agent 不负责：

- 新文献入库。
- `references.bib` 日常维护。
- citation checker 运行。
- PDF 收集和归档。
- 知识图谱更新。

## 主要文献方向

### 1. 算法权威与信息校准

- Bayesian updating
- information acquisition
- rational inattention
- information design
- non-Bayesian persuasion
- generative AI summary
- perceived signal structure
- epistemic ownership

### 2. 分离 / 来源标签 / 人机区分

- same-summary source-label design
- AI label effect
- self vs AI
- algorithmic authority
- algorithmic trust
- human vs AI source effect

### 3. EWA / 重复学习

- EWA
- reinforcement learning
- belief learning
- repeated games
- beauty contest
- delegation learning
- asymmetric learning

### 4. AIA 责任归因

该方向待补。

- responsibility attribution
- AI agency
- moral agency
- blame
- accountability
- control
- intentionality
- responsibility gap

## 给文献库 agent 的任务提示

如果后续需要更新文献库，主 Agent 应只生成清晰任务说明，例如：

- 哪篇文章需要补文献。
- 需要补哪个理论方向或机制方向。
- 这些文献预计服务哪一段论证。
- 是否可能同时连接多篇文章。

然后由专门的文献库 agent 执行入库、核查和知识图谱更新。
