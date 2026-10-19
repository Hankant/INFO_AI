# 仓库管理与同步规则

## 当前边界（2026-10-10）

- 研究仓库：`E:\Info_AI`，现有远端 `https://github.com/Hankant/INFO_AI.git`。
- 实验仓库：`E:\Info_AI\projects\paper2-slot-prototype`，独立 `.git`，分支 `main`，跟踪独立私有远端 `https://github.com/Hankant/paper2-slot-prototype.git` 的 `origin/main`。2026-10-10 已推送 6 次拆分历史提交，顶端为 `0ab97f1`；现有未提交功能改动尚未上传。
- 国自然题目一、题目四及博士论文保留在研究仓库，通过根 README 分区导航。
- 实验路径不变，现有依赖、运行数据与本地启动配置留在原处。两个仓库分别提交；在研究根目录执行 Git 命令不再管理实验文件。

## 默认同步顺序

用户说“同步 Git”或“更新项目到 Git”时，先检查实验仓库。若明确指定某个研究子课题，则按指定范围执行。

1. 在实验仓库检查 `git status --short`、差异和未跟踪文件；保留其他任务在途改动。
2. 按改动执行相关测试。运行数据、SQLite 数据库、参与者信息、管理凭证、`.env`、依赖及构建产物不提交。忽略规则不能替代对已跟踪文件的审查。
3. 显式暂存本次涉及的实验文件，单独提交。不要在研究根目录执行 `git add .` 或 `git add -A` 来同步实验。
4. 核实实验仓库的 `origin` 为 `https://github.com/Hankant/paper2-slot-prototype.git`；该私有仓库已创建。不得将实验提交推向 `INFO_AI` 的 `main`。
5. 推送实验仓库，并核对远端分支提交与本地一致。已有其他本地未推送提交时，先检查这些提交，因为 push 推送的是提交历史，不是指定目录。
6. 随后根据用户范围处理研究仓库。论文、国自然子课题、文献库分别审查和提交，不自动打包全部未提交材料。

只读检查：

```powershell
git -C E:/Info_AI/projects/paper2-slot-prototype status --short
git -C E:/Info_AI/projects/paper2-slot-prototype remote -v
git -C E:/Info_AI status --short
```

## 拆分记录与恢复依据

- 从原仓库 `5802343` 提取实验目录历史，实验历史顶端为 `0ab97f15436d8ebe5b0ac3715c3f11f965364707`，共 6 个提交。
- 原仓库保留 `codex/experiment-history` 分支作为本地历史引用，不需要将其推送到研究远端。
- 初始化实验仓库后只重建索引，未检出或覆盖工作文件；229 个已跟踪或未忽略文件的 SHA-256 全部与拆分前一致。
- 本地审计文件在 `tmp/repository-split-20261010/`，包含文件哈希清单、原跟踪清单与未提交差异。该目录不提交。
- 原仓库的实验文件移除仅使用 `git rm --cached`，文件仍在磁盘；这批索引删除是停止跟踪的迁移变更，需与根 `.gitignore` 和本次导航文档作为独立整理提交处理。
- 本次未提交既有实验功能改动，也未执行功能测试；文件一致性验证不代表功能测试通过。
- 未来换电脑需分别克隆两个仓库，再安装实验依赖。本地私有数据和凭证通过单独的备份恢复。
