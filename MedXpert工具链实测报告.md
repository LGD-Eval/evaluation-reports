# MedXpert 医疗产品线工具链实测报告
# MedXpert Medical Toolkit Live Test Report

> **Evaluation body / 评测方**: LGD-Eval evaluation line · independent third party（Lifecycle Governance Doctrine）
> **Subject / 被评测方**: GitHub 账号 `stevenzhao07`（25 仓，其中 21 个自有工具 + 3 个 fork + 1 个 profile）；锚点仓 `medical-ai-toolkit@8bcb152cd0b3`
> **Evaluation time / 评测时间**: 2026-10-14（+08:00）
> **Environment fingerprint / 评测环境指纹**: 本机 Python 3.12.10（零依赖标准库运行）
> **Method / 实测方法**: 真实拉取全部仓库 README 与路由文件 → 本机实跑 router.py / discover.py / 4 个代表性工具 → 10 个业务场景路由命中测试
> English: this report evaluates the `stevenzhao07` GitHub account (25 repos: 21 own tool modules + 3 forks + 1 profile) for runnability, discoverability and AI-loadability of the MedXpert toolchain (2026-10-14).

---

## 一、结论速览

| 验证项 | 结果 | 说明 |
|---|---|---|
| 工具覆盖度 | ✅ 基本完整 | 21 个自有模块覆盖医械 AI 全生命周期 7 大阶段，核心环节均有专用工具 |
| 工具可运行性 | ✅ 抽样 4/4 通过 | pms-vigilance 7/7、udi-assignment 6/6、ml-validation 3/3、ai-a3-laws 3/3 自测全过 |
| 路由可发现性 | ✅ 21/21 可发现 | router.py 列出全部模块，10 个场景命中率 100%（首选正确 8/10，次选正确 2/10） |
| AI 技能加载载体 | ✅ 完整 | AGENTS.md / CLAUDE.md / llms.txt / module.json / skeleton.json / teamai/skills 21 个 SKILL.md 全部真实存在 |

**总体结论**：这套"骨架 + 可插拔技能 + AI 自动路由"的套娃结构是真实落地、可运行的，不是空壳。AI（编码代理）克隆门户即可发现全部 21 个技能并按意图懒加载。存在 2 处路由首选歧义与若干覆盖缺口（详见第四节）。

---

## 二、覆盖度实测（21 模块 × 7 阶段）

| 生命周期阶段 | 直接支持工具 | 相关工具 | 覆盖评价 |
|---|---|---|---|
| 设计研发 | design-controls(ISO13485§7.3/820.30)、iec62304(软件分级) | iso14971、udi、cybersecurity、delivery-guard | ✅ 完整 |
| 验证与安全 | iso14971(风险矩阵)、iso10993(生物相容)、sterilization(灭菌/F0)、cybersecurity(81001-5-1/FDA)、ml-validation(AUC/公平性) | delivery-guard | ✅ 完整 |
| 临床评价 | clinical-evaluation(CER/PMCF) | fhir-ortho、omop-ortho | ⚠️ 偏薄（无临床试验管理模块） |
| 注册申报 | device-regulatory-map(NMPA/EU/FDA/PMDA)、samd-ra-toolkit、udi-assignment | clinical-eval、fhir、multilingual-ifu | ✅ 完整 |
| 生产质量 | manufacturing-gmp(含 2025/2014 diff) | design-controls、sterilization、udi、ifu、delivery-guard | ✅ 完整 |
| 上市后 | pms-vigilance(时限计算) | iso14971、fhir、omop | ⚠️ 偏薄 |
| AI 治理 | ai-a3-laws(三定律)、ai-governance-checklist、ai-model-passport | delivery-guard、ml-validation、samd-ra | ✅ 完整 |

**辖区覆盖**：代码层已实现 CN(NMPA) / US(FDA) / EU(MDR) / JP(PMDA) 四辖区；ASEAN / LATAM **明确未实现**（README 明示拒绝，21/21 模块）。

---

## 三、路由命中实测（AI 能否找到对应技能）

**实跑方式**：`python router.py "<业务意图>"`，router 按 module.json 的 triggers 加权匹配（intent 3 > keyword 2 > provides 1）。

