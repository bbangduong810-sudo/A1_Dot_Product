
#!/usr/bin/env bash

set -euo pipefail

# Project root
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

# GCC from MSYS2 UCRT64
CXX="/ucrt64/bin/g++"

if [ ! -x "$CXX" ]; then
    echo "ERROR: GCC UCRT64 not found."
    exit 1
fi

COMMON_FLAGS=(
    -std=c++17
    -O2
    -Wall
    -Wextra
    -pedantic
)

echo "================================"
echo "A1 DOT PRODUCT - BUILD"
echo "================================"

echo ""
echo "[1/2] Building sequential version..."

"$CXX" "${COMMON_FLAGS[@]}" \
    src/sequential.cpp \
    -o sequential.exe

echo "Sequential build successful."

echo ""
echo "[2/2] Building parallel version..."

"$CXX" "${COMMON_FLAGS[@]}" \
    -fopenmp \
    src/parallel.cpp \
    -o parallel.exe

echo "Parallel build successful."

echo ""
echo "Compiler:"
"$CXX" --version | head -n 1

echo ""
echo "BUILD COMPLETED SUCCESSFULLY"
