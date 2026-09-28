# Phase 1 collection and inventory

Run these commands from the repository root. They inventory source artifacts and generate factual summaries; they do not normalize topics or change curriculum decisions.

Dependencies: Python 3 with `requests`, `beautifulsoup4`, and `PyYAML`; Poppler's `pdfinfo` and `pdftotext` on `PATH`. Network commands need public internet access. The completed inventories can be validated and their summaries regenerated without network access.

## Validate or regenerate existing reports

```sh
python3 scripts/phase1_report.py --check-only
python3 scripts/phase1_report.py
```

The validator checks source identities, unique material IDs, required fields, provenance-file existence, local-file hashes and inventory completeness, and configuration YAML including duplicate keys. It also checks that Phase 2's normalized evidence file and a book manifest have not been created. This is a Phase 1 validator; revise its phase-boundary checks if reusing it after later phases begin.

During the original collection run, `/private/tmp/rl_phase1_protected.json` held pre-run hashes of normally read-only project files. When present, the validator also checks those hashes. This optional session record is not required to regenerate reports elsewhere.

## Refresh evidence

Refreshing replaces snapshots and manifests. Review the resulting diff: websites can change offerings and structure, and the builder contains reviewed source-specific extraction rules, link selectors, and factual observations that must be checked against refreshed evidence.

```sh
python3 scripts/phase1_collect.py local
python3 scripts/phase1_collect.py pages
python3 scripts/phase1_collect.py page berkeley_cs285 starter_code https://github.com/berkeleydeeprlcourse/homework_spring2026
python3 scripts/phase1_collect.py page current_course hw1b_dependency https://inst.eecs.berkeley.edu/~cs188/sp24/projects/proj6/
python3 scripts/phase1_collect.py pdf-set
python3 scripts/phase1_build.py
python3 scripts/phase1_collect.py probe silver_rl
python3 scripts/phase1_collect.py probe berkeley_cs285
python3 scripts/phase1_collect.py probe stanford_cs234
python3 scripts/phase1_collect.py probe stanford_cs224r
python3 scripts/phase1_collect.py probe current_course
python3 scripts/phase1_build.py
python3 scripts/phase1_report.py
```

The second build incorporates the HTTP checks into manifests. To inspect an additional PDF or index an additional page, use:

```text
python3 scripts/phase1_collect.py pdf SOURCE_ID URL
python3 scripts/phase1_collect.py page SOURCE_ID SNAPSHOT_SLUG URL
```

New catalogs do not automatically become reviewed manifest entries. Update the relevant inventory extraction rule after inspecting the evidence. Keep each configured course's original ID and local files in place. The HW1B dependency is a referenced assignment resource, not another comparison course.

## Evidence and storage conventions

- `sources/<source_id>/snapshots/` contains page catalogs, source context, retrieval metadata, selected PDF inspection metadata, local file hashes, and HTTP checks. Catalogs preserve links and headings rather than full websites.
- Remote PDFs are inspected in the temporary `rl-phase1-cache` directory under Python's `tempfile.gettempdir()`. Extracted full text and transient downloads are not repository deliverables. Local teaching files are read in place.
- `observed_at` and `checked_at` are UTC inspection times. They do not substitute for unknown original download dates or establish that a listed lecture was delivered.
- `http_metadata_only_not_content_review` verifies a response, not code execution, video playback, or document contents. `pdf_text_inspected` denotes the additional PDF inspection. Linked-but-unchecked material remains explicitly labeled.
- Optional papers, archived recordings, and current teaching material remain distinct. The project-report gallery is indexed as a collection; individual reports were not assessed.
- The collector checks public access and robots policy, follows bounded redirects, and does not authenticate. These are implementation safeguards, not added project governance or curriculum rules.
- Manifests contain source evidence. Generated source READMEs and summaries are views of that evidence. Source-specific extraction notes live in `phase1_build.py`; rebuilding overwrites manifests, so corrections must also be reflected there when appropriate.
- The configured book is a direct reference file and has no manifest. Course-to-book mapping and all cross-course topic normalization remain Phase 2 work.

