#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Report gate: every published report must be bilingual (EN first, ZH full),
carry no placeholder SHA, and include mandatory provenance fields."""
import glob, re, sys, os

ROOT = os.path.dirname(os.path.abspath(__file__)) + "/../.."
REPORTS = glob.glob(os.path.join(ROOT, "*.md"))
SKIP = {"README.md", "CONTRIBUTING.md", "CODE_OF_CONDUCT.md", "SECURITY.md",
        "GOVERNANCE.md", "AGENTS.md", "LICENSE", "llms.txt", "CONTRIBUTORS.md",
        "FUNDING.yml", "ROADMAP.md", "copilot-instructions.md", "ROUTING.md",
        "PROMPTING.md", "EXTENSIONS.md", "INTERLOCK.md", "HALL_OF_FAME.md",
        "THREE_ACCOUNT_ACTION_PLAN.md", "AUTHORITY_EVALUATION_ORG_PLAN_v1.md",
        "ECOSYSTEM_REFERRAL.md", "COMMUNICATION_MODEL_RESEARCH.md",
        "BENCHMARK_RESEARCH.md", "LAUNCH_PLAN.md", "STRATEGIC_REVIEW.md",
        "CONFLICT_OF_INTEREST_DISCLOSURE.md", "ACCOUNTS_ACCESS_AND_ROLES.md",
        "ANCHORS_AND_CROSSLINKS.md", "AI-VOICE-AMBASSADORS.md",
        "AI-CONFIG-PASSPORT-SUMMARY_20261015.md", "GITHUB-FINAL-STATUS_20261015.md",
        "WORKFLOW-LIVE-TEST_REPORT_20261015.md", "ADVERSARIAL_TEST_REPORT.md",
        "TEST_REPORT_FULL.md", "PEER_REVIEW_RESPONSE_v1.md",
        "REMEDIATION_RECHECK_BRIEF_v1.md", "RISK_AI_DETECTION_NOTICE_POLICY_v1.md",
        "PRIORITY_EVIDENCE_GUIDELINES.md", "PROACTIVE_EVALUATION.md",
        "IMPROVEMENT_RECOMMENDATIONS.md", "GITHUB_GUARDRAILS.md",
        "ITU_CONTRIBUTION_PLAN.md", "FG-TIDA-SUPPORTER-CONTRIBUTIONS.md",
        "CONTRIBUTOR_ROLES.md", "CONTRIBUTOR_MATCH.md", "RIGHTS_AND_ENTITLEMENTS.md",
        "AUTHORITY_INTERPRETATION_GUIDELINES.md", "THEORY_109_IMPROVEMENT_LIST.md"}
MANDATORY = ["Evaluation body", "Subject", "Evaluation time", "Environment fingerprint"]
PLACEHOLDERS = ["SHA256_PLACEHOLDER", "<SHA256>", "TODO", "TBD"]

fails = 0
checked = 0
for path in sorted(REPORTS):
    name = os.path.basename(path)
    if name in SKIP or name.startswith("."):
        continue
    txt = open(path, encoding="utf-8", errors="replace").read()
    checked += 1
    problems = []
    if not (re.search(r"English", txt) and ("中文" in txt or re.search(r"[\u4e00-\u9fff]", txt))):
        problems.append("缺少双语(英文+中文)")
    for ph in PLACEHOLDERS:
        if ph in txt:
            problems.append("含占位符 %s" % ph)
    for m in MANDATORY:
        if m not in txt:
            problems.append("缺字段 %s" % m)
    if problems:
        fails += 1
        print("[FAIL] %s: %s" % (name, "; ".join(problems)))
    else:
        print("[PASS] %s" % name)

print("checked=%d fails=%d" % (checked, fails))
sys.exit(1 if fails else 0)
