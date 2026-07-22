# Agent 职责与成果台账

更新时间：2026-07-22

## 一、当前建议保留的职责体系

项目不需要长期维持许多平级 Agent。建议收敛为“1 个主控 + 4 类专项职责”，按任务临时启用。

| 角色 | 是否常驻 | 负责 | 不负责 | 写入边界 |
| --- | --- | --- | --- | --- |
| 主 Agent | 是 | 项目映射、基准版本、任务分派、跨文章一致性、最终整合 | 日常文献入库、替第三篇擅自定题 | `主Agent/` 的索引与总控文件；最终整合入口 |
| 文章主写 Agent | 按篇启用 | 对应文章的论证、研究设计和正文 | 修改其他文章、另建孤立文献库 | `主Agent/文章项目/0X_*` |
| 文献库 Agent | 按需启用 | 文献检索、核验、入库、BibTeX、PDF 归档、知识图谱 | 决定文章主张或替主写 Agent 改稿 | `defense_project/reference_materials`、共享 Bib |
| 方法审查 Agent | 按需启用 | 实验识别、变量、模型、替代解释、预实验方案 | 独自宣布最终理论口径 | 审查意见写入对应文章目录，不覆盖基准稿 |
| 答辩/PPT Agent | 按需启用 | 叙事结构、图示、幻灯片、讲稿与视觉检查 | 改变文章基准口径 | `主Agent/答辩材料` |

推荐协作链：`文章主写 -> 方法/文献审查 -> 主 Agent 定稿 -> PPT Agent 转译`。

## 二、历史多 Agent：已经完成，不应视为仍在工作

### Agent A / Lovelace

- 历史任务：理论监管、文献边界、研究缺口、阶段门、答辩问答、抽查标准。
- 已完成：6 份理论与监管材料，包括文献矩阵、理论边界、红线、方法/表达抽查清单、导师级问答库。
- 成果位置：`outputs/真实多Agent重做版/AgentA/`。
- 当前判断：历史审查材料；部分基于第二篇旧设计，不应直接当现行理论基准。

### Agent B / Erdos

- 历史任务：实验设计、变量体系、识别逻辑、EWA-inspired 模型、替代解释排除。
- 已完成：6 份方法材料，包括研究设计总览、实验流程、变量字典、EWA 模型、识别策略、实施建议。
- 成果位置：`outputs/真实多Agent重做版/AgentB/`。
- 当前判断：可回收 early/late/distributed error、performance parity、reduced-form 和简化 EWA；beauty contest/strategic belief 骨架已过时。

### Agent C / Euclid

- 历史任务：会议表达、摘要与 punchline、图示、汇报大纲、贡献表达。
- 已完成：5 份会议与表达材料。
- 成果位置：`outputs/真实多Agent重做版/AgentC/`。
- 当前判断：可参考表达组件；涉及旧研究设计的内容须按当前第二篇口径重写。

### 当时的主线程

- 已完成：创建分离写入目录、搭建 LaTeX/BibTeX、交叉审查、汇总 `final/`。
- 当前有效成果：第二篇基准 PDF `outputs/真实多Agent重做版/final/02_研究计划_当前基准版_2026-07-04.pdf`。
- 其余 `final` Markdown 多为被替代或被退回版本。

## 三、其他专项 Agent / 线程

### 第一篇 PPT 专项线程

- 记录的 threadId：`019f1e13-d3a6-7af2-85a0-748cb17bc1cc`。
- 原任务：参考旧英文 deck 的视觉风格，重做第一篇答辩 PPT，先做中文审查大纲。
- 已产出：多版 Paper 1 PPT、中文审查大纲、实验流程单页。
- 当前状态：应视为一次性历史专项线程。现存版本过多，需要确定唯一当前版。

### 第三篇 Agent 1

- 任务：检索并整理 Notion 中第三篇页面树、proposal、实验设计和文献入口。
- 已完成：`Notion材料地图_Agent1_2026-07-05.md`。
- 结论：Notion 已有丰富草稿，但本地尚未确认正式基准。

### 第三篇 Agent 2

- 任务：以严格导师视角审查第三篇的 RQ、理论、操控、变量与识别链。
- 已完成：`Agent2_导师视角实验设计审查_2026-07-05.md`。
- 结论：责任归因、责任结构、道德距离和不诚实行为混杂；主 RQ 尚未锁定。

### 第三篇主线程整合

- 已完成：整合 Notion 材料地图、导师审查、两张逻辑/文献工作图，并指出 role proximity 与 responsibility design 两条路线需要二选一。
- 当前状态：第三篇有材料、有审查，但没有经用户确认的正式基准设计。

### 文献库 Agent

- 身份：专门负责核验与正式入库的独立专项 Agent；不是主 Agent，也不是历史 Agent A（理论文献架构）。
- Agent ID：项目中未发现像 Lovelace/Erdos/Euclid 那样的统一执行记录，因此暂记为“身份存在、ID 未登记”。
- 负责：引用存在性核查、BibTeX 去重与写入、DOI/官方链接确认、PDF 下载与主题归档、待收集清单、引用健康报告、知识图谱重建。
- 不负责：决定论文理论主张、替文章主写 Agent 改正文、把未经核验的候选文献直接写进正式库。
- 已完成的 2026-06-29 批次：Self vs AI 等 22 篇文献整理、引用健康报告、官方链接核查、部分原始 PDF 归档。
- 已完成的 2026-07-06 批次：核验用户提供的 accountability / AI delegation 文献；11 条写入 `defense_project/latex/references.bib`；知识图谱更新到 79 条、11 类、184 个概念；该批付费墙文献未下载 PDF。
- 核心成果位置：`defense_project/reference_materials/`、`defense_project/latex/references.bib`、`defense_project/reference_materials/knowledge_graph/`。
- 2026-07-21 候选批次：`behavioral_economics_belief_search_literature/pdf/` 新收集 5 篇文献。目前仍在独立候选目录，尚未看到正式写入共享 Bib、主题目录和知识图谱的批次报告。
- 相关会话痕迹：`.claudian/sessions/conv-1784703373775-h3abvnagf.meta.json`，标题为“帮我整理一下直属库，还有关系图谱”，但未保存可用于恢复的 sessionId。
- 当前风险：新候选目录与多份 Bib 并存；后续必须继续由该职责的 Agent 完成正式并库，其他 Agent 只提交“待入库任务单”。

## 四、按文章归纳“已经做了什么”

| 项目 | 已完成 | 尚未解决 |
| --- | --- | --- |
| 总框架 | 建立 AI as Decision Architecture；明确 belief -> reliance/action -> responsibility 三段链 | 需要保持为整合框架，避免包装成成熟理论 |
| 第一篇 | 当前基准稿、文献批判靶子、英文映射、多轮 PPT 与讲稿 | 旧 Double Bayesian 口径尚未完全归档；PPT 当前版未唯一化 |
| 第二篇 | 多 Agent 理论/方法/表达包；用户修订的当前基准 PDF | 旧 strategic belief/beauty contest 材料仍与当前基准并列；需要按 repeated forecasting 重构可编辑底稿 |
| 第三篇 | Notion 材料地图、导师审查、RQ/操控图、文献目标图、多版 PPT | 用户尚未确认主轴；role proximity 与 responsibility design 尚未二选一 |
| 文献库 | 文献综述、原始 PDF、Bib、citation health、知识图谱 | 新下载文献与多 Bib 需要统一并库和去重 |
| 答辩 | 总领引言、三篇分节 PPT、组合 deck、多份审查大纲 | 版本链过长；需要指定总 deck 和每篇唯一 CURRENT 版本 |

## 五、新任务分派规则

1. 理论/正文任务：分给对应文章主写 Agent。
2. 找文献、核引用、维护 PDF/Bib：只分给文献库 Agent。
3. 实验可识别性和模型问题：分给方法审查 Agent，交付审查意见，不直接覆盖正文。
4. 做 PPT/讲稿：只在主 Agent 已登记基准后交给 PPT Agent。
5. 跨文章冲突、版本冲突、是否定稿：由主 Agent裁决并更新台账。
