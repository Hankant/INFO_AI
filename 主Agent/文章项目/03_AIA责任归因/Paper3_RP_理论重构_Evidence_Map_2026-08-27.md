# Paper 3 正式 RP 重构：Evidence Map

## Material Passport

- 文件性质：新正式 RP 的证据工作表，不替代当前正式基准
- 日期：2026-08-27
- 证据范围：项目内既有文献总结 + DOI/期刊官网核验
- 状态：WORKING EVIDENCE MAP

## 一、核心概念审计

| 概念 | 原始术语与来源 | 理论定义与边界 | 分析层级 | 在本文中的位置 | 经验对应 | 可区分的竞争解释 |
|---|---|---|---|---|---|---|
| 角色义务 | `prescription–identity link`，Schlenker et al. (1994)；`obligation`，Malle et al. (2014) | 行动者因其身份或角色而受到相关规范约束。它不等同于是否亲手作出最后一步选择 | 个体行动者—社会角色 | 责任判断的依据 | “该行动者是否有职责预防不良结果/确保决定符合规则” | 人类失去最后控制即免责 vs. 人类因保留角色义务仍被责备 |
| 决策控制 | `personal control`，Schlenker et al. (1994)；`capacity to prevent`，Malle et al. (2014)；`control`，Grote et al. (2026) | 行动者能够选择、修改、阻止或避免某项结果的程度。它不等同于仅仅参与流程 | 个体/组织角色 | 责任判断的依据；AI 委托直接改变的结构维度 | 最终决定权、否决权、干预机会、可预防性判断 | 责任取决于最后控制 vs. 责任取决于授权和持续义务 |
| 因果贡献 | `causal connection/causality`，Schlenker et al. (1994); Malle et al. (2014) | 行动者的行为是否构成结果发生的原因。它不自动等于道德责备 | 事件—行动者 | 因果责任的直接依据 | 人类授权、AI 最终选择、结果反事实依赖；独立因果责任评分 | AI 获得因果责任必然挤出人类责任 vs. 二者可同时承担责任 |
| 因果责任 | `causal responsibility`，责任归因研究常用结果变量 | 对某行动者在因果链中贡献程度的判断。它不包括该行动者是否应受谴责 | 评价者个体 | 核心因变量之一 | 对人类与 AI 分别作 0–100 独立评分 | 结构性因果判断 vs. 带有利益动机的重解释 |
| 道德责备 | `blame`，Malle et al. (2014)；`moral fault`，Shank et al. (2019) | 对违反规范的行动者作出的负面道德评价。它与惩罚行为、法律责任和因果责任均需分开 | 评价者个体 | 核心因变量之一 | 对人类与 AI 分别评分；不以实际处罚替代 | AI 有因果作用即可被责备 vs. AI 缺少意图/义务承载能力使责备仍集中于人类 |
| 评价者利益位置 | `self-interest bias`，Dong & Bocian (2024)；与 Alicke (2000) 的 `spontaneous evaluation` 逻辑相容 | 评价者因结果使其所属一方受益或受损而处于不同利益位置。它不是人格特质，也不等于一般群体认同 | 评价者个体、嵌套于群体 | 调节变量 | 由真实群体收益结果定义为受益方或受损方 | 同一责任结构产生一致判断 vs. 责任依据的权重随利益位置变化 |
| 社会偏好 | Fehr & Schmidt (1999) 的 inequity aversion；Rabin (1993) 的 intention-based reciprocity | 个体效用可能受到收益差距或对方意图判断影响。本文不估计其结构参数，也不将其直接等同于责任归因 | 个体决策者/互动双方 | 群体与真实收益设计的理论依据；非主机制 | 真实收益差距、对方行动记录；如测量则需另行采用经过验证的量表或选择任务 | 纯物质收益解释 vs. 对行动者意图和责任的社会评价解释 |

## 二、本文提出的分析概念

### 责任配置（responsibility configuration）

“责任配置”是本文提出的分析标签，不是既有文献中的成熟构念。它指：AI 获得最终决定权后，人类与 AI 的责任评分如何联合变化。该标签用于区分以下三种经验结果：

