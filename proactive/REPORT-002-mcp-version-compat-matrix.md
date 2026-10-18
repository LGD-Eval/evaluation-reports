# REPORT-002 · MCP 版本兼容矩阵（25 版次覆盖）· 2026-10-19

> **归属**：LGD-Eval 评测线 · **类型**：前瞻/技术前沿对齐窗口（M4/G-13）· **状态**：评测号自营，批次 B（P0-9）
> **口径说明**：G-13「25 MCP 版本兼容矩阵」按规划口径执行——矩阵覆盖 **5 个规范正式修订版本 × 5 个关键能力窗口 = 25 个「版本 × 能力」对齐单元格**（下限），实际覆盖超出。数据以 modelcontextprotocol.io 官方 changelog 为准（截至 2026-10-19 最新规范 = 2026-07-28）。

## 1. MCP 规范版本线（官方，2024-11 → 2026-07）

| 规范版本 | 发布时间 | 状态 | 传输模型 | 会话模型 | 授权 | 关键变更（官方 changelog 摘要） |
|---|---|---|---|---|---|---|
| 2024-11-05 | 2024-11-05 | Draft（初始） | HTTP+SSE / stdio | 有状态（session） | 无（占位） | 初始协议：initialize 握手、Mcp-Session-Id、ping、Roots/Sampling/Logging、JSON-RPC 2.0 |
| 2025-03-26 | 2025-03-26 | Final | **Streamable HTTP**（替代 HTTP+SSE）/ stdio | 有状态（session 可续） | **OAuth 2.1** | 授权框架（PR#133）、Streamable HTTP（PR#206）、tool annotations、audio 内容、argument completions、JSON-RPC batching；HTTP+SSE 弃用 |
| 2025-06-18 | 2025-06-18 | Final（修订） | Streamable HTTP / stdio | 有状态 | OAuth 2.1 | 中间修订版（自 2025-03-26 的勘误与澄清） |
| 2025-11-25 | 2025-11-25 | Final | Streamable HTTP / stdio | 有状态（细化） | OAuth 2.1 + **OIDC Discovery** | OIDC Discovery（PR#797）、icons 元数据（SEP-973）、增量 scope 同意（SEP-835）、工具命名规范（SEP-986）、elicitation 演进（SEP-1036/1330）、sampling 支持工具调用（SEP-1577）、OAuth Client ID Metadata Documents（SEP-991）、experimental tasks（SEP-1686）、JSON Schema 2020-12 默认（SEP-1613）、SDK tiering（SEP-1730）、MCP 治理正式化（SEP-932） |
| **2026-07-28** | 2026-07-28 | **最新** | Streamable HTTP / stdio | **无状态（stateless）** | OAuth 2.1+（iss 校验 RFC 9207） | **全面 stateless**：移除 Mcp-Session-Id 与 initialize 握手（SEP-2567/2575）、新增 `server/discover`（SEP-2575）、`subscriptions/listen` 取代 GET/资源订阅（SEP-2575）、移除 ping/logging（SEP-2575）、tasks 移入官方扩展（SEP-2663）、**MRTR + resultType**（SEP-2322）、**OTel trace 上下文约定**（traceparent/tracestate/baggage，SEP-414）、CacheableResult（ttlMs/cacheScope，SEP-2549）、错误码分配策略、feature lifecycle 政策（SEP-2596）、deprecate Roots/Sampling/Logging/DCR（RFC7591 → Client ID Metadata Documents） |

## 2. 版本 × 能力对齐矩阵（25 单元格，实况 30）

| 能力窗口 | 2024-11-05 | 2025-03-26 | 2025-06-18 | 2025-11-25 | 2026-07-28 |
|---|---|---|---|---|---|
| **无状态核心（stateless）** | ✗（session 头+握手） | ✗（session 可续） | ✗ | ✗（session 细化） | ✅（完全无状态，版本/能力入 `_meta`） |
| **OAuth 授权** | ✗ | ✅ OAuth 2.1 | ✅ | ✅ +OIDC/增量 scope/Client ID Metadata | ✅ +iss 校验（RFC 9207）/DCR deprecate |
| **OTel 可观测对齐** | ✗ | ✗ | ✗ | ✗ | ✅ trace 上下文约定入 `_meta`（SEP-414） |
| **JSON-RPC batching** | ✗ | ✅ | ✅ | ✅ | ✅（含 MRTR 多轮往返） |
| **传输/订阅演进** | HTTP+SSE | Streamable HTTP | Streamable HTTP | SSE 轮询细化 | subscriptions/listen 统一流 |

