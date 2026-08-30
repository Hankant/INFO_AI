# LaTeX 正式稿统一目录

本目录用于集中管理当前可独立编译、仍在使用的论文 LaTeX 正式稿。

## 当前文件

| 论文 | LaTeX 文件 | 状态 |
| --- | --- | --- |
| Paper 1 | `Paper1_AI_Group_Information_Acquisition_and_Opinion_Formation_Formal_RP_EN.tex` | 当前英文 RP 1.4；与已交付的 36 页英文 PDF 对应 |
| Paper 2 | `Paper2_Asymmetric_Error_Tolerance_English_Research_Proposal_2026-08-27.tex` | 英文研究计划版本 |
| Paper 3 | `Paper3_AI_Decision_Agents_Conflict_Escalation_and_Responsibility_Attribution_Formal_RP_EN_2026-08-30.tex` | 全英文导师汇报正式稿；已通过 XeLaTeX 编译检查 |

## 编译方式

三份正式稿均已改为 Overleaf 可移植版本，可以使用 Overleaf 默认的 pdfLaTeX，也可以使用 XeLaTeX 或 LuaLaTeX。Paper 3 源文件顶部保留 `% !TeX program = xelatex`，但不再强制依赖 XeLaTeX。

使用默认 pdfLaTeX：

```powershell
pdflatex -interaction=nonstopmode -halt-on-error <filename>.tex
pdflatex -interaction=nonstopmode -halt-on-error <filename>.tex
```

使用 XeLaTeX：

```powershell
xelatex -interaction=nonstopmode -halt-on-error <filename>.tex
xelatex -interaction=nonstopmode -halt-on-error <filename>.tex
```

连续编译两次用于更新目录和内部链接。三份正式稿均不再依赖本地安装的 Times New Roman 或 Arial；pdfLaTeX 使用 `newtx` 字体，XeLaTeX/LuaLaTeX 使用 Overleaf 自带的 TeX Gyre Termes 和 TeX Gyre Heros。

## 管理规则

1. 新生成的现行论文正式稿统一放在本目录。
2. 文件名必须包含论文编号、主题、语言或版本日期。
3. 编译产生的 `.aux`、`.log`、`.out`、`.toc` 和临时 PDF 不作为正式源文件提交到本目录。
4. 多文件旧工程继续保留原目录结构，避免破坏 `\input`、参考文献和资源依赖。

## 旧 LaTeX 工程索引

以下属于历史答辩或会议工程，不是当前独立正式稿：

- `E:\Info_AI\defense_project\latex`
- `E:\Info_AI\outputs\研究计划执行产出\latex会议包`
- `E:\Info_AI\outputs\真实多Agent重做版\latex`
