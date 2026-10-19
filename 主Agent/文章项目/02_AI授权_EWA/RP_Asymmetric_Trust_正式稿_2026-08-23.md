# Research Proposal

# Asymmetric Error Tolerance: Measuring and Explaining the Relative Weight of AI Errors

## 文档状态

- 日期：2026 年 8 月 27 日
- 状态：正式研究计划稿（Asymmetric Error Tolerance、$\alpha$ 测量与来源解释整合版）
- 研究阶段：理性比较基准、单参数 $\alpha$ 与“先测量、再解释”的两阶段路径已收束；参数恢复、稳定性和解释效度仍需通过预试验证
- 主要领域：behavioral decision research、AI adoption and trust research、management and public policy
- 目标期刊：以 *Management Science* 为主要工作目标；若最终贡献集中于行为测量与判断机制，*Organizational Behavior and Human Decision Processes*、*Journal of Behavioral Decision Making* 或 *Human Factors* 更匹配

---

## 1. 摘要

医疗 AI、自动驾驶和公共部门算法的实际部署发生在 AI 与现实 Human alternative 之间；“零错误系统”通常并不存在。现有研究同时发现了对算法的规避、欣赏和过度依赖，说明人们对 AI 错误的容忍可能低于、等于或高于对等价 Human 错误的容忍。现有指标却通常只报告某个方向上的平均采用差异或可接受错误率，难以在同一尺度上比较三种结果，也难以解释差异为什么出现。

本文以 relevant human alternative 为比较基准，用单一参数 $\alpha$ 统一测量 AI 错误相对于等价 Human 错误所获得的额外或较低行为权重。$\alpha>0$ 表示额外惩罚，$\alpha=0$ 表示来源中立，$\alpha<0$ 表示额外宽容。第一阶段使用客观概率已知的老虎机任务，在同时公开 Human 与 AI 客观正确率的条件下从选择阈值恢复 $\alpha$，并检验其稳定性与行为预测能力。第二阶段随机操纵是否同时公开双方正确率，并分别测量参与者对 Human 与 AI 正确率的判断。两类绝对判断误差之和 $M_i^{A4}$ 检验总体能力误判能否解释 $|\alpha|$；若其显著，再分解 AI 与 Human 误差分量。另以有符号的相对误差 $R_i^{A4}$ 解释 $\alpha$ 的方向，并以错误后果 $L$ 检验 Asymmetric Error Tolerance 是否随 stakes 变化。Perceived trustworthiness 另行测量，不参与正确率误差或 $\alpha$ 的计算。本文的贡献由此形成三个递进步骤：提出 $\alpha$、证明 $\alpha$ 可以从行为中测量、解释 $\alpha$ 为什么变化。

---

## 2. 研究定位

### 2.1 研究对象

研究对象是个人决策者如何评价并选择完成同一任务的 Human 与 AI 来源。Human 指现实中会被 AI 替代或补充的人类总体来源，例如人类驾驶员总体或人类医生总体；它不是参与者本人，也不预设为一个抽象的“完美专家”。AI 指在同一任务、同一目标人群和同一统计口径下具有可比较表现的 AI 系统。

分析层级首先是个人层：个人对来源绩效的判断、perceived trustworthiness 与部署选择。组织采用和公共监管是这些个人判断可能进入的制度结果，不在没有组织或监管数据时被直接当作已经观察到的制度行为。

### 2.2 论文类型

本文属于 measurement and modelling contribution with an explanatory extension。论文不以“首次发现人们更不容忍 AI”作为贡献，因为医疗、自动驾驶和算法建议研究已经直接测量过 Human–algorithm 门槛差异（Lenskjold et al., 2023; Shariff et al., 2021）。本文首先提出一个可正可负的共同参数，并检验它能否从行为中稳定恢复；随后检验参与者对 Human 与 AI 相对正确率的判断误差是否解释 $\alpha$，并考察错误后果是否改变 $\alpha$。Perceived trustworthiness 作为独立心理评价变量，用于补充判断数值能力判断是否伴随更广义的可信性评价。A1–A5 用于识别检查和替代解释。

### 2.3 一句话定位

> 本文研究人们为什么对可比的 Human 与 AI 错误表现出非对称容忍，并使用 $\alpha$ 测量这种差异的方向与程度。

### 2.4 全文的分析结构

| 层次 | 本文采用的概念 | 在研究中的作用 |
|---|---|---|
| 研究现象 | **Asymmetric Error Tolerance** | 描述可比条件下 Human 与 AI 错误对来源选择产生的不同影响 |
| 核心参数 | **Relative AI error-weighting deviation $\alpha$** | 第一阶段从选择阈值恢复；汇总相对于理性比较基准仍未解释的来源差异 |
| 核心解释路径 | **Objective task accuracy $(q_a,q_h) \rightarrow$ perceived task accuracy $(\widehat q_{a,i},\widehat q_{h,i}) \rightarrow (M_i^{A4},R_i^{A4}) \rightarrow (|\alpha|,\alpha)$** | $M_i^{A4}$ 检验总体能力误判是否解释非对称容忍的幅度；$R_i^{A4}$ 检验相对能力误判是否解释其方向 |
| 信任与情境变量 | **Perceived trustworthiness；错误后果 $L$ 与成本** | 前者检验能力判断是否伴随更广义的来源可信性评价；后者进入客观选择基准，并检验 $\alpha$ 是否随 stakes 变化 |
| 研究定位 | **Behavioral decision research 与 AI trust research 的交叉** | 前者提供选择基准与参数识别，后者提供心理构念和态度—行为边界 |

这一结构决定全文的论证顺序：先建立来源中立的理性比较基准，再用来源选择识别 $\alpha$，随后解释 $\alpha$ 为什么变化。Source choice 保持中性名称；只有在排除成本、错误后果等其他行动动机并验证其与信任态度的关系后，才讨论 trusting behaviour。

---

## 3. 现实问题：AI 应当与谁比较

AI 部署经常被描述为“AI 是否足够准确”，但真实决策还包含一个被省略的反事实：若不使用 AI，将由谁完成任务。医疗诊断中的替代来源可能是人类医生，自动驾驶中的替代来源可能是人类驾驶员，公共部门预测中的替代来源可能是人工审查流程。AI 的绝对错误率因此不足以单独决定是否部署；决策还取决于 relevant human alternative 的表现、错误后果、成本、可复核性和责任条件。

当这一比较基准被忽略时，可能出现两种镜像错误。第一，AI 客观上优于 Human，却因来源身份受到更严格要求，从而造成 under-adoption。第二，AI 客观上劣于 Human 或其不确定性更高，却因自动化权威、技术乐观或其他来源线索受到更宽松要求，从而造成 over-adoption。两种结果都不是“信任越高越好”或“信任越低越安全”能够处理的问题。

因此，本文的评价标准是：AI 的部署判断是否以现实 Human alternative 为基准，并控制所有会合理改变风险判断的条件。该标准不要求 Human 与 AI 在所有制度条件下被机械地同等对待；当错误相关性、复核、责任、可申诉性或损害分布不同时，不同门槛可能完全合理。

---

## 4. 理论背景

### 4.1 Trust calibration：规范标准

Lee and See（2004）把自动化信任的目标界定为 appropriate reliance：人在自动化适合被依赖时依赖，在不适合时拒绝或接管。Everett et al.（2026）进一步区分 actual trustworthiness、perceived trustworthiness、attitudinal trust 与 trusting behaviour，并把 calibrated trust 定义为信任程度与对象值得信任程度相称。Mehrotra et al.（2024）对 appropriate trust 研究的系统综述也强调 belief、intention 与 action 不能混用。

现有元分析进一步表明，使用者、系统与情境因素均能预测自动化或 AI 信任，但这类平均前因效应并不直接回答所形成的信任是否得到对象实际表现支持（Schaefer et al., 2016; Kaplan et al., 2023）。因此，本文以相对于现实 Human alternative 的校准作为评价标准。

