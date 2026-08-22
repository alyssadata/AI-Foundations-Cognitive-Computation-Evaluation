#!/usr/bin/env python3
"""
TEST_001 — EXT-CLM-004
Hierarchical recognition scaling benchmark.

This test measures comparison/distinction counts for:
1. flat sequential recognition;
2. a balanced 50/50 binary hierarchy;
3. a moderately imbalanced 75/25 hierarchy;
4. a pathological 1-vs-rest hierarchy.

The first two conditions adjudicate the registered recognition-scaling claim.
The imbalanced conditions expose the dependency on useful partition structure.

This script does not model the cost of discovering or constructing the hierarchy.
That mechanism is not specified sufficiently in the evaluated source and remains
outside the decision rule for this first protocol.
"""

import math
import platform

SIZES = [2**4, 2**8, 2**12, 2**16, 2**20]


def flat_worst_case_comparisons(n: int) -> int:
    """Actually scan n candidate identifiers for a target placed last."""
    target = n - 1
    comparisons = 0
    for candidate in range(n):
        comparisons += 1
        if candidate == target:
            return comparisons
    raise RuntimeError("target not found")


def balanced_binary_depth(n: int) -> int:
    """Traverse a perfectly balanced binary hierarchy until one candidate remains."""
    remaining = n
    depth = 0
    while remaining > 1:
        remaining //= 2
        depth += 1
    return depth


def moderate_75_25_worst_depth(n: int) -> int:
    """Follow the larger side of repeated approximately 75/25 partitions."""
    remaining = n
    depth = 0
    while remaining > 1:
        if remaining == 2:
            remaining = 1
        else:
            remaining = min(remaining - 1, math.ceil(0.75 * remaining))
        depth += 1
    return depth


def one_vs_rest_worst_depth(n: int) -> int:
    """Worst-case depth when each distinction removes only one candidate."""
    return n - 1


def main() -> None:
    print(f"python_version,{platform.python_version()}")
    print(
        "N,log2_N,flat_worst_comparisons,flat_expected_comparisons,"
        "balanced_50_50_worst_depth,moderate_75_25_worst_depth,"
        "pathological_1_vs_rest_worst_depth,flat_worst_to_balanced_ratio"
    )
    for n in SIZES:
        flat_worst = flat_worst_case_comparisons(n)
        balanced = balanced_binary_depth(n)
        row = [
            n,
            int(math.log2(n)),
            flat_worst,
            (n + 1) / 2,
            balanced,
            moderate_75_25_worst_depth(n),
            one_vs_rest_worst_depth(n),
            flat_worst / balanced,
        ]
        print(",".join(str(value) for value in row))


if __name__ == "__main__":
    main()
