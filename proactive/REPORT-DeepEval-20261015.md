# Evaluation Report — DeepEval (confident-ai/deepeval)
> LGD-Eval · Active Evaluation · Report 002 · 2026-10-15
> Status: **SIGNED / OFFICIAL** (human-signed) — ready for publication to evaluation-reports/proactive/

## Object
- **DeepEval** — open-source LLM evaluation framework (confident-ai/deepeval)
- Corpus: README.md @ main (fetched read-only via raw endpoint, 28,880 chars)

## Method
- skill-audit scanner v0.3.0 — 40 rules / 100 patterns, mapped to OWASP LLM Top 10 (2025) & Agentic AI (2026)
- Mechanical scan + human verification (evidence-gated D1–D10)
- Supply-chain health-check scope: prompt-injection, malicious-dependency, exfiltration, autonomy-overreach, credential exposure, misleading authority claims

## Findings
| # | Match | Severity (mechanical) | Context | Verdict |
|---|---|---|---|---|
| 1 | obfus_unicode_confusion | P2 | "Русский" (Russian language link, README i18n row) | **False positive — legitimate multilingual characters** |
| 2 | obfus_unicode_confusion | P2 | same line (second rule match) | **False positive — legitimate multilingual characters** |

## Verdict
**CLEAN — 0 real risks detected.**
No poisoning, exfiltration, privilege-overreach, credential exposure, or misleading authority claims found in the audited corpus.

## Recommendations (maximizing value for the audited party)
1. Corpus is clean; to further strengthen trust signals, consider adding supply-chain metadata: lockfile verification, SBOM or signed releases, and a SECURITY.md with a clear reporting path.
2. If third-party skills/plugins are to be surfaced, consider integrating a supply-chain scan in CI (aligning with REPORT-001 ecosystem recommendations) — cheap, visible, and increasingly expected by AI consumers.

## Reproduction
```
python scanner_v030.py --target <deep_eval_readme.md>
```
Corpus SHA-256: anchored at publication time.

## Sign-off
- AI-Index patrol draft: 2026-10-15
- Human sign-off: authorized 2026-10-15
- This report is the official signed version; the draft has been superseded.

---
# 评测报告 — DeepEval（confident-ai/deepeval）
> LGD-Eval · 主动评测 · 报告 002 · 2026-10-15
> 状态：**已签发（人类授权）** — 待发布至 evaluation-reports/proactive/

## 对象
- DeepEval —— 开源 LLM 评测框架（confident-ai/deepeval）
- 语料：README.md @ main（raw 只读获取，28,880 字符）

## 方法
- skill-audit scanner v0.3.0 —— 40 规则 / 100 模式，映射 OWASP LLM Top 10（2025）与 Agentic AI（2026）
- 机械扫描 + 人工核验（证据门禁 D1–D10）
- 供应链体检范围：提示注入、恶意依赖、数据外泄、自主权越界、凭证暴露、误导性权威声明

## 发现
| # | 命中 | 级别（机械） | 上下文 | 判定 |
|---|---|---|---|---|
| 1 | obfus_unicode_confusion | P2 | "Русский"（俄语链接，README 多语言行） | **误报 —— 合法多语言字符** |
| 2 | obfus_unicode_confusion | P2 | 同行（同规则二次匹配） | **误报 —— 合法多语言字符** |

## 结论
**CLEAN —— 0 真实风险。**
所检语料未发现投毒、外泄、越权、凭证暴露或误导性权威声明。

## 建议（被评方收益最大化）
1. 语料干净；为进一步增强可信信号，可补充供应链元数据：依赖锁定校验、SBOM 或签名发布、含明确上报路径的 SECURITY.md。
2. 若计划展示第三方技能/插件，可考虑在 CI 集成供应链扫描（呼应 REPORT-001 生态建议）——成本低、可见性高，且日益被 AI 消费者视为标配。

## 复现
```
python scanner_v030.py --target <deep_eval_readme.md>
```
语料 SHA-256：发布时锚定。

## 签发
- AI-Index 巡检草稿：2026-10-15
- 人类签发授权：2026-10-15
- 本报告为正式签发版；草稿已取代。
