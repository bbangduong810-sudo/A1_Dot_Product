
import subprocess
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SEQ = ROOT / "sequential.exe"
PAR = ROOT / "parallel.exe"

SIZES = [1, 4, 7, 100, 101, 1000, 1000000]
THREADS = [1, 2, 4, 8]


def expected_dot_product(n):
    # Independent reference calculation
    cycle = sum(
        (i % 100 + 1) * ((i % 100 + 4) % 100 + 1)
        for i in range(100)
    )
    full_cycles, remainder = divmod(n, 100)

    return full_cycles * cycle + sum(
        (i % 100 + 1) * ((i % 100 + 4) % 100 + 1)
        for i in range(remainder)
    )


def run_program(exe, *args):
    result = subprocess.run(
        [str(exe), *map(str, args)],
        capture_output=True,
        text=True,
        timeout=60,
        cwd=ROOT
    )

    if result.returncode != 0:
        raise RuntimeError(
            f"{exe.name} exited with {result.returncode}\n"
            f"{result.stdout}\n{result.stderr}"
        )

    match = re.search(
        r"^Dot product:\s*([+-]?\d+(?:\.\d+)?)\s*$",
        result.stdout,
        re.MULTILINE
    )

    if not match:
        raise RuntimeError(
            f"Dot product not found:\n{result.stdout}"
        )

    return float(match.group(1))


def check_invalid(exe, *args):
    result = subprocess.run(
        [str(exe), *map(str, args)],
        capture_output=True,
        text=True,
        timeout=60,
        cwd=ROOT
    )
    return result.returncode != 0


def main():
    for exe in [SEQ, PAR]:
        if not exe.is_file():
            print(f"Missing executable: {exe}")
            return 1

    passed = 0
    failed = 0

    print("=== DOT PRODUCT AUTOMATED TESTS ===")

    for n in SIZES:
        expected = expected_dot_product(n)

        cases = [("Sequential", SEQ, (n,))]

        for threads in THREADS:
            cases.append(
                (f"Parallel-{threads}", PAR, (n, threads))
            )

        for name, exe, args in cases:
            try:
                actual = run_program(exe, *args)

                if actual != expected:
                    raise AssertionError(
                        f"Expected {expected}, got {actual}"
                    )

                print(f"PASS | N={n} | {name}")
                passed += 1

            except Exception as exc:
                print(f"FAIL | N={n} | {name}: {exc}")
                failed += 1

    print("\n=== INVALID INPUT TESTS ===")

    invalid_cases = [
        (SEQ, ("0",)),
        (SEQ, ("-1",)),
        (PAR, ("0", "2")),
        (PAR, ("4", "0")),
        (PAR, ("4", "-1")),
        (PAR, ("4", "abc")),
    ]

    for exe, args in invalid_cases:
        try:
            if check_invalid(exe, *args):
                print(f"PASS | {exe.name} {args}")
                passed += 1
            else:
                print(f"FAIL | {exe.name} {args}")
                failed += 1
        except Exception as exc:
            print(f"FAIL | {exe.name} {args}: {exc}")
            failed += 1

    print("\n=== SUMMARY ===")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")

    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
