# 广州市教育局高校科研项目申请书内容草稿

## 1. 基本信息建议

- 学科类别：人文社会科学类
- 学科分类及代码：`【待按你的一级学科确认，建议优先考虑 1201 管理科学与工程 或 1202 工商管理学】`
- 项目类别：`【待按你的身份确认：青年博士启动项目 / 青年人才发展项目 / 研究生科研项目】`
- 项目名称：生成式人工智能重构高风险决策的信息校准与依赖学习机制研究
- 项目英文名称：Generative AI, Information Calibration, and Reliance Learning in High-Risk Decision-Making
- 研究方向：生成式人工智能与高风险决策；信息校准；人机协作依赖学习
- 预期研究期限：`【建议 2026.09-2028.09 或 2026.09-2029.09，按申报类别最终确认】`

## 2. 项目摘要（400字以内）

生成式人工智能正从信息检索工具转向判断与辅助决策基础设施。本项目围绕“AI如何重构高风险决策”的关键问题，聚焦两个相互衔接的机制：一是 answer-first summary 及其来源标签如何改变用户对额外证据价值、信息充分性和后续信念更新的判断；二是在重复反馈中，早期AI错误是否会引发相对于人类来源更强、更持久的低依赖与低授权。项目将采用 same-summary source-label 实验、重复预测/判断实验、贝叶斯基准以及简化 EWA/来源特异性学习模型，识别生成式AI对信息校准与依赖学习的影响机制，并为高校及公共部门在AI辅助判断场景中的界面设计、使用规范和风险治理提供经验证据。

## 3. 主题词

生成式人工智能, 信息校准, 依赖学习

## 4. 立项依据

### 4.1 研究意义

生成式人工智能正在显著改变人们获取信息、整合证据和做出判断的方式。与传统搜索或决策支持系统不同，生成式AI往往以 answer-first 的方式直接给出总结、建议或默认判断，这意味着用户在尚未逐条接触原始证据之前，已经面对一个被系统压缩、组织和叙事化的结果。在高风险决策场景中，这一变化带来的问题不再只是“AI是否更准确”，而是“AI如何改变人对证据价值、信息充分性和后续依赖边界的判断”。因此，围绕生成式AI展开研究，必须把分析单位从单次正确率比较推进到信息校准与依赖学习过程。

现有 trust in automation、algorithm aversion、algorithm appreciation 与 AI-assisted decision-making 文献，为理解人类如何评价算法系统提供了重要基础，但大多集中在单轮建议采纳、局部置信校准或短期错误反应层面。第一，这些研究较少区分“搜索减少”究竟意味着理性的信息压缩，还是有害的信息获取偏离。第二，它们较少考察人在重复反馈中如何学习AI应当扮演什么角色，以及早期AI错误是否会被赋予比人类来源错误更高的负向学习权重。第三，现有研究往往把信息获取、后验更新和依赖行为分别处理，尚未把 evidence-to-belief 与 belief-to-reliance 两个关键环节置于同一研究计划中加以识别。

本项目因此聚焦两个前后衔接的问题。其一，在初始 summary 内容相同、额外搜索成本相同的条件下，AI 来源标签是否会改变用户对额外证据价值、主观信息获得感、epistemic ownership 和后续信念更新的判断。其二，在重复反馈任务中，即使 AI 与 human source 的总体表现等价，早期AI错误是否仍会引发更强、更持久的后续低依赖。前者对应高风险决策中的信息校准问题，后者对应动态依赖校准问题。将两者放在同一项目中研究，可以更系统地解释生成式AI如何重构高风险决策中的“证据—信念—依赖”链条。

从现实意义看，生成式AI已经进入高校科研、政策分析、内容审核、风险筛查、例外复核与专业判断等多种场景。无论在高校科研训练还是公共部门辅助决策中，仅凭平均准确率并不足以判断AI系统是否被恰当使用。真正关键的是：用户是否过早停止搜索、是否误判自身信息掌握程度、是否在少量早期错误后长期回到过强的人为保守状态。本项目有助于为高校和公共部门建立更审慎的AI使用规范、界面设计原则与依赖审计框架提供实验依据，也可为广州在智能治理与高层次人才培养中的制度建设提供可操作的知识支持。

