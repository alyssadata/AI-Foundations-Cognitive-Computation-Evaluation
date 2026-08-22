#!/usr/bin/env python3
import csv
import math
import sys
from pathlib import Path

YES = {"YES", "Y", "TRUE", "1"}
NO = {"NO", "N", "FALSE", "0"}

ACTIVE_PROPERTIES = {
    8: ["P01", "P03", "P04", "P07", "P08", "P10"],
    16: ["P01", "P02", "P03", "P04", "P06", "P07", "P08", "P10"],
    32: ["P01", "P02", "P03", "P04", "P06", "P07", "P08", "P09", "P10", "P11"],
    64: ["P01", "P02", "P03", "P04", "P05", "P06", "P07", "P08", "P09", "P10", "P11", "P12"],
}


def norm(value):
    text = str(value).strip().upper()
    if text in YES:
        return "YES"
    if text in NO:
        return "NO"
    raise ValueError(f"Expected YES/NO value, got {value!r}")


def load_candidates(path):
    with open(path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    if not rows or "candidate" not in rows[0]:
        raise ValueError("Candidate matrix must contain a 'candidate' column.")
    properties = [c for c in rows[0].keys() if c != "candidate"]
    data = {}
    for row in rows:
        data[row["candidate"]] = {p: norm(row[p]) for p in properties}
    return data, properties


def load_trace(path):
    with open(path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    required = {
        "run_id",
        "candidate_space_n",
        "target",
        "final_answer",
        "step",
        "property",
        "answer",
    }
    if not rows or not required.issubset(rows[0].keys()):
        raise ValueError(f"Trace must contain columns: {sorted(required)}")
    return rows


def guarantee(active, data, prop):
    yes = sum(data[c][prop] == "YES" for c in active)
    no = len(active) - yes
    worst = max(yes, no)
    return 1 - (worst / len(active)), yes, no


def main():
    if len(sys.argv) != 3:
        print("usage: python score_test_001.py TEST_001_CANDIDATES.csv RUN_TRACE.csv")
        raise SystemExit(2)

    data, properties = load_candidates(sys.argv[1])
    trace = load_trace(sys.argv[2])

    for n, active_props in ACTIVE_PROPERTIES.items():
        missing = [p for p in active_props if p not in properties]
        if missing:
            raise ValueError(f"Candidate matrix is missing required properties for N={n}: {missing}")

    grouped = {}
    run_identity = {}
    for row in trace:
        run_id = row["run_id"].strip()
        if not run_id:
            raise ValueError("run_id may not be blank")
        n = int(row["candidate_space_n"])
        target = row["target"].strip()
        final_answer = row["final_answer"].strip()
        identity = (n, target, final_answer)
        if run_id in run_identity and run_identity[run_id] != identity:
            raise ValueError(
                f"Run ID {run_id} appears with inconsistent N/target/final_answer values"
            )
        run_identity[run_id] = identity
        key = (run_id, n, target, final_answer)
        grouped.setdefault(key, []).append(row)

    scored_steps = []
    summaries = []

    for (run_id, n, target, final_answer), rows in grouped.items():
        if n not in ACTIVE_PROPERTIES:
            raise ValueError(f"candidate_space_n must be one of 8,16,32,64; got {n}")

        universe = [f"C{i:02d}" for i in range(1, n + 1)]
        if target not in universe:
            raise ValueError(f"Target {target} is not in C01..C{n:02d}")
        if final_answer not in universe:
            raise ValueError(f"Final answer {final_answer} is not in C01..C{n:02d}")

        active_props = ACTIVE_PROPERTIES[n]
        active = universe[:]
        used = set()
        seen_steps = set()
        rows = sorted(rows, key=lambda r: int(r["step"]))
        run_ratios = []

        for row in rows:
            step = int(row["step"])
            prop = row["property"].strip()
            answer = norm(row["answer"])

            if step in seen_steps:
                raise ValueError(f"Repeated step {step} in run {run_id}")
            seen_steps.add(step)

            if prop not in properties:
                raise ValueError(f"Unknown property {prop}")
            if prop not in active_props:
                raise ValueError(
                    f"Inactive property {prop} used in run {run_id} with N={n}; "
                    f"active properties are {active_props}"
                )
            if prop in used:
                raise ValueError(f"Repeated property {prop} in run {run_id}")
            if data[target][prop] != answer:
                raise ValueError(
                    f"Recorded answer {answer} conflicts with target {target} value "
                    f"{data[target][prop]} for {prop}"
                )

            before = len(active)
            chosen_g, yes_count, no_count = guarantee(active, data, prop)

            available = []
            for p in active_props:
                if p in used:
                    continue
                g, y, nn = guarantee(active, data, p)
                if y > 0 and nn > 0:
                    available.append((g, p))

            best_g = max((g for g, _ in available), default=0.0)
            divider_ratio = (chosen_g / best_g) if best_g > 0 else 1.0

            active = [c for c in active if data[c][prop] == answer]
            after = len(active)
            run_ratios.append(divider_ratio)

            scored_steps.append({
                "run_id": run_id,
                "candidate_space_n": n,
                "target": target,
                "final_answer": final_answer,
                "step": step,
                "property": prop,
                "answer": answer,
                "candidates_before": before,
                "yes_branch": yes_count,
                "no_branch": no_count,
                "worst_case_guaranteed_elimination": round(chosen_g, 6),
                "best_available_guaranteed_elimination": round(best_g, 6),
                "divider_efficiency_ratio": round(divider_ratio, 6),
                "candidates_after_actual_answer": after,
            })
            used.add(prop)

        correct_final = final_answer == target
        unique_resolution = len(active) == 1
        resolved_candidate = active[0] if unique_resolution else ""
        success = correct_final and unique_resolution and resolved_candidate == final_answer
        questions = len(rows)
        q_min = math.ceil(math.log2(n))

        summaries.append({
            "run_id": run_id,
            "candidate_space_n": n,
            "active_property_count": len(active_props),
            "target": target,
            "final_answer": final_answer,
            "correct_final_answer": "YES" if correct_final else "NO",
            "unique_resolution": "YES" if unique_resolution else "NO",
            "success": "YES" if success else "NO",
            "questions": questions,
            "information_theoretic_minimum": q_min,
            "question_overhead": questions - q_min,
            "mean_divider_efficiency_ratio": round(sum(run_ratios) / len(run_ratios), 6) if run_ratios else "",
            "final_remaining": "|".join(active),
        })

    step_path = Path(sys.argv[2]).with_name(Path(sys.argv[2]).stem + "_SCORED_STEPS.csv")
    summary_path = Path(sys.argv[2]).with_name(Path(sys.argv[2]).stem + "_SUMMARY.csv")

    if scored_steps:
        with open(step_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=scored_steps[0].keys())
            writer.writeheader()
            writer.writerows(scored_steps)
    else:
        raise ValueError("Trace contains no scored property questions")

    with open(summary_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=summaries[0].keys())
        writer.writeheader()
        writer.writerows(summaries)

    print(f"Wrote {step_path}")
    print(f"Wrote {summary_path}")


if __name__ == "__main__":
    main()
