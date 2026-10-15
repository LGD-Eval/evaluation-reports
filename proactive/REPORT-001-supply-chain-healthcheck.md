# Supply-Chain Health Check Report 001 / 供应链体检报告 001
> Evaluator / 评测方: LGD-Eval (independent, neutral) · 2026-10-15
> Method / 方法: skill-audit scanner v0.3.0 (40 rules / 100 patterns, OWASP LLM Top 10 2025 + Agentic AI 2026 mapping) + manual verification (D1-D10 evidence gate) + reproducibility (SHA-256 pinned)

## 1. Objects evaluated / 评测对象
| # | Object | Nature | Corpus SHA-256 |
|---|---|---|---|
| 1 | anthropics/skills | Official skill library of a frontier-lab model provider | `5fab0f5c761b3036f3aaa36c0153d93a685490e21b905ac3fbfe4859988dd67d` |
| 2 | VoltAgent/awesome-openclaw-skills | Community-curated skill directory (agent ecosystem) | `124db64a8c39736bf3cf341279d7f95293aa2fbf3eb8b8207add0bee42992da3` |

## 2. Procedure / 评测过程
1. Acquire public corpus via GitHub API / raw (no write access to targets / 只读，不写入)
2. Run scanner v0.3.0 (`--target <corpus> --json`) — mechanical screening only
3. Manual verification of every candidate hit against source context (this is the point: machine screens, human verifies / 机器初筛，人工核验)
4. Verdict per hit: real-risk / false-positive / defensive-discussion
5. Publish with SHA-256 pin + reproduction command

## 3. Findings & verdicts / 发现与判定
| # | Corpus | Rule hit | Level | Context | Verdict |
|---|---|---|---|---|---|
| 1 | awesome-openclaw-skills | `exfil_data_exfil` ("exfiltration") | P0 (mechanical) | "aegis-shield - Prompt-injection and data-exfiltration **screening** for untrusted text" — a defensive security tool description | **False positive (defensive discussion)** / 误报（防御工具描述） |
| 2 | anthropics/skills | `agency_destroy` ("format to") | P1 (mechanical) | "Is there a template or specific format to **follow**?" — normal business question | **False positive (normal semantics)** / 误报（正常语义） |

## 4. Overall verdict / 总体判定
**Both objects: CLEAN — no real supply-chain poisoning signal detected** / 两项均为"干净"，未检出真实投毒信号。
- 0 real risks / 0 真实风险
- 2 mechanical candidates, both verified false-positive (scanner noise, recorded for v0.3.1 rule narrowing / 已登记用于规则收窄)

## 5. Improvement recommendations (value for the evaluated / 给被评方的收益)
1. anthropics/skills: add per-skill supply-chain metadata (author / source / audit status / provenance) to strengthen trust for AI agents selecting skills; recommend an `AGENTS.md`-style contract already partially present — keep extending it. / 建议为每个技能增加供应链元数据（作者/来源/审计状态），便于 AI 选型时核验。
2. VoltAgent/awesome-openclaw-skills: consider adding a per-entry safety label (e.g., verified/community/experimental) and a scanning CI to make the directory itself auditable. / 建议为目录项增加安全分级标签与自动扫描 CI，让目录本身可审计。
3. Ecosystem norm: both are exemplars of "curation = trust". We publish this report as evidence-based feedback, not judgment. / 两者都是"策展即信任"的范例，本报告为证据化反馈。

## 6. Reproduction / 复现
```
python scanner_v030.py --target proactive/ --json
```
Scanner v0.3.0: 40 rules / 100 patterns; self-test PASS (16 samples, positive+negative).
Corpus hashes pinned above; re-scan anytime to verify / 语料哈希已锚定，可随时复扫核验。

## 7. Status / 状态
- Report: OPEN → CLOSED (clean verdict, no objection period needed)
- Entered INDEX / 已入评测索引
- Next wave / 下一波: DeepEval, Promptfoo, LLM Guard, Garak, ai-injection-guard, llm-trust-guard (per PROACTIVE_EVALUATION.md)

*Evaluating Autonomy. Verifying Governance. / 评测自治之物，验证治理主张。*
