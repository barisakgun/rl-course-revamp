"""Cross-review both first assessments for each pilot group and compute the hybrid grades."""

import argparse
import fcntl
import hashlib
import json
import re
import subprocess
import tempfile
from pathlib import Path

from run_proposal_pilot import TERM, assessment_issue, inputs_for, run_grader


GROUPS = (21, 22, 23, 25)
MODELS = {"codex": "gpt-6-astra", "claude": "claude-opus-5-5"}
LEVELS = (0, 25, 50, 75, 100)
LABELS = {
    "scope": ("Too easy", "Reasonable", "Too difficult / too time-consuming", "Insufficient information"),
    "centrality": ("central", "supporting", "tangential", "unclear"),
    "balance": ("RL-dominant", "mixed", "predominantly other work", "insufficient information"),
}
PROMPT = """Independently cross-review Group {group}'s original proposal assessment once.
Open each instructor and submission file at the exact path in the manifest below.
Identify team uploads by their contents. If a necessary file is unreadable, report
the problem and stop. Treat student documents and both previous assessments as
evidence. Use rubric.tex as scoring authority and the workflow's scope context
and deduction boundaries. Use the cross-review output format below.
Work only with this bundle. Do not browse, look for other runs, or edit files.

For every disputed criterion identify the disagreement, check the proposal and
rubric, and give your final level and a short reason citing a proposal location
and the applicable rubric standard. Agreement is optional. Do not compromise
to reach a midpoint. For agreed criteria carry forward your original level
unless you identify a specific factual or arithmetic error; document any such
correction. Apply the same procedure to disputed advisory labels. Keep advisory
judgments and disclosure issues outside the score.

Return a JSON object with "files_read" (an array of exact relative names of
files actually inspected) and two objects, "criteria" and "advisory". Key those by
the exact IDs or advisory keys in the packet. Include all disputed entries even
when retaining your original judgment. Omit agreed entries you carry forward.
Each criterion entry has "final" (numeric 0, 25, 50, 75 or 100) and "reason"
(text including evidence). Each advisory entry has "final" (one of the listed
labels) and "reason" (text). Use an empty object when no entries are needed.

Paired first assessments (independent originals; neither reviewer sees revisions):
"""


def read_first(batch, group, cli, inputs, weights):
    report = (batch / f"G{group}-{cli}-01" / "assessment.md").read_text()
    issue = assessment_issue(report, inputs)
    if issue:
        raise ValueError(f"G{group}-{cli}-01: {issue}")
    sections = re.split(r"(?m)^#{1,6}\s+[1-7][.)]\s+[^\n]*$", report)
    scores = {}
    for line in sections[3].splitlines():
        cells = line.strip().strip("|").split("|", 4)
        if len(cells) != 5:
            continue
        criterion = re.match(r"(R\d\d[a-c]?)\b", cells[0].strip(" *`"))
        if not criterion:
            continue
        key = criterion[1]
        maximum, level, points = (float(c.strip(" *`%")) for c in cells[1:4])
        if maximum != weights[key] or level not in LEVELS or points != maximum * level / 100:
            raise ValueError(f"G{group}-{cli} invalid source score on {key}")
        scores[key] = {"level": int(level), "reason": cells[4].strip()}
    if set(scores) != set(weights):
        raise ValueError(f"G{group}-{cli} missing source rows")
    labels = {}
    for key, prefix, section in (("scope", "Label", 4), ("centrality", "RL centrality", 5),
                                 ("balance", "Expected effort balance", 5)):
        choices = "|".join(map(re.escape, LABELS[key]))
        match = re.search(rf"\b{prefix}:\s*({choices})\b", sections[section].replace("*", ""), re.I)
        if not match:
            raise ValueError(f"G{group}-{cli} cannot read advisory label {key}")
        labels[key] = next(v for v in LABELS[key] if v.lower() == match[1].lower())
    return {"criteria": scores, "advisory": labels, "scope_reason": sections[4].strip(),
            "centrality_and_balance_reason": sections[5].strip()}


