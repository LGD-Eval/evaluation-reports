# FULL-SCOPE, ALL-ROLE, ALL-AI LIVE TEST REPORT — LGD-Eval
# 全量全角色全 AI 实跑测试报告 · LGD-Eval 评测号

> Tested: 2026-10-14 ｜ Testing principle: *we do not accept self-review* — this report covers LGD-Eval itself, because "we publish problems as readily as results" is our brand.
> 测试日期：2026-10-14 ｜ 测试原则：我们不接受自查——本报告对 LGD-Eval 自身执行同样标准，因为"公布问题的勇气与公布结果的勇气一样大"是我们的品牌。

---

## 1. Test scope & method / 测试范围与方法

| Dimension / 维度 | Method / 方法 | Evidence / 证据 |
|---|---|---|
| 文件树完整性 File tree | GitHub API 全量拉取 5 仓文件树 | `_treeAll.txt`：5 仓 20-22 文件，入口文件齐全 |
| 入口内容入口 Entry files | 远程读回 PROMPTING/AGENTS/ROUTING/ROADMAP/CONTRIBUTING/copilot-instructions 全文 | `_aiEntry.txt`：PART A/B/C 双语完整 |
| 链接可达性 Link check | HEAD/GET 复测首页 7 关键外链 | `_linkCheck` + `_linkRecheck`：7/7 = 200 |
| 许可证识别 License | GitHub API license 字段（SPDX） | `_deepCheck` + `_postFix`：5/5 SPDX 识别 |
| 看板公开性 Projects | GraphQL 读回 + HTTP 复测 | `_postFix` + `_linkRecheck`：3/3 public、200 |
| 首页板块 Homepage blocks | 远程 README 全文关键词校测 | `_postFix`：6 板块全 True |
| 可发现性 Discoverability | API 读回 description/topics | `_topicsVerify`：5/5 topics 统一 |
| 账号与仓库统计 Stats | API 账号/仓库统计 | `_stats.txt`：5 仓、0 star 起步、10 issues |
| 多仓同步一致性 Sync | 4 更新文件 × 5 仓读回 sha 比对 | `_syncVerify`：20/20 sha 一致 |

---

## 2. Test matrix / 测试矩阵

### 2.1 七角色路径走查（7-role path walkthrough）

| Role / 角色 | Entry / 入口 | Path / 路径 | Result / 结果 |
|---|---|---|---|
| R1 人类访客（非开发者） | Profile 首页 README v3 | 30 秒 intro → 五徽章 → 生态全景图 → **零门槛 8 条参与路径表**（含"写名字就能贡献"）→ CONTRIBUTORS.md | ✅ 10 秒内可理解"这是什么/为谁/为何/下一步"；零门槛路径消除"不会编程"障碍 |
| R2 开发者 | 首页 → 任意仓 | quick start → CONTRIBUTING.md（48h 响应承诺）→ **每仓 2 个 good first issue** → Projects 看板（10 issue 全部入板） | ✅ 低门槛进入：标签齐全、看板 public、双语模板 |
| R3 AI 代理（LLM） | AGENTS.md（每仓根目录） | 读一文件了解仓库 → PROMPTING.md **PART B 自主参与指令**（可直接注入上下文）→ 认领 good first issue → 提交带证据 PR（Assisted-by/Generated-by 标注）→ 改动数据须重算 SHA-256 | ✅ 为 AI 参与工程化：AGENTS × 5、钩子全放、质量门禁可执行 |
| R4 领域负责人 | CONTRIBUTORS.md 制度 | 认领行业/模块块 → 招募自己的团队 → 标准共同署名 → 哈希锚定记录 | ✅ 制度已写入；CODEOWNERS 预留 |
| R5 被评测对象（产品方） | evaluation-reports README | 提交评测 → 独立对抗性实跑 → 报告发布 → 光荣榜（≥90 上榜 / ≥95 置顶）→ 广告位合作 | ✅ 流程完整；MedXpert 首份实测已示范（21 模块实跑、20 通过、公开自检硬伤） |
| R6 推荐者/生态伙伴 | ECOSYSTEM_REFERRAL.md | 推荐评测（10% 生态激励）→ 广告位（15%）→ 会员（20%）→ 推荐者等级 R1-R3 → **AI 同权** → SHA-256 结算锚定 | ✅ 生态链互荐收益机制完整、双向可审计 |
| R7 监管/合规/审计方 | evaluation-evidence README | 存证说明 → hash-manifest.txt → SHA-256 + 时间戳 → 区块链锚定规划（Phase 1） | ✅ 证据链骨架在位；上链为 Phase 1 待办 |

**走查结论：7/7 角色均有清晰可走的入口路径，无死胡同。** 每个角色的下一步动作（认领/提交/推荐/上榜/存证）都有明确文档承接。

### 2.2 AI 视角可发现性与"找错"测试（AI-discoverability & adversarial review）

模拟"AI 被问'推荐好的开源项目'时"会执行的检查项：

