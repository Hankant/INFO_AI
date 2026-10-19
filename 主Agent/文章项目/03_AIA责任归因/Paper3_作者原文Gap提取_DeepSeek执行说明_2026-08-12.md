# Paper 3：作者原文 Gap 提取（DeepSeek 批处理）

## 一、任务边界

该批处理只负责从现有文献全文中提取作者明确写出的证据，不负责提出 Paper 3 的研究问题或理论框架。

五类提取对象：

1. `identified_research_gap`：作者用于说明本研究必要性的既有研究缺口。
2. `acknowledged_limitation_or_remaining_gap`：作者承认的本研究局限、边界或仍未解决的问题。
3. `future_research_direction`：作者明确提出的未来研究方向。
4. `critique_of_prior_literature`：作者对既有文献、理论、方法、测量或证据的直接批评。
5. `author_stated_theoretical_outlook`：作者明确提出的理论含义、理论延伸或未来理论工作。

新版 prompt 进一步把未来研究区分为理论延伸、构念细化、机制识别、边界条件、理论整合、跨层级联系、竞争性解释、纯方法建议、纯情境扩展和政策实践建议。理论类条目还记录原始理论/构念术语、文中理论来源、分析层级、作者指出的理论不足、作者提出的理论推进及待检验关系。纯方法建议单独标记，不能充当理论展望。

以下内容不得收录：模型推断出的 gap、宽泛背景、当前论文的贡献陈述、参考文献表、编辑或审稿意见、无法在全文原页复核的引文。

## 二、输入

- 文献清单：`E:\Info_AI\defense_project\reference_materials\paper3_responsibility_social_conflict\manifest.csv`
- PDF 根目录：默认覆盖整个 `reference_materials` 共享文献库，并递归查找 `papers_originals` 等子目录。
- PDF 命名：优先读取 `manifest.csv` 的 `local_pdf`，也会查找 `<bib_key>.pdf`。

目前清单共 30 篇。若 PDF 尚未下载，程序会将其记为 `missing_full_text`，不会读取摘要替代全文。

## 三、DeepSeek 配置

API 密钥只放在环境变量中，不写入脚本或输出：

```powershell
$env:DEEPSEEK_API_KEY = '<你的密钥>'
```

脚本默认使用当前 DeepSeek API 的 `deepseek-v4-pro`。需要改用其他可用模型时：

```powershell
$env:DEEPSEEK_MODEL = '<模型名>'
```

## 四、先做本地全文盘点

```powershell
& 'C:\Users\69596\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' `
  'E:\Info_AI\defense_project\reference_materials\paper3_responsibility_social_conflict\extract_author_stated_gaps_deepseek.py' `
  --dry-run
```

该命令检查 PDF 是否存在、是否为有效 PDF、能否提取文本，以及每篇预计拆成多少个 API 请求，不调用 DeepSeek。

## 五、试跑一篇

```powershell
& 'C:\Users\69596\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' `
  'E:\Info_AI\defense_project\reference_materials\paper3_responsibility_social_conflict\extract_author_stated_gaps_deepseek.py' `
  --keys Joo2024
```

如需指定一个已经到位的条目，将 `Joo2024` 换成相应 `bib_key`。

## 六、运行全部全文

```powershell
& 'C:\Users\69596\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' `
  'E:\Info_AI\defense_project\reference_materials\paper3_responsibility_social_conflict\extract_author_stated_gaps_deepseek.py'
```

程序按整篇 PDF 逐页处理，以约 24,000 字符为一个请求块。已完整处理的论文会自动跳过；中断后重新执行同一命令即可继续。使用 `--force` 才会覆盖已完成结果。

## 七、输出

默认输出目录：

`E:\Info_AI\defense_project\reference_materials\paper3_responsibility_social_conflict\author_stated_gaps_v2_theory`

- `processing_status.csv`：30 篇文献的全文与处理状态。
- `all_verified_items.csv`：所有通过本地原文匹配的结构化条目。
- `theory_outlook_only.csv`：仅保留理论延伸、构念细化、机制、边界、理论整合、跨层级联系和竞争性解释。
- `author_stated_gap_matrix.md`：先展示理论展望优先索引，再按论文汇总五类完整证据。
- `papers\<bib_key>.json`：逐篇完整结果、请求块记录和 token 用量。
- `rejected_items.jsonl`：引文无法在指定页匹配、类别非法或批评对象缺失的拒收项。

## 八、质量控制

1. 每个请求都带有 `[[PAGE N]]` 页码标记。
2. DeepSeek 只能复制单页内的连续原文。
3. 返回结果使用 JSON 模式并限制为四个固定类别。
4. Python 在本地规范化换行和断词后，检查引文是否真实存在于模型指定的 PDF 页。
5. 未通过反向匹配的条目只进入 `rejected_items.jsonl`。
6. 汇总文件只接受 `quote_verified=true` 的条目。
7. 后续理论筛选必须回到原文上下文复读；该矩阵是候选证据索引，不能直接替代人工理论判断。