| # | 业务场景 | 首选命中 | 结果 | 次选 |
|---|---|---|---|---|
| 1 | 骨科植入物风险评估与风险管理文件 | iso14971-risk-file | ✅ | iec62304, fhir-ortho |
| 2 | NMPA 二类医疗器械注册分类查询 | device-regulatory-map | ✅ | iec62304, ai-a3-laws |
| 3 | 欧盟不良事件报告时限 | pms-vigilance | ✅ | iec62304, sterilization |
| 4 | 灭菌验证 F0 值计算 | sterilization-validation | ✅ | ml-validation, delivery-guard |
| 5 | 给骨科器械生成 UDI 条码 | fhir-ortho-toolkit | ⚠️ 首选歧义 | **udi-assignment**（更准确） |
| 6 | AI 模型人群公平性评估 | ai-governance-checklist | ⚠️ 首选歧义 | **ml-validation-toolkit**（更准确） |
| 7 | 给医疗 AI 系统签发 AI 护照 | ai-model-passport | ✅ | gov-checklist, portal |
| 8 | CE 标志临床评价报告 | clinical-evaluation | ✅ | pms-vigilance, iso10993 |
| 9 | GMP 生产质量管理规范自查 | manufacturing-gmp | ✅ | iec62304, iso14971 |
| 10 | 软件安全等级 A/B/C 判定 | iec62304-software | ✅ | cybersecurity, pms-vigilance |

**命中率**：10/10 有命中（100% 可发现）；首选精确 8/10；2 处首选偏到语义相近模块，但次选正确——AI 能找到技能，但可能先打开稍欠精确的模块。

---

## 四、发现的问题与缺口

### 路由层（2 处，建议优化）
1. **UDI 场景首选歧义**：`fhir-ortho-toolkit` 因含"骨科+udi"双关键词权重高于 `udi-assignment`（专做赋码）。建议给 udi-assignment 增加"赋码/条码/GTIN/校验位"高权重 triggers。
2. **公平性场景首选歧义**：`ai-governance-checklist` 的 "fairness" 关键词命中优先级高于 `ml-validation-toolkit`（真正计算公平性缺口）。建议给 ml-validation 增加"子组公平/均等/equity gap"专属关键词，或调整权重。

### 覆盖层（5 处，均为建议而非缺陷）
3. **辖区缺口**：ASEAN（新加坡 HSA/泰国 TFDA）、LATAM（ANVISA）代码层未实现；官网宣称"东南亚/拉美"是人工咨询服务口径，README 已诚实澄清——若工具链要出海需扩展 JURISDICTIONS。
4. **医院端偏薄**：AI 护照、IFU、ml-validation 可服务医院，但缺"医疗 AI 采购评估/设备入院评估"专用模块。
5. **临床试验管理（CTMS/EDC）缺位**：clinical-evaluation 覆盖 CER/PMCF 规划，不含试验执行管理。
6. **卫生经济学/医保准入（HTA/reimbursement）缺位**：医院与监管常见场景无专用工具。
7. **文档口径不一致**：llms.txt 写"AI 治理 9"，最新 README/module.json 是"AI 治理 4 + AI/ML 2 + 互操作 3"；README 的"21/21 模块已实现 selftest"与"🔵 专家评审全线 pending"并存（诚实但易误读）。

### 成熟度（项目自述，非缺陷）
8. 全部模块 🔵 专家评审 **pending**，⚪ 官方源验证部分完成——定位为"参考实现 + 决策支持"，README 免责声明完整（不构成注册申报依据）。

---

## 五、验证方法与复现

所有结论均可复现，关键命令：

```bash
# 1. 路由表（21 模块全列出）
git clone https://github.com/stevenzhao07/medical-ai-toolkit.git
python router.py --list

# 2. 意图路由（10 场景实测）
python router.py "骨科植入物断裂风险评估与风险管理文件"

# 3. 门户发现（20 模块路由表 + 自测）
python scripts/discover.py --demo && python scripts/discover.py --selftest

# 4. 抽样工具自测（4 个全部 PASS）
git clone https://github.com/stevenzhao07/pms-vigilance.git && python scripts/pms_report.py --selftest
git clone https://github.com/stevenzhao07/udi-assignment.git && python scripts/udi_assign.py --selftest
git clone https://github.com/stevenzhao07/ml-validation-toolkit.git && python scripts/ml_validation.py --selftest
git clone https://github.com/stevenzhao07/ai-a3-laws.git && python scripts/a3_laws.py --selftest
```

**数据来源**：全部来自 GitHub 真实仓库内容（25 仓 README、medical-ai-toolkit 源码文件树 125 个文件、模块仓 18-34 文件的结构核查、本机实际运行输出）。覆盖矩阵的阶段映射为基于各模块 README 声明的人工归类。