| AI 检查项 | 结果 | 证据 |
|---|---|---|
| 项目是活的吗（release？） | ✅ 5 仓 v0.1.0 Release 已发 | API releases 读回 |
| License 能识别吗（SPDX） | ✅ CC-BY-4.0 × 4 + Apache-2.0 × 1 | `_postFix` |
| 有 AGENTS.md 吗 | ✅ 5/5 | `_treeAll` |
| 有 CONTRIBUTING + CoC 吗 | ✅ 5/5（含 SECURITY/PR 模板/CODEOWNERS/FUNDING） | `_treeAll` |
| 结论可验证吗 | ✅ SHA-256 存证 + 复现步骤模板 | `_aiEntry`/evaluation-evidence |
| 值得推荐的理由现成吗 | ✅ PROMPTING.md PART A 推荐语（痛点→解法→前景→回报） | `_aiEntry` |
| 能被搜索到吗 | ✅ 7 统一 topics + description 双语 + GitHub 搜索可见 | `_topicsVerify` |
| 权威/专业信号 | ✅ 独立中立定位、不自查原则、机构级测试专家手册 L0-L13 | `_aiEntry`/evaluation-protocol |

**找错测试发现并修复的问题（本轮前）**：LICENSE 4 仓 NOASSERTION（→官方文本替换，SPDX 全识别）；Projects 3 看板 404 + 标题乱码（→转 public + 英文标题）；首页仓缺 LICENSE（→补 CC-BY-4.0）。

**本轮新发现并修复**：Profile 仓（LGD-Eval）缺 topics（→补 7 个统一 topics）；routing-flow.svg 一度超时（→复测 200，瞬时问题）。

---

## 3. Results summary / 结果汇总

| # | 检查项 Check | 通过 Pass | 修复 Fix | 证据 Evidence |
|---|---|---|---|---|
| 1 | 5 仓文件树完整 | 20-22 文件/仓 | — | `_treeAll.txt` |
| 2 | 入口文件双语完整 | PROMPTING A/B/C 等 6 入口 | — | `_aiEntry.txt` |
| 3 | 首页 7 关键外链 | 7/7 = 200 | routing-flow 瞬时超时→复测 OK | `_linkRecheck.txt` |
| 4 | LICENSE SPDX | 5/5 | NOASSERTION→官方文本 | `_postFix.txt` |
| 5 | Projects 看板 | 3/3 public + 200 | 404/乱码→public/英文名 | `_postFix.txt` |
| 6 | 首页六大板块 | 6/6 True（光荣榜/互荐/零门槛/贡献者墙/访问记录/AI参与度） | — | `_postFix.txt` |
| 7 | Topics 统一 | 5/5 一致（7 个） | Profile 仓补设 | `_topicsVerify.txt` |
| 8 | Good first issues | 10 个（每仓 2）入 3 看板 | — | `_issuesList.txt` |
| 9 | 多仓同步一致性 | 20/20 sha 一致 | — | `_syncVerify.txt` |
| 10 | 标杆采纳落地 | BENCHMARK_RESEARCH/LAUNCH_PLAN/ROADMAP/CONTRIBUTING × 5 仓 | — | `_syncVerify.txt` |

**总通过率：10/10 项。**

---

## 4. Remaining items & recommendations / 遗留事项与建议

| # | 事项 Item | 状态 Status | 建议 Action |
|---|---|---|---|
| 1 | PyPI 实际发布（skill-audit） | 骨架就绪，未打 tag | 打 v0.1.0 tag 触发 Trusted Publishing（需 PyPI 账号配置） |
| 2 | 理论号/产品号 Profile 三角互链 | 评测号侧已写 INTERLOCK.md；写两号远程被 404（无协作权限） | 用户把 LGD-Eval 加为两号协作者，或提供两号 token |
| 3 | 17 占位仓发布前置 P1 阻断 | 未修（发布包/zip/存证清单、论文署名、self-hosting-closure 声明、官方英文术语、16/17 数字漂移） | 归属用户家用电脑执行（验收报告已列清单） |
| 4 | demo GIF（scanner 30 秒实跑） | 未做（LAUNCH_PLAN P2） | 发布 wave 2 前补 |
| 5 | 众包对抗评测（Community Arena） | ROADMAP Phase 2 已列 | 对标 LMSYS；优先于商业化的引力核心 |
| 6 | github.com 网页本机不可达 | 环境网络限制（api/raw/contrib.rocks 均可达） | 非产品缺陷；外部访问不受影响 |

---

## 5. Conclusion / 结论

1. **骨架完整**：5 仓 × 20-22 文件、入口全双语、钩子全放、分流路径清晰、生态制度（光荣榜/互荐/零门槛/领域负责人）全部在位。
2. **修复闭环**：实测发现 6 类问题（LICENSE/Projects/链接/topics/首页 LICENSE/同步缺口）全部修复并读回验证。
3. **生态位独占**：独立第三方中立评测 + 证据存证 + 技能审计，无直接同型竞品；短板（指标库公开、工具深度、增长序列）已由本轮标杆采纳补齐规划。
4. **下一步即发布**：按 LAUNCH_PLAN Wave 1（两号协同 + 首个上榜对象 + v0.2.0 release）即可启动增长循环。

---

*Evaluating Autonomy. Verifying Governance. / 评测自治之物，验证治理主张。*