这一文献为本文解释 $\alpha$ 提供心理测量基础，但不直接定义本文的核心参数。研究首先测量 Human 与 AI 错误是否获得不同的行为权重；信任变量随后用于判断这种选择差异是否伴随相应的来源评价与依赖意愿。由此，信任研究在本文中承担解释和构念验证作用，不能替代对错误容忍阈值和 $\alpha$ 的直接测量。

### 4.2 既有信任研究如何进入本文

Everett et al.（2026）的构念区分使本文可以把同一次 Human–AI 选择拆成四个不同层次。第一，$q_a,q_h$ 是客观任务表现，属于技术或绩效条件。第二，$\widehat q_{a,i},\widehat q_{h,i}$ 是参与者对正确率的数值判断，属于能力信念。第三，perceived trustworthiness、performance trust 与 attitudinal trust 是心理变量，分别对应来源是否值得信任、对其可靠性和能力的信任内容，以及在不确定情境中愿意依赖该来源的态度。第四，source choice 是可观察行为。

这些变量不能相互替代。参与者可能错误判断 AI 的正确率，也可能错误判断 Human 的正确率；即使双方正确率均被准确理解，参与者仍可能认为其中一个来源较不值得信任。参与者选择 AI 还可能源于价格、便利性或制度要求。本文因此保留 source choice 这一中性名称。第二阶段首先检验参与者对 Human 与 AI 相对正确率的判断误差是否解释 $\alpha$；perceived trustworthiness 用于补充判断数值能力判断是否伴随更广义的可信性评价。

据此，本文采用两阶段分析顺序：

$$
\underbrace{\text{Objective benchmark}+\text{Source choice}}_{\text{Stage 1}}
\longrightarrow \alpha,
$$

$$
\underbrace{\text{Objective task accuracy}}_{q_a,q_h}
\longrightarrow
\underbrace{\text{Perceived task accuracy}}_{\widehat q_{a,i},\widehat q_{h,i}}
\longrightarrow
\underbrace{M_i^{A4}
=
|\widehat q_{a,i}-q_a|
+|\widehat q_{h,i}-q_h|}_{\text{total absolute error in perceived task accuracy}}
\longrightarrow
\underbrace{|\alpha|}_{\text{magnitude of asymmetric tolerance}}.
$$

第一阶段只回答 $\alpha$ 能否从行为中测量。第二阶段分别计算参与者对 AI 与 Human 正确率的有符号判断误差 $G_{a,i}^{acc}$ 与 $G_{h,i}^{acc}$。两类绝对误差之和 $M_i^{A4}$ 表示 A4 被违反的总体程度，用于解释 $|\alpha|$；若其显著，再比较 AI 与 Human 误差分量。有符号的相对误差 $R_i^{A4}=G_{a,i}^{acc}-G_{h,i}^{acc}$ 则用于解释 $\alpha$ 的方向。$M_i^{A4}$ 与 $R_i^{A4}$ 都是为检验模型假设而构造的描述性派生变量，不是既有信任构念。Perceived trustworthiness 使用独立量表，不能与 $q_a$ 或 $q_h$ 直接相减。$L$ 与 $c_j$ 已进入客观选择基准，其中 $L$ 进一步用于检验 $\alpha$ 是否随错误后果变化。

### 4.3 Algorithm aversion、algorithm appreciation 与 automation bias：方向冲突

Dietvorst et al.（2015）发现，参与者观察算法和人类预测者犯同样错误后，会更快失去对算法的信心，并可能拒绝总体表现更好的算法。该现象是 algorithm aversion，但它首先描述特定反馈条件下的信心与选择差异，不是一条普遍的 AI 负向态度定律。

Logg et al.（2019）在六项实验中发现，普通参与者在部分估计和预测任务中对算法建议赋予的权重高于人类建议；algorithm appreciation 会因比较对象是参与者本人还是外部人类、以及参与者是否具有专业经验而变化。Automation-bias 研究则把过度依赖自动化定义为在警告信号或自动化错误存在时仍过度遵循自动化输出（Goddard et al., 2012）。

这些研究没有提供稳定的单向预测。来源效应可以表现为规避、欣赏、过度依赖或无差异，而且任务的主观性与客观性会改变算法规避的方向和大小（Castelo et al., 2019）。本文用同一个有符号参数表示这些相反方向，并对参数符号保持开放。

### 4.4 可接受错误率与最低绩效门槛：现象已被直接测量

Lenskjold et al.（2023）直接询问放射科员工对 Human 与 AI 报告的可接受错误率，发现受访者对 AI 提出的平均容错率更低。Shariff et al.（2021）发现，受访者可能要求自动驾驶汽车达到高于人类司机的安全门槛。Rebitschek et al.（2021）的德国代表性样本却没有发现算法与人类专家之间一致的错误估计或容忍差异。现有研究因此已经证明门槛问题可以测量，也同时说明来源差异并不稳定。

这些研究没有完成本文需要的三重分离：参与者可能认为 AI 的实际表现更差；可能存在与错误水平无关的固定 AI 来源折价；也可能对等价错误施加来源依赖的边际权重。Longoni et al.（2019）的医疗 AI conjoint 研究已经分解来源、准确率和价格效用，但其主要结果更接近固定自动化来源折价，并未直接识别来源与错误风险的不同斜率。只报告“AI 的可接受错误率低多少”，不能识别是哪一种过程产生了门槛差。

### 4.5 Evaluability hypothesis：human counterfactual 为什么可能有效

Hsee（1996）的 evaluability hypothesis 指出，某些属性在单独评价时缺少参照、难以解释；将备选方案放入 joint evaluation 可以改变属性的可评价性及其决策权重。对于 AI 部署，单独呈现 AI 的准确率可能无法告诉决策者该数值是否足够好；同时呈现同任务、同口径的 Human performance benchmark，则可能使绩效信息获得可解释的比较含义。

该理论只支持一个有限预测：共同展示可比较的人类基准可能把判断拉近来源中立的比较标准。它不保证所有差异都会消失，也不意味着 Human 现状天然具有规范正当性。

---

## 5. 文献缺口

现有文献已经研究过 AI 错误，也已经比较过 AI 与 Human。仍然缺少一套将测量与解释连接起来的共同框架：

1. 以现实 Human alternative 而非完美系统作为比较基准；
2. 用一个有符号参数在同一尺度上表示 excess intolerance、source-neutral error weighting 与 excess tolerance；
3. 证明该参数能够从行为阈值中恢复，并能预测来源选择；
4. 分别计算参与者对 Human 与 AI 正确率的判断误差，用绝对误差之和解释 $|\alpha|$，用有符号的相对误差解释 $\alpha$ 的方向；
5. 使用 perceived trustworthiness 检查数值能力判断是否伴随更广义的来源可信性评价，并以 A1–A5 排查风险反应和其他尚未建模的来源差异。

由此，本文以 Asymmetric Error Tolerance 为研究现象，以 $\alpha$ 为核心测量对象，以 Human 与 AI 正确率判断的总体误差幅度与相对误判方向为 A4 的主要经验检查，以错误后果为情境因素，并将 perceived trustworthiness 保留为独立的信任评价变量。

---

## 6. 核心概念与变量边界

### 6.1 Asymmetric Error Tolerance

本文将 Asymmetric Error Tolerance 定义为：在任务、客观表现指标、错误后果和相关成本具有可比性的条件下，等价 Human 错误与 AI 错误对来源选择产生不同影响。

它首先是一种行为差异，不是 Everett et al.（2026）定义的信任类型。该差异可以朝两个方向出现：参与者可能要求 AI 达到高于 Human 的绩效门槛，也可能在 AI 表现更差时仍然选择 AI。本文使用 $\alpha$ 在同一尺度上表示这种方向与大小。

Perceived trustworthiness 不用于定义或计算 $\alpha$。它用于解释：当参与者已经理解 Human 与 AI 的客观表现后，观察到的来源权重差异是否伴随不同的可信性评价。只有当感知可信性与行为权重的方向相互对应时，本文才讨论 Asymmetric Trust 的可能表现。

### 6.2 Human counterfactual

