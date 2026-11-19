"""Launch independent Codex and Claude Code assessments for the Fall 2026 pilot."""

import argparse
import fcntl
import json
import os
import re
import shutil
import subprocess
import tempfile
from pathlib import Path
from urllib.parse import unquote


REPO = Path(__file__).resolve().parents[1]
TERM = REPO.parent / "studentHWs" / "fall26"
COMMON = {
    "rubric.tex": REPO / "course/projects/proposal_rubric_chatgpt/main.tex",
    "grading_workflow.tex": REPO / "course/projects/ai_proposal_grading_guidelines_chatgpt/main.tex",
    "proposal_guidelines.pdf": REPO / "course/projects/handouts/proposal_guidelines_chatgpt.pdf",
    "llm_use_guidelines.pdf": REPO / "course/projects/handouts/llm_use_written_reports_chatgpt.pdf",
}
# LearnHub submission identifiers from the four selected groups and optional fifth.
SUBMISSIONS = {21: 19231, 23: 19256, 22: 19236, 25: 19277, 29: 19234}
PROMPT = """Independently assess Group {group}'s COMP438/538 Fall 2026 project proposal.
Run ID: {run_id}. Work only with the files in this working directory.
The four files at the top level are shared instructor materials for both graders.
Use rubric.tex for all criterion IDs, anchors, weights and advisory labels. Follow
grading_workflow.tex, including its common scope context and all seven output sections.
Use proposal_guidelines.pdf and llm_use_guidelines.pdf for the released expectations.
The file list below gives the relative name and exact absolute path of every
input. Open each path directly, including every team upload. Read all proposal
pages and figures. Identify the proposal, any completed LLM-use report, and
any extra instructions by their contents, even if filenames suggest otherwise.
In section 1 record one plain line per listed file: READ followed by a space
and its exact relative name. Use UNREAD instead if reading failed, and explain
the failure on the next line. Only mark a file READ after inspecting it.
Grade only this
team, using only this bundle. Do not seek other assessments or browse externally.
Score all 18 rows with evidence locations and reasons. Check the total out of 100
and its contribution out of 5. Apply format findings only through R16, keep
advisory judgments and disclosure flags outside the score, and distinguish
observed facts from uncertainties. Flag any required input you cannot read.
Return the seven sections as numbered Markdown headings. In section 3 use a
Markdown table with columns ID, maximum, level (%), awarded points, and
evidence/reason. Write the total as "Total: <points>/100". Record
model/version and settings if known. Do not edit files or send grades.
"""
ROW_IDS = {"R01a", "R01b", "R01c", *(f"R{i:02d}" for i in range(2, 17))}


def inputs_for(group):
    folders = list((TERM / "Project Proposals").glob(f"*_{SUBMISSIONS[group]}_assignsubmission_file"))
    if len(folders) != 1:
        raise ValueError(f"Expected one submission folder for group {group}, found {len(folders)}")
    files = dict(COMMON)
    submissions = sorted(folders[0].glob("*.pdf"))
    if not submissions:
        raise ValueError(f"No PDFs for group {group}")
    files.update({f"submission/{p.name}": p for p in submissions})
    for path in files.values():
        if not path.is_file():
            raise FileNotFoundError(path)
    return files


def assessment_issue(report, inputs, require_read_status=False):
    sections = re.split(r"(?m)^#{1,6}\s+([1-7])[.)]\s+[^\n]*$", report)
    if sections[1::2] != list("1234567") or not all(s.strip() for s in sections[2::2]):
        return "missing or empty assessment section"
    status, scores = sections[2], sections[6].replace("*", "").replace("`", "")
    rows = re.findall(r"(?m)^\s*\|\s*(R\d\d[a-c]?)\b[^|\n]*\|\s*\d+(?:\.\d+)?\s*\|"
                      r"\s*\d+(?:\.\d+)?\s*%?\s*\|\s*\d+(?:\.\d+)?\s*\|", scores)
    if len(rows) != len(ROW_IDS) or set(rows) != ROW_IDS:
        return f"expected 18 numeric rubric rows, found {len(set(rows) & ROW_IDS)} distinct scored IDs"
    if not re.search(r"\d+(?:\.\d+)?\s*/\s*100\b", scores):
        return "no numeric total out of 100"
    if require_read_status or re.search(r"(?m)^\s*(?:UNREAD|READ) ", status):
        lines = {line.strip() for line in status.splitlines()}
        missing = [name for name in inputs if f"READ {name}" not in lines or f"UNREAD {name}" in lines]
    else:
        # Older prompts asked for a file inventory in prose. Some graders used Markdown links.
        inventory = unquote(status).casefold()
        missing = [name for name in inputs if Path(name).name.casefold() not in inventory]
    if missing:
        return "input status does not account for " + ", ".join(missing)
    return None


