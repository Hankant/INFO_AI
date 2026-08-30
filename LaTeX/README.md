# LaTeX 正式稿统一目录

本目录保存三篇当前英文研究计划的独立 LaTeX 源文件。2026-08-30 已依据联合审查完成正文、版式与引用修订；历史中文稿、共享文献库及旧 PDF 不随之覆盖。

## 当前 LaTeX 文件

| 论文 | 当前源码 |
| --- | --- |
| Paper 1 | [群体信息获取与意见形成](Paper1_AI_Group_Information_Acquisition_and_Opinion_Formation_Formal_RP_EN.tex) |
| Paper 2 | [Asymmetric Error Tolerance](Paper2_Asymmetric_Error_Tolerance_English_Research_Proposal_2026-08-27.tex) |
| Paper 3 | [AI 决策代理、冲突升级与责任归因](Paper3_AI_Decision_Agents_Conflict_Escalation_and_Responsibility_Attribution_Formal_RP_EN_2026-08-30.tex) |

本次交付以 LaTeX 源码为准，不上传 PDF、编译中间文件或本地核查产物。

## 本轮修订与研究边界

- **Paper 1**：同步传统搜索引擎与 LLM 信息搜索的主比较；共享人工简报保留为共同信息输入的替代解释检查。修正消息编号、主张集合和重复暴露定义，分开固定模型输入与经验处理效应。具体场景、样本、主结局、空消息规则和轮内调度仍待确定。
- **Paper 2**：保留自己答案与 AI 建议之间的选择任务，以及准确率披露和真实奖金条件。明确 α 相对总体 Human 基准的识别边界，区分 M/R 相关性与随机处理效应。两阶段样本关系、stakes 分配及不披露条件的阈值恢复仍需设计或预试。
- **Paper 3**：恢复 C0 仅评人类、C1/Study 2 分别评人类和 AI 的范围；缺席的 AI 评分不置零。补回 Study 1 评分分析，修正 H2 支持条件，区分两重与三重交互。Study 2 记录来源、真实奖金联系和收益位置参照仍待确定。

三篇均压缩了模板化措辞及过强结论，没有把未验证的设计写成既定结果。共享文献库和中文历史稿不在本次修订范围内。

## 统一格式

A4、11pt、2.35cm 页边距；统一封面、正文层级、页眉页码、摘要和关键词。采用 natbib 作者—年份引用及同一文献表规则；这是项目内部统一体例，并非指定期刊或严格 APA 样式。表格均有标题和交叉引用；被正文引用的核心公式编号，其余公式无编号。

## 编译方式

三篇均已在本地通过 XeLaTeX 和 pdfLaTeX 各三轮编译。未在 Overleaf 网页或 LuaLaTeX 中执行本轮验证；无需已有 PDF 即可编译源码。

```powershell
xelatex -interaction=nonstopmode -halt-on-error <filename>.tex
xelatex -interaction=nonstopmode -halt-on-error <filename>.tex
xelatex -interaction=nonstopmode -halt-on-error <filename>.tex
```

使用 pdfLaTeX 时将命令中的 `xelatex` 替换为 `pdflatex`。重复编译用于稳定作者—年份引用及交叉引用。pdfLaTeX 使用 newtx 字体；XeLaTeX 使用 TeX Gyre Termes 和 TeX Gyre Heros，不依赖专有字体。源码可独立使用，不依赖另一个本地 `.bib` 文件。

本轮编译检查未发现未解析引用、缺字或文字越界；Paper 1 保留两处长网址的 Underfull 行距松散提示，已目视核查，无裁切。Paper 2、3 最后一轮编译无警告。Paper 2、3 展示公式内容在忽略编号和空白后与修订前一致；Paper 1 的公式修改对应上述集合定义与比较条件的修正。

## 研究状态与管理规则

- 当前文件是研究计划，不表示已完成预试、伦理审批、预注册或经验验证。各篇待定设计见上文与正文。
- 以本目录源码为当前版本；不要将旧版本页数、旧 PDF 或旧项目记忆作为本次修订稿的状态说明。
- 临时 `.aux`、`.log`、`.out` 和编译 PDF 保存在 `tmp/rp_revision_20260830`，不放入本目录。
- 历史工程继续保留原结构；本轮未改写主 Agent 历史记忆。

## 旧 LaTeX 工程索引

- `defense_project/latex`
- `outputs/研究计划执行产出/latex会议包`
- `outputs/真实多Agent重做版/latex`