1. **责任转移**：AI 责任上升，人类责任下降；
2. **责任累积**：AI 责任上升，人类责任没有相应下降；
3. **责任稀释**：人类责任下降，但 AI 获得的责任不足以补足该下降。

本文不预设责任总量固定。强制总和为 100 的分配题只能测量相对份额；独立评分才能检验责任是否累积或稀释。因此，两种测量需要并行使用，且独立评分承担主要理论检验。

## 三、关键主张—证据对应

| 拟写入 RP 的主张 | 直接来源 | 来源实际支持的内容 | 可写强度 | 核验状态 |
|---|---|---|---|---|
| 责任判断取决于规范与事件、规范与角色、角色与事件之间的连接 | Schlenker et al. (1994) | Triangle Model 明确提出三条连接，实验支持连接强度共同预测责任判断 | 可直接写 | PubMed/DOI 已核验 |
| 非意图性伤害仍可通过义务与预防能力路径产生责备 | Malle et al. (2014) | Path Model 将意图性行为与非意图性行为的义务、能力判断分开 | 可直接写 | 期刊页与作者 PDF 已核验 |
| 委托可改变责任归因，并成为交出决定权的动机 | Bartling & Fischbacher (2012) | 有激励实验以惩罚选择刻画责任归因，发现委托能够转移责备 | 可直接写；不可推断所有 AI 委托都为避责 | OUP/DOI 已核验 |
| AI 组织需要控制与问责相匹配 | Grote et al. (2026) | 理论论文认为控制使利益相关者能够实现或避免结果，问责提供相应动机；AI 自主适应和多方依赖增加错配 | 可用于组织层理论动机；当前实验只检验用户端局部结构 | AOM/DOI 已核验 |
| 人机决策结构可能降低监督者受到的道德过错归因，且 AI 责任不一定相应上升 | Shank et al. (2019) | 情境实验中，人类监督 AI 时比人类单独决策或接受 AI 建议时受到更少 fault；AI fault 对结构不敏感 | 可直接写；需注明情境实验 | Taylor & Francis/DOI 已核验 |
| 人机共同错误不必使机器承担更多责备 | Awad et al. (2020) | 自动驾驶共享控制情境中，人类和机器同时犯错时，分配给机器的责备下降 | 可用于反对责任简单守恒 | Nature/DOI 已核验 |
| AI 参与可能降低道德愤怒与组织负面评价 | Bigman et al. (2023) | 八项研究显示算法歧视引发较少道德愤怒，偏见动机归因是重要解释 | 可用于意图/动机路径；不能泛化到所有 AI 决策 | APA/DOI 已核验 |
| 控制选项的存在可能把责备推回人类 | Arnestad et al. (2024) | 手动接管选项即使未被使用且难以实际介入，也会提高人类对 AI 错误的责备 | 可直接写；区分实际控制与控制表象 | ScienceDirect/DOI 已核验 |
| 评价自身或内群体违规时，人们会更宽松，并可能向 AI 分配更多责任 | Dong & Bocian (2024) | 三项预注册 vignette studies 发现 self-interest bias 与 AI responsibility attribution 相关 | 可直接写；不能声称真实群体利益已被检验 | ScienceDirect/DOI 已核验 |
| 机器委托接口可能增加不诚实行为 | Köbis et al. (2025) | 13 项实验显示部分委托接口提高不诚实请求，机器对不道德指令的服从也高于人类 | 可作为行为端证据；不能直接推断冲突升级 | Nature/DOI 已核验 |
| 困难且无理想选项的决策可能提高 AI 委托，并与责任回避相关 | Xu et al. (2026) | 八项以情境、意愿和自报变量为主的随机分派研究 | 只能作为近期支持；本文不预设避责动机 | ScienceDirect/DOI 已核验，2026 年期刊卷期信息需提交前刷新 |
| 利益位置可能使相同控制证据得到不同责备解释 | Alicke (2000); Dong & Bocian (2024) | Culpable Control Model 允许评价先影响控制证据加工；Dong & Bocian 提供 AI 情境中的自利偏差证据 | 作为推导性假设写，不能写成既定 AI 群体效应 | PubMed/ScienceDirect 已核验 |

## 四、证据边界