Human counterfactual 指：如果不采用 AI，在相同目标人群、任务定义、时间范围和绩效口径下实际承担该任务的人类替代来源。它是本文的规范比较基准，不是心理量表，也不是一条既有理论构念。

Human counterfactual 只有在以下条件可比时才能发挥规范作用：任务与输入分布、错误率口径、错误后果、错误相关性、复核与纠正机会、成本、责任和可申诉性。任何未被匹配的差异都可能为不同门槛提供理性解释。

### 6.3 核心变量与辅助测量

| 符号 | 建议英文名称 | 变量性质 | 准确含义 | 模型位置 |
|---|---|---|---|---|
| $q_a$ | Objective task accuracy of AI | 客观系统变量 | AI 在特定任务和规定测试条件下的客观正确率 | 外生技术条件或客观基准 |
| $q_h$ | Objective aggregate human task accuracy | 客观绩效变量 | Human 总体在相同任务、样本和评分规则下的客观正确率 | Human counterfactual 的客观基准 |
| $e_a=1-q_a$ | Objective AI error rate | 派生的客观绩效指标 | 由 AI 客观正确率推导的错误率 | 进入成本与采用模型 |
| $e_h=1-q_h$ | Objective aggregate human error rate | 派生的客观绩效指标 | 由 Human 总体客观正确率推导的错误率 | 进入成本与采用模型 |
| $\widehat q_{a,i},\widehat q_{h,i}$ | Perceived AI/human task accuracy | 主观能力信念 | 参与者认为 AI 或 Human 的任务正确率 | 直接检查 A4 |
| $G_{a,i}^{acc}=\widehat q_{a,i}-q_a$ | Signed error in perceived AI task accuracy | 主观判断与客观基准的派生变量 | 参与者对 AI 正确率的高估、低估或准确判断 | 构成 $M_{a,i}^{A4}$ 与 $R_i^{A4}$ |
| $G_{h,i}^{acc}=\widehat q_{h,i}-q_h$ | Signed error in perceived Human task accuracy | 主观判断与客观基准的派生变量 | 参与者对 Human 正确率的高估、低估或准确判断 | 构成 $M_{h,i}^{A4}$ 与 $R_i^{A4}$ |
| $M_{a,i}^{A4}=|G_{a,i}^{acc}|$ | Absolute error in perceived AI task accuracy | 判断误差幅度 | 参与者对 AI 正确率判断偏离客观值的程度 | $M_i^{A4}$ 的 AI 分量 |
| $M_{h,i}^{A4}=|G_{h,i}^{acc}|$ | Absolute error in perceived Human task accuracy | 判断误差幅度 | 参与者对 Human 正确率判断偏离客观值的程度 | $M_i^{A4}$ 的 Human 分量 |
| $M_i^{A4}=M_{a,i}^{A4}+M_{h,i}^{A4}$ | Total absolute error in perceived task accuracy | 为检验 A4 构造的描述性派生变量 | 参与者对 AI 与 Human 正确率的总体误判程度 | 第二阶段解释 $|\alpha|$ 的核心变量 |
| $R_i^{A4}=G_{a,i}^{acc}-G_{h,i}^{acc}$ | Signed relative error in perceived task accuracy | 为检验 A4 构造的方向性派生变量 | 参与者对 AI 相对 Human 的正确率优势判断，与客观差异之间的偏差 | 第二阶段解释 $\alpha$ 的方向 |
| $TW^{P}_{a,i},TW^{P}_{h,i}$ | Perceived trustworthiness of AI/human | 主观心理变量 | 参与者认为 AI 或 Human 在多大程度上具备值得信任的特征 | 检查数值能力判断是否伴随更广义的来源可信性评价 |
| $PT_{a,i},PT_{h,i}$ | Performance trust | 补充心理测量 | 对 AI 或 Human 的可靠性、能力和表现的信任 | 检查可信性评价是否主要涉及性能内容 |
| $AT_{a,i},AT_{h,i}$ | Attitudinal trust | 补充心理测量 | 在不确定情境中愿意依赖 AI 或 Human 的态度 | 检查来源评价是否转化为依赖意愿 |
| $S_{it}$ | Confidence in one’s own answer | 主观判断 | 参与者在看到 AI 建议之前，认为自己本轮答案正确的概率 | 控制个人自信以及题目层面的私人信息 |
| $Y_{it}$ | Source choice / AI adoption | 可观察行为 | 参与者最终保留自己的答案，还是采用 AI 的答案 | 识别 $e_{a,i}^{*}$ 与 $\alpha_i$ 的主要行为数据 |
| $\alpha_i$ | Relative AI error-weighting deviation | 本文提出的约化行为参数；经识别检验后才讨论结构解释 | AI 错误的相对权重为 $1+\alpha_i$；$\alpha_i$ 汇总相对于 A1–A5 理性比较基准仍未解释的来源差异 | 第一阶段的核心测量对象；第二阶段的待解释结果 |

Objective task accuracy 只是 performance-related actual trustworthiness 的指标，不能直接称为完整的 actual trustworthiness。$\widehat q$ 是数值能力信念，不等于 perceived trustworthiness；performance trust 与 attitudinal trust 也不能与正确率直接相减。$M_i^{A4}$ 表示双方正确率判断的总体误差幅度，$R_i^{A4}$ 表示相对误判方向；二者都不是 calibrated trust。Source choice 是识别 $\alpha$ 的行为数据。只有当客观收益、成本、错误后果和制度要求已被匹配或进入模型，而且 source choice 与独立测得的 attitudinal trust 相联系时，本文才进一步将其解释为 trusting behaviour。

$q_h$ 应优先由独立预试样本在相同任务、信息与评分规则下估计，随后固定为主实验中的 aggregate Human benchmark。主实验参与者实际面对的 Human 选项是其本人在未采用 AI 时作出的答案，而不是另一名 Human 生成的方案。因此，$q_h$ 提供的是同一参与者总体中的先验比较基准，不能直接代替每个参与者在每道题上的真实正确概率。研究必须在 AI 建议出现前测量 $S_{it}$，并利用参与者的练习及正式任务表现检查个人能力与总体基准之间的差异。若研究直接设定一个 Human 来源的固定正确率，则应称为 `experimentally specified Human-source accuracy`，不能写成未经预试得到的“平均参与者正确率”。

第一阶段直接恢复的 $\alpha$ 是约化行为参数：它概括实际选择相对于当前理性基准的剩余差异。这个剩余差异可能来自心理偏差，也可能来自参与者合理考虑、但研究者尚未纳入模型的来源差异。只有在 A1–A5 得到支持、替代解释得到检查、参数恢复与行为预测成立后，本文才进一步把 $\alpha$ 解释为稳定的来源依赖错误权重。

---

## 7. 研究问题

### 主研究问题

> **Why do people exhibit asymmetric error tolerance toward Human and AI errors?**

> **为什么人们对 Human 与 AI 错误表现出非对称容忍？**

### 两个递进的分析问题

**RQ1 — Measurement**  
$\alpha$ 能否从行为选择阈值中测量 Asymmetric Error Tolerance？

**RQ2 — Explanation**  
对 Human 与 AI 正确率的判断误差以及错误后果，如何解释 $\alpha$ 的幅度与方向？

RQ1 是进入 RQ2 的测量前提。若 $\alpha$ 不能从行为选择阈值中得到可靠测量，研究不能继续讨论它为什么变化。第二阶段先以 $M_i^{A4}=|\widehat q_{a,i}-q_a|+|\widehat q_{h,i}-q_h|$ 检验总体能力误判是否解释 $|\alpha|$；若其显著，再分别检验 AI 与 Human 误差分量。有符号的 $R_i^{A4}$ 检验相对能力高估或低估是否解释 $\alpha$ 的方向；随后考察错误后果是否改变 $\alpha$。Perceived trustworthiness 另行测量。

---

## 8. 理论框架

### 8.1 Notation and rational adoption rule

一个决策者（principal）在 Human agent $H$ 与 AI system $A$ 之间进行选择。首先定义两类来源的客观任务表现：

$$
q_a=\text{objective task accuracy of AI},
$$

