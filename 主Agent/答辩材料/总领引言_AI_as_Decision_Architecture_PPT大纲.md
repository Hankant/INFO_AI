# 总领引言 PPT 大纲：AI as Decision Architecture

本文件用于放在三篇文章 PPT 最前面，承担博士课题总开场功能。目标不是介绍某一篇文章，而是回答委员会的上位问题：为什么这三篇能共同构成一个博士研究？为什么它们既独立又互有关联？

## 总体定位

建议总领引言单独做 7 页，放在三篇文章之前。

视觉风格可以参考旧英文 PPT：

- 深色封面；
- 米白正文页；
- 细线分区；
- 低饱和强调色；
- 多用结构图、三列表、过程链条，不堆满文字。

内容上不要直接沿用旧 PPT。旧 PPT 的美术风格可以参考，但总领引言应以当前三篇文章的上位框架为准。

## Slide 1：总标题

标题：

**AI as Decision Architecture**

副标题：

**生成式 AI 如何重构高风险人类决策中的信念、依赖与责任**

核心信息：

本博士课题不是研究 AI 是否“好用”或“可信”，而是研究 AI 如何改变高风险决策过程本身。

讲稿要点：

我把三篇论文放在一个共同框架下：AI 不只是外部工具，而是一种新的 decision architecture。它改变的不只是答案，而是信念如何形成、行动阈值如何被校准、责任如何被归属。

## Slide 2：为什么现有问题不够

标题：

**现有研究容易把 AI 当作外部工具**

页面结构：

左侧列出现有三类常见问题：

1. AI 是否提升判断准确性？
2. 人们是否信任或采纳 AI 建议？
3. AI 参与后责任应如何分配？

右侧给出本文转向：

这些问题重要，但它们仍把 AI 理解为提供信息、给出建议或引发责任争议的外部工具。本文关注更深层的问题：AI 是否重构了决策过程本身？

核心信息：

从“AI 作为工具”转向“AI 作为决策架构”。

## Slide 3：Decision Architecture 的定义

标题：

**Decision architecture 不是成熟理论，而是整合性分析框架**

页面结构：

用一行定义：

Decision architecture 描述决策环境如何安排信息流、认知负担、行动阈值、决策权和责任关系。

下方用两列对比：

| Choice architecture | AI decision architecture |
| --- | --- |
| 默认项、框定、反馈、激励 | 搜索、总结、解释、建议、确认、执行、记录、责任分配 |
| 关注选择如何被呈现 | 关注信念如何形成、行动如何触发、后果如何归属 |

核心信息：

AI 不只是改变选项呈现，而是参与证据组织、依赖校准和责任结构。

## Slide 4：三篇文章共享的过程链条

标题：

**一次AI 辅助决策可以拆成三个机制环节**

视觉：

横向链条：

```text
Belief Formation → Risk Appraisal / Reliance Calibration → Responsibility
```

下方中文问题：

```text
人相信什么？
在既有信念下，人如何校准依赖并转化为行动？
如果采取行动，后果算谁的？
```

核心信息：

三篇文章共享同一个 AI-mediated decision process，但分别识别不同因果环节。

## Slide 5：三篇文章如何对应三个机制

标题：

**三篇论文分别隔离决策链条中的不同映射**

建议表格：

| 论文 | 核心映射 | 核心机制 | 记忆点 |
| --- | --- | --- | --- |
| Paper 1 | evidence → belief | answer-first belief anchoring / 信息充分性感知与贝叶斯更新偏离 | Belief anchoring |
| Paper 2 | belief / feedback → action threshold | AI-mediated reliance calibration / early AI error as calibration shock | Calibration shock |
| Paper 3 | action → responsibility | ownership dilution / responsibility sharing | Ownership dilution |

核心信息：

统一性来自同一决策过程；独立性来自不同因果映射。

## Slide 6：为什么它们不是三个松散实验

标题：

**三篇不是同质化 AI 应用实验，而是分层识别同一决策过程**

页面结构：

左侧写“共同点”：

- 都研究高风险 AI 辅助决策；
- 都关注 AI 如何改变人类行为机制；
- 都服务 AI governance 的行为科学基础。

右侧写“差异点”：

- Paper 1：信息获取实验 + process tracing + 贝叶斯后验；
- Paper 2：repeated strategic belief task + 激励性选择 + EWA-inspired 动态模型；
- Paper 3：委托与问责实验 + ownership / accountability / credit-blame allocation。

核心信息：

三篇共享实验识别优势，但任务结构、行为数据和因变量不同。

## Slide 7：博士课题总命题与贡献

标题：

**总命题：AI 重构高风险决策，而不只是影响某个答案**

页面中心放总命题：

> AI 通过改变人们相信什么、在既有信念与反馈下如何校准依赖和行动阈值，以及如何归属行动后果，重构了高风险人类决策。

下方三点贡献：

1. 理论贡献：提出 AI as decision architecture 的行为决策框架。
2. 机制贡献：区分信息路径、依赖路径和责任路径。
3. 治理贡献：为高风险 AI 系统的设计、监督与问责提供行为基础。

结尾过渡：

接下来第一篇论文先进入这个链条的第一环节：AI 如何改变 evidence-to-belief 的映射。

## 可选 Slide 8：进入第一篇的过渡页

标题：

**第一篇：从证据到信念**

核心信息：

如果 AI 在最前端已经改变了证据如何到达决策者，那么后续的依赖与责任都建立在一个被重构过的信念基础上。

过渡句：

因此，第一篇文章首先研究生成式 AI 的 answer-first 信息结构如何改变信息搜索、贝叶斯更新和主观信息掌握感。

## 需要避免的问题

1. 不要把 decision architecture 写成一个已经成熟的既有理论。它应被表述为整合性分析框架。
2. 不要把三篇文章写成“AI trust 的三个应用”。第一篇不是 trust，第二篇也不只是 trust，第三篇不只是 blame。
3. 不要把第一篇的机制写成简单的“AI 让人少搜索”。应强调理性信息压缩与有害偏离的区分。
4. 不要让第三篇提前被固定为单纯事后 blame attribution。更准确的是 responsibility architecture，包括 decisional ownership、felt accountability、responsibility sharing 和 credit/blame allocation。
5. 不要让总开场过长。它的任务是建立博士课题统一性，而不是提前讲完三篇文章。

