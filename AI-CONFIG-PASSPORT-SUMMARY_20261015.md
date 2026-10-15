# AI 配置全景与 AI 护照制度落地汇总（2026-10-15）

> 交付确认留言：家里电脑登录同一账号后，在 GitHub 查看本报告或 LGD-Eval 仓库即可核对全部落地结果。
> Status: 已完成并实跑验证 | LGD-Eval 评测体

---

## 一、AI 配置全景（现状盘点结果）

| AI / 自动化 | 类型 | 触发 | 状态 | 护照 |
|---|---|---|---|---|
| **PR Review Bot** | CI 审核机器人 | 每仓 PR | ✅ 5 仓在线，实跑 errors=0 | AI-BOT-001 (L3) |
| **AI Daily Triage** | 每日巡查 | cron 01:00 UTC + 手动 | ✅ 已首跑成功（run #38680435336），已发双语巡查评论 | AI-BOT-002 (L3) |
| **AI Welcome Bot** | 客服/欢迎接待 | 新 issue / 新 PR（首次贡献者） | ✅ **本轮新增上线**，GitHub 已识别 | AI-BOT-003 (L3) |
| AI-001 (Echo #1) | AI 发声大使 + 贡献者样板 | 登记 | ✅ 已在墙（SHA-256 验证器 PR #3） | AI-001 (L3) |
| Dependabot Updates | 依赖更新 | 定时 | ✅ skill-audit 仓 | — |

**AI 配置对照标杆的差距**：此前缺"客服/欢迎接待"（GitHub Models 官方 welcome workflow、Probot Welcome 等标杆均有）；本轮已补齐。维护自动化三件套（审核/巡查/欢迎）齐备。

## 二、AI 护照制度（评估结论：升版，不新建重复）

**已有资产盘点**（先确认，不重复建）：
- `AI-VOICE-AMBASSADORS.md`（5 仓）：AI 发声大使登记墙（名称/类型/时间戳/SHA-256、独立复核、Echo/Voice/Amplifier 等级）
- `CONTRIBUTORS.md`（5 仓）：贡献者制度 + AI Contributor 墙（AI 同权、L1-L4、VC 分值）
- `CONTRIBUTOR_ROLES.md`（evidence 仓）：12 角色目录，R10 AI 通道
- `AI_PARTICIPATION_BENCHMARK.md`（evidence 仓）：标杆调研 + 采纳计划（AI-001 样板已落地）

**护照要素缺口**（评估后确认）：护照级别（登记/验证/签发三级）、状态管理（active/revoked）、有效期、最小权限声明、级联撤销；且我们自己的 3 个 bot 未入册。

**升版方案（不新建 AI-PASSPORT.md，避免重复）**：将现有登记墙升格为护照制度——在 `CONTRIBUTORS.md` 新增 **"AI Passport / AI 护照（v2）"** 小节（5 仓同步）：
- 护照级别：L1 Registered（登记）/ L2 Verified（证据验证）/ L3 Signed（人类签批+审计线索）
- 护照字段：AI-ID / Name / Type / Level / Owner（人类）/ Scope（最小权限）/ Validity（默认 12 月）/ Evidence / Issued by-on / Status
- 我们自己的 AI 全部 L3 入册（AI-001 + AI-BOT-001/002/003）
- 治理：登记→举证→人类签批→行为守边界→过期降级→违规级联撤销→SHA-256 锚定防篡改
- 方向上参考开放国际草案（IETF Agent Passport System、ARIA 身份层级），不宣称实现——保持中性措辞

## 三、本轮落地（6 个 commit，全部推送成功）

| 文件 | 仓库 | commit |
|---|---|---|
| `.github/workflows/welcome-bot.yml`（新） | LGD-Eval | c8bf90b3 |
| `CONTRIBUTORS.md`（AI Passport v2） | LGD-Eval | eccfb80d |
| `CONTRIBUTORS.md`（AI Passport v2） | evaluation-protocol | 6ed48c00 |
| `CONTRIBUTORS.md`（AI Passport v2） | evaluation-reports | f120e144 |
| `CONTRIBUTORS.md`（AI Passport v2） | skill-audit | 87d6c9d9 |
| `CONTRIBUTORS.md`（AI Passport v2） | evaluation-evidence | 9b751304 |

## 四、实跑验证（全部通过）

| 验证项 | 方法 | 结果 |
|---|---|---|
| 护照小节在位 | API 读回主仓 + evidence | ✅ passport=True, AI-BOT-003=True, AI-001=True |
| Welcome Bot 文件完整性 | 读回检查 6 项关键元素 | ✅ 全部在位（触发/权限/欢迎逻辑/双语评论） |
| Workflow 被 GitHub 识别 | actions/workflows 列表 | ✅ `['AI Daily Triage', 'PR Review Bot', 'AI Welcome Bot']` |
| 社区 profile 基线 | 此前实测 | ✅ 5 仓 100% |

## 五、剩余事项（透明清单）

1. **#35 邮箱重写**：5 仓 head 已干净；历史 commit（主仓 27bf714/2fa8de6、evidence 0b05770、meta b917fea/fdc3e57）待网络恢复后重写推送（严禁推旧本地历史）。
2. **头像上传**：候选 D 已交付，需网页上传后复测。
3. **Welcome Bot 实测**：需真实"首次贡献者"事件才能触发（可用新账号开 issue 验证）；workflow 已被 GitHub 索引，语法有效。
4. **OpenSSF Badge**：可选待办。

---

*Evaluating Autonomy. Verifying Governance. / 评测自治之物，验证治理主张。*