$$
q_h=\text{objective aggregate human task accuracy}.
$$

对应的客观错误率为：

$$
e_a=1-q_a,
\qquad
e_h=1-q_h.
$$

令 $L>0$ 表示一次错误造成的客观后果（objective loss from an error），$c_h,c_a\geq0$ 分别表示部署 Human 与 AI 的成本。对于 $j\in\{h,a\}$，预期总成本为：

$$
C_j=e_jL+c_j.
$$

来源中立的理性决策者选择 AI，当且仅当：

$$
C_a<C_h,
$$

等价地：

$$
e_h-e_a>\frac{c_a-c_h}{L}.
$$

这一 rational adoption rule 是客观比较基准，不包含心理变量。$L$ 表示一次错误的客观后果，与机器学习中的 loss function 无关。

### 8.2 Model assumptions

**A1. Comparable alternatives**  
Human and AI perform the same task and are evaluated using the same performance metric. The same type of error produces the same objective consequence:

$$
L_h=L_a=L.
$$

Any other source-specific difference that rationally affects choice must be matched or explicitly represented in $c_h$ and $c_a$.

**A2. Risk neutrality**  
The principal minimizes expected total cost.

**A3. Independent errors**  
Errors are independent draws.

**A4. Costless evaluation**  
The principal observes $e_h$ and $e_a$ accurately.

**A5. Stationary environment**  
The parameters $e_h,e_a,L,c_h,c_a$ remain fixed within each decision block.

These assumptions define the rational benchmark. They are maintained conditions of the model rather than empirical hypotheses about whether $\alpha$ is positive, zero, or negative.

### 8.3 用 $\alpha$ 表示 Asymmetric Error Tolerance

在客观基准上，引入本文唯一的核心测量对象 $\alpha$。为保持模型简洁，将 Human 错误的行为权重标准化为 1，将 AI 错误的行为权重写为 $1+\alpha$：

$$
\widetilde L_h=L,
\qquad
\widetilde L_a=(1+\alpha)L,
$$

因此：

$$
\widetilde C_h=e_hL+c_h,
$$

$$
\widetilde C_a=(1+\alpha)e_aL+c_a,
\qquad \alpha\in(-1,\infty).
$$

$\widetilde L_a$ 表示选择模型中 AI 错误获得的有效行为权重；它不改变一次错误的客观后果 $L$。

AI 被选择的条件变为：

$$
e_h-e_a-\alpha e_a>\frac{c_a-c_h}{L}.
$$

$$
\begin{cases}
\alpha>0, & \text{AI errors receive greater decision weight},\\
\alpha=0, & \text{source-neutral error weighting},\\
\alpha<0, & \text{AI errors receive lower decision weight}.
\end{cases}
$$

$\alpha$ 的正值对应 excess intolerance，负值对应 excess tolerance，零值对应来源中立。本文将其命名为 `relative AI error-weighting deviation`，中文为“AI 错误相对权重偏差”。该名称只描述参数在模型中的功能；研究现象仍称为 Asymmetric Error Tolerance。$\alpha$ 不等于 trust，也不预先对应某一种心理机制。

### 8.4 从行为阈值识别 $\alpha$

令 $e_{a,i}^{*}$ 表示参与者 $i$ 仍愿意选择 AI 时可接受的最高客观 AI 错误率。在 Human 与 AI 选择无差异的阈值点：

$$
(1+\alpha_i)e_{a,i}^{*}L+c_a=e_hL+c_h.
$$

因此：

$$
\alpha_i=
\frac{e_hL+c_h-c_a}{e_{a,i}^{*}L}-1.
$$

当 $c_h=c_a$ 时：

$$
\alpha_i=\frac{e_h}{e_{a,i}^{*}}-1.
$$

这一公式使 $\alpha$ 可以由客观 Human 基准与参与者的 AI 接受阈值直接计算。第一阶段据此检验三个问题：$\alpha$ 能否从多水平选择数据中恢复；同一参与者或同一条件下是否稳定；能否预测未用于估计的来源选择。该计算不需要先把来源选择称为信任行为。

### 8.5 第二阶段：解释 $\alpha$ 为什么变化

第一阶段在同时呈现 $q_h$ 与 $q_a$、并确认参与者理解这些数值的条件下恢复 $\alpha$。这一阶段尽量满足 A4，使 $\alpha$ 接近“在已知客观绩效条件下，AI 错误相对于 Human 错误获得的额外或较低行为权重”。第二阶段随机操纵比较性正确率信息：公开组同时呈现 $q_h$ 与 $q_a$，未公开组两者均不呈现。该因素与错误后果 $L$ 交叉形成 $2\times2$ 设计。参与者在每个区块先完成若干观察轮次，再报告自己的答案与答对把握 $S_{it}$，随后看到 AI 建议并作出 source choice。研究分别测量 $\widehat q_{a,i}$ 与 $\widehat q_{h,i}$，用总体误判程度 $M_i^{A4}$ 解释 $|\widehat\alpha_i|$，用有符号的相对误差 $R_i^{A4}$ 解释 $\widehat\alpha_i$ 的方向，并检验 $L$ 是否进一步改变非对称容忍。

| 基准假设 | 现实中可能出现的问题 | 在研究中的检查方式 |
|---|---|---|
| A1 Comparable alternatives | Human 与 AI 在参与者看来仍存在会合理影响选择的差异 | 在设计中匹配客观条件，并测量参与者对错误后果、成本、复核和其他来源条件的理解 |
| A2 Risk neutrality | 参与者的选择不只取决于平均损失，尤其可能对高后果错误作出不同反应 | 以真实奖金操纵 $L$，区分 $L$ 对选择的直接作用与 $L$ 是否进一步改变 $\alpha$ |
| A3 Independent errors | 参与者可能把一次 AI 错误理解为后续错误的信号 | 明确说明抽取规则，并测量一次错误是否改变其对后续错误率的判断 |
| A4 Costless evaluation | 参与者不能准确理解 Human 与 AI 的客观正确率 | 操纵是否同时公开 $q_h$ 与 $q_a$；分别比较 $\widehat q_{a,i},\widehat q_{h,i}$ 与 $q_a,q_h$，并计算总体误判幅度与相对误判方向 |
| A5 Stationary environment | 参与者认为来源能力随轮次改变，或在固定环境中持续更新能力判断 | 在每个 decision block 内固定参数，并记录各轮能力估计和选择 |

为直接检查 A4，本文测量：

$$
\widehat q_{a,i}=\text{perceived AI task accuracy},
$$

$$
\widehat q_{h,i}=\text{perceived human task accuracy}.
$$

$\widehat q$ 与客观正确率使用同一概率量尺，用于检查参与者是否理解双方的任务表现。先分别计算：

$$
G_{a,i}^{acc}=\widehat q_{a,i}-q_a,
\qquad
G_{h,i}^{acc}=\widehat q_{h,i}-q_h.
$$

先取双方判断误差的绝对值：

$$
M_{a,i}^{A4}=|G_{a,i}^{acc}|=|\widehat q_{a,i}-q_a|,
\qquad
M_{h,i}^{A4}=|G_{h,i}^{acc}|=|\widehat q_{h,i}-q_h|.
$$

总体能力误判定义为：

$$
M_i^{A4}
=M_{a,i}^{A4}+M_{h,i}^{A4}
=|\widehat q_{a,i}-q_a|+|\widehat q_{h,i}-q_h|.
$$

$M_i^{A4}\geq0$ 表示参与者对两类来源正确率的总体误判程度。使用绝对值可避免“高估 AI、低估 Human”或其他相反误差在加总时相互抵消。若 $M_i^{A4}$ 能解释 $|\alpha|$，后续再将 $M_{a,i}^{A4}$ 与 $M_{h,i}^{A4}$ 同时进入模型，比较误判主要来自 AI 还是 Human。

为保留误判方向，另定义：

$$
R_i^{A4}
=G_{a,i}^{acc}-G_{h,i}^{acc}
=(\widehat q_{a,i}-q_a)-(\widehat q_{h,i}-q_h).
$$

