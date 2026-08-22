#!/usr/bin/env python3
import csv
import math
import sys
from pathlib import Path

YES = {"YES", "Y", "TRUE", "1"}
NO = {"NO", "N", "FALSE", "0"}


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
    required = {"candidate_space_n", "target", "step", "property", "answer"}
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

    grouped = {}
    for row in trace:
        key = (int(row["candidate_space_n"]), row["target"])
        grouped.setdefault(key, []).append(row)

    scored_steps = []
    summaries = []

    for (n, target), rows in grouped.items():
        if n not in {8, 16, 32, 64}:
            raise ValueError(f"candidate_space_n must be one of 8,16,32,64; got {n}")

        universe = [f"C{i:02d}" for i in range(1, n + 1)]
        if target not in universe:
            raise ValueError(f"Target {target} is not in C01..C{n:02d}")

        active = universe[:]
        used = set()
        rows = sorted(rows, key=lambda r: int(r["step"]))
        run_ratios = []

        for row in rows:
            prop = row["property"].strip()
            answer = norm(row["answer"])

            if prop not in properties:
                raise ValueError(f"Unknown property {prop}")
            if prop in used:
                raise ValueError(f"Repeated property {prop} in run N={n}, target={target}")
            if data[target][prop] != answer:
                raise ValueError(
                    f"Recorded answer {answer} conflicts with target {target} value "
                    f"{data[target][prop]} for {prop}"
                )

            before = len(active)
            chosen_g, yes_count, no_count = guarantee(active, data, prop)

            available = []
            for p in properties:
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
                "candidate_space_n": n,
                "target": target,
                "step": int(row["step"]),
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

        success = len(active) == 1 and active[0] == target
        questions = len(rows)
        q_min = math.ceil(math.log2(n))

        summaries.append({
            "candidate_space_n": n,
            "target": target,
            "success": "YES" if success else "NO",
            "questions": questions,
            "information_theoretic_minimum": q_min,
            "question_overhead": questions - q_min,
            "mean_divider_efficiency_ratio": round(sum(run_ratios) / len(run_ratios), 6) if run_ratios else "",
            "final_remaining": "|".join(active),
        })

    step_path = Path(sys.argv[2]).with_name(Path(sys.argv[2]).stem + "_SCORED_STEPS.csv")
    summary_path = Path(sys.argv[2]).with_name(Path(sys.argv[2]).stem + "_SUMMARY.csv")

    with open(step_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=scored_steps[0].keys())
        writer.writeheader()
        writer.writerows(scored_steps)

    with open(summary_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=summaries[0].keys())
        writer.writeheader()
        writer.writerows(summaries)

    print(f"Wrote {step_path}")
    print(f"Wrote {summary_path}")


if __name__ == "__main__":
    main()
