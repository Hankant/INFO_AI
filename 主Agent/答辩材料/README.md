# 答辩材料

本目录用于统一规划三篇文章的答辩材料。答辩不是三篇文章孤立展示，而是一个整体研究计划，内部按三节展开。

## 推荐结构

1. 总开场：为什么三篇文章共同研究生成式 AI 对人类判断、授权和责任的影响。
2. 第一节：算法权威与信息校准。
3. 第二节：AI 授权 / EWA / 重复策略信念任务。
4. 第三节：AIA 责任归因。
5. 总结：三篇文章如何形成整体贡献。

## PPT 叙事总则

从 2026-07-05 起，每个子课题的 PPT 叙事顺序优先遵循：

1. 生活化具体例子
2. 现有研究做了什么
3. 传统理论怎么理解
4. 当前 gap 在哪里
5. 由 gap 引出研究问题 `RQ`
6. 介绍我们的 framing / analytical framing
7. 说明所依托的理论基础
8. 说明实验原型为什么合理、它要满足什么要求
9. 再进入具体实验设计
10. 最后讲预期结果与预期贡献

详细说明见：

- `E:\Info_AI\主Agent\答辩材料\PPT_叙事顺序与文献使用总则_2026-07-05.md`

默认要求：

- 不要一开始就进入技术细节。
- 技术细节只保留那些能防止误解、对识别关键的部分。
- 重点是先讲清研究问题、讲明白 gap 为什么成立且必须研究。
- 文献库优先用于支撑 `现有研究 / 传统理论 / gap`，而不是只在结尾堆 citation。

## 已有材料入口

- `E:\Info_AI\outputs\019e9e26-a704-79e1-8478-8a7f65a6f8d3\presentations\defense-project`
- `E:\Info_AI\outputs\研究计划执行产出\AgentA_监管与答辩材料`
- `E:\Info_AI\outputs\真实多Agent重做版\final`

## 第一篇已有 PPT

第一篇当前题目应为“算法权威与信息校准 / Algorithmic Authority and Information Calibration”。旧材料中曾使用“双重贝叶斯偏离 / Double Bayesian Distortion”，但这不是当前主标题。

第一篇已有一套较完整的英文答辩 PPT：

- PPTX：`E:\Info_AI\outputs\019e9e26-a704-79e1-8478-8a7f65a6f8d3\presentations\defense-project\output\algorithmic-authority-defense-deck.pptx`
- 预览总览：`E:\Info_AI\outputs\019e9e26-a704-79e1-8478-8a7f65a6f8d3\presentations\defense-project\preview\contact-sheet.png`
- 英文讲稿：`E:\Info_AI\outputs\019e9e26-a704-79e1-8478-8a7f65a6f8d3\presentations\defense-project\output\speech_script_en.md`

这套旧版共 20 页，内容包括：研究动机、认知顺序反转、文献定位、三类 calibration、研究问题、修订逻辑、same-summary source-label design、Study 1/2/3、Bayesian benchmark、贡献、治理含义、修订优点和答辩前待改问题。其美术风格可参考，但内容需要按当前“算法权威与信息校准”版本重写。

2026-07-01 另生成了一版中文压缩 PPT：

- `E:\Info_AI\主Agent\答辩材料\第一章_双重贝叶斯偏离_PPT初版.pptx`

该中文版本应视为“中文压缩草稿”，且仍带有旧标题口径，不是正式基准。后续若用户要求“第一章 PPT”，应优先确认是否按当前“算法权威与信息校准”版本重做。

正式做法应是：参考旧英文 20 页 deck 的美术风格，以 `E:\Info_AI\主Agent\文章项目\01_算法权威与信息校准\当前第一章_算法权威与信息校准_基准稿.md` 为第一内容基准，重新制作英文 PPT；中文只作为审查大纲。

## PPT 专项 Agent

2026-07-01 创建了一个专门负责 PPT 的 Codex 线程，用于重做第一篇中文答辩 PPT：

- threadId: `019f1e13-d3a6-7af2-85a0-748cb17bc1cc`
- 任务边界：参考旧英文 20 页 deck 的美术风格与版式节奏，但不直接沿用其内容。
- 内容基准：以 `E:\Info_AI\修改版本.md` 和 `defense_project/latex` 下第一篇相关章节为准。
- 当前第一步：先输出新版中文审查大纲和旧版内容差异检查，不立即生成 PPTX。
- 重要修正：第一篇当前主标题不是 Double Bayesian Distortion，而是 Algorithmic Authority and Information Calibration。

## 讲稿规则

- 每次写讲稿前，先确认当前讲的是哪一篇。
- 讲稿要能直接开口讲。
- 不要写成论文摘要。
- 不要把文献综述堆进讲稿。
- 三篇文章之间要有过渡句，说明它们共同服务于一个更大的研究主题。
