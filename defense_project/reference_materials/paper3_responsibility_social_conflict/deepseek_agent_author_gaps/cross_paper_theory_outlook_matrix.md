# 跨论文理论展望矩阵

> **本文归纳**标记说明：所有带此标记的内容为整理Agent从多篇论文中归纳的模式，非任何单一作者的原话。
> **当前无本文归纳**——所有 4 条原有归纳已被移除，原因：引入未逐篇提取的文献（Rabin, Jervis, Schelling, Malle）；自行组合成新框架违反"不自行拼理论"规则；跨层级类比缺乏可比性。待 Payne 核验完成、更多论文获得全文后，再重新评估是否可做跨论文归纳。

## 理论展望总表

| 论文 | 理论/构念 | 分析层级 | 作者指出的理论不足 | 理论推进方向 | 待检验关系 | 可区分的解释 | 原文页码 |
|---|---|---|---|---|---|---|---|
| VanBaarEtAl2019 | psychological game theory; guilt aversion; inequity aversion | individual | 心理博弈论未充分区分guilt aversion和inequity aversion，未考虑guilt-averse偏好的情境依赖性 | 揭示guilt-averse行为可能由inequity aversion驱动且情境依赖 | guilt-averse行为是否可被inequity aversion解释；guilt-averse偏好如何随情境变化 | guilt aversion vs inequity aversion as distinct motivations | p.9 |
| Joo2024 | mind perception; blame; affective responses | individual | 仅关注责备认知过程，未考察情感反应 | 探索心智感知如何影响情感反应，扩展责备归因的机制理解 | 心智感知与情感反应之间的关系 | cognitive blame vs affective blame | p.12 |
| Joo2024 | blame; cognitive component; affective component | individual | 责备认知与情感成分关系不清楚 | 明确责备认知与情感成分的区别与联系 | 责备认知成分与情感成分在AI道德违规情境中的关系 | cognitive vs affective components of blame | p.12 |

> **已隔离**：Payne (2026) 的 5 条条目已从本表移除，全部标记为 `needs_manual_check`（见 `all_author_stated_records.csv` 第 45–59 行）。原因：部分引文非连续原句；"PTT得到验证"属当篇结果非理论展望；"machine psychology"框架名称为Agent扩写；WebFetch 截断。

## 按分析层级分组

### individual（个人层级）

| 论文 | 理论/构念 | 作者指出的理论不足 | 理论推进方向 | 待检验关系 | 可区分的解释 | 原文页码 |
|---|---|---|---|---|---|---|
| VanBaarEtAl2019 | psychological game theory; guilt aversion; inequity aversion | 心理博弈论未充分区分guilt aversion和inequity aversion，未考虑情境依赖性 | 揭示guilt-averse行为可能由inequity aversion驱动且情境依赖 | guilt-averse行为是否可被inequity aversion解释 | guilt aversion vs inequity aversion | p.9 |
| Joo2024 | mind perception; blame; affective responses | 仅关注认知过程，未考察情感反应 | 探索心智感知如何影响情感反应 | 心智感知与情感反应之间的关系 | cognitive vs affective blame | p.12 |
| Joo2024 | blame; cognitive component; affective component | 认知与情感成分关系不清楚 | 明确认知与情感成分的区别与联系 | 认知与情感成分在AI违规情境中的关系 | cognitive vs affective components of blame | p.12 |

### state_system（国家/体系层级）

> 待 Payne (2026) 核验完成后补充。5 条待核验条目涉及：deterrence theory（§3.3.6）、credibility trap（§3.3.7）、Power Transition Theory（§3.3.5）。

### AI_system（AI系统层级）

> 待 Payne (2026) 核验完成后补充。2 条待核验条目涉及：RLHF context-dependency（§3.3.7）、strategic theory / machine psychology（§1.1, Conclusion）。

## 跨论文归纳

> **当前无跨论文归纳。** 原有 4 条归纳已被移除，原因如下：

1. **"人类与AI共享情境依赖性"**：两个主体、构念和因变量都不同，最多算待研究观察，不是可用的跨论文归纳。且 Payne 端的 evidence 本身待核验。
2. **"credibility连接social preferences与地缘冲突"**：引入了尚未完成全文提取的 Rabin (1993)、Jervis (1978) 和 Schelling，并自行加入 AI opacity 机制，证据链不成立。
3. **"AI blame 2×2框架"**：引入了尚未逐篇提取的 Malle et al. (2014)，并由 Agent 自行组合成新框架，违反任务书中"不自行拼理论"的要求。
4. **"约束情境依赖性是普遍特征"**：与第 1 条基本重复，又进一步外推到"任何决策代理的普遍特征"，理论外推过大。

待以下条件满足后再重新评估跨论文归纳：
- Payne (2026) 全部记录经人工逐句核验
- 更多论文获得全文（当前仅 5/30）

## 覆盖总结

| 理论类别 | 有明确作者陈述的论文数 | 论文 |
|---------|---------------------|------|
| theory_extension | 1 | VanBaar 2019 |
| construct_refinement | 2 | Joo 2024, VanBaar 2019 |
| mechanism_specification | 1 | Joo 2024 |
| boundary_condition | 1 | VanBaar 2019 |
| theory_integration | 0 | — |
| cross_level_link | 0 | — |
| competing_explanation | 0 | — |

**重要限制**：
- 仅 5/30 篇论文有全文，25 篇不可及（全部因出版商付费墙/认证阻断）
- Payne (2026) 全部 15 条记录隔离待核验
- IgweEtAl2024 和 SIPRI2025 为方法/政策导向论文，无理论展望
- 当前覆盖不代表该领域文献中实际的理论展望丰富程度
