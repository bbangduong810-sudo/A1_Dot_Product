
import csv
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent.parent

INPUT = ROOT / "results" / "summary_20261123_161151.csv"
OUTPUT = ROOT / "results" / "plots"
OUTPUT.mkdir(parents=True, exist_ok=True)

with INPUT.open(encoding="utf-8", newline="") as f:
    rows = list(csv.DictReader(f))

sizes = sorted({int(r["N"]) for r in rows})


def parallel_rows(n):
    return sorted(
        [
            r for r in rows
            if int(r["N"]) == n and r["mode"] == "parallel"
        ],
        key=lambda r: int(r["threads"])
    )


def save_plot(filename):
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(OUTPUT / filename, dpi=200)
    plt.close()
    print("Created:", filename)


# 1. Speedup
plt.figure(figsize=(9, 5))

for n in sizes:
    data = parallel_rows(n)
    x = [int(r["threads"]) for r in data]
    y = [float(r["speedup_compute"]) for r in data]
    plt.plot(x, y, marker="o", label=f"N={n:,}")

plt.axhline(1, linestyle="--", label="Sequential baseline")
plt.xlabel("Number of threads")
plt.ylabel("Speedup")
plt.title("OpenMP Dot Product - Compute Speedup")
plt.legend()
save_plot("speedup.png")


# 2. Efficiency
plt.figure(figsize=(9, 5))

for n in sizes:
    data = parallel_rows(n)
    x = [int(r["threads"]) for r in data]
    y = [
        float(r["efficiency_compute"]) * 100
        for r in data
    ]
    plt.plot(x, y, marker="o", label=f"N={n:,}")

plt.xlabel("Number of threads")
plt.ylabel("Efficiency (%)")
plt.title("OpenMP Dot Product - Compute Efficiency")
plt.legend()
save_plot("efficiency.png")


# 3. Compute time for each vector size
for n in sizes:
    data = parallel_rows(n)
    x = [int(r["threads"]) for r in data]
    y = [float(r["compute_median_ms"]) for r in data]

    seq = next(
        r for r in rows
        if int(r["N"]) == n and r["mode"] == "sequential"
    )

    baseline = float(seq["compute_median_ms"])

    plt.figure(figsize=(9, 5))
    plt.plot(x, y, marker="o", label="OpenMP")
    plt.axhline(
        baseline,
        linestyle="--",
        label="Sequential"
    )

    plt.xlabel("Number of threads")
    plt.ylabel("Median compute time (ms)")
    plt.title(f"Dot Product Performance - N={n:,}")
    plt.legend()

    save_plot(f"compute_time_N{n}.png")


print("\nAll plots generated successfully.")
