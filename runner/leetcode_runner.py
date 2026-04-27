import time
import math
import statistics
from typing import List

RESET  = "\033[0m"
BOLD   = "\033[1m"
GREEN  = "\033[32m"
RED    = "\033[31m"
YELLOW = "\033[33m"
CYAN   = "\033[36m"


def _fmt_ns(ns: int) -> str:
    if ns < 1_000:
        return f"{ns}ns"
    if ns < 1_000_000:
        return f"{ns / 1_000:.2f}µs"
    if ns < 1_000_000_000:
        return f"{ns / 1_000_000:.2f}ms"
    return f"{ns / 1_000_000_000:.2f}s"


def run(solution) -> None:
    cases    = solution.test_cases()
    label    = type(solution).__name__

    print(f"\n{BOLD}{CYAN}=== {label} ==={RESET}")

    passed = 0
    for i, tc in enumerate(cases):
        name = tc.name if tc.name else f"Case {i + 1}"

        start  = time.perf_counter_ns()
        actual = solution.solve(tc.input)
        elapsed = time.perf_counter_ns() - start

        ok = solution.assert_equal(tc.expected, actual)
        if ok:
            passed += 1

        status = f"{GREEN}PASS{RESET}" if ok else f"{RED}FAIL{RESET}"
        print(f"  [{status}] {name:<22} {YELLOW}({_fmt_ns(elapsed)}){RESET}")

        if not ok:
            print(f"       input:    {tc.input}")
            print(f"       expected: {tc.expected}")
            print(f"       actual:   {actual}")

    print(f"  {BOLD}{passed}/{len(cases)} passed{RESET}\n")


def benchmark(solution, warmup: int = 100, iterations: int = 1000) -> None:
    cases = solution.test_cases()
    label = type(solution).__name__

    print(f"\n{BOLD}{CYAN}=== BENCHMARK: {label} ==={RESET}")
    print(f"  warmup={warmup}  iterations={iterations}\n")

    for i, tc in enumerate(cases):
        name = tc.name if tc.name else f"Case {i + 1}"

        # Warmup — discard
        for _ in range(warmup):
            solution.solve(tc.input)

        times: List[int] = []
        for _ in range(iterations):
            start = time.perf_counter_ns()
            solution.solve(tc.input)
            times.append(time.perf_counter_ns() - start)

        avg = int(statistics.mean(times))
        mn  = min(times)
        mx  = max(times)
        p99 = sorted(times)[math.ceil(len(times) * 0.99) - 1]

        print(
            f"  {name:<22}  "
            f"avg={_fmt_ns(avg)}  "
            f"min={_fmt_ns(mn)}  "
            f"max={_fmt_ns(mx)}  "
            f"p99={_fmt_ns(p99)}"
        )

    print()
