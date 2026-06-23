# 03 AgentA 监管红线与阶段门

## 总原则

- 本项目允许做复杂，不允许做降级。
- 凡是会把题目写回 `trust / adoption / advice-taking / calibration` 的做法，一律视为方向性错误，而不是措辞小问题。
- 任何阶段只要触碰一票否决项，必须停下来返工，不能带病推进。

## 一票否决红线

### 红线 1

主问题被表述为“人是否信任 AI”或“是否采用 AI”。

### 红线 2

主因变量不是 architecture choice / autonomy path / convergence / lock-in，而是 trust、满意度、一次性 reliance。

### 红线 3

实验没有 repeated feedback，只是单轮或双轮 advice-taking。

### 红线 4

AI 与 human 的长期平均表现没有被严格对齐，却试图解释授权路径差异。

### 红线 5

没有操纵 `early error / late error / error source`，却声称研究路径依赖。

### 红线 6

没有客观基准架构，却声称观察到“次优锁定”。

### 红线 7

EWA 只在结果部分被拿来装饰性拟合，前面理论和设计没有按 attraction updating 构造。

### 红线 8

把 `human-in-the-loop 是否更好` 当成核心结论。

### 红线 9

把个体实验结果直接上升为“组织制度已经被证明如此形成”，没有中间桥梁。

### 红线 10

用 anthropomorphism、风险厌恶、loss aversion 等替代机制，偷换掉“AI error 改写角色授权”的主机制。

## 阶段门 0：选题冻结

### 通过标准

- 标题、摘要第一段、研究问题第一页必须出现 `architecture learning` 或等价表述。
- 文本必须明确写出：研究对象是 `AI 在流程中的角色配置`，不是 `AI 本身是否被接受`。
- 至少有一句话明确区分 capability learning 与 role learning。

### 未通过信号

- 题目里最醒目的词是 trust、adoption、reliance。
- 研究问题用的是“是否使用 AI”“是否相信 AI”。

## 阶段门 1：理论冻结

### 通过标准

- 已明确定义 architecture 的离散集合或清晰梯度。
- 已明确定义 `architecture attraction updating`。
- 已提出 `AI error -> 非对称负向更新 -> 路径依赖 -> 低 autonomy 锁定` 的完整链条。
- 已明确写出为什么 early error 比 late error 更关键。

### 未通过信号

- 机制只剩“AI 错误让人不舒服/不信任”。
- 没有说明为什么错误作用于“角色”而非只作用于“答案”。

## 阶段门 2：识别冻结

### 通过标准

- 条件至少能区分 `AI early error`、`human early error`、`even distribution`，最好再加 `AI late error`。
- AI 与 human 的长期平均准确率相同，错误严重程度相同，差异只在来源与时点。
- 不同 architecture 有清楚的时间成本、复核成本、错误成本。
- 预先定义客观最优架构或至少定义可比较的 objective benchmark。

### 未通过信号

- 某条件下 AI 客观上更差，却还试图把结果解释成“对 AI 的偏见”。
- 没有办法分离 `error timing` 与 `average quality`。

## 阶段门 3：测量冻结

### 通过标准

- 主结果变量必须包含后期平均 autonomy level、架构切换率、收敛速度、是否形成低 autonomy steady state。
- 次级结果变量可以有 trust、perceived control、betrayal concern，但不得喧宾夺主。
- 已定义 lock-in 判准，例如后 15 至 20 轮某类架构占比、波动幅度、恢复速度。
- 已定义 recovery asymmetry，能够比较“AI 后续正确表现”是否不足以对冲早期错误。

### 未通过信号

- 结果部分主要靠问卷量表堆出来。
- 没有轨迹变量，只有终点态度变量。

## 阶段门 4：模型冻结

### 通过标准

- 动态模型与理论语言一致，至少能识别不同来源错误的更新权重差异。
- 模型能区分 attraction、即时收益、历史权重、选择敏感度等核心成分。
- 有与 reduced-form 结果相互校验的策略。

### 未通过信号

- 只做静态 logit 或 OLS，然后在讨论里口头说“这说明路径依赖”。
- 动态模型无法识别 AI 与 human error 的更新系数差异。

## 阶段门 5：叙事冻结

### 通过标准

- 摘要结论必须是“长期收敛路径被改写”。
- contribution 段落必须有“从单轮 reliance 到架构学习”的升级句。
- 所有图示都要把时间顺序放进去，而不是静态方框图。

### 未通过信号

- 摘要结尾写成“AI error lowers trust and adoption”。
- 贡献段只说“补充了 algorithm aversion 文献”。

## 方法与表达的共同纪律

### 纪律 1

不能为了讲故事，把 architecture 定义得太抽象；必须可操作化。

### 纪律 2

不能为了追求“宏大”，把实验层面的学习直接等同于组织层面的制度形成。

### 纪律 3

不能为了好懂，把 asymmetry 讲成“AI 更容易背锅”这么浅。

### 纪律 4

不能为了统计显著，把长期平均质量差异偷偷放进条件差异里。

## 导师最终审查问题

- 如果把 repeated feedback 删掉，你的理论还剩什么？
- 如果把 architecture 换成一次性 advice acceptance，你的贡献还成立吗？
- 如果 AI 和 human 平均准确率不相等，你凭什么说是 learning path 而不是 rational response？
- 如果没有 objective benchmark，你凭什么说 lock-in 是次优而非理性稳态？

只要这四问里有一问答不硬，阶段门就不能过。
