# LaTeX 正式稿统一目录

本目录保存三篇当前英文研究计划的独立 LaTeX 源文件。2026-08-30 的本轮修订重点是压缩结构、删除重复说明，并将长句改为较短的学术表达。历史中文稿、共享文献库和旧 PDF 均未改动。

## 当前文件

| 论文 | 当前源码 | 本轮结构处理 |
| --- | --- | --- |
| Paper 1 | [群体信息获取与意见形成](Paper1_AI_Group_Information_Acquisition_and_Opinion_Formation_Formal_RP_EN.tex) | 主体重组为 Introduction、Theory、Research Design、Analysis、Expected Contribution 五部分。删除内部概念检查表、厂商说明、独立的 Falsification/Scope 章节及重复验证说明。 |
| Paper 2 | [Asymmetric Error Tolerance](Paper2_Asymmetric_Error_Tolerance_English_Research_Proposal_2026-08-27.tex) | 保留原有七部分主体顺序和核心模型。仅压缩重复定义、解释性清单、远端政策延伸及独立的可行性、限制和伦理章节。 |
| Paper 3 | [AI 决策代理、冲突升级与责任归因](Paper3_AI_Decision_Agents_Conflict_Escalation_and_Responsibility_Attribution_Formal_RP_EN_2026-08-30.tex) | 重新组织为 Introduction、Theory、Study 1、Study 2、Expected Contribution 五部分。研究问题、责任归因逻辑、两项研究及分析单位直接对应。 |

三篇均删除独立的 `Falsification and Scope Conditions` 类章节。必要的识别边界、待定设计和适用范围保留在相应理论或方法段落中。

## 保留的研究边界

- **Paper 1**：主比较仍是传统搜索与 LLM 信息搜索。暴露、分享、意见更新和群体分布保持分离。独立模型路由仍以 SQ2 出现稳定结果为前提。共享人工简报继续用于检验共同信息解释。
- **Paper 2**：`alpha` 仍表示相对于总体 Human 基准的行为阈值偏离。客观准确率、准确率知觉、个体能力、信心、选择和 perceived trustworthiness 没有合并。两阶段样本关系、stakes 分配及未披露条件的阈值恢复仍待预试。
- **Paper 3**：最终行为与事后责任评分仍由两项研究分别检验。C0 只评人类，C1 和 Study 2 分别评人类与 AI。缺失的 AI 评分不置零。Study 2 不解释 Study 1 的中介机制。

## 统一格式与引用

三篇采用 A4、11pt、2.35cm 页边距，并统一封面、标题层级、页眉页码、摘要和关键词。引用采用 natbib 作者—年份格式。每篇源码含独立参考文献表，不依赖外部 `.bib` 文件。

## 本轮核查

本轮只生成并检查 LaTeX 源码，没有生成 PDF。三篇均通过三轮 XeLaTeX `--no-pdf` 编译，生成 XDV 中间文件用于语法检查。最终日志没有未解析引用、未解析交叉引用、缺字、Overfull 或 Underfull 警告。

自动核查还确认：

- 正文引用键均存在于各自文献表，文献表没有未使用条目；
- 正文 `label` 与 `ref` 对应完整；
- Paper 1 保留的 12 个公式、Paper 2 保留的 23 个公式、Paper 3 保留的 2 个公式与修订前源码逐块一致；
- 三篇正文未发现 `not only ... but`、`rather than`、`instead of`、`in contrast` 等机械转折；
- 本轮没有改写共享文献库、历史工程或主 Agent 记忆。

## 旧 LaTeX 工程索引

- `defense_project/latex`
- `outputs/研究计划执行产出/latex会议包`
- `outputs/真实多Agent重做版/latex`