$R_i^{A4}>0$ 表示参与者相对高估 AI，$R_i^{A4}<0$ 表示相对低估 AI，$R_i^{A4}=0$ 表示对双方相对正确率的判断与客观差异一致。$M_i^{A4}$ 与 $R_i^{A4}$ 均是为检查 A4 而构造的描述性派生变量，不是既有信任构念。

第二阶段先估计随机实验条件对 $|\alpha|$ 的总体影响：

$$
|\widehat{\alpha}_i|
=
\delta_0
+\delta_1N_i^{Info}
+\delta_2L_i^{High}
+\delta_3(N_i^{Info}\times L_i^{High})
+u_i,
$$

其中，$N_i^{Info}=1$ 表示 Human 与 AI 客观正确率均不向参与者公开，$L_i^{High}=1$ 表示高赌注条件。平行的有符号 $\widehat\alpha_i$ 模型用于判断实验条件将容忍推向额外宽容还是额外不宽容。随后使用能力判断误差与个人自信解释非对称容忍的幅度：

$$
|\widehat{\alpha}_i|
=
\gamma_0
+\gamma_1M_i^{A4}
+\gamma_2L_i
+\gamma_3(M_i^{A4}\times L_i)
+\gamma_4\overline S_i
+\varepsilon_i.
$$

$|\widehat{\alpha}_i|$ 是个体非对称容忍的幅度；$M_i^{A4}$ 检验总体能力误判是否解释该幅度；$L_i$ 检验在其对预期成本和选择的直接作用已经进入第一阶段模型后，错误后果是否进一步改变非对称容忍；$\overline S_i$ 用于控制个人自信与题目层面的私人信息。该幅度模型不预设 $\gamma_1$ 的必然方向。

若 $M_i^{A4}$ 与 $|\widehat\alpha_i|$ 显著对应，进一步估计分量模型：

$$
|\widehat\alpha_i|
=
\kappa_0
+\kappa_aM_{a,i}^{A4}
+\kappa_hM_{h,i}^{A4}
+\kappa_2L_i
+\kappa_3\overline S_i
+\nu_i.
$$

$\kappa_a$ 与 $\kappa_h$ 分别表示 AI 正确率判断误差与 Human 正确率判断误差同非对称容忍幅度的关联。两者的大小比较必须使用标准化变量或联合系数检验，不能只比较未标准化系数。

非对称容忍的方向另用有符号模型检验：

$$
\widehat\alpha_i
=
\theta_0
+\theta_1R_i^{A4}
+\theta_2L_i
+\theta_3(R_i^{A4}\times L_i)
+\theta_4\overline S_i
+\xi_i.
$$

按上述符号定义，相对高估 AI 通常对应更低的 $\alpha$，因此预期 $\theta_1<0$；该方向性预测只属于 $R_i^{A4}$ 模型，不属于 $M_i^{A4}$ 幅度模型。

该模型把第一阶段的约化参数进一步分解。$M_i^{A4}$ 解释非对称容忍的幅度，$M_{a,i}^{A4}$ 与 $M_{h,i}^{A4}$ 识别误判来源，$R_i^{A4}$ 解释方向。如果能力误判充分解释 $|\widehat\alpha_i|$ 及其方向，观察到的 Asymmetric Error Tolerance 主要来自 A4 的违反；如果控制这些指标后 $\widehat\alpha_i$ 仍稳定偏离零，则能力误判不足以解释全部来源差异，仍需继续检查 A1、A2、A3 与 A5。

Perceived trustworthiness $TW_{a,i}^{P},TW_{h,i}^{P}$ 继续单独测量。它回答参与者认为某一来源在多大程度上具备值得信任的特征，范围宽于正确率，因此不能与 $q_a$ 或 $q_h$ 直接相减，也不参与 $M_i^{A4}$、$R_i^{A4}$ 或 $\alpha$ 的计算。它的作用是检验：数值能力判断和行为上的非对称容忍，是否伴随方向一致的来源可信性评价。

Performance trust 与 attitudinal trust 作为补充测量进入构念验证。Performance trust 检查可信性评价是否具体涉及可靠性、能力和表现；attitudinal trust 检查参与者是否愿意在不确定情境中依赖该来源。二者都不参与 $\alpha$ 的计算。若 attitudinal trust 与 source choice 在控制 $L$、$c_h$、$c_a$ 及其他行动约束后仍然对应，source choice 才获得被解释为 trusting behaviour 的证据；若二者分离，本文只报告来源选择和错误容忍差异。

第二阶段的解释顺序为：

1. **双方能力判断**：分别比较 $\widehat q_{a,i}$ 与 $q_a$、$\widehat q_{h,i}$ 与 $q_h$，并记录参与者对自己答案的把握 $S_{it}$；
2. **A4 的总体违反**：$M_i^{A4}$ 是否解释 $|\alpha|$；若显著，再分解 $M_{a,i}^{A4}$ 与 $M_{h,i}^{A4}$；
3. **A4 的方向性违反**：$R_i^{A4}$ 是否解释 $\alpha$ 的正负方向；
4. **情境因素**：$L$ 是否只按基准模型改变选择，还是进一步改变 $\alpha$；
5. **信任与替代解释**：perceived trustworthiness 是否与能力判断及 $\alpha$ 的方向相对应，以及错误相关性、复核、责任等未匹配条件是否仍能解释 $\alpha$。

因此，$\alpha$ 可以统一承接心理变量和非心理变量的解释，但不能把所有这些因素统一命名为“不理性”。在替代解释尚未排除时，$\alpha$ 只表示当前模型未解释的来源差异。

$\alpha=0$ 只表示对等价 Human 与 AI 错误使用来源中立的决策权重，不单独证明完整的 calibrated trust。当 AI 的客观预期成本低于 Human 却因 $\alpha>0$ 被拒绝时，可形成 under-adoption；当 AI 的客观预期成本高于 Human 却因 $\alpha<0$ 被选择时，可形成 over-adoption。

### 8.6 监管延伸的证据边界

相同逻辑可以映射到最低部署绩效或最高可接受错误率：$\alpha>0$ 可能产生过严的 AI 门槛，$\alpha<0$ 可能产生过宽的 AI 门槛。若数据来自一般公众，结论限于 deployment threshold 或 regulatory preference；只有实际监管者、正式规则或制度数据才能支持关于 regulation 本身的经验结论。

---

## 9. 参数结果与解释路径

本文不把 algorithm aversion 设为默认方向。第一阶段判断 $\alpha$ 的符号并检验其可测量性；第二阶段再检验其偏离零的来源。

### 9.1 方向性竞争

**CP0 — Source-neutral evaluation**  
在客观任务表现、错误后果和部署成本匹配后，$\alpha=0$。Human 与 AI 的行为差异由客观条件解释。

**CP1 — Excess intolerance**  
在可比条件下，$\alpha>0$。AI 错误获得高于等价 Human 错误的决策权重，并可能导致 under-adoption。

**CP2 — Excess tolerance**  
在可比条件下，$\alpha<0$。AI 错误获得低于等价 Human 错误的决策权重，并可能导致 over-adoption。

### 9.2 A4 检查与 $\alpha$ 的结构解释

**Violation of A4**  
若 $\widehat q_{a,i}$ 或 $\widehat q_{h,i}$ 明显偏离客观值，则 costless evaluation 未得到支持。$M_i^{A4}>0$ 表示至少一类来源的正确率被误判；$R_i^{A4}\neq0$ 表示对 Human–AI 相对能力的判断偏离客观差异。此时仍可计算描述性的 $\alpha$，但不能把它偏离零全部归因于来源身份。

**Residual source difference**  
若 A4 得到支持且 $\alpha$ 仍稳定偏离零，则能力误判不足以解释行为差异。此时仍需继续检查 A1、A2、A3 与 A5；只有这些替代解释也不能解释结果时，才把剩余差异进一步解释为稳定的来源依赖错误权重。

### 9.3 参数恢复与行为意义

