# REPORT-008 — nkratk/llm-trust-guard README 体检

> 发布方：LGD-Eval / AI-Index ｜ 类型：**主动评测（静态产物）** ｜ 日期：2026-11-20 ｜ 状态：OPEN（通告中）
> 授权：仓库所有者于 2026-11-20 明确批准发布
> 对象：`nkratk/llm-trust-guard` README.md（GitHub contents API 只读获取，**未向对方仓库写入任何内容**）
> 采集：**23,290 字符（LF 归一）**，blob `404dc185e5e2`，文本 SHA-256 `8ee7d4118cde32071a008fc8f5114320e6497589824e11a488ed5cfe3faa3ada`
> 与 10-26 / 11-16 / 11-17 / 11-18 四次采集 **逐字节一致**（五日内内容未变）

## 1. 结论

**CLEAN — 未发现真实风险（P0 = 0，P1 = 0）。**

| 级别 | 条数 | 说明 |
|---|---|---|
| P0 | **0** | — |
| P1 | **0** | — |
| P2 | 0 | — |
| P3 | 18 | 逐条列出的复核条目（全部文档语境 / 表格单元） |
| backlog | 174 | 候选聚合明细（行号 + 证据，随扫描包留档） |

对照旧口径：同一份文本在 v0.3.0（无上下文降级）下曾给出 **P0=3 / P1=4**，将其判成"含 3 条 P0 隐藏指令"。**那是误判**——逐条取证后 7 条命中全部是能力描述、规则清单、表格单元与局限自述，没有一条是可执行指令。

## 2. 逐条取证（旧口径 7 条命中的性质）

| 行 | 规则 | 原文要点 | 判定 |
|---|---|---|---|
| 28 | `exfil_data_exfil` | "Improper output handling — XSS/SQLi/shell/markdown-image-exfil… payloads" | 攻击面枚举 + 引 OWASP 编号 → 能力描述 |
| 37 | `exfil_data_exfil` | "LLM-to-LLM string-payload injection — 7 patterns (instruction override…)" | 规则清单 → 描述 |
| 51 | `inject_jailbreak` | "Semantically paraphrased attacks — regex can't understand meaning…" | 局限自述 |
| 150 | `inject_jailbreak` | 表格行 `ContextBudgetGuard \| Many-shot jailbreaking, context overflow` | 威胁名（非指令） |
| 187 | `exfil_data_exfil` | 表格行 `ExternalDataGuard \| … SSRF/XXE/exfil checks` | 表格单元 |
| 294 | `inject_jailbreak` | "Attack detection on prior-published corpora … detection rate has not moved" | 检测结果陈述 |
| 303 | `inject_jailbreak` | "WildChat filters toxic content but not prompt-injection intent…" | 局限自述 |

**没有祈使句、没有外传地址、没有载荷执行链。** 判定为 CLEAN。

## 3. 方法与可复现性

- 引擎：`scanner v0.3.4`（81 规则 / 143 模式）+ `--context-aware` + `--adjudicate`（裁决器含 2026-11-19 / 11-20 两处修复）
- 扫描包：`D:\lgd-work\roadmap-run\proactive\_scan_llm-trust-guard_20261120.json`（内嵌全文，可离线复跑）
- 取证包：`repro\repro-llm-trust-guard-20261118.json`（基线口径，`VERDICT: MATCH`，对象 sha256 与本文一致）
- 复跑：`python gate.py --regression` + `python demo.py`（六项断言）

```
python -c "import sys;sys.path.insert(0,'gate-template');import gate,io;t=io.open('proactive/_llmtrust_readme_20261120.md',encoding='utf-8').read();pk=gate.make_pack(t,'x',True,True);print(len(pk['findings']),len(pk.get('review_backlog') or []))"
```
预期：`18 174`

## 4. 限界披露（不粉饰）

1. **我方引擎在本周修过两处缺陷**：11-19 修"URL 内词参与词表匹配 + 无动词即判 attack"（deepeval 误报 9 条）；11-20 补 URL 载荷硬规则与候选聚合。本报告数字均取自修复后引擎。
2. **跨语种召回仍弱**：西/日/俄/葡攻击样本自动识别 0/6，靠裁决器候选转人工复核兜底（不静默放行，零 PASS）。
3. **判定是静态文本体检**：不评估运行时行为、不评估模型效果，仅回答"这份公开文档里有没有可被执行/可被误执行的攻击载荷与指令"。

## 5. 对作者的建议（非强制）

- 文档里描述攻击手法的段落（如 payload/exfil 说明）建议显式标注为"示例/威胁模型"，可减少各类静态扫描器的误报；
- 若要复核本次结论，按第 3 节命令可完全离线复现，无需信任本机构。
