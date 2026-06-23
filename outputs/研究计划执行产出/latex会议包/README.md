# LaTeX 会议包说明

本目录用于存放可继续扩展的 `LaTeX + BibTeX` 学术写作文件，不改动原始计划文本，只服务于后续正式写作、投稿初稿和会议分享版本整理。

## 目录结构

1. [main.tex](E:\Info_AI\outputs\研究计划执行产出\latex会议包\main.tex)
2. [references.bib](E:\Info_AI\outputs\研究计划执行产出\latex会议包\references.bib)
3. [sections/01_introduction.tex](E:\Info_AI\outputs\研究计划执行产出\latex会议包\sections\01_introduction.tex)
4. [sections/02_literature_and_gap.tex](E:\Info_AI\outputs\研究计划执行产出\latex会议包\sections\02_literature_and_gap.tex)
5. [sections/03_theory_and_hypotheses.tex](E:\Info_AI\outputs\研究计划执行产出\latex会议包\sections\03_theory_and_hypotheses.tex)
6. [sections/04_research_design.tex](E:\Info_AI\outputs\研究计划执行产出\latex会议包\sections\04_research_design.tex)
7. [sections/05_expected_contributions.tex](E:\Info_AI\outputs\研究计划执行产出\latex会议包\sections\05_expected_contributions.tex)
8. [sections/06_conclusion.tex](E:\Info_AI\outputs\研究计划执行产出\latex会议包\sections\06_conclusion.tex)

## 建议用途

1. `main.tex`：整篇文稿主入口。
2. `references.bib`：统一文献数据库。
3. `sections/`：分章节独立写作，便于后续扩写和改投不同会议。

## 编译建议

建议使用 `XeLaTeX -> BibTeX -> XeLaTeX -> XeLaTeX`。

如果本地已经安装 TeX Live 或 MiKTeX，可在该目录下使用类似流程：

```text
xelatex main.tex
bibtex main
xelatex main.tex
xelatex main.tex
```

## 当前定位

这套文件不是终稿，而是**会议分享级研究构想稿**的正式写作底座。它比当前 markdown 版本更接近论文结构，但还保留了研究计划/研究设计的开放性。