def run_grader(dest, inputs, cli, model, effort, version, instructions):
    with tempfile.TemporaryDirectory(prefix="rl-grader-") as root:
        work = Path(root).resolve()
        (work / "submission").mkdir()
        for name, path in inputs.items():
            shutil.copyfile(path, work / name)
        manifest = "\n".join(f"{name} -> {work / name}" for name in inputs)
        prompt = instructions + "\nInput files:\n" + manifest + "\n"
        (dest / "prompt.txt").write_text(prompt)
        env = os.environ.copy()
        if cli == "codex":
            cmd = ["codex", "exec", "--disable", "memories", "--disable",
                   "external_agent_memory_import", "--ephemeral", "--skip-git-repo-check",
                   "--sandbox", "read-only", "-o", str(dest / "response.tmp"),
                   "--model", model, "-c", f"model_reasoning_effort={json.dumps(effort)}", "-"]
        else:
            env["CLAUDE_CODE_DISABLE_AUTO_MEMORY"] = "1"
            cmd = ["claude", "-p", "--no-session-persistence", "--safe-mode",
                   "--tools", "Read", "--allowedTools", "Read", "--output-format", "json",
                   "--model", model, "--effort", effort]
        result = subprocess.run(cmd, cwd=work, env=env, input=prompt, text=True, capture_output=True)
    (dest / "stderr.log").write_text(result.stderr)
    (dest / "stdout.log").write_text(result.stdout)
    (dest / "run.json").write_text(json.dumps(dict(cli=version, requested_model=model,
                                                    requested_effort=effort, command=cmd,
                                                    returncode=result.returncode), indent=2))
    if cli == "claude":
        payload = json.loads(result.stdout) if result.stdout.strip() else {}
        if result.returncode or payload.get("is_error") or payload.get("subtype") != "success":
            raise ValueError(payload.get("result") or result.stderr.strip() or f"Claude exit {result.returncode}")
        (dest / "response.tmp").write_text(payload["result"])
    elif result.returncode:
        raise ValueError(f"Codex exit {result.returncode}")
    draft = dest / "response.tmp"
    if not draft.is_file() or not draft.read_text().strip():
        raise ValueError("No response text")
    return draft


def run_assessment(dest, inputs, cli, model, effort, version, group, run_id):
    prompt = PROMPT.format(group=group, run_id=run_id)
    draft = run_grader(dest, inputs, cli, model, effort, version, prompt)
    issue = assessment_issue(draft.read_text(), inputs, require_read_status=True)
    if issue:
        draft.rename(dest / "incomplete.md")
        raise ValueError(issue)
    draft.rename(dest / "assessment.md")


def publish_retry(run, ready):
    current = run / "assessment.md"
    if current.is_file():
        archive = Path(tempfile.mkdtemp(prefix="superseded-", dir=run))
        os.link(current, archive / current.name)
    # Keep the old assessment readable until its replacement is fully available.
    with tempfile.TemporaryDirectory(dir=run) as temp:
        replacement = Path(temp) / current.name
        os.link(ready, replacement)
        os.replace(replacement, current)


