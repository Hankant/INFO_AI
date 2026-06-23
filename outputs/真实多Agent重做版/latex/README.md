# LaTeX 工作区

本目录用于存放这次真实多 agent 重做版的正式写作文件。

## 当前文件

1. [main.tex](E:\Info_AI\outputs\真实多Agent重做版\latex\main.tex)
2. [references.bib](E:\Info_AI\outputs\真实多Agent重做版\latex\references.bib)

## 说明

当前 `main.tex` 是骨架文件，等 Agent A/B/C 的结果回传后，主线程会把理论、方法、会议表达整合进去。

## 编译建议

```text
xelatex main.tex
bibtex main
xelatex main.tex
xelatex main.tex
```
