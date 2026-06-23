# 04 AgentA 对 AgentB 的方法抽查清单

## 使用说明

- 这份清单不是建议，而是抽查标准。
- AgentB 只要有三项以上核心项答不出来，就说明方法设计还在旧问题框架里。

## 一、研究对象抽查

- 参与者每一轮选的是 `协作架构`，还是只是在一条 AI 建议上“接受/拒绝”？
- 主因变量是 `architecture trajectory`，还是一次性 reliance？
- 设计里是否明确存在多个 autonomy level，而不是只有 `AI on/off`？
- 参与者是否真的在扮演“系统监督者/授权者”，而不是普通答题者？

## 二、识别逻辑抽查

- AI 与 human 的长期平均正确率是否严格相同？
- AI 与 human 的错误严重程度是否对齐？
- 唯一关键差异是否真的是 `error source` 与 `error timing`？
- 是否同时存在 `AI early error` 与 `human early error` 条件？
- 是否有 `AI late error` 或至少 `evenly distributed errors` 作为时间对照？
- 若没有 late-error 对照，凭什么识别路径依赖而不是一般性 aversion？

## 三、架构操作化抽查

- architecture 选项是否清楚区分 `advice`、`confirmation`、`override`、`autonomous decision`？
- 不同 architecture 的成本结构是否明示给参与者？
- autonomy 提升是否伴随更低时间成本与更低复核成本，而不是只有抽象标签？
- architecture 之间是否存在真实权衡，而不是一眼可见的支配选项？

## 四、客观基准抽查

- 是否预先定义 `objective benchmark architecture`？
- 该 benchmark 是否由准确率、错误惩罚、时间成本、人工复核成本共同构成？
- 若最终出现低 autonomy 锁定，是否能证明它偏离 benchmark，而不是本来就最优？
- 若做不到 benchmark，是否至少能证明若干条件下中等 autonomy 更优？

## 五、动态性抽查

- 轮次数是否足够让收敛出现，而不是只有早期冲击没有后期轨迹？
- 是否事先规定 steady state / convergence 的判定标准？
- 是否记录每轮 architecture choice、切换方向、切换幅度与反应时？
- 是否能识别“早期 AI 错误后，后续回到高 autonomy 的恢复速度较慢”？

## 六、机制抽查

- 你测的是 `AI 准不准` 的感知，还是 `AI 配不配占据这个位置` 的感知？
- 是否有变量刻画 architecture attraction，而不只是 trust？
- 是否区分了对 `AI output` 的评价与对 `AI role` 的评价？
- 是否计划检验 AI error 的负向更新系数是否大于 human error？
- 是否计划检验 later successes 的正向恢复是否弱于 early failures 的负向冲击？

## 七、替代解释抽查

- 是否把 general trust、risk aversion、loss aversion、betrayal aversion 当作次级解释而非主解释？
- 是否准备了控制或附加测量来区分 anthropomorphism 与 role-allocation learning？
- 若参与者只是“对新技术更谨慎”，你的设计如何排除？
- 若参与者只是“怕高风险”，你的设计如何证明他们是在学角色而不是回避损失？
- 若参与者只是“疲劳后懒得切换”，你的设计如何排除？

## 八、统计与建模抽查

- reduced-form 分析是否至少报告 treatment 对后期 autonomy level、切换率、锁定概率的影响？
- 动态模型是否能估计不同来源错误的 updating weight？
- 是否区分 immediate payoff effect 与 historical attraction effect？
- EWA 或相近动态模型是否服务于理论识别，而不是纯粹拟合？
- 是否有个体层异质性设定，允许部分人更容易锁在低 autonomy？

## 九、实验执行抽查

- comprehension check 是否确认参与者理解五类架构含义？
- 是否有练习轮让参与者学会 cost structure，而不把误解当成理论效应？
- 错误反馈是否足够显眼但不额外夸大 AI 错误的情绪冲击？
- AI 与 human 的呈现方式是否对称，避免标签本身制造额外偏差？
- 是否预先决定排除标准，防止事后删样本追显著？

## 十、最危险的方法错误

### 错误 1

把因变量做成 trust scale，然后只把 architecture choice 当补充。

### 错误 2

让 AI 条件平均更差，再把低授权解释成“偏见”。

### 错误 3

没有 late-error 对照，却声称 early error 形成路径依赖。

### 错误 4

EWA 放在附录里，正文全靠静态均值比较。

### 错误 5

没有 objective benchmark，却把任何低 autonomy 收敛都叫“锁定”。

## 十一、AgentA 认可的方法输出应满足的句式

- “参与者在重复绩效反馈中选择的是协作架构，而不是单次建议采纳。”
- “AI 与 human 的长期平均绩效被对齐，处理差异仅来自错误来源与时间分布。”
- “核心结果是后期 autonomy 收敛路径与低 autonomy 锁定，而非一次性 trust 变化。”
- “动态模型用于识别 architecture attraction updating 的非对称性，而非事后装饰。”
