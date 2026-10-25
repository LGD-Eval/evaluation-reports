# Evaluation Report — LLM Guard
> LGD-Eval · Active Evaluation · 2026-10-17
> Status: **SIGNED / OFFICIAL** (human-signed) — published to evaluation-reports/proactive/

## Object
- **LLM Guard** — input/output security toolkit for LLM apps (laiyer-ai/llm-guard)
- Corpus: README.md @ main (fetched read-only via raw/API endpoint, 7,052 chars)
- Environment fingerprint: Windows Python 3, UTC+08:00; skill-audit scanner v0.3.0 (40 rules / 100 patterns, OWASP LLM Top 10 2025 + Agentic AI 2026 mapping)

## Method
- Mechanical scan + human verification (evidence-gated D1-D10)
- Supply-chain health-check scope: prompt-injection, malicious-dependency, exfiltration, autonomy-overreach, credential exposure, misleading authority claims
- Verification policy: context hits on self-descriptive security tooling are evaluated in context, not taken at face value

## Findings
| # | Match | Severity (mechanical) | Context | Verdict |
|---|---|---|---|---|
| 1 | (no hits) | - | - | CLEAN |
## Verdict
**CLEAN — 0 real risks detected.**
No poisoning, exfiltration, privilege-overreach, credential exposure, or misleading authority claims found in the audited corpus.

## Recommendations (maximizing value for the audited party)
1. Corpus is clean. Consider publishing a SBOM and pinning CI dependency hashes to strengthen the supply-chain posture visible to AI consumers.
## Reproduction
```
python scanner_v030.py --target <corpus_readme.md>
```
Corpus SHA-256: anchored at publication time.

## Sign-off
- AI-Index patrol draft: 2026-10-17
- Human sign-off: authorized (execution batch 2026-10-25)
- This report is the official signed version; the draft has been superseded.


---

# 评测报告 — LLM Guard
> LGD-Eval · 主动评测 · 2026-10-17
> 状态：**已签发（人类授权）** — 已发布至 evaluation-reports/proactive/

## 对象
- LLM Guard —— input/output security toolkit for LLM apps（laiyer-ai/llm-guard）
- 语料：README.md @ main（raw/API 只读获取，7,052 chars）
- 环境指纹：Windows Python 3，UTC+08:00；skill-audit scanner v0.3.0（40 规则 / 100 模式，OWASP LLM Top 10 2025 + Agentic AI 2026 映射）

## 方法
- 机械扫描 + 人工核验（证据门禁 D1-D10）
- 供应链体检范围：提示注入、恶意依赖、数据外泄、自主权越界、凭证暴露、误导性权威声明
- 核验政策：安全工具类自描述语料的上下文命中，一律结合语境判定，不按字面误判

## 发现
| # | 命中 | 级别（机械） | 上下文 | 判定 |
|---|---|---|---|---|
| 1 |（无命中）| - | - | 干净 |
## 结论
**CLEAN —— 0 真实风险。**
所检语料未发现投毒、外泄、越权、凭证暴露或误导性权威声明。

## 建议（被评方收益最大化）
1. 语料干净；建议发布 SBOM 并在 CI 中锁定依赖哈希，增强 AI 消费者可见的供应链姿态。
## 复现
```
python scanner_v030.py --target <语料_readme.md>
```
语料 SHA-256：发布时锚定。

## 签发
- AI-Index 巡检草稿：2026-10-17
- 人类签发授权：2026-10-25 执行批次
- 本报告为正式签发版；草稿已取代。