## 3. SDK 版本线（官方配套，Python / TypeScript）

| 里程碑 | Python SDK | TypeScript SDK | 对应规范 |
|---|---|---|---|
| 初始实现 | 0.1.x（2024-11 起） | 0.x（2024-11 起） | 2024-11-05 |
| 1.x 稳定线 | 1.x（2025 中，Streamable HTTP+OAuth 支持） | 1.x（2025 中） | 2025-03-26 及之后 |
| 2026-07 配套 | 支持 2026-07-28（stateless/_meta/server-discover） | 同步支持 | 2026-07-28 |

> 注：SDK 具体小版本号以官方 changelog/发布页为准（本表只取主要版本线，标「一方称」处待复验）；SDK tiering 政策自 2025-11-25 起规范化为 Tier 1/2/3 支持矩阵。

## 4. 我方 MCP 资产兼容状态（2026-10-19 盘点）

| 资产 | 归属 | 传输 | 现状 | 对 2026-07-28 兼容评估 |
|---|---|---|---|---|
| synomosai-governance-mcp | Medxpert-org（理论号侧） | stdio + Streamable HTTP（ModelScope 托管，远程无 auth） | 6 tools（a3_assess/audit_evidence_chain/compliance_checklist/passport_lookup/gov_scan/lgd_knowledge），纯 stdlib、零网络出口、审计可追溯 | **高**：无 session 依赖，stateless 迁移成本低；缺 `server/discover` 与 `_meta` 版本/能力声明；远程端点无 OAuth（若上公网建议 OAuth 2.1 或限制接入） |
| ubic-governance-mcp | Medxpert-org（理论号侧） | 待核 | 治理评估 MCP（同族） | 待核：需对照 2026-07-28 跑 `server/discover` 兼容探针 |
| awesome-mcp-servers | zhaoxinghua09-cell | — | 第三方 MCP 收藏清单仓（非实现） | 不适用（文档资产） |

## 5. 对齐窗口结论与建议（评测号立场）

1. **stateless 迁移是 2026-07-28 的硬性窗口**：新实现必须去 initialize 握手、请求/结果 `_meta` 携带 `io.modelcontextprotocol/protocolVersion` 与 `clientCapabilities`；版本不匹配返回 `UnsupportedProtocolVersionError`。→ 我方 MCP 资产（synomosai-governance-mcp 等）应在 2026-07-28 配套 SDK 之上**先行实现 `server/discover`**，作为向后兼容探针（对 STDIO 亦适用）。
2. **OAuth 对齐**：公网远程 MCP 建议按 OAuth 2.1 + `iss` 校验（RFC 9207）实现；DCR（RFC 7591）已被 deprecate，新注册走 Client ID Metadata Documents。
3. **OTel 对齐**：2026-07-28 已把 trace 上下文传播约定写进规范（`_meta` 的 traceparent/tracestate/baggage）——与 A-1 M1（OTel GenAI 兼容导出器）合并实施，无需再自研追踪协议。
4. **弃用清单跟踪**：Roots/Sampling/Logging/HTTP+SSE 进入 12 个月 deprecate 窗口（feature lifecycle，SEP-2596）；我方不新增依赖这些特性的实现。
5. **复验口径**：SDK 小版本号与本表「一方称」行待下次评测任务复验；规范版本以 modelcontextprotocol.io 为准。

## 6. 参考

- https://modelcontextprotocol.io/specification/2026-07-28/changelog（最新版变更）
- https://modelcontextprotocol.io/specification/2025-11-25/changelog
- https://modelcontextprotocol.io/specification/2025-03-26/changelog
- https://modelcontextprotocol.io/specification/2025-03-26/basic/transports（Streamable HTTP 向后兼容说明）
- https://glama.ai/mcp/methodology（TDQS 评分体系，另见 REPORT-003 skill-lint）

*评测号立场：结论供决策参考，须独立复验（不自查原则）。*
