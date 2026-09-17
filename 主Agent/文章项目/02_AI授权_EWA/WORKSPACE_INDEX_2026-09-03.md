# Paper 2 工作目录索引

更新时间：2026-09-17

本索引用于区分 Paper 2 的当前可编辑稿、研究记录、交付物和历史材料。源材料的原文件名与原路径保留，便于既有链接继续使用。

## 实验原型开发入口（2026-09-17 新增）

- 独立工作区：[paper2-slot-prototype](../../../projects/paper2-slot-prototype/README.md)
- 并行实施任务书：[PARALLEL_TASKS.md](../../../projects/paper2-slot-prototype/docs/PARALLEL_TASKS.md)
- 当前状态：[STATUS.md](../../../projects/paper2-slot-prototype/docs/STATUS.md)

前端使用 jsPsych，后端按统一接口替换；支持手机/电脑扫码或链接进入，现场优先、远程补充。任务是预测下一轮实际中奖的机器。第二项解释性实验仍待设计，不以工程配置替代研究决定。

此工作区已建立目录和实施规划，尚无可运行代码或部署。既有 RP、讨论记录和交付规划保留原位；后续代码与开发规格集中在该工作区，来源快照在其 sources 目录追溯。正式 LaTeX 主稿不迁移。

## 当前主稿与交付物

- 英文 LaTeX 主稿：`E:\Info_AI\LaTeX\Paper2_Asymmetric_Error_Tolerance_English_Research_Proposal_2026-08-27.tex`
- 英文 PPT：`E:\Info_AI\outputs\Paper2\deliverables\ppt\Asymmetric_Error_Tolerance_English_2026-08-27.pptx`
- PPT 生成追踪文件：同一 `ppt` 目录下的 `.trace.json`
- PDF 交付物：`E:\Info_AI\outputs\Paper2\deliverables\pdf\`

当前主稿的研究口径是 **Asymmetric Error Tolerance**：先从行为选择阈值测量单一参数 \(\alpha\)，再检验表现判断误差与真实奖金后果如何解释其变化。英文主稿不把 perceived trustworthiness、performance trust 或 attitudinal trust 作为本轮实验测量变量。

## 研究记录与分析材料

以下材料仍保留在本目录根部，作为研究思路和决策记录：

- `研究计划构造思路_人类与AI错误的非对称权重_2026-08-23.md`
- `Paper2_项目进展说明_2026-08-23.md`
- `Evidence_Map_Asymmetric_Trust_2026-08-23.md`
- `Blueprint_Asymmetric_Trust_2026-08-23.md`
- `AI_Human_Asymmetric_Error_Weighting_Discussion_Summary.md`
- `Asymmetric_Tolerance_评语_2026-08-23.md`
- `AI信任核心概念_Everett等2026_原文定义与文献来源_2026-08-22.md`
- `Paper2_EWA_参考文献导航.md`

`README.md` 和 `RP_Asymmetric_Trust_正式稿_2026-08-23.md` 保留为较早的 Asymmetric Trust 口径。阅读时以当前 LaTeX 主稿和本索引为准，不将其中已取消的信任量表或旧研究问题恢复到当前设计。

## 历史方向

经济激励、AI 能力高估和早期 EWA/重复反馈材料仍在本目录，用于追溯研究转向，不属于当前主线。包括：

- `研究计划：经济激励能否纠正 AI 非对称容忍？.md`
- `RP_AI使用经济激励与性能信任校准_正式稿_2026-08-03.md`
- `RP_使用AI的奖励与能力高估_2026-08-02.md`
- `RP_AI_Use_Rewards_and_AI_Ability_Overestimation_English_2026-08-02.md`
- `AI使用补贴作为经济激励_理论基础与研究改造讨论稿_2026-08-03.md`
- `研究计划_经济激励能否纠正AI非对称容忍_审核意见_2026-08-18.md`

这些文件没有移动，以避免破坏既有引用；它们不应被当作当前 RP。

## 审查与修订记录

- 研究一致性审查：`E:\Info_AI\outputs\RP_audit_2026-08-30\Paper2_research_alignment_review.md`
- 内容修订记录：`E:\Info_AI\outputs\RP_revision_2026-08-30\Paper2_content_changes.md`
- 语言修订与备份：`E:\Info_AI\outputs\RP_revision_2026-08-30\`
- 精简修订工作文件：`E:\Info_AI\outputs\RP_concise_revision_2026-08-30\`

这些目录是跨 Paper1–3 的修订批次，Paper2 文件按文件名识别，不将整批目录误称为 Paper2 专属目录。

## 临时构建物

Paper2 专属临时目录已集中到：

`E:\Info_AI\tmp\Paper2\`

- `pdf_checks`：LaTeX/PDF 检查产生的临时文件
- `ppt_asymmetric_trust_model_20260824`：模型 PPT 构建过程
- `paper2_bias_formation_20260806_staging`：早期 PPT 构建过程
- `asymmetric_tolerance_*`：导师 PPT 与早期审查过程
- `paper2_asymmetric_trust`、`paper2_ewa_library`：早期研究材料整理过程

跨论文的临时目录（例如合并三篇论文的渲染目录）继续留在 `tmp` 原位置。

## 维护规则

1. 新的正式英文 RP 只放在 `LaTeX`，不在 `outputs` 复制一份可编辑主稿。
2. 最终 PPT/PDF 放在 `outputs\Paper2\deliverables`，并在文件名中保留日期。
3. 新的审查和修订批次放在带日期的 `outputs\RP_*` 目录，并通过本索引补充入口。
4. 历史材料保留原路径，不覆盖当前主稿；如需移动，先更新引用路径并保留可追溯记录。
