# Knowledge Graph Viewer — 运行指南

## 启动

```bash
cd "e:\Info_AI\defense_project\reference_materials\knowledge_graph"
py -m http.server 8765
```

然后浏览器打开：

```
http://127.0.0.1:8765/index.html
```

> 注意：必须用 HTTP 服务器，不要直接双击打开 HTML。`file://` 协议下 `fetch()` 会被浏览器拦截。

## 三个 Tab

| Tab | 内容 | 用途 |
|-----|------|------|
| **Concept Co-occurrence** | 68 论文 + 184 概念，二分图 | 看哪些论文讨论相似主题、定位概念簇 |
| **Category Hierarchy** | 10 类别 + 68 论文，分层布局 | 看主题分布、类别结构 |
| **Temporal Evolution** | 68 论文按年份分层，24 共被引边 | 看研究脉络演化、共被引关系 |

## 交互

- **点击节点** → 右侧详情面板
- **点击 concept tag** → 自动跳转到 Tab 1 并高亮该概念
- **拖拽 / 缩放** → 画布操作（默认开启）
- **顶部搜索** → 输入标题/作者/概念名过滤
- **类别筛选** → 多选下拉框
- **年份范围** → 输入 min/max
- **Reset 按钮** → 清除所有过滤

## 数据规模

- 68 篇论文
- 184 个概念
- 10 个类别
- 24 条共被引边（实际 23 唯一对，有 7 对重复）

## 已知问题（不影响使用）

- `cited_count` 字段缺失 → viewer 用 `cited_in.length` 作 fallback
- 部分 LaTeX 转义字符可能在浏览器显示为源码（如 `\&`）
- 7 对重复的共被引边未去重

详见 [`data_integrity_report.md`](./data_integrity_report.md)。

## 依赖

- vis-network 9.1.9（从 unpkg.com CDN 加载）
- 现代浏览器（Chrome / Edge）
- Python 3（仅用于本地 HTTP 服务器）