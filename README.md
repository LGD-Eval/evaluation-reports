# Evaluation Reports · 评测报告

> **门户 / Portal:** [LGD Hub · 生态超市入口](https://zhaoxinghua09-cell.github.io/lgd-hub/) ｜ LGD 生态（Lifecycle Governance Doctrine）

> 隶属：凡自治之物 · LGD 治理学（Lifecycle Governance Doctrine）· 创造术家族
> 角色：LGD-Eval 评测线 · 关联关系见 [COI 披露](https://github.com/LGD-Eval/LGD-Eval/blob/main/CONFLICT_OF_INTEREST_DISCLOSURE.md)
> 官方英文：Lifecycle Governance Doctrine
> 许可证：CC BY 4.0

## 报告列表
- **MedXpert工具链实测报告.md**：首份实测（20/21 PASS，含口径漂移修正）——**关联方评测**（被评方 stevenzhao07 与评测号同属三号生态，详见 [COI 披露](https://github.com/LGD-Eval/LGD-Eval/blob/main/CONFLICT_OF_INTEREST_DISCLOSURE.md)）

## 每份报告必含
1. 中立声明（评测方/被评测方/利益隔离/是否关联方评测）
2. 完整可复放步骤（他人可复核）
3. 证据（哈希/时间戳/原文引用）
4. 结论分级（P0-P3）

## 报告规范
- 不自查原则：报告结论须由独立方执行
- 口径漂移修正：与产品方口径不一致时以原始证据为准
- 反泡沫：不夸大任何结论，区分"已查证"与"一方称"

## 精度声明 / Precision statement (2026-11-27)

- 评测引擎与“一键复跑总闸”不在本仓：公开入口在 `LGD-Eval/lgd-gate` 的分支 `ai-index-kit`，
  命令 `python verify_all.py`（7 PASS + 1 SKIP，rc=0；内部语料不随包发布，记 SKIP 而非通过）。
- 公开包 `ai-index-gate/scanner.py` 自检为 **93 规则 / 176 模式**；本地工作分支为 **98 / 189**。
  两者是不同版本，任何把 98/189 说成“公开仓里那份”的表述都不成立。
- 本仓不作“全面超越 / 行业唯一 / 生态闭环”类主张；对外陈述以逐条可复跑、可核对为准。
- 引用与复跑均按“匿名可及”验证：API 200 + 目录树可下载；`git ls-remote` 在 20 秒内可能超时，属通道问题。