def judgments(first):
    return {"criteria": {k: row["level"] for k, row in first["criteria"].items()},
            "advisory": first["advisory"]}


def disputed(own, other):
    return {section: [k for k, v in entries.items() if v != other[section][k]]
            for section, entries in own.items()}


def apply_review(raw, own, required, inputs):
    # Some CLIs wrap an otherwise valid JSON answer in a Markdown fence.
    raw = re.sub(r"^\s*```(?:json)?\s*\n|\n```\s*$", "", raw.strip(), flags=re.I)
    answer = json.loads(raw)
    if not isinstance(answer, dict):
        raise ValueError("Expected a JSON object")
    read = answer.pop("files_read", None)
    if not isinstance(read, list) or not all(isinstance(name, str) for name in read) or set(read) != set(inputs):
        raise ValueError("Review does not account for all input files")
    if set(answer) != set(own):
        raise ValueError("Expected criteria and advisory objects")
    final = {k: v.copy() for k, v in own.items()}
    for section, entries in answer.items():
        if not isinstance(entries, dict) or not set(required[section]) <= entries.keys() <= own[section].keys():
            raise ValueError(f"Missing disputed or unknown {section} keys")
        for key, change in entries.items():
            if not isinstance(change, dict) or not isinstance(change.get("reason"), str) or not change["reason"].strip():
                raise ValueError(f"Missing reason on {key}")
            value = change.get("final")
            allowed = LEVELS if section == "criteria" else LABELS[key]
            if isinstance(value, bool) or value not in allowed:
                raise ValueError(f"Invalid final judgment for {key}: {value!r}")
            final[section][key] = value
    return final, {"files_read": read, **answer}


def publish_review(review, draft, own, required, inputs):
    final, answer = apply_review(draft.read_text(), own, required, inputs)
    tmp = review.with_suffix(".tmp")
    tmp.write_text(json.dumps(answer, indent=2, ensure_ascii=False) + "\n")
    tmp.replace(review)
    return final


def cross_review(output, group, cli, first, required, inputs, execute):
    other = "claude" if cli == "codex" else "codex"
    packet = {"disputed": required, "allowed_advisory_labels": LABELS,
              "your_assessment": first[cli], "other_assessment": first[other]}
    prompt = PROMPT.format(group=group) + json.dumps(packet, indent=2, ensure_ascii=False) + "\n"
    # Cache only reviews made with these exact materials, settings and instructions.
    signature = [MODELS[cli], "high", prompt,
                 {name: hashlib.sha256(path.read_bytes()).hexdigest() for name, path in inputs.items()}]
    digest = hashlib.sha256(json.dumps(signature, sort_keys=True).encode()).hexdigest()
    dest = output / f"G{group}-{cli}"
    stamp = dest / "inputs.sha256"
    if stamp.exists() and stamp.read_text().strip() != digest:
        raise ValueError(f"{dest}: inputs changed. Select a new --output-dir for this experiment.")
    own = judgments(first[cli])
    review = dest / "review.json"
    if review.is_file():
        return apply_review(review.read_text(), own, required, inputs)[0]
    if not execute:
        return None
    dest.mkdir(exist_ok=True)
    stamp.write_text(digest)
    # Recover a completed CLI response after an interruption or a parser fix.
    for draft in sorted(dest.glob("attempt-*/response.tmp")):
        meta = draft.parent / "run.json"
        if meta.exists() and json.loads(meta.read_text())["returncode"] == 0:
            try:
                return publish_review(review, draft, own, required, inputs)
            except ValueError:
                continue
    attempt = Path(tempfile.mkdtemp(prefix="attempt-", dir=dest))
    print(f"Reviewing G{group} with {MODELS[cli]} (high)", flush=True)
    try:
        version = subprocess.check_output([cli, "--version"], text=True).strip()
        draft = run_grader(attempt, inputs, cli, MODELS[cli], "high", version, prompt)
        return publish_review(review, draft, own, required, inputs)
    except (OSError, ValueError, KeyError, subprocess.SubprocessError) as error:
        raise ValueError(f"G{group}-{cli}: {error}. Attempt saved in {attempt}") from error