---

## 六、改进意见（14 条，按优先级矩阵）

优先级矩阵坐标：横轴=实施成本（1-5），纵轴=影响价值（1-5）。A=结构性，B=覆盖层，C=工程质量，D=生态。

| 编号 | 成本 | 价值 | 意见 | 说明 / 改法 |
|---|---|---|---|---|
| A1 | 1 | 4 | 修复路由首选歧义 | 实测"UDI 条码"首选偏到 fhir-ortho、"公平性评估"首选偏到 gov-checklist。给 udi-assignment 加"赋码/条码/GTIN/校验位"关键词；ml-validation 加"子组公平/equity"并提权重 |
| A2 | 2 | 3 | router 增加同族模块推荐 | README 的关联模块信息未被 router 利用；建议 route() 返回"首选+备选"而非只取 top1 |
| A3 | 2 | 4 | triggers 增加专属词+排除词 | 纯正向加权无法判别"谁更专属"；支持 negative_triggers 降权 |
| B1 | 4 | 4 | 扩展 ASEAN/LATAM 辖区 | 现状仅 CN/US/EU/JP；优先新加坡 HSA + 巴西 ANVISA |
| B2 | 2 | 3 | 医院侧 AI 护照验证器 | 护照有签发无医院侧验证/采购评估落地包 |
| B3 | 3 | 4 | 注册申报文件包生成器 | 把 DHF 索引、CER、风险文件汇总成申报文档树 |
| B4 | 2 | 3 | GMP 2025 条款框架随仓 | 13 章 84 条结构 JSON 随仓，避免用户自备条款 |
| B5 | 4 | 3 | 临床试验管理 CTMS/随访 | CER/PMCF 是规划层，缺试验执行/随访数据 |
| B6 | 4 | 3 | 上市后信号检测工具 | 不良事件数据→信号识别/趋势告警 |
| C1 | 1 | 3 | 模块 README 挂 CI 徽章 | 验证状态表变可点击核验 |
| C2 | 2 | 4 | manifest 生成器统一文档 | 实测 llms.txt("AI 治理 9")与 README(4) 口径漂移；统一从 module.json 生成 AGENTS/llms.txt/README |
| C3 | 2 | 3 | 全模块仓统一 CI+selftest | 21 模块都有 --selftest，建议统一 workflow 模板批量启用 |
| D1 | 3 | 5 | 推进上游投稿获背书 | OWASP/OpenRegulatory/HL7/OHDSI 促成 1-2 个合并，缓解"专家评审 pending" |
| D2 | 3 | 3 | 双账号技能格式互通 | 主账号 109 技能仓与 teamai/skills 21 个 SKILL.md 统一规范，形成生态闭环 |

**建议执行顺序**：A1+A3（半天，直接提升路由准确性）→ C2 → B1/B3 → D1 → B2/B4/C1/C3 → B5/B6（较大工程排后）。

---

## 七、认知边界与「提醒价值」复盘（方法论反思）

> 本节记录实测过程中的认知复盘：哪些是无需用户说明、仅凭公开信息即可自明的；哪些是用户点明方向后才执行深挖的；以及本次实测的方法论约定。

### 7.1 无需提醒即可自明（浅层理解）

- **账号定位**：从 profile 与 bio 可直接得出"医疗器械合规 + AI 治理"定位；
- **工具矩阵**：21 个模块的分类、功能、适用阶段，读 README 即可建立；
- **账号关联**：从 `uibc-core` / `silent-failure-catalog` 的 fork 关系与 `lgd-theory` 的 SSOT 引用，可推断"理论仓在上游、工程仓在下游"；
- **架构线索**：每个 README 都明示"可插拔模块契约（lgd-skeleton/1.0）"、"机器可发现入口：AGENTS.md · CLAUDE.md · llms.txt"——线索一直都在文档里。

### 7.2 需用户提醒才执行（深层验证）

- 不会**主动**拉取 `router.py` 源码、在本地实跑、验证"AI 自动加载技能"是否真实工作——默认行为是"浏览 + 归纳"，而非"审计 + 实跑"；
- 不会把"套娃结构/可插拔"当作**待验证的架构假设**，而只当作仓库自述文案；
- 不会把两个账号连成"同一人 + 理论/工程分工"的完整体系图——fork 关系只能证明关联，分工意图只能由账号所有者确认。

### 7.3 提醒的实质作用

