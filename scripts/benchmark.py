
import csv
import random
import re
import statistics
import subprocess
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RESULTS = ROOT / "results"
RESULTS.mkdir(exist_ok=True)

SEQ = ROOT / "sequential.exe"
PAR = ROOT / "parallel.exe"

# Initial smoke benchmark; expand after verification
SIZES = [1_000_000, 10_000_000, 50_000_000]
THREADS = [1, 2, 4, 8, 16, 22]
REPETITIONS = 5

stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
raw_file = RESULTS / f"raw_{stamp}.csv"
summary_file = RESULTS / f"summary_{stamp}.csv"


def expected_result(n):
    cycle = sum(
        (i % 100 + 1) * ((i % 100 + 4) % 100 + 1)
        for i in range(100)
    )
    return (n // 100) * cycle + sum(
        (i % 100 + 1) * ((i % 100 + 4) % 100 + 1)
        for i in range(n % 100)
    )


def extract(label, output):
    pattern = rf"^{re.escape(label)}\s*:\s*([0-9.]+)"
    match = re.search(pattern, output, re.MULTILINE)

    if not match:
        raise RuntimeError(f"Missing {label}:\n{output}")

    return float(match.group(1))


def execute(n, mode, threads):
    if mode == "sequential":
        command = [str(SEQ), str(n)]
    else:
        command = [str(PAR), str(n), str(threads)]

    result = subprocess.run(
        command,
        cwd=ROOT,
        capture_output=True,
        text=True,
        timeout=120,
        check=True
    )

    dot = extract("Dot product", result.stdout)
    expected = expected_result(n)

    if dot != expected:
        raise RuntimeError(
            f"Wrong result: got {dot}, expected {expected}"
        )

    return {
        "N": n,
        "mode": mode,
        "threads": threads,
        "dot_product": dot,
        "compute_ms": extract(
            "Compute time (ms)", result.stdout
        ),
        "total_ms": extract(
            "Total time (ms)", result.stdout
        ),
    }


def median(values):
    return statistics.median(values)


def iqr(values):
    q1, _, q3 = statistics.quantiles(
        values, n=4, method="inclusive"
    )
    return q3 - q1


def main():
    if not SEQ.exists() or not PAR.exists():
        raise FileNotFoundError(
            "Compile sequential.exe and parallel.exe first"
        )

    rows = []
    rng = random.Random(20261123)

    for n in SIZES:
        print(f"\n=== N = {n:,} ===", flush=True)

        cases = [("sequential", 1)]
        cases += [("parallel", p) for p in THREADS]

        # Warm up each configuration before recording data
        for mode, p in cases:
            execute(n, mode, p)

        for repetition in range(1, REPETITIONS + 1):
            order = cases.copy()
            rng.shuffle(order)

            for mode, p in order:
                row = execute(n, mode, p)
                row["repetition"] = repetition
                rows.append(row)

                print(
                    f"Run {repetition}/5 | {mode:10} "
                    f"| threads={p:2} "
                    f"| compute={row['compute_ms']:.6f} ms",
                    flush=True
                )

    raw_fields = [
        "N", "mode", "threads", "repetition",
        "dot_product", "compute_ms", "total_ms"
    ]

    with raw_file.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=raw_fields)
        writer.writeheader()
        writer.writerows(rows)

    summaries = []

    for n in SIZES:
        subset = [r for r in rows if r["N"] == n]

        baseline = median([
            r["compute_ms"] for r in subset
            if r["mode"] == "sequential"
        ])

        baseline_total = median([
            r["total_ms"] for r in subset
            if r["mode"] == "sequential"
        ])

        for mode, p in [("sequential", 1)] + [
            ("parallel", t) for t in THREADS
        ]:
            selected = [
                r for r in subset
                if r["mode"] == mode and r["threads"] == p
            ]

            compute = [r["compute_ms"] for r in selected]
            total = [r["total_ms"] for r in selected]

            cm = median(compute)
            tm = median(total)

            speedup = baseline / cm if cm > 0 else None
            total_speedup = (
                baseline_total / tm if tm > 0 else None
            )

            summaries.append({
                "N": n,
                "mode": mode,
                "threads": p,
                "runs": len(selected),
                "compute_median_ms": cm,
                "compute_min_ms": min(compute),
                "compute_max_ms": max(compute),
                "compute_iqr_ms": iqr(compute),
                "total_median_ms": tm,
                "total_min_ms": min(total),
                "total_max_ms": max(total),
                "total_iqr_ms": iqr(total),
                "speedup_compute": speedup,
                "efficiency_compute": (
                    speedup / p if speedup is not None
                    else None
                ),
                "speedup_total": total_speedup,
                "efficiency_total": (
                    total_speedup / p
                    if total_speedup is not None else None
                )
            })

    with summary_file.open(
        "w", newline="", encoding="utf-8"
    ) as f:
        writer = csv.DictWriter(
            f, fieldnames=list(summaries[0].keys())
        )
        writer.writeheader()
        writer.writerows(summaries)

    print("\n=== BENCHMARK COMPLETE ===")
    print("Raw data:", raw_file)
    print("Summary:", summary_file)

    for item in summaries:
        print(
            f"N={item['N']} | {item['mode']:10} "
            f"| threads={item['threads']:2} "
            f"| median={item['compute_median_ms']:.6f} ms"
        )


if __name__ == "__main__":
    main()
