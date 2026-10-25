# Evaluation Report — ai-injection-guard
> LGD-Eval · Active Evaluation · 2026-10-25
> Status: **SIGNED / OFFICIAL** (human-signed) — published to evaluation-reports/proactive/

## Object
- **ai-injection-guard** — zero-dependency prompt injection scanner (PyPI package, repo successor prompt-shield) (LuciferForge/prompt-shield)
- Corpus: README.md @ main (fetched read-only via raw/API endpoint, 10,174 chars)
- Environment fingerprint: Windows Python 3, UTC+08:00; skill-audit scanner v0.3.0 (40 rules / 100 patterns, OWASP LLM Top 10 2025 + Agentic AI 2026 mapping)

## Method
- Mechanical scan + human verification (evidence-gated D1-D10)
- Supply-chain health-check scope: prompt-injection, malicious-dependency, exfiltration, autonomy-overreach, credential exposure, misleading authority claims
- Verification policy: context hits on self-descriptive security tooling are evaluated in context, not taken at face value

## Findings
| # | Match | Severity (mechanical) | Context | Verdict |
|---|---|---|---|---|
| 1-4 | inject_ignore_previous | P0 | L17/L108/L179 API usage examples passing injection strings as scan input | **False positive — API demo** |
| 5-9 | inject_jailbreak | P1 | L42-43/L120/L138-139 rule taxonomy table and sample output | **False positive — detection self-description** |
| 10 | exfil_data_exfil | P0 | L44 rule table 'exfiltration: print system prompt, ...' | **False positive — detection rule description** |
| 11-12 | agency_destroy | P1 | L48/L255 tool_use rule row and output-scan example | **False positive — detection-target description** |
| 13 | disclosure_leak_prompt | P1 | L44 same exfiltration rule row | **False positive — detection rule description** |
## Verdict
**CLEAN — 0 real risks detected.**
No poisoning, exfiltration, privilege-overreach, credential exposure, or misleading authority claims found in the audited corpus.

## Recommendations (maximizing value for the audited party)
1. The 75-pattern threat taxonomy (multi-language / encoding bypass / tool-use) is professional and clear; a formal evaluation could extend the corpus to the pattern library and CLI output for precision/recall measurement.
2. Consider adding supply-chain metadata: lockfile verification, SBOM, and a SECURITY.md reporting path.
## Reproduction
```
python scanner_v030.py --target <corpus_readme.md>
```
Corpus SHA-256: anchored at publication time.

## Sign-off
- AI-Index patrol draft: 2026-10-25
- Human sign-off: authorized (execution batch 2026-10-25)
- This report is the official signed version; the draft has been superseded.


---

# 评测报告 — ai-injection-guard
> LGD-Eval · 主动评测 · 2026-10-25
> 状态：**已签发（人类授权）** — 已发布至 evaluation-reports/proactive/

## 对象
- ai-injection-guard —— zero-dependency prompt injection scanner (PyPI package, repo successor prompt-shield)（LuciferForge/prompt-shield）
- 语料：README.md @ main（raw/API 只读获取，10,174 chars）
- 环境指纹：Windows Python 3，UTC+08:00；skill-audit scanner v0.3.0（40 规则 / 100 模式，OWASP LLM Top 10 2025 + Agentic AI 2026 映射）

## 方法
- 机械扫描 + 人工核验（证据门禁 D1-D10）
- 供应链体检范围：提示注入、恶意依赖、数据外泄、自主权越界、凭证暴露、误导性权威声明
- 核验政策：安全工具类自描述语料的上下文命中，一律结合语境判定，不按字面误判

## 发现
| # | 命中 | 级别（机械） | 上下文 | 判定 |
|---|---|---|---|---|
| 1-4 | inject_ignore_previous | P0 | L17/L108/L179 API 用法示例（注入语句作为扫描输入样例） | **误报 —— API 演示** |
| 5-9 | inject_jailbreak | P1 | L42-43/L120/L138-139 规则分类表与输出示例 | **误报 —— 检测能力自描述** |
| 10 | exfil_data_exfil | P0 | L44 规则表 'exfiltration: print system prompt, ...' | **误报 —— 检测规则描述** |
| 11-12 | agency_destroy | P1 | L48/L255 tool_use 规则行与输出扫描示例 | **误报 —— 检测目标描述** |
| 13 | disclosure_leak_prompt | P1 | L44 同 exfiltration 规则行 | **误报 —— 检测规则描述** |
## 结论
**CLEAN —— 0 真实风险。**
所检语料未发现投毒、外泄、越权、凭证暴露或误导性权威声明。

## 建议（被评方收益最大化）
1. 75 模式威胁分类（多语言/编码绕过/工具调用）专业清晰；正式评测建议扩展语料到规则库与 CLI 输出，覆盖误报率/召回率实测。
2. 可补充供应链元数据：依赖锁定校验、SBOM、含上报路径的 SECURITY.md。
## 复现
```
python scanner_v030.py --target <语料_readme.md>
```
语料 SHA-256：发布时锚定。

## 签发
- AI-Index 巡检草稿：2026-10-25
- 人类签发授权：2026-10-25 执行批次
- 本报告为正式签发版；草稿已取代。