1. 当前设计没有人类代理或规则算法条件，因此不能识别 AI 相对于一般委托或自动化的独有效应。
2. 当前 AI 若执行固定、公开规则，实验识别的是 AI 决策代理结构，不足以检验 Grote et al. 所强调的自主适应性。
3. 受益方与受损方差异同时包含物质利益和群体位置，除非另设正交操纵，否则不能把差异单独归因于其中一项。
4. 决策者自评同时包含利益位置与行动者—观察者差异，必须与外部评价分开分析。
5. 责任评分与实际处罚、组织纪律或法律问责不同。当前核心研究不使用“实际处罚”作为结果变量。

## 五、核心参考文献

- Alicke, M. D. (2000). Culpable control and the psychology of blame. *Psychological Bulletin, 126*(4), 556–574. https://doi.org/10.1037/0033-2909.126.4.556
- Arnestad, M. N., Meyers, S., Gray, K., & Bigman, Y. E. (2024). The existence of manual mode increases human blame for AI mistakes. *Cognition, 252*, 105931. https://doi.org/10.1016/j.cognition.2024.105931
- Awad, E., Levine, S., Kleiman-Weiner, M., Dsouza, S., Tenenbaum, J. B., Shariff, A., Bonnefon, J.-F., & Rahwan, I. (2020). Drivers are blamed more than their automated cars when both make mistakes. *Nature Human Behaviour, 4*(2), 134–143. https://doi.org/10.1038/s41562-019-0762-8
- Bartling, B., & Fischbacher, U. (2012). Shifting the blame: On delegation and responsibility. *The Review of Economic Studies, 79*(1), 67–87. https://doi.org/10.1093/restud/rdr023
- Bigman, Y. E., Wilson, D., Arnestad, M. N., Waytz, A., & Gray, K. (2023). Algorithmic discrimination causes less moral outrage than human discrimination. *Journal of Experimental Psychology: General, 152*(1), 4–27. https://doi.org/10.1037/xge0001250
- Dong, M., & Bocian, K. (2024). Responsibility gaps and self-interest bias: People attribute moral responsibility to AI for their own but not others’ transgressions. *Journal of Experimental Social Psychology, 111*, 104584. https://doi.org/10.1016/j.jesp.2023.104584
- Fehr, E., & Schmidt, K. M. (1999). A theory of fairness, competition, and cooperation. *The Quarterly Journal of Economics, 114*(3), 817–868. https://doi.org/10.1162/003355399556151
- Grote, G., Parker, S. K., & Crowston, K. (2026). Taming artificial intelligence: A theory of control–accountability alignment among AI developers and users. *Academy of Management Review, 51*(2), 278–299. https://doi.org/10.5465/amr.2023.0117
- Köbis, N., Rahwan, Z., Rilla, R., Supriyatno, B. I., Bersch, C., Ajaj, T., Bonnefon, J.-F., & Rahwan, I. (2025). Delegation to artificial intelligence can increase dishonest behaviour. *Nature, 646*(8083), 126–134. https://doi.org/10.1038/s41586-025-09505-x
- Malle, B. F., Guglielmo, S., & Monroe, A. E. (2014). A theory of blame. *Psychological Inquiry, 25*(2), 147–186. https://doi.org/10.1080/1047840X.2014.877340
- Rabin, M. (1993). Incorporating fairness into game theory and economics. *American Economic Review, 83*(5), 1281–1302. https://www.jstor.org/stable/2117561
- Schlenker, B. R., Britt, T. W., Pennington, J., Murphy, R., & Doherty, K. (1994). The triangle model of responsibility. *Psychological Review, 101*(4), 632–652. https://doi.org/10.1037/0033-295X.101.4.632
- Shank, D. B., DeSanti, A., & Maninger, T. (2019). When are artificial intelligence versus human agents faulted for wrongdoing? Moral attributions after individual and joint decisions. *Information, Communication & Society, 22*(5), 648–663. https://doi.org/10.1080/1369118X.2019.1568515
- Xu, L., Tian, H., Zhang, Y., & Yu, F. (2026). Shifting accountability to artificial intelligence: Delegating challenging decisions to AI for responsibility avoidance. *Journal of Business Research, 215*, 116313. https://doi.org/10.1016/j.jbusres.2026.116313
