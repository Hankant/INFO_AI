# 真实多 Agent 重做版

本目录是对前一轮工作的彻底重做版，区别在于：

1. 这次使用了**真实独立子 agent**并行工作。
2. 各 agent 拥有**分离的写入目录**，避免“看似分工、实际混写”。
3. 主线程只负责搭建基础骨架、收集子 agent 结果、做交叉审查与最终整合。

## 目录

1. [AgentA](E:\Info_AI\outputs\真实多Agent重做版\AgentA)
2. [AgentB](E:\Info_AI\outputs\真实多Agent重做版\AgentB)
3. [AgentC](E:\Info_AI\outputs\真实多Agent重做版\AgentC)
4. [final](E:\Info_AI\outputs\真实多Agent重做版\final)
5. [latex](E:\Info_AI\outputs\真实多Agent重做版\latex)

## 子 agent 当前职责

1. `Agent A / Lovelace`：理论监管、文献边界、答辩与抽查材料
2. `Agent B / Erdos`：实验设计、识别策略、变量体系、模型方法
3. `Agent C / Euclid`：会议表达、构想稿、图示与汇报材料

## 主线程职责

1. 维护目录结构
2. 搭建 `LaTeX + BibTeX` 工作流
3. 接收并交叉审查三位 agent 的结果
4. 在 `final` 中形成新的总整合版