### 4.2 国内外研究现状与发展趋势

国外相关研究主要来自四条脉络。第一，trust in automation 与 appropriate reliance 文献强调，人机协作的关键不在于盲目提升信任，而在于形成与系统能力相匹配的依赖关系。第二，algorithm aversion 与 algorithm appreciation 研究表明，人类对算法错误与算法建议的反应并不稳定，既可能在见到算法出错后过度回避，也可能在某些情境下偏好算法判断。第三，AI-assisted decision-making 文献开始关注 explanation、confidence 以及 human/AI correctness likelihood 如何影响局部信任校准。第四，learning to defer、human-AI teaming 和系统综述研究则提示，人机组合绩效并非取决于谁单独更强，而取决于分工结构是否合理。

但现有研究仍存在明显缺口。一方面，生成式AI的 summary-first 机制使“行为搜索深度”“信息深度”和“更新深度”之间可能发生分离，传统研究常用的点击数、搜索时间和建议采纳率已不足以准确刻画生成式AI环境中的信息获取质量。另一方面，多数研究仍以单轮任务或短期反应为主，较少直接检验早期AI错误是否会通过路径依赖机制改变后续依赖轨迹。随着生成式AI从信息工具转向默认判断和协作架构的一部分，研究重心正在从“这一次是否采纳AI”转向“人在持续反馈中如何学习AI的角色边界”。这也是本项目拟切入的核心趋势。

总体来看，未来该领域最值得推进的方向至少包括：其一，用更严格的识别设计区分AI内容效应与AI标签效应；其二，用规范性基准区分理性的信息压缩与非理性的过早停止搜索；其三，用多轮反馈设计识别AI错误冲击如何影响后续依赖、恢复速度和长期授权边界；其四，把个体层面的实验发现转化为高校和公共部门在AI使用规范上的可执行原则。本项目将围绕这些方向形成系统研究。

### 4.3 主要参考文献

[1] Lee J D, See K A. Trust in automation: Designing for appropriate reliance[J]. Human Factors, 2004, 46(1): 50-80.

[2] Dietvorst B J, Simmons J P, Massey C. Algorithm aversion: People erroneously avoid algorithms after seeing them err[J]. Journal of Experimental Psychology: General, 2015, 144(1): 114-126.

[3] Logg J M, Minson J A, Moore D A. Algorithm appreciation: People prefer algorithmic to human judgment[J]. Organizational Behavior and Human Decision Processes, 2019, 151: 90-103.

[4] Parasuraman R, Sheridan T B, Wickens C D. A model for types and levels of human interaction with automation[J]. IEEE Transactions on Systems, Man, and Cybernetics-Part A: Systems and Humans, 2000, 30(3): 286-297.

[5] Endsley M R, Kaber D B. Level of automation effects on performance, situation awareness and workload in a dynamic control task[J]. Ergonomics, 1999, 42(3): 462-492.

[6] Zhang Y, Liao Q V, Bellamy R K E. Effect of confidence and explanation on accuracy and trust calibration in AI-assisted decision making[C]//Proceedings of the 2020 Conference on Fairness, Accountability, and Transparency. New York: ACM, 2020: 295-305.

[7] Ma S, Lei Y, Wang X, et al. Who should I trust: AI or myself? Leveraging human and AI correctness likelihood to promote appropriate trust in AI-assisted decision-making[C]//Proceedings of the 2023 CHI Conference on Human Factors in Computing Systems. New York: ACM, 2023: Article 759, 1-19.

[8] Camerer C, Ho T H. Experience-weighted attraction learning in normal form games[J]. Econometrica, 1999, 67(4): 827-874.

[9] Mozannar H, Sontag D. Consistent estimators for learning to defer to an expert[C]//Proceedings of the 37th International Conference on Machine Learning. PMLR, 2020: 7076-7087.

[10] Arthur W B. Competing technologies, increasing returns, and lock-in by historical events[J]. The Economic Journal, 1989, 99(394): 116-131.

[11] David P A. Clio and the economics of QWERTY[J]. American Economic Review, 1985, 75(2): 332-337.

[12] Vaccaro M, Almaatouq A, Malone T W. When combinations of humans and AI are useful: A systematic review and meta-analysis[J]. Nature Human Behaviour, 2024, 8: 2293-2303.