老虎机任务提供已知且可重复的客观概率，使本文能够区分“公式上可以计算”与“参数在行为中可以识别”。$\alpha$ 获得行为意义至少需要满足：它能够从多水平选择阈值中恢复；同一条件下具有可接受的稳定性；能够预测未用于估计的后续来源选择；并且其结果不能被参与者对客观概率的误解完全解释。

只有在这些条件得到支持后，本文才把 $\alpha$ 从描述性的阈值差异进一步解释为候选结构参数。

### 9.4 A4 判断误差、信任评价与情境因素

本文的核心解释路径是 objective task accuracy $\rightarrow$ perceived task accuracy $\rightarrow (M_i^{A4},R_i^{A4})\rightarrow(|\alpha|,\alpha)$。$M_i^{A4}$ 表示双方能力误判的总体程度，$R_i^{A4}$ 表示相对误判方向。Perceived trustworthiness 不处在这两条公式中；它用于检验能力判断与行为参数是否伴随更广义的来源可信性评价。

$L$ 承担情境因素的作用。$L$ 表示一次错误的客观后果，$c_h,c_a$ 表示来源成本。$L$ 或成本变化会先按照 rational adoption rule 直接改变选择。只有在控制该直接作用后，不同 $L$ 条件下恢复的 $\alpha$ 仍有差异，才能说明错误后果改变了 Asymmetric Error Tolerance。

因此，本文把可能结果分为三类。第一，$M_i^{A4}$ 与 $|\alpha|$ 显著对应，说明总体能力误判解释了非对称容忍的幅度；随后比较 $M_{a,i}^{A4}$ 与 $M_{h,i}^{A4}$，判断误判主要来自哪一类来源。第二，$M_i^{A4}\approx0$，但 $\alpha$ 与 perceived trustworthiness 对应，说明数值绩效已经得到理解，来源可信性评价仍可能解释非对称容忍。第三，能力判断与 perceived trustworthiness 均不能解释 $\alpha$，而 $\alpha$ 随 $L$ 或其他条件变化，说明需要从情境因素或其他尚未建模的来源差异解释。

### 9.5 比较基准预测

依据 evaluability hypothesis，joint evaluation 中同时展示同任务、同口径的 Human 与 AI 正确率，应当提高绩效证据的可评价性。因此，本文提出：

> 与不公开双方正确率相比，同时公开可比较的 Human 与 AI 正确率将减小 $|\alpha|$。

该预测关注 $\alpha$ 与零点的距离，不预设干预只会提高 AI 信任。若原本存在 excess intolerance，基准可能改善对 AI 的相对评价；若原本存在 excess tolerance，基准也可能降低对 AI 的相对评价。

---

## 10. 经验研究框架

### 10.1 总体设计原则

本文保留抽象老虎机任务，但不再要求参与者在三个通道之间进行连续资源分配。每个决策区块包含三个老虎机。后台控制各老虎机的客观中奖概率，并在实验开始前按该概率生成完整结果序列，因此研究者知道每一轮的实际结果，参与者只看到已经发生的结果。

每个区块由两部分组成。第一部分为四至五轮观察或练习：参与者根据老虎机的历史结果寻找规律并作出练习判断；AI 同时给出建议，随后显示该轮结果。第二部分为一轮影响真实实验奖金的正式下注：参与者先独立判断下一轮哪个老虎机会中奖，并报告自己答对的把握 $S_{it}$；系统随后显示 AI 的建议；参与者最终选择保留自己的答案或采用 AI 的答案。正式下注的正确或错误真实增加或减少实验奖金，使错误后果 $L$ 成为有实际支付含义的变量，而不是文字情境。

Human benchmark $q_h$ 由独立预试样本在相同任务、信息和评分规则下估计，主实验中表述为“此前参与者在该任务中的平均正确率”。它是一项总体比较信息，不对应另一名 Human 提供的分配方案。AI 客观正确率 $q_a$ 由研究者控制，并通过预先生成的 AI 建议序列实现。为了识别接受阈值，主实验设置多个相互独立的决策区块，并在区块之间改变 $q_a$；单次正式下注只能产生一次 source choice，不能单独恢复个体 $\alpha$。

第一阶段在低赌注条件下同时公开 $q_h$ 与 $q_a$，并设置理解检查，使 A4 尽可能成立，随后从多个 $q_a$ 水平下的选择阈值恢复 $\alpha_i$。第二阶段操纵比较性正确率信息：公开组同时告知 $q_h$ 与 $q_a$，未公开组两者均不告知；该因素与错误后果 $L$ 交叉。该设计依次回答：$\alpha$ 能否从行为中测量；对 Human 或 AI 能力的误判是否解释 $|\alpha|$ 及其方向；高赌注是否进一步改变 $\alpha$。

双方正确率信息一旦向参与者公开，之后便无法对同一来源恢复为“未知”。因此，比较性正确率信息原则上采用组间随机分配。高、低赌注可以组间操纵，也可以在参与者内交叉出现；若采用组内操纵，顺序必须随机或平衡。

### 10.2 核心操纵与测量

核心实验采用比较性正确率信息与赌注大小的 $2\times2$ 设计。公开组同时显示真实的 Human 平均正确率 $q_h$ 与 AI 客观正确率 $q_a$；未公开组两者均不显示。

| 条件 | Human 平均正确率 $q_h$ | AI 客观正确率 $q_a$ | 错误后果 $L$ | 识别作用 |
|---|---|---|---|---|
| Control | 告知 | 告知 | 低 | 双方绩效信息明确时的 $\alpha$ 基准 |
| T1：双方正确率均不公开 | 不告知 | 不告知 | 低 | 检验对 Human 或 AI 能力的误判是否改变 $\alpha$ |
| T2：高赌注 | 告知 | 告知 | 高 | 检验错误后果提高是否改变 $\alpha$ |
| T3：双方正确率均不公开且高赌注 | 不告知 | 不告知 | 高 | 检验能力误判与高赌注的联合作用 |

除两项实验操纵外，四组使用相同的老虎机概率、结果序列、AI 客观正确率水平、题目顺序规则和奖金计算方式。不得向参与者提供虚假的 Human 或 AI 正确率；信息条件只改变真实数字是否公开。各组仍需在区块间设置多个 AI 正确率水平，以恢复 $e_{a,i}^{*}$，而不是把“是否选择一次 AI”直接当作 $\alpha$。

| 当前变量 | 准确名称 | 经验测量 | 模型位置 |
|---|---|---|---|
| $q_h$ | Objective aggregate human task accuracy | 独立预试参与者在相同任务中的平均正确率 | Human 客观比较基准；仅在公开条件告知参与者 |
| $q_a$ | Objective AI task accuracy | 研究者控制 AI 在规定测试条件下的正确比例 | AI 客观表现；在不同区块中改变 |
| $\widehat q_{h,i}$ | Perceived human task accuracy | 参与者报告其记得或认为的 Human 正确率 | Human 能力判断；构成 $M_i^{A4}$ 与 $R_i^{A4}$ |
| $\widehat q_{a,i}$ | Perceived AI task accuracy | 参与者报告其认为的 AI 正确率 | AI 能力判断；构成 $M_i^{A4}$ 与 $R_i^{A4}$ |
| $S_{it}$ | Confidence in one’s own answer | AI 建议出现前，参与者报告自己本轮答对的概率 | 控制个人自信与题目层面的私人信息 |
| $TW_{a,i}^{P}$ | Perceived trustworthiness of AI | 与正确率判断分开的独立量表 | 补充心理解释；不参与 $\alpha$ 计算 |
| $L$ | Objective loss from an error | 低或高赌注，并真实改变实验奖金 | 实验自变量；检查 A2 |
| $Y_{it}$ | Source choice | 保留自己的答案记为 0，采用 AI 答案记为 1 | 估计 AI 接受阈值的行为数据 |
| $e_{a,i}^{*}$ | Maximum acceptable objective AI error rate | 从多个 $q_a$ 水平下的选择转换点估计 | 计算 $\alpha_i$ 的阈值 |
| $\widehat\alpha_i$ | Estimated relative AI error-weighting deviation | 由 $e_h$ 与 $e_{a,i}^{*}$ 恢复 | 第二阶段的待解释结果 |

