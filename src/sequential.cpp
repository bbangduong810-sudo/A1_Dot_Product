#include <iostream>
#include <vector>
#include <chrono>
#include <iomanip>
#include <string>

int main(int argc, char* argv[]) {
    if (argc != 2) {
        std::cerr << "Usage: ./sequential.exe N\n";
        return 1;
    }

    // Read vector size
    size_t N;
    try {
        if (argv[1][0] == '-') {
            std::cerr << "N must be positive\n";
            return 1;
        }
        N = std::stoull(argv[1]);
        if (N == 0) {
            std::cerr << "N must be positive\n";
            return 1;
        }
    } catch (...) {
        std::cerr << "Invalid N\n";
        return 1;
    }

    using Clock = std::chrono::steady_clock;
    auto total_start = Clock::now();

    // Initialize vectors
    std::vector<double> A(N);
    std::vector<double> B(N);

    for (size_t i = 0; i < N; ++i) {
        A[i] = static_cast<double>(i % 100 + 1);
        B[i] = static_cast<double>((i % 100 + 4) % 100 + 1);
    }

    // Sequential dot product
    auto compute_start = Clock::now();

    double sum = 0.0;
    for (size_t i = 0; i < N; ++i) {
        sum += A[i] * B[i];
    }

    auto compute_end = Clock::now();
    auto total_end = Clock::now();

    double compute_ms =
        std::chrono::duration<double, std::milli>(
            compute_end - compute_start).count();

    double total_ms =
        std::chrono::duration<double, std::milli>(
            total_end - total_start).count();

    std::cout << "Mode: Sequential\n";
    std::cout << "N: " << N << "\n";
    std::cout << "Dot product: "
              << std::setprecision(17) << sum << "\n";

    std::cout << std::fixed << std::setprecision(6);
    std::cout << "Compute time (ms): "
              << compute_ms << "\n";
    std::cout << "Total time (ms): "
              << total_ms << "\n";

    return 0;
}