## 5. 研究方案

### 5.1 研究内容、研究目标与拟解决的关键问题

本项目围绕“生成式人工智能如何重构高风险决策中的信息校准与依赖学习”展开，拟设置两个彼此衔接的实证研究模块。

第一模块聚焦信息校准。研究在初始 summary 内容相同、后续证据池相同、额外搜索成本相同的条件下，仅操纵是否标注为“AI生成”，以识别 AI 来源标签是否改变用户对额外证据价值、信息充分性、epistemic ownership 和后续信念更新的判断。该模块将重点区分三种可能结果：一是搜索减少但后验判断并未恶化，说明AI实现了理性的信息压缩；二是搜索减少且后验判断更偏离规范基准，说明AI标签诱发了过早停止搜索；三是客观判断更准但主观掌握感更低，说明出现信息校准错配。

第二模块聚焦动态依赖学习。研究在重复反馈任务中比较 AI early error、AI late error、AI distributed error 与 human-source error 等条件，在总体表现等价的前提下，识别早期AI错误是否会引发更强、更持久的后续低依赖，并考察这种差异是否源于来源特异性的学习权重，而非单纯的能力差异或近期冲击。

本项目的总体目标是：第一，构建一个将 evidence-to-belief 与 belief-to-reliance 串联起来的研究框架；第二，提供关于生成式AI何时促进理性信息压缩、何时诱发有害低依赖的实验识别证据；第三，形成面向高校与公共部门AI辅助判断场景的设计和治理建议。

拟解决的关键问题包括：第一，AI标签是否在不改变信息内容的情况下改变用户对“是否还需要继续搜索”的主观判断；第二，AI导致的搜索减少究竟是效率提升还是信息获取偏离；第三，早期AI错误是否比人类来源错误更容易被赋予过强的负向学习权重；第四，如何区分路径依赖、一般性惯性和先验偏见对后续AI依赖的影响。

### 5.2 本项目的特色与创新之处

本项目的创新主要体现在三个方面。其一，研究对象从一般性的“AI信任”推进到“信息校准与依赖学习”，不再只问用户是否接受某次建议，而是追问AI如何改变证据获取阈值、后验更新和后续依赖轨迹。其二，采用 same-summary source-label design，在 summary 内容不变、边际搜索成本相同的条件下识别 AI 标签效应，从方法上更清楚地区分了内容效应、来源效应和成本效应。其三，将单轮贝叶斯基准实验与多轮反馈实验结合起来，既能识别AI是否诱发信息获取偏离，也能识别早期AI错误是否在后续多轮中造成持续性低依赖，从而把信息搜索、行为学习与人机协作边界置于同一框架中讨论。

### 5.3 研究方法

本项目采用行为实验、规范性基准比较与动态学习模型相结合的方法。第一模块拟开展被试间实验，设置 no-summary control、unlabeled summary 与 AI-labeled summary 等条件，并区分 representative summary 与 incomplete summary。通过固定证据库、预设 likelihood ratio 和 log-odds 形式的贝叶斯基准，分别计算 conditional Bayesian deviation 与 full-information deviation，用以衡量用户对已接触证据的吸收质量，以及其相对于完整证据集的偏离程度。与此同时，测量 confidence、perceived information acquisition、epistemic ownership 和 perceived sufficiency of evidence 等变量，以识别主观—客观校准错配。

第二模块拟采用有限重复窗口下的重复预测/判断实验。参与者在多轮任务中反复面对 AI 与 human source 的建议或判断结果，并根据每轮反馈更新后续依赖。研究通过在总体表现等价的前提下操控 early/late/distributed error 的来源与时点，结合 reduced-form 动态分析和简化 EWA / source-specific learning 模型，估计 AI error 与 human-source error 的负向更新权重是否存在系统性差异。

在分析方法上，项目将使用多层回归模型、事件窗口分析、混合效应模型与参数恢复检验，以排除任务难度、风险态度、基线AI态度、切换成本和近期冲击等替代解释。正式实验前将通过预实验对任务理解、材料难度、轮次设置和参数可识别性进行校准。

### 5.4 技术路线