Start with [the completion report](../analysis/source_summaries/phase1_completion.md) for exit criteria and evidence gaps.

# Phase 2 normalization and evidence views

Start with [the Phase 2 completion report](../analysis/phase2_completion.md). The maintained evidence model is `analysis/normalized_topics.yaml`. Its topic IDs, source observations, ambiguity records and book references are reviewed data, not the output of automatic keyword matching. Edit that file to correct normalization, then regenerate the views. Do not maintain separate topic mappings in scripts or generated Markdown.

## Validate and render offline

```sh
python3 scripts/phase2_report.py --check-only --check-generated
python3 scripts/phase2_report.py
```

The first command validates the model and verifies that its six Markdown views are current; the second validates and regenerates them. Both run without network access or the temporary PDF cache. Dependencies are Python 3 and PyYAML. Checks cover duplicate YAML keys, configured source and book IDs, complete source-topic records, material provenance, physical page bounds, evidence indices, inferred-depth labels, assessment taxonomy, book page offsets and local-file hashes. Every weekly topic/exposure/optional/transition item, video content item and assignment hypothesis must have an exact configuration-pointer mapping.

The optional `/private/tmp/rl_phase2_protected.json` session record contains historical pre-Phase-2 hashes. Differences or missing historical files appear in `protected_snapshot_warnings` in the JSON result and do not fail ordinary validation. These warnings report drift, not permission: review changes against the decision log and Git history. The script never updates the snapshot or asks to accept new hashes. Current evidence hashes, provenance, configuration pointers and generated-view checks still fail on inconsistencies.

For a strict historical audit, add `--strict-protected-hashes`; it fails if the snapshot is absent or any recorded project file differs. Finder `.DS_Store` metadata is ignored in both modes. This is useful for checking the original phase boundary, not normal work after accepted changes. With no snapshot, ordinary validation reports `protected_snapshot_status: unavailable` and continues; the temporary record is not a repository dependency.

The Phase 1 validator intentionally has a pre-Phase-2 boundary assertion; use the Phase 2 validator now, not the Phase 1 validator. Rendering Phase 2 views does not rerun collection or alter source manifests. Local source PDFs and the book must still be present to validate their recorded hashes, even when excluded from Git. A fresh session in this existing workspace can use them; a fresh clone needs those files restored separately.

Generated views:

- `analysis/topic_matrix.md`
- `analysis/sequencing.md`
- `analysis/phase2/evidence_by_topic.md`
- `analysis/phase2/book_mapping.md`
- `analysis/phase2/ambiguities.md`
- `analysis/phase2_completion.md`

## Reinspect inventoried PDFs

```sh
python3 scripts/phase2_inspect.py
python3 scripts/phase2_inspect.py --network
```

Inspection reads local PDFs and the temporary `rl-phase1-cache`; `--network` additionally fetches already-inventoried PDFs missing from that cache. It requires the Phase 1 collection dependencies and Poppler. It writes only the Phase 2 inspection ledger, `analysis/phase2/corpus.json`, plus temporary PDFs/text. It does not expand the source inventory or infer topic coverage.

Reinspection replaces the ledger. On a machine without cached remote PDFs, the offline inspection command records them as `not_cached`; use `--network` when reconstructing the corpus. Review changed hashes and page locators before reusing an existing normalized mapping against refreshed artifacts. The normal report/validation commands do not need reinspection and do not download anything.

Physical PDF pages are 1-based. Book references additionally record printed pages; the configured book uses a verified +22 offset. The book remains a direct reference file without a manifest. Course coverage, course reading pointers and book correspondence are distinct. Unknown source-topic pairs are not evidence of absence; apparent depth is an inference. Phase 2 creates no redesigned-course decisions and does not start Phase 3.
