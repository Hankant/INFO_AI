# 第二篇：AI 授权 / EWA / 重复反馈依赖校准

## 当前项目基准

- 2026-07-04 起，第二篇当前项目内基准文件为：
  `E:\Info_AI\outputs\真实多Agent重做版\final\02_研究计划_当前基准版_2026-07-04.pdf`
- 该文件来自用户修订后的正式 PDF 版本。
- 若本 README 中较早的重构建议与该 PDF 存在冲突，应以该 PDF 为准。

## 文章身份

这是第二篇或后续研究，不是第一篇。

## 当前判断

- 旧的 `repeated strategic belief task + beauty contest + repeated decision game` 版本存在结构性问题，默认不再作为基准设计。
- 第二篇真正要研究的不是“人是否会做高阶博弈推理”，而是“人在重复反馈中如何更新对 AI 的依赖与授权”。
- 因此，任务层应尽量从策略博弈中抽离，改为更干净的 repeated forecasting / judgment / social prediction with AI advice。

## 当前建议题目

**Early AI Errors and Persistent Under-Reliance in Repeated Forecasting with Feedback**

中文可写为：

**早期 AI 错误与重复反馈预测任务中的持续性低依赖**

## 核心问题

在重复反馈任务中，即使 AI 与 human source 在 20 轮窗口内总体表现等价，早期 AI 错误是否仍会引发更强、更持久的后续低依赖 / 低授权？

## 用户偏好的 gap

1. AI 错误与人类错误的不对称性。
2. 多轮反馈中的学习，而不是单轮 trust / advice adoption / calibration。

## 当前保留的核心设计

- 20 轮左右的有限重复窗口
- AI Early Error / Human Early Error / AI Late Error / AI Distributed Error
- AI 与 human source 的 performance parity
- reduced-form dynamic analysis 作为主证据
- simplified EWA / source-specific learning 作为机制检验

## 当前应放弃的旧设计

- beauty contest 作为默认任务骨架
- repeated strategic belief task / repeated decision game 的主 framing
- 把研究问题表述为高阶信念博弈学习
- 同时并列五种复杂协作架构，导致角色、控制权和任务理解混在一起

## 推荐任务方向

优先顺序：

1. repeated forecasting task
2. repeated judgment task
3. repeated social prediction task

优先理由：

- 这些任务足以识别 reliance updating，不需要额外引入博弈学习噪音。
- 更容易控制 task difficulty 与 AI/human 表现等价。
- 更适合把理论贡献收紧为 dynamic under-reliance / asymmetric updating。

## 机制表述口径

- 不再默认使用完整博弈 EWA。
- 更稳妥的写法是：
  `experience-weighted reliance updating` 或 `source-specific learning model`
- 核心机制句式应是：
  `early AI errors receive greater negative updating weight than comparable human-source errors`

## 写作禁区

- 不要写成金融学、行为金融学、投资决策或金融市场研究。
- 不要再默认把 beauty contest 说成“可控高阶信念任务”，除非用户明确要保留该方向。
- 不要过度强调责任和高责任治理流程。
- 不要把 20 轮窗口写成“长期锁定”或“长期稳态”。

## 主要材料入口

- `E:\Info_AI\outputs\真实多Agent重做版`
- `E:\Info_AI\outputs\研究计划执行产出`
- 当前用户修订后的项目内基准文件：
  `E:\Info_AI\outputs\真实多Agent重做版\final\02_研究计划_当前基准版_2026-07-04.pdf`
- 此前用户退回的旧基准附件：
  `C:\Users\69596\.codex\attachments\90d4f461-ff0f-4214-a96b-05861a460641\pasted-text.txt`

## 材料使用边界

- 上述材料主要用于回收可保留组件，不作为直接续写底稿。
- 可回收组件：
  early/late/distributed error、performance parity、reduced-form、简化 EWA
- 需整体重写组件：
  beauty contest、strategic belief framing、复杂协作架构设计

## 明确退回

- 除非用户明确要求，不要继续沿用：
  `E:\Info_AI\outputs\真实多Agent重做版\final\04_研究计划_20轮策略信念任务打磨版.md`