| 维度 | 未提醒（默认浏览） | 提醒后（本次实测） |
|---|---|---|
| 深度 | 理解文档 | 验证系统 |
| 手段 | 读 README + 归纳 | 拉源码 + 本机实跑 + 场景测试 |
| 产出 | 概览 | 可复现结论（覆盖度/命中率/缺口） |
| 可证伪性 | 低（信仓库自述） | 高（负对照 + 退出码 + 输出核验） |

### 7.4 默认行为边界声明

本报告的结论均产生于"深挖 + 实跑"模式（用户明确要求实测后执行）。默认情况下对 GitHub 仓库类请求的处理深度为**读得细、验证得浅**；若期望后续对"自称有架构"的项目默认做到源码级核验与实跑验证，需在任务开始时明确声明，或作为长期偏好设定。

---

## 八、全量实跑结果（21/21 模块，2026-10-14 本机 Python 3.12 实测）

> 方法：逐个下载各模块 `scripts/*.py`，运行 `--selftest` 与 `--demo`；输出重定向至 UTF-8 文件后核验退出码与断言输出。下载瞬时失败项均已重试并澄清。

| 模块 | selftest | demo | 备注 |
|---|---|---|---|
| ai-a3-laws | ✅ 3/3 | OK | 含负对照 |
| ai-governance-checklist | ✅ 3/3 | OK | 含负对照 |
| ai-model-passport | ✅ 3/3 | OK | 含负对照 |
| biocompatibility-iso10993 | ✅ 4/4 | OK | |
| clinical-evaluation | ✅ 5/5 | OK | |
| cybersecurity-medical | ✅ 4/4 | OK | |
| delivery-guard | ✅ 3/3 | OK | 首测"下载失败"为网络瞬时，重试 PASS |
| design-controls-toolkit | ✅ 3/3 | OK | |
| device-regulatory-map | ✅ 4/4 | OK | |
| fhir-ortho-toolkit | ✅ 4/4 | OK | |
| iec62304-software | ✅ 7/7 | OK | |
| iso14971-risk-file | ✅ 5/5 | OK | |
| manufacturing-gmp | ✅ 4/4 | OK | 重试后 PASS |
| medical-ai-toolkit | ✅ 3/3 | OK | 重试后 PASS |
| ml-validation-toolkit | ✅ 3/3 | OK | |
| multilingual-ifu | ❌ **FAIL** | OK | **真实缺陷：selftest 期望 `--lang-dir .` rc=0，实际 rc=2** |
| omop-ortho-toolkit | ✅ 4/4 | OK | |
| pms-vigilance | ✅ 7/7 | OK | 重试后 PASS |
| samd-ra-toolkit | ✅ 5/5 | OK | |
| sterilization-validation | ✅ 7/7 | OK | |
| udi-assignment | ✅ 6/6 | OK | 早前独立实测 PASS；续跑网络波动 |

**结论：20/21 PASS；multilingual-ifu 的 selftest 存在断言与实现不一致（硬伤）。** 另注意 README 自述"21/21 模块已实现 selftest"与"CI 全绿"口径，需与实际（1 个 FAIL）对齐。

---

## 九、找错发现清单（批判性审查，带找错目的测试）

| 级别 | 发现 | 证据 |
|---|---|---|
| 🔴 硬伤 | multilingual-ifu selftest 失败 | `--lang-dir .` 期望 rc=0 实际 rc=2，selftest 断言与程序行为不一致 |
| 🟠 路由歧义 | UDI 条码场景首选 fhir-ortho-toolkit | 10 场景实测：首选偏到 fhir（"骨科+udi"双关键词），次选才是 udi-assignment |
| 🟠 路由歧义 | 公平性评估首选 ai-governance-checklist | 首选偏到治理清单，次选才是计算公平性缺口的 ml-validation |
| 🟡 口径漂移 | llms.txt 写"AI 治理 9"，README/module.json 是 4 | 同一体系三处手工维护，必然漂移；建议 manifest 生成器统一 |
| 🟡 声明漂移 | README 声称"21/21 实现 selftest"，实测 1 个 FAIL | 建议 CI 接入真实 selftest 结果，可点击核验 |
| 🟢 网络/环境 | 多次 raw 下载瞬时失败（WinError 10054） | 均重试成功，与仓库无关；实测环境网络波动 |
| 🟢 过程教训 | 实测脚本缺目录创建导致 4 个模块误报"下载失败" | 系测试脚本缺陷（已修复），仓库代码无恙 |