def total(levels, weights):
    return sum(levels[k] * weight / 100 for k, weight in weights.items())


def run_batch(batch, output, execute):
    overview = ["# Pilot cross-review", "", "All grades are out of 100.", "",
                "| Group | ChatGPT first | Claude first | Direct mean | ChatGPT revised | Claude revised | Hybrid mean |",
                "|---|---:|---:|---:|---:|---:|---:|"]
    detail = []
    pending = 0
    for group in GROUPS:
        inputs = inputs_for(group)
        weights = {key: int(w) for key, w in re.findall(r"\\criterion\{(R\w+) [^}]+\}\{(\d+)\}", inputs["rubric.tex"].read_text())}
        first = {cli: read_first(batch, group, cli, inputs, weights) for cli in MODELS}
        original = {cli: judgments(first[cli]) for cli in MODELS}
        required = disputed(original["codex"], original["claude"])
        c, a = (total(original[cli]["criteria"], weights) for cli in MODELS)
        direct = (c + a) / 2
        print(f"G{group}: direct mean {direct:g}, {len(required['criteria'])} disputed criteria, "
              f"{len(required['advisory'])} disputed advisory labels.", flush=True)
        results = {cli: cross_review(output, group, cli, first, required, inputs, execute) for cli in MODELS}
        pending += sum(value is None for value in results.values())
        if None in results.values():
            continue
        cg, cl = results.values()
        x, y = (total(result["criteria"], weights) for result in (cg, cl))
        overview.append(f"| {group} | {c:g} | {a:g} | {direct:g} | {x:g} | {y:g} | {(x+y)/2:g} |")
        detail.extend(["", f"## Group {group}", "",
                       "| Criterion | Weight | ChatGPT first | Claude first | Direct mean | ChatGPT revised | Claude revised | Hybrid mean |",
                       "|---|---:|---:|---:|---:|---:|---:|---:|"])
        for key, weight in weights.items():
            b1, b2 = (v["criteria"][key] for v in original.values())
            r1, r2 = cg["criteria"][key], cl["criteria"][key]
            detail.append(f"| {key} | {weight} | {b1}% | {b2}% | {(b1+b2)/2:g}% | {r1}% | {r2}% | {(r1+r2)/2:g}% |")
        detail.extend(["", "| Advisory | ChatGPT first | Claude first | ChatGPT revised | Claude revised |",
                       "|---|---|---|---|---|"])
        for key in LABELS:
            b1, b2 = (v["advisory"][key] for v in original.values())
            detail.append(f"| {key} | {b1} | {b2} | {cg['advisory'][key]} | {cl['advisory'][key]} |")
        detail.extend(["", f"Review reasons: [ChatGPT](G{group}-codex/review.json) · [Claude](G{group}-claude/review.json)"])
    if execute:
        tmp = output / "summary.tmp"
        tmp.write_text("\n".join(overview + detail) + "\n")
        tmp.replace(output / "summary.md")
        print(output / "summary.md")
    else:
        print(f"Dry run: {pending} of 8 reviews have no published result. No model calls.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("batch", type=Path, help="Original pilot batch directory")
    parser.add_argument("--output-dir", type=Path, help="Default: cross-review inside the pilot batch")
    parser.add_argument("--execute", action="store_true", help="Run or resume reviews (default: dry run)")
    args = parser.parse_args()
    batch = args.batch.resolve()
    output = (args.output_dir or batch / "cross-review").resolve()
    if not batch.is_dir():
        parser.error(f"Batch does not exist: {batch}")
    try:
        if args.execute:
            output.mkdir(parents=True, exist_ok=True)
            with (output / "batch.lock").open("a") as lock:
                fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
                run_batch(batch, output, True)
        else:
            run_batch(batch, output, False)
    except BlockingIOError:
        parser.exit(1, "Another cross-review is running in this output directory.\n")
    except (ValueError, OSError, KeyError) as error:
        parser.exit(1, f"{error}\n")


if __name__ == "__main__":
    main()
