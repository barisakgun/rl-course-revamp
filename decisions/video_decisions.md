# Accepted video delivery decisions

Accepted by the instructor in the Phase 3 iteration-1 response on 2026-09-28. Videos are a substantive delivery channel for prerequisites and background. The former optional-search/minimal-LLM-video recommendation is superseded.

The following structured block is authoritative for accepted video scope and prerequisite use. `scripts/phase3_audit.py` reads it when rendering analysis. Scope is semi-frozen with the Week 4/8/11 checkpoints below. The accepted tentative release rule is seven days before use. Recording durations, study-time estimates, detailed outlines and fallback options belong to `analysis/phase3_proposal.yaml` until accepted. This does not create a new live session or change the calendar calculation in `config/course.yaml`.

```yaml
schema_version: 1
videos:
- id: search_background
  required: true
  scope: Use a search-background video to prepare students for search/planning and MCTS. BFS/DFS knowledge can be
    assumed for this CS audience; additional search material builds on that background rather than reteaching a
    full introductory search course. Any BFS/DFS recap is skippable background.
  prerequisite_use: Before live search/MCTS; live time develops RL connections and examples.
  before: mcts
- id: llm_background
  required: true
  scope: Move transformer architecture background, autoregressive language modeling, LLM pretraining and supervised
    fine-tuning to video. Use this preparation to allow greater live emphasis on RL-based LLM post-training.
  prerequisite_use: Before live LLM RL; retain interactive treatment of RL objectives, estimators and failure modes.
  before: llm_mapping
scope_state: semi-frozen-with-delivery-checkpoints
checkpoints:
- week: 4
  action: Plan search/planning video against observed background and progress.
- week: 8
  action: Verify search/planning preparation; decide whether policy-search supplementation is needed; plan LLM prerequisites.
- week: 11
  action: Verify LLM prerequisite-video requirements and close remaining preparation gaps before live LLM RL.
change_rule: Adjust examples, chaptering and detail within accepted prerequisite scope at checkpoints. Record material
  changes in required scope, timing or student workload before use; a policy supplement is not automatically required.
release_policy:
  lead_days: 7
  state: tentative-initial-plan
  rule: Release one week before the first relevant live topic; review at the accepted in-semester checkpoints.
```

The transformer material is an instructor-requested prerequisite subtopic, not a new external-evidence claim or an invented normalized topic. Its architecture depth remains an outline choice. The two video units remain compatible with the configured target of two videos; splitting recordings into chapters does not add a new curricular unit. No third policy-method video is accepted by this decision.
