#include <iostream>
#include <vector>
#include <chrono>
#include <iomanip>
#include <string>
#include <omp.h>

int main(int argc, char* argv[]) {
    if (argc != 3) {
        std::cerr << "Usage: ./parallel.exe N THREADS\n";
        return 1;
    }

    size_t N;
    int threads;

    try {
        std::string n_arg = argv[1];
        std::string t_arg = argv[2];

        size_t pos_n = 0, pos_t = 0;

        if (n_arg.empty() || t_arg.empty() ||
            n_arg[0] < '0' || n_arg[0] > '9' ||
            t_arg[0] < '0' || t_arg[0] > '9') {
            throw std::invalid_argument("Invalid input");
        }

        unsigned long long parsed_n =
            std::stoull(n_arg, &pos_n);
        threads = std::stoi(t_arg, &pos_t);

        if (pos_n != n_arg.size() ||
            pos_t != t_arg.size() ||
            parsed_n == 0 ||
            threads <= 0 ||
            threads > 256) {
            throw std::invalid_argument("Invalid input");
        }

        N = static_cast<size_t>(parsed_n);

        if (static_cast<unsigned long long>(N) != parsed_n) {
            throw std::out_of_range("N too large");
        }
    } catch (...) {
        std::cerr << "Invalid N or THREADS\n";
        return 1;
    }

    using Clock = std::chrono::steady_clock;

    auto total_start = Clock::now();

    // Initialize vectors exactly as in sequential.cpp
    std::vector<double> A(N);
    std::vector<double> B(N);

    for (size_t i = 0; i < N; ++i) {
        A[i] = static_cast<double>(i % 100 + 1);
        B[i] = static_cast<double>((i % 100 + 4) % 100 + 1);
    }

    // Disable dynamic thread adjustment
    omp_set_dynamic(0);

    // Parallel dot product
    auto compute_start = Clock::now();

    double sum = 0.0;

    #pragma omp parallel for reduction(+:sum) schedule(static) num_threads(threads)
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

    std::cout << "Mode: Parallel\n";
    std::cout << "N: " << N << "\n";
    std::cout << "Requested threads: " << threads << "\n";
    std::cout << "Dot product: "
              << std::setprecision(17) << sum << "\n";

    std::cout << std::fixed << std::setprecision(6);
    std::cout << "Compute time (ms): "
              << compute_ms << "\n";
    std::cout << "Total time (ms): "
              << total_ms << "\n";

    return 0;
}