def retry_failed(batch, execute):
    batch = batch.resolve()
    if not batch.is_dir():
        raise SystemExit(f"Batch directory not found: {batch}")

    # A nonblocking directory lock releases automatically if the retry is interrupted.
    fd = os.open(batch, os.O_RDONLY)
    try:
        if execute:
            try:
                fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except BlockingIOError:
                raise SystemExit("Another retry is already running for this batch.")
        pending = []
        for run in sorted(batch.iterdir()):
            match = re.fullmatch(r"G(\d+)-(codex|claude)-(\d+)", run.name)
            if not match or not (run / "run.json").is_file():
                continue
            group = int(match[1])
            inputs = inputs_for(group)
            current = run / "assessment.md"
            issue = assessment_issue(current.read_text(), inputs) if current.is_file() else "missing assessment"
            if not issue:
                continue
            # Recover a completed retry or a saved response that now passes validation.
            ready = next((p for p in sorted(run.glob("retry-*/assessment.md"))
                          if not assessment_issue(p.read_text(), inputs)), None)
            if ready is None:
                rejected = [run / "incomplete.md", *sorted(run.glob("retry-*/incomplete.md"))]
                ready = next((p for p in rejected if p.is_file()
                              and not assessment_issue(p.read_text(), inputs, require_read_status=True)), None)
            if ready:
                print(f"{run.name}: recover saved response from {ready.relative_to(run)}", flush=True)
                if execute:
                    publish_retry(run, ready)
                continue
            meta = json.loads((run / "run.json").read_text())
            pending.append((run, match[2], inputs, meta, group))
            print(f"{run.name}: {issue}", flush=True)
        print(f"{len(pending)} runs to retry.", flush=True)
        if not execute:
            return
        versions = {cli: subprocess.check_output([cli, "--version"], text=True).strip()
                    for cli in sorted({entry[1] for entry in pending})}
        for run, cli, inputs, meta, group in pending:
            attempt = Path(tempfile.mkdtemp(prefix="retry-", dir=run))
            print(f"Retrying {run.name}", flush=True)
            try:
                run_assessment(attempt, inputs, cli, meta["requested_model"], meta["requested_effort"],
                               versions[cli], group, run.name)
            except (OSError, ValueError, KeyError, TypeError) as error:
                raise SystemExit(f"{run.name} failed: {error}. Logs: {attempt}")
            publish_retry(run, attempt / "assessment.md")
    finally:
        os.close(fd)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--groups", nargs="+", type=int, choices=SUBMISSIONS, default=[21, 23, 22, 25])
    parser.add_argument("--runs", type=int, default=2, help="Repetitions per model and proposal")
    parser.add_argument("--codex-model", default="gpt-6-astra", help="Codex model (default: %(default)s)")
    parser.add_argument("--claude-model", default="claude-opus-5-5", help="Claude model (default: %(default)s)")
    parser.add_argument("--codex-effort", default="high", help="Codex reasoning effort (default: %(default)s)")
    parser.add_argument("--claude-effort", default="high", help="Claude reasoning effort (default: %(default)s)")
    parser.add_argument("--output-dir", type=Path, default=TERM / "Proposal Pilot Results")
    parser.add_argument("--execute", action="store_true", help="Launch graders (default: dry run)")
    parser.add_argument("--retry-failed", type=Path, metavar="BATCH",
                        help="Retry missing or incomplete assessments using the current prompt and saved model settings")
    args = parser.parse_args()
    if args.retry_failed:
        retry_failed(args.retry_failed, args.execute)
        return
    if args.runs < 1 or len(set(args.groups)) != len(args.groups):
        parser.error("Specify distinct groups and a positive number of runs.")
    bundles = {group: inputs_for(group) for group in args.groups}
    models = {"codex": args.codex_model, "claude": args.claude_model}
    efforts = {"codex": args.codex_effort, "claude": args.claude_effort}
    versions = {cli: subprocess.check_output([cli, "--version"], text=True).strip() for cli in models}
    for cli, model in models.items():
        print(f"{versions[cli]}: {model}, effort={efforts[cli]}")
    print(f"Groups {args.groups}, {args.runs} runs per grader: {len(bundles)*2*args.runs} assessments.")
    if not args.execute:
        print("Dry run. Input paths and CLI installations checked. Use --execute to grade.")
        return
    args.output_dir.mkdir(parents=True, exist_ok=True)
    batch = Path(tempfile.mkdtemp(prefix="pilot-", dir=args.output_dir)).resolve()
    print(f"Results: {batch}", flush=True)
    failures = []
    for group, inputs in bundles.items():
        for rep in range(1, args.runs + 1):
            for cli, model in models.items():
                run_id = f"G{group}-{cli}-{rep:02d}"
                print(run_id, flush=True)
                dest = batch / run_id
                dest.mkdir()
                try:
                    run_assessment(dest, inputs, cli, model, efforts[cli], versions[cli], group, run_id)
                except (ValueError, KeyError, TypeError) as error:
                    failures.append(run_id)
                    print(f"{run_id} failed: {error}. See {dest}", flush=True)
    if failures:
        raise SystemExit(f"Failed runs: {', '.join(failures)}")


if __name__ == "__main__":
    main()
