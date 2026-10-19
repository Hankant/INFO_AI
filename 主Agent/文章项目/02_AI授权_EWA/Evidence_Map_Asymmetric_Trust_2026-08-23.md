# Evidence Map: Asymmetric Trust

## 文档用途

本文件为 `RP_Asymmetric_Trust_正式稿_2026-08-23.md` 的写作证据表。正式稿以本地存档与本地全文为主要依据；网页检索仅用于核对书目信息。表中的“不能支持”用于限制正式稿的论断边界。

| ID | 本地来源 | 证据层级 | 可以支持 | 不能支持 | 在 RP 中的用途 |
|---|---|---|---|---|---|
| E1 | `AI信任核心概念_Everett等2026_原文定义与文献来源_2026-08-22.md`；本地 Everett et al. (2026) PDF | L1 全文与逐项概念档 | actual/perceived trustworthiness、attitudinal/performance trust、calibrated trust 与 trusting behaviour 的边界；信任具有系统特异性和策略性 | 不能把 objective task accuracy 等同于完整 actual trustworthiness；不能把所有来源选择称为 trusting behaviour | 概念定义、变量表、规范边界 |
| E2 | `AI信任研究背景与整体架构_讨论稿_2026-07-31.md` | L1 本地证据综述 | AI 信任元分析主要研究信任前因，未充分检验信任是否有根据；appropriate trust 文献区分 belief、intention、action | 不能证明某一具体干预必然改善校准 | 研究背景与总体缺口 |
| E3 | `AI信任与实际能力错配_现有测量方法_2026-08-01.md` | L1 本地方法综述 | 客观表现、感知表现、信任态度、依赖/选择行为应分开；现有方法可组合但不能被压成一个总信任变量 | 不能声称首次测量信任与能力错配 | 测量框架与经验识别 |
| E4 | 本地 `Dietvorst2015.pdf`；`Paper2_EWA_参考文献导航.md` | L1 全文 | 观察算法犯错后，参与者比面对人类错误更快失去信心并可能放弃总体更优的算法 | 不能支持静态、普适、跨任务的 AI 不容忍参数 | algorithm aversion 分支与负向来源效应 |
| E5 | 本地 `Logg2019.pdf`；`Paper2_EWA_参考文献导航.md` | L1 全文 | 普通参与者在部分估计和预测任务中对算法建议赋予更高权重；效应受比较对象和专业性限制 | 不能支持无条件的 AI 过度信任 | algorithm appreciation 分支与正向来源效应 |
| E6 | `07_相关研究检索与Alpha识别综述_2026-08-11.md` | L1 本地审计式综述 | 直接门槛研究、反向结果与无来源效应并存；固定来源折价、能力信念与风险斜率需要分离 | 不能声称现象或门槛测量首次出现；不能把 alpha 当成熟构念 | 文献缺口、识别边界、竞争模型 |
| E7 | 同上对 Lenskjold et al. (2023) 的全文审计 | L1 本地全文摘要 | 医疗人员报告的 AI 可接受错误率低于人类；直接证明门槛测量已有先例 | 小样本、固定顺序，不能支持普遍因果机制 | 现象证据与新颖性边界 |
| E8 | 同上对 Rebitschek et al. (2021) 的全文审计 | L1 本地全文摘要 | 代表性样本中，算法与人类专家的错误估计/容忍差异并不一致 | 不能支持稳定、单向的来源偏差 | 零效应与情境依赖证据 |
| E9 | 同上对 Shariff et al. (2021) 的全文审计 | L1 本地全文摘要 | 自动驾驶场景中，人们可能要求自动驾驶系统达到高于人类司机的安全门槛；human benchmark 是现实相关参照 | 未正交分离错误概率与后果，不能直接识别来源依赖损失权重 | human counterfactual 与部署门槛 |
| E10 | 同上对 Longoni et al. (2019) 的全文审计 | L1 本地全文摘要 | 医疗 AI 选择可由来源、准确率、价格与 uniqueness neglect 共同解释；conjoint 可分解 part-worth | 未直接识别来源 × 错误风险斜率 | 固定来源偏好与机制替代解释 |
| E11 | 同上对 Dietvorst and Bharti (2020) 的审计 | L2 摘要/本地综述 | 一般预测误差效用可能具有边际敏感度递减 | 不能把任何非线性都归因于 AI 来源 | 函数形式竞争与稳健性要求 |
| E12 | `02_概念核查与理论来源.md` | L1 本地概念审计 | Hsee (1996) 的 evaluability hypothesis 为 joint versus separate evaluation 提供理论依据 | 不保证 human benchmark 一定消除偏差 | 比较基准信息的因果预测 |
| E13 | `Asymmetric_Tolerance_评语_2026-08-23.md` | L1 用户提供的理论评语 | 单边 alpha 无法覆盖 overreliance；概率误判与错误后果权重必须区分；参数应允许双向 | 不能作为既有理论或已验证结果引用 | 从单向不容忍扩展为双向失准 |
| E14 | `AI_Human_Asymmetric_Error_Weighting_Discussion_Summary.md` | L1 用户讨论存档 | signed parameter、任务依赖、参数分布与 functional-form horse race 的研究价值 | 其中任务方向示例均为待检验，不是经验事实 | 理论扩展与反证条件 |
| E15 | `导师PPT_Asymmetric_Tolerance_想法存档_2026-08-18.md` | L1 用户提供的想法存档 | human counterfactual、采用阈值和监管含义是原模型可保留的骨架 | 导师 PPT 本身不构成理论证据；监管者更保守等命题未经验证 | 规范基准与宏观治理连接 |
| E16 | `Management_Science_AI性能与信任文献普查_2026-08-02.md` | L1 本地期刊普查 | 管理学研究已大量考察非能力线索如何改变算法采用；“更多采用”并不等同于更适当的信任或更好绩效 | 不能据采用行为反推主观信任 | 管理学定位与采用—信任边界 |

## 证据约束

1. `Asymmetric Trust` 是本文限定的新问题框架，不冒充 Everett et al.（2026）的既有信任类型。
2. `human counterfactual` 是本文采用的规范比较基准，不冒充已经验证的心理构念。
3. `tau`、`delta`、`lambda_A` 都只能称为简约参数或结构参数，不能称为心理量表或成熟理论构念。
4. Human 与 AI 的信任差异只有在任务、绩效口径、错误后果、复核条件和其他决策相关因素可比后，才可解释为来源依赖失准。
5. Human–AI 无差异不自动等于绝对校准；它只支持来源中立。绝对校准还要求信任或行为与每个来源的客观表现相称。
6. 若 AI 与 rules-based algorithm 无差异，结论只能落在算法或自动化来源效应，不能声称 AI 特异性。