---

## 十、主账号 zhaoxinghua09-cell 实测（技能体系 + ITU-T FG-TIDA 表现）

### 10.1 技能体系（109 仓结构）

- **技能聚合**：`agent-skills`（109 技能治理库）、`synomos-ai-skills`（技能镜像）、`synomosai-skill-index`（技能索引）——SKILL 仓均带 `module.json` / `AGENTS.md` / `llms.txt` 可发现入口（与 stevenzhao07 同构的套娃契约）
- **理论体系**：LGD（生命周期治理）/ UIBC / XLGD / XCGS / Nomos 等理论仓 + `lgd-hub` 门户 + `agent-trust-identity-spec` 规范
- **自我治理实践**：190 个 PR、repo-gate 可失败门禁、三层机器人审核（L0/L1/L2·零外部 action）、REDTEAM 探针（含 `medxpert-standards` 的 `/itu-review` 红队路径）

### 10.2 ITU-T FG-TIDA 贡献（GitHub 可核验）

组织：**FG-TIDA**（ITU-T Focus Group on Trust and Identity for Humans and Agentic AI，tida.community，7 个公开仓库）

| 仓库 | PR | 状态 | 内容 |
|---|---|---|---|
| wg1-ra-aai | #4 | closed（未合并） | 填充第 01、05 章 landscape / building blocks（+288/-12） |
| wg1-ra-aai | #3 | closed（未合并） | 填充第 02、03、06、07 章（problem statement / challenges / future / references，+318/-16） |
| wg1-ra-aai | #2 | open | 第 04 章 Three Fundamental Questions（+215/-9） |
| use-cases | #18 | **✅ MERGED 2026-09-29** | submissions index 十个用例登记 |
| use-cases | #15 | closed（未合并） | use case #14 索引 |
| use-cases | #23 | open | verifier-side challenge 引用（silent-failure-catalog：可执行 SF-005/006/011） |

**结论**：参与真实、深度（wg1 三个章节级 PR 合计 800+ 行），但正式合并率 1/6（多数 PR 停留 open/closed 未合并）——标准影响力在建，尚未形成"主导者"地位。PR#23 将主账号的 silent-failure-catalog 作为 ITU 用例提交，是两个账号体系在标准层面的直接联通。

---

## 十一、企业级就绪度评估（8 维，满分 5）

| 维度 | 得分 | 依据 |
|---|---|---|
| 可运行性 | 4/5 | 20/21 实跑 PASS，1 个 FAIL |
| 架构完备性 | 5/5 | 套娃 + 路由 + 可发现全链路实跑验证 |
| 内容权威性 | 2/5 | 专家评审全线 pending、官方源部分验证 |
| 治理机制 | 4/5 | 门禁/负对照/PR 制/红队实践优秀 |
| 企业集成能力 | 1.5/5 | 单机 CLI，无 RBAC/审计运行时/部署形态 |
| 标准影响力 | 3/5 | ITU 1 合并 + 章节贡献，影响力在建 |
| 数据覆盖 | 3/5 | 四辖区实现，ASEAN/LATAM 未实现，部分数据待核验 |
| 质量一致性 | 2/5 | 文档口径漂移 + selftest 声明与实际有缝 |

**总评**：原型级（接近 MVP），理念领先（可证伪/护照/追溯，契合未来高自主 AI 治理），工程化与内容可信度是下一阶段重点。补齐路线：①运行时审计与身份集成 ②专家评审/官方源核验 ③部署形态与 SLA ④质量一致性修复（含 multilingual-ifu）。
---

## Rerun Quadruple / 复跑四元组（G-17 · MLCommons 复跑要求）

> **Subject commit SHA / 被评提交**：`stevenzhao07/medical-ai-toolkit@8bcb152cd0b3`（门户仓，评测日快照 2026-10-14T06:08:56Z；覆盖账号级 25 仓 README/路由快照）
> **Tool version / 工具版本**：CPython 3.12.10（stdlib only）；`router.py` / `discover.py` + 4 个代表性工具（pms-vigilance / udi-assignment / ml-validation / ai-a3-laws）内置 selftest
> **Evaluation date / 评测日期**：2026-10-14
> **Rerun command / 复跑命令**：`git clone https://github.com/stevenzhao07/medical-ai-toolkit && cd medical-ai-toolkit && python router.py && python discover.py`，随后按报告第四节清单对 4 个代表性工具执行 `python <script>.py --selftest`（应全部 exit 0）