项目技术路线分为“理论梳理—预实验校准—正式实验—综合整合”四步。首先，围绕 information calibration 与 dynamic reliance learning 两个核心问题完成文献整合与研究设计收束。其次，开展预实验，对 summary 材料、证据库、风险判断任务、重复反馈任务及关键测量指标进行校准。再次，分别完成信息校准实验与动态依赖实验，形成两个模块的核心数据。最后，通过统一的研究框架整合 evidence-to-belief 与 belief-to-reliance 结果，提炼面向高校和公共部门的AI辅助判断设计建议。

### 5.5 预期风险及规避措施

本项目的主要风险包括：第一，AI标签效应可能较弱，导致信息校准结果不显著。对此，将通过预实验优化 summary 文本、标签措辞和任务情境，提高操控强度并保留多个主观机制变量。第二，多轮任务可能出现理解偏差或疲劳问题。对此，将设置练习轮、理解检验和任务中途提醒，并在正式实验前校准轮次长度。第三，动态学习模型存在参数可识别性不足的风险。对此，将把 reduced-form 结果作为主证据，并在结构估计前进行参数恢复检验，确保结构模型只在可识别时作为机制补充。第四，若样本招募不足可能影响统计功效。对此，将采用“预实验—正式实验”两阶段方案，并根据效应大小动态调整正式样本量。

### 5.6 年度研究计划及预期研究结果

第一阶段（2026年9月—2027年8月）：完成文献综述、理论框架和研究设计定稿；搭建固定证据库与 summary 材料；完成信息校准模块预实验和任务修订；形成1份阶段性研究备忘录。

第二阶段（2027年9月—2028年8月）：完成信息校准模块正式实验和初步论文写作；开展重复反馈任务预实验，校准 error timing、performance parity 与测量设计；参加至少1次国内学术会议交流。

第三阶段（2028年9月—2029年8月）：完成动态依赖学习模块正式实验与综合分析；形成完整研究报告、论文初稿和治理建议稿；参加至少1次学术交流活动，推动研究成果转化为高校与公共部门AI使用规范建议。

预期研究结果包括：形成围绕“信息校准—依赖学习”主线的阶段性论文与研究报告；构建可复用的实验材料和分析框架；提出关于AI辅助判断场景中证据呈现、错误恢复和依赖审计的政策建议。

### 5.7 项目预期研究成果转移转化情况

本项目虽属于人文社会科学研究，但具有明确的应用转化潜力。项目可为高校科研训练、研究方法课程、AI素养教育和公共部门辅助判断场景提供可操作的使用原则，包括：何种界面设计会降低用户继续搜索的意愿、何种错误反馈机制更有利于避免长期低依赖、何种指标可用于审计AI系统是否被“恰当依赖”。项目成果可转化为研究报告、培训材料、内部讲座与规范建议，为广州高校和公共部门开展AI工具治理提供经验支持。

## 6. 研究基础与工作条件

### 6.1 工作基础

本项目已经具备较好的前期研究基础。围绕“AI as Decision Architecture”这一总体研究主线，申请人所在研究已形成较为清晰的项目结构，并将核心问题拆分为 evidence-to-belief、belief-to-reliance 和 responsibility 三个阶段。就本次申报而言，前两个阶段已经形成较成熟的研究积累。

在信息校准模块方面，已完成“算法权威与信息校准：生成式AI如何改变额外搜索与信念更新”的基准稿，并明确形成 same-summary source-label design、固定证据库、likelihood ratio、conditional/full-information Bayesian deviation、epistemic ownership 和 information calibration mismatch 等关键设计要素。说明项目并非从零起步，而是在已有较系统的研究推演基础上进一步凝练。

在动态依赖模块方面，已围绕“重复反馈中的AI依赖校准”形成当前项目基准材料，明确将研究重点从一般性 trust/advice adoption 收束到 early AI errors、performance parity、dynamic under-reliance 与简化 EWA / source-specific learning 机制。相关研究计划、评审修订意见和答辩材料已经较充分地暴露了理论边界、识别难点和替代解释，为正式申报后的项目推进提供了扎实准备。

### 6.2 工作条件

项目已具备开展行为实验与文本分析所需的基本工作条件。现有工作区已形成共享文献库、研究计划底稿、实验任务设想和文献批判材料，可直接支持后续研究设计完善与材料迭代。项目研究主要依赖文献整合、实验设计、在线问卷/行为实验实施和统计分析，对大型实验设备依赖较低。现阶段已具备完成预实验与正式实验的数据处理方案和写作条件；后续如需扩大样本招募，将依托申请人所在单位的科研平台、被试招募渠道和学术交流资源推进实施。

### 6.3 申请人和主要参与者简介

此部分建议按真实信息补充，建议写法如下：

1. 申请人学历与研究经历：`【待你补充真实简历】`
2. 近三年与本项目相关的主要论著：`【待你补充真实成果；没有就不要硬写】`
3. 近三年获得的学术奖励情况：`【待你补充真实情况；没有可写“无”】`
4. 主要参与者简介与分工：`【待按团队真实情况填写】`

### 6.4 承担科研项目情况

此部分必须按真实情况填写，建议格式为：

- 项目名称：
- 项目编号：
- 经费来源：
- 起止年月：
- 与本项目关系：
- 承担内容：

如目前无在研相关项目，可据实填写“无”。

## 7. 重复申报自查

建议填写：本项目目前未同时申报其他市级或以上财政资金资助项目；如后续存在与其他项目交叉申报情况，将严格按照广州市教育局有关规定据实申报并作出说明。`【若你实际有在报项目，必须改成真实信息】`

## 8. 项目主要验收指标建议

### 8.1 主要技术指标（建议值）

- 新产品（或新材料、新装备、新品种/系）：0
- 新工艺（或新方法、新模式、新技术、新服务）：1
  说明：形成1套关于生成式AI信息校准与动态依赖学习的实验研究框架
- 发明专利申请/授权：0
- 实用新型专利申请/授权：0
- 外观设计专利申请/授权：0
- 国外专利（PCT受理/授权）：0
- 技术标准制定（牵头/参与）：0
- 软件著作权：0
- 论文论著（SCI/SSCI/EI等）：0或1 `【如你有把握再填1】`
- 论文论著（核心期刊）：1
- 论文论著（其他）：1
- 研究报告：1
- 获得国家级/省级/市级奖项：0
- 获得人才奖励：0
- 引进人才：0
- 培养人才（博士/硕士/其他）：`【待按真实团队情况补】`
- 获市级以上政府领导批示：0

其他成果及形式说明（150字内）建议写法：

围绕生成式AI辅助判断场景形成1套可复用的研究框架、1份研究报告和若干论文成果，为高校与公共部门优化AI界面设计、搜索提示与错误恢复机制提供经验证据和规范建议。

### 8.2 主要经济指标及社会效益（建议值）

- 建设期内承接的横向技术服务数：0
- 建设期内承接的横向技术服务到账收入：0
- 建设期内完成的科技成果转移转化数：0
- 建设期内完成的科技成果转移转化收入：0

其他经济指标及社会效益说明（150字内）建议写法：

项目将为高校科研训练、研究方法教学和公共部门AI辅助判断提供机制证据，帮助识别何种AI呈现方式会诱发过早停止搜索、何种错误反馈会造成持续性低依赖，从而提升生成式AI使用的规范性、审慎性与治理有效性。

## 9. 预算口径提示

预算部分必须结合`项目类别`和`申请金额`来回填，暂不宜硬写死。当前只给口径：

- 人文社科项目一般不建议列设备购置，设备费可填0。
- 经费重点可放在图书资料、调研/会议差旅、问卷与实验平台服务、数据处理、直接人力成本和间接费用。
- 直接人力资源成本不得超过总经费60%。
- 若最终项目资助额度为2万元，可优先做“2万元版预算”；
- 若最终项目资助额度为3万元，可在会议差旅、实验服务和直接人力成本上适度上调。

## 10. 当前必须由你确认的真实信息

1. 你准备申报的项目类别到底是哪一类。
2. 申请人姓名、性别、民族、出生年月、职称、职务、学位、学历、手机、邮箱。
3. 申请单位全称、统一社会信用代码、联系人、单位电话、地址、邮编。
4. 是否有合作单位；如果有，合作单位完整信息。
5. 近三年科研绩效统计表的数据。
6. 项目组成员名单与分工。
7. 是否有在研项目或重复申报情况。
8. 预算总额以及你希望按几年执行。