### 10.3 最低识别条件

1. 三个老虎机的概率和每轮结果必须由后台控制并在参与者作答前固定；不得根据参与者选择事后改变结果。
2. 正式下注必须真实影响实验奖金；高、低赌注应改变错误后果 $L$，而不是只改变文字描述。
3. AI 客观正确率必须有多个水平；单一 $q_a$ 只能产生一次选择，不能识别接受阈值与 $\alpha$。
4. $q_h$ 必须来自独立预试或明确的实验设定，并与主实验采用相同的任务和评分规则。
5. 参与者选择自己的答案还是 AI 答案，因此必须在 AI 建议出现前测量 $S_{it}$；否则个人自信可能被错误计入 $\alpha$。
6. 必须直接测量 $\widehat q_{a,i}$ 与 $\widehat q_{h,i}$；perceived trustworthiness、performance trust 或 attitudinal trust 不能替代正确率判断。
7. 四个实验条件除双方正确率是否同时公开与 $L$ 外必须保持相同。若公开条件与不公开条件使用不同结果序列，信息效应将与任务难度混在一起。
8. 四至五轮观察是当前初版设定，能否形成可测的 $\widehat q_{a,i}$ 必须通过预试验证；若判断误差主要来自样本过少，应增加观察信息，而不能把噪声直接解释为稳定偏差。
9. 若要声称 AI-specific effect，应在后续研究加入 rules-based algorithm；当前核心实验首先识别参与者自己的判断与 AI 建议之间的来源差异。

### 10.4 主要待估参数

本文只有一个核心参数 $\alpha$。控制组首先从多个 $q_a$ 水平下的 source choice 恢复 $\alpha$，报告总体平均、个体分布以及 $\alpha>0$、$\alpha\approx0$、$\alpha<0$ 的比例。随后在 T1—T3 中重新估计 $\alpha$，比较双方正确率信息与高赌注是否改变其方向和大小。平均值接近零可能表示普遍的来源中立，也可能来自正负参数相互抵消，因此不能只报告平均值。

第二阶段分别使用 $|\widehat\alpha_i|$ 与 $\widehat\alpha_i$ 为因变量。幅度模型检验双方正确率均不公开、高赌注及其交互项对 $|\alpha|$ 的影响，并以 $M_i^{A4}$ 解释总体能力误判；若显著，再比较 $M_{a,i}^{A4}$ 与 $M_{h,i}^{A4}$。方向模型以 $R_i^{A4}$ 解释 $\alpha$ 的正负方向。Perceived trustworthiness 只作为独立心理解释进入补充分析。

Perceived task accuracy、perceived trustworthiness、performance trust、attitudinal trust 与 $S_{it}$ 都不构成新的结构参数。Perceived task accuracy 用于直接检查 A4，并形成 $M_i^{A4}$、$M_{a,i}^{A4}$、$M_{h,i}^{A4}$ 与 $R_i^{A4}$；$S_{it}$ 控制参与者对自己答案的私人判断；信任变量用于解释和验证信任评价与行为参数的关系。$L$ 已进入客观基准，其中 $L$ 进一步检验 stakes 是否改变 $\alpha$。

### 10.5 反证标准

以下结果将限制或否定本文的核心主张：

- $\alpha$ 无法从多水平行为数据中稳定恢复，或不能预测未用于估计的来源选择；
- matched evidence 下 $\alpha$ 稳定接近零，说明没有可重复的来源依赖错误权重；
- $M_i^{A4}$ 与 $R_i^{A4}$ 充分解释 $|\alpha|$ 及其方向，说明观察到的差异主要来自能力误判，而不能支持独立的来源依赖错误容忍解释；
- $\alpha$ 与 perceived trustworthiness 无关，说明信任不足以解释该行为参数；
- attitudinal trust 与 source choice 在控制客观选择条件后无关，说明不能把该行为命名为 trusting behaviour；
- AI 与 rules-based algorithm 无差异，说明效应不是 AI 特异的；
- 单一 $\alpha$ 无法跨绩效水平描述行为，说明单一来源依赖错误权重不足以解释数据；
- 同时公开 Human 与 AI 正确率不减少 $|\alpha|$；
- 不同领域的符号反转无法由预先提出的任务差异解释，只能被视为未建模的情境异质性。

---

## 11. 理论贡献

### 11.1 对行为决策与测量研究的贡献

第一，本文以现实 Human alternative 为基准，提出有符号参数 $\alpha$，在同一尺度上统一表示 AI 错误受到额外惩罚、来源中立和额外宽容。由此，algorithm aversion、algorithm appreciation 与 overreliance 可以被放入同一个双向行为空间比较。

第二，本文把参数提出与参数识别分开。老虎机式概率任务用于检验 $\alpha$ 是否能够从行为阈值恢复、是否稳定以及是否预测后续选择，从而说明该参数是否具有超过代数定义的行为意义。

第三，本文把 A1–A5 从形式化前提转化为识别检查和替代解释。第一阶段测量 $\alpha$；第二阶段用 $M_i^{A4}$ 检查总体能力误判幅度，用 $M_{a,i}^{A4}$ 与 $M_{h,i}^{A4}$ 识别误判来源，用 $R_i^{A4}$ 检查相对误判方向，再以 $L$ 检查错误后果是否改变 $\alpha$。

### 11.2 对 AI trust research 的贡献

第一，本文把客观表现、能力信念、信任评价、信任态度与来源选择分开。Perceived task accuracy 检查参与者是否理解客观表现；perceived trustworthiness、performance trust 与 attitudinal trust 分别测量来源可信性评价、性能信任内容和依赖意愿；$\alpha$ 则由来源选择阈值恢复。

第二，本文区分能力误判的幅度、方向与信任评价。$M_i^{A4}$ 检验对 Human 与 AI 正确率的总体误判程度，$M_{a,i}^{A4}$ 与 $M_{h,i}^{A4}$ 识别误判来源，$R_i^{A4}$ 识别相对误判方向；perceived trustworthiness 则检验这些能力判断和行为差异是否伴随更广义的可信性评价。

第三，本文直接检验态度—行为边界。只有当 attitudinal trust 能够在控制成本、错误后果和其他行动约束后解释 source choice，来源选择才被进一步解释为 trusting behaviour。这样可以避免用行为名称预设其心理来源。

### 11.3 对管理与公共政策研究的贡献

第一，本文把 AI 采用问题从“AI 是否达到绝对标准”改写为“AI 相对于现实 Human alternative 获得多大的错误权重”。

第二，本文把来源权重映射到 under-adoption 与 over-adoption，不把增加 AI 使用率本身当作管理目标。

第三，跨医疗与智能驾驶的比较检验相对能力误判、感知可信性和错误后果是否解释 $\alpha$ 的变化，为组织和政策制定者判断不同领域应采用何种 Human–AI 比较标准提供依据。

本文提出的政策评价原则仍然是使 $\alpha$ 接近由可比证据支持的水平，而不是单向提高或降低 AI 采用。可比较的人类绩效披露、共同口径的错误报告、复核条件说明和不确定性呈现，可以按照是否减少缺乏证据支持的来源权重差异来评价。

---

## 12. 预期管理与政策含义

1. AI 的绩效披露应同时说明 relevant Human alternative 的同口径表现；脱离反事实的单一准确率可能缺乏可评价性。
2. 评价制度应同时警惕过严与过宽两类来源标准。只纠正 algorithm aversion，可能把判断推向 overreliance；只强调 AI 风险，也可能固化 under-adoption。
3. AI 与 Human 的不同门槛只有在任务和制度条件可比时才需要纠正。系统性失效、复核困难、责任缺口和不可申诉性均可能支持不同门槛。
4. 公众、管理者、专业人员与监管者可能具有不同的 $\alpha$。研究应比较这些群体距离来源中立基准有多远以及原因是什么，而不预设“监管者更保守”。

---

## 13. 可行性与实施顺序

研究的实施顺序服从“先测量、再解释”的逻辑：

1. 在老虎机式概率任务中确定多水平客观概率、错误后果与选择阈值的呈现方式。
2. 通过参数恢复模拟与预试检验 $\alpha$ 能否从来源选择中稳定恢复，并检验它是否预测未用于估计的选择。
3. 分别测量参与者对 Human 与 AI 正确率的判断，用 $M_i^{A4}$ 检验总体误判是否解释 $|\widehat\alpha_i|$；若显著，再比较 AI 与 Human 误差分量，并用 $R_i^{A4}$ 解释方向。
4. 平行测量 Human 与 AI 的 perceived trustworthiness；performance trust 与 attitudinal trust 只作为补充构念验证，不与客观正确率直接相减。
5. 操纵或比较 $L$，区分其对选择的直接作用与其是否进一步改变 $\alpha$。
6. 在医疗与智能驾驶等领域重新估计 $\alpha$，检验相对能力误判、信任变量、错误后果和其他来源条件能否解释跨领域变化。
7. 只有在个体层参数得到可靠测量后，再扩展到真实管理者、专业人员或监管材料。

样本量不在当前 RP 中凭经验填写。正式数值应由参数恢复模拟、预试效应分布和预注册的最小可识别效应共同确定。

---

## 14. 研究边界与局限

第一，human counterfactual 是现实比较基准，不等于规范上完美的社会最优。若 Human 现状本身低效或不公，来源对称仍可能保留绝对失准。

第二，$\alpha$ 在第一阶段首先是约化行为参数。它可能吸收未充分控制的错误相关性、复核、责任与其他来源差异；在这些因素未分离、参数恢复和稳定性尚未得到支持时，不得把 $\alpha$ 命名为单一心理机制或稳定结构参数。

第三，本文的信任测量聚焦于任务相关的 perceived trustworthiness、performance trust 与 attitudinal trust。它们与 perceived task accuracy 分属不同层次，是解释 $\alpha$ 和验证态度—行为关系的候选变量，不能保证完全解释 $\alpha$。医疗、军事或公共权力场景还可能涉及 moral trust 和程序正当性，本文不以一个错误权重模型包办这些问题。

第四，情境研究首先测量个人评价和政策偏好，不等于真实组织决策或实际监管。标题中的 regulation 只有在正式理论推导和制度层证据形成后才能作为已完成贡献；否则应在投稿时把副标题收窄为 Human–AI comparative evaluation and adoption。

第五，宏观任务提高现实意义，也带来背景知识和价值冲突。跨领域结果只能在各领域内部识别成立后比较，不能用医疗与自动驾驶的制度差异直接反推来源偏差。

---

## 15. 伦理与开放科学

涉及人类参与者的研究将在数据收集前完成伦理审查和知情同意。高风险医疗与自动驾驶情境需明确说明其为研究材料，避免参与者把假设性性能信息误解为现实产品建议。研究将预注册主要构念、排除规则、参数符号、模型比较和反证条件；材料、匿名化数据与分析代码将在伦理和隐私许可范围内公开。

---

## 16. 当前最精炼的论文论证

> 现有研究同时发现了对算法的规避、欣赏和过度依赖，却缺少一个能够在同一尺度上表示这些相反方向的行为参数。本文以 relevant human alternative 为比较基准，用有符号参数 $\alpha$ 测量 Asymmetric Error Tolerance。第一阶段在同时公开 Human 与 AI 客观正确率的条件下从行为选择阈值恢复 $\alpha$；第二阶段操纵是否同时公开双方正确率，并分别测量参与者对双方正确率的判断。$M_i^{A4}$ 检验总体能力误判是否解释 $|\alpha|$，AI 与 Human 误差分量识别误判来源，$R_i^{A4}$ 解释 $\alpha$ 的方向；错误后果 $L$ 检验 stakes 是否进一步改变非对称容忍。Perceived trustworthiness 保持为独立心理评价。由此，本文形成一条完整论证：提出 $\alpha$，证明 $\alpha$ 可以从行为中测量，再解释 $\alpha$ 为什么变化。

---

## 参考文献

Castelo, N., Bos, M. W., & Lehmann, D. R. (2019). Task-dependent algorithm aversion. *Journal of Marketing Research, 56*(5), 809–825. https://doi.org/10.1177/0022243719851788

Dietvorst, B. J., & Bharti, S. (2020). People reject algorithms in uncertain decision domains because they have diminishing sensitivity to forecasting error. *Psychological Science, 31*(10), 1302–1314. https://doi.org/10.1177/0956797620948841

Dietvorst, B. J., Simmons, J. P., & Massey, C. (2015). Algorithm aversion: People erroneously avoid algorithms after seeing them err. *Journal of Experimental Psychology: General, 144*(1), 114–126. https://doi.org/10.1037/xge0000033

Everett, J. A. C., Claessens, S., Knöchel, T.-D., & Reinecke, M. G. (2026). Principles for understanding trust in artificial intelligence. *Nature Reviews Psychology, 5*(6), 388–401. https://doi.org/10.1038/s44159-026-00562-1

Goddard, K., Roudsari, A., & Wyatt, J. C. (2012). Automation bias: A systematic review of frequency, effect mediators, and mitigators. *Journal of the American Medical Informatics Association, 19*(1), 121–127. https://doi.org/10.1136/amiajnl-2011-000089

Hsee, C. K. (1996). The evaluability hypothesis: An explanation for preference reversals between joint and separate evaluations of alternatives. *Organizational Behavior and Human Decision Processes, 67*(3), 247–257. https://doi.org/10.1006/obhd.1996.0077

Kaplan, A. D., Kessler, T. T., Brill, J. C., & Hancock, P. A. (2023). Trust in artificial intelligence: Meta-analytic findings. *Human Factors, 65*(2), 337–359. https://doi.org/10.1177/00187208211013988

Lee, J. D., & See, K. A. (2004). Trust in automation: Designing for appropriate reliance. *Human Factors, 46*(1), 50–80. https://doi.org/10.1518/hfes.46.1.50_30392

Lenskjold, A., Nybing, J. U., Trampedach, C., Galsgaard, A., Brejnebøl, M. W., Raaschou, H., Rose, M. H., & Boesen, M. (2023). Should artificial intelligence have lower acceptable error rates than humans? *BJR Open, 5*(1), 20220053. https://doi.org/10.1259/bjro.20220053

Logg, J. M., Minson, J. A., & Moore, D. A. (2019). Algorithm appreciation: People prefer algorithmic to human judgment. *Organizational Behavior and Human Decision Processes, 151*, 90–103. https://doi.org/10.1016/j.obhdp.2018.12.005

Longoni, C., Bonezzi, A., & Morewedge, C. K. (2019). Resistance to medical artificial intelligence. *Journal of Consumer Research, 46*(4), 629–650. https://doi.org/10.1093/jcr/ucz013

Mehrotra, S., Degachi, C., Vereschak, O., Jonker, C. M., & Tielman, M. L. (2024). A systematic review on fostering appropriate trust in human–AI interaction: Trends, opportunities and challenges. *ACM Journal on Responsible Computing, 1*(4), Article 26, 1–45. https://doi.org/10.1145/3696449

Rebitschek, F. G., Gigerenzer, G., & Wagner, G. G. (2021). People underestimate the errors made by algorithms for credit scoring and recidivism prediction but accept even fewer errors. *Scientific Reports, 11*, 20171. https://doi.org/10.1038/s41598-021-99802-y

Schaefer, K. E., Chen, J. Y. C., Szalma, J. L., & Hancock, P. A. (2016). A meta-analysis of factors influencing the development of trust in automation: Implications for understanding autonomy in future systems. *Human Factors, 58*(3), 377–400. https://doi.org/10.1177/0018720816634228

Shariff, A., Bonnefon, J.-F., & Rahwan, I. (2021). How safe is safe enough? Psychological mechanisms underlying extreme safety demands for self-driving cars. *Transportation Research Part C: Emerging Technologies, 126*, 103069. https://doi.org/10.1016/j.trc.2021.103069
