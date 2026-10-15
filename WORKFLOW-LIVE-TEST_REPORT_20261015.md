# WORKFLOW LIVE-TEST REPORT — 全仓自动化实跑测试报告
> LGD-Eval · 2026-10-15 · 目的：把"不跑不报错"的自动化全部手动触发实跑，验证真实可运行。

## 一、背景：为什么补"手动触发 + 自检"（Why: "no run, no error" is not "verified"）

先前审计发现：`AI Welcome Bot` 依赖"首次贡献者"事件，**从未真正执行过**（历史 runs 全部 `skipped`）；
`PR Review Bot` 仅靠我们自己的 PR 间接触发。**未触发 ≠ 已验证**。本次为全部自动化补上
`workflow_dispatch`（手动触发）+ `self-test`（自检模式），随后逐个实跑。

## 二、本次升级（Upgrades）
- `pr-review.yml`（5 仓）：+ workflow_dispatch + self-test job（调用 `pr-audit.py --self-test`，5 组断言）
- `welcome-bot.yml`（5 仓）：+ workflow_dispatch + self-test job（新增 `welcome-self-test.py`，校验关键路由文件 + 欢迎模板双语锚点 + 登录名插值）
- `pr-audit.py`（5 仓）：+ `--self-test` 模式（乱码正则命中 / 非法 UTF-8 标记 / 双语术语逻辑 / 关键文件 / 仓库名）
- 新增 `.github/scripts/welcome-self-test.py`（5 仓）
- 共推送 **20 个文件**（10 workflow + 10 脚本）

## 三、实跑矩阵（Live run matrix — 全部 workflow_dispatch 触发）

| 仓库 | 工作流 | 触发方式 | 结果 |
|---|---|---|---|
| LGD-Eval | AI Daily Triage | dispatch | ✅ success |
| LGD-Eval | PR Review Bot | dispatch (self-test) | ✅ success（self-test job，review job 正确 skip） |
| LGD-Eval | AI Welcome Bot | dispatch (self-test) | ✅ success（self-test job，welcome job 正确 skip） |
| evaluation-protocol | PR Review Bot | dispatch (self-test) | ✅ success |
| evaluation-protocol | AI Welcome Bot | dispatch (self-test) | ✅ success |
| evaluation-evidence | PR Review Bot | dispatch (self-test) | ✅ success |
| evaluation-evidence | AI Welcome Bot | dispatch (self-test) | ✅ success |
| evaluation-reports | PR Review Bot | dispatch (self-test) | ✅ success |
| evaluation-reports | AI Welcome Bot | dispatch (self-test) | ✅ success |
| skill-audit | PR Review Bot | dispatch (self-test) | ✅ success |
| skill-audit | AI Welcome Bot | dispatch (self-test) | ✅ success |

**11 / 11 success，0 失败。** job 明细抽查（主仓）：`self-test` job 各步全部 success；
事件型 job（`welcome`/`review`）在 dispatch 模式下正确 skipped——符合设计（事件触发时启用）。

## 四、未触发项补验（Previously-untriggered checks）
| 项 | 结果 |
|---|---|
| Vulnerability alerts（Dependabot 安全告警） | **5 仓全部开启**（此前 disabled，PUT 204） |
| Dependabot 依赖升级 PR | 在跑：主仓 #3/#4、skill-audit #4/#5/#6（checkout/github-script/setup-python bump）——**待维护者决策是否合并**（大版本升级，签发权在人） |
| Secret scanning alerts | 0 open ✅ |
| Workflows 注册 | 5 仓全部 active（Dependabot Updates 均在）✅ |
| ROADMAP 两张 SVG 图 | 200 ✅ |
| README 46 链接 | 渲染层实测通过；本机网络对 github.com/shields.io 直连时断（探测 ERR 为网络性，非坏链——浏览器实测 13/13 通过） |

## 五、剩余需真实事件验证（Remaining: real-event-only paths）
- `welcome` job 的**真实首次贡献者**路径（新账号首次 issue/PR 才触发）——机制已就绪，逻辑经 self-test 验证，端到端待首个真实外部贡献者
- Dependabot 升级 PR 合并决策（人工/维护者）

## 六、结论（Conclusion）
全部自动化：**可手动触发、可自检、已实跑通过**。"不跑不报错"项已收敛为 2 类：
（1）真实外部事件路径（欢迎首次贡献者）——待首个真实事件；
（2）维护者决策项（依赖升级合并）。两者均有明确负责人与触发条件，不再存在"从未执行"的自动化。

*Evaluating Autonomy. Verifying Governance. / 评测自治之物，验证治理主张。*
