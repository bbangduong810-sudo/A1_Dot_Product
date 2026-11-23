
# A1 - Tính tích vô hướng của hai vectơ

## 1. Giới thiệu

Bài tập lớn môn Tính toán song song.

Bài A1: Tính tích vô hướng của hai vectơ bằng C++,
triển khai phiên bản tuần tự và phiên bản song song OpenMP.

### Mục tiêu

- Thiết kế thuật toán theo PCAM.
- Cài đặt thuật toán tuần tự.
- Song song hóa thuật toán bằng OpenMP.
- Kiểm thử tính đúng đắn.
- Đo hiệu năng trên nhiều kích thước dữ liệu.
- Tính Speedup và Efficiency.
- Phân tích kết quả thực nghiệm.

## 2. Bài toán

Cho hai vectơ A và B gồm N phần tử.

Tính:

S = sum(A[i] * B[i]), i = 0,...,N-1

Ví dụ:

A = [1, 2, 3, 4]
B = [5, 6, 7, 8]

Kết quả:

S = 70

## 3. Thiết kế PCAM

### Partitioning

Chia các phần tử vectơ thành những nhóm công việc độc lập.

### Communication

Mỗi luồng tính tổng cục bộ. Sử dụng OpenMP reduction
để kết hợp kết quả, tránh race condition trên biến tổng.

### Agglomeration

Gom nhiều lượt lặp vào tác vụ được phân phối cho luồng.

### Mapping

Sử dụng OpenMP parallel for và schedule(static)
để phân phối công việc cho các luồng CPU.

Thiết kế chi tiết: docs/PCAM.md

## 4. Công nghệ

- C++17
- GCC/G++ 16.2.0
- OpenMP
- Python 3.14.10
- Matplotlib 3.11.2
- MSYS2 UCRT64
- Git

Hệ điều hành thực nghiệm:
Windows 11 Home Single Language, build 26300.

Thông tin chi tiết: docs/ENVIRONMENT.md

## 5. Cấu trúc project

A1_Dot_Product/
    src/
        sequential.cpp
        parallel.cpp
    tests/
        test_dot_product.py
    scripts/
        build.sh
        benchmark.py
        plot.py
    data/
    results/
        raw_20261123_161151.csv
        summary_20261123_161151.csv
        plots/
    docs/
        PCAM.md
        ENVIRONMENT.md
    README.md
    AI_USAGE.md
    CONTRIBUTIONS.md
    .gitignore

## 6. Yêu cầu môi trường

Hướng dẫn dưới đây dành cho Windows sử dụng MSYS2 UCRT64.

Cần cài đặt:

- GCC UCRT64
- GNU OpenMP runtime (libgomp)
- Python UCRT64
- Matplotlib
- Git

Các gói có thể cài trong MSYS2 UCRT64 bằng pacman.

## 7. Biên dịch

Mở terminal MSYS2 UCRT64 tại thư mục project.

Chạy:

    bash scripts/build.sh

Script sẽ tạo hai chương trình:

- sequential.exe
- parallel.exe

Cờ biên dịch chính:

    -std=c++17 -O2

Phiên bản song song sử dụng thêm:

    -fopenmp

## 8. Chạy chương trình

### Phiên bản tuần tự

Cú pháp:

    ./sequential.exe N

Ví dụ:

    ./sequential.exe 1000000

### Phiên bản song song

Cú pháp:

    ./parallel.exe N THREADS

Ví dụ:

    ./parallel.exe 1000000 4

Trong đó:

- N: Số phần tử của mỗi vectơ.
- THREADS: Số luồng OpenMP yêu cầu.

Chương trình xuất:

- Tích vô hướng
- Thời gian tính toán (ms)
- Tổng thời gian (ms)

## 9. Kiểm thử

Chạy:

    python tests/test_dot_product.py

Bộ kiểm thử hiện tại gồm 41 trường hợp.

Kết quả kiểm thử đã ghi nhận:

    Passed: 41
    Failed: 0

Đây là kết quả của bộ kiểm thử hiện có,
không phải chứng minh chương trình không có lỗi.

## 10. Benchmark

Script:

    scripts/benchmark.py

Để chạy:

    python scripts/benchmark.py

Cấu hình thực nghiệm:

- N = 1.000.000
- N = 10.000.000
- N = 50.000.000
- Số luồng = 1, 2, 4, 8, 16, 22
- 5 lần đo mỗi cấu hình
- 1 lượt warm-up trước mỗi cấu hình

Tổng số lượt đo chính thức: 105.

Script tạo dữ liệu CSV trong thư mục results.

## 11. Phương pháp đánh giá

Các chỉ số:

- Compute time
- Total time
- Median
- Min
- Max
- IQR
- Speedup
- Efficiency

Công thức:

Speedup(p) = T_sequential / T_parallel(p)

Efficiency(p) = Speedup(p) / p

Trong đó p là số luồng được yêu cầu.

Speedup được tính từ các median của cùng kích thước dữ liệu.

## 12. Tạo biểu đồ

Chạy:

    python scripts/plot.py

Script tạo:

- speedup.png
- efficiency.png
- compute_time_N1000000.png
- compute_time_N10000000.png
- compute_time_N50000000.png

Các biểu đồ được lưu trong results/plots/.

Lưu ý: Phiên bản plot.py hiện tại sử dụng
đường dẫn CSV benchmark đã được cấu hình sẵn.
Khi tái lập với dữ liệu mới, cần cập nhật biến
INPUT trong script tương ứng.

## 13. Kết quả thực nghiệm

### Median Compute Time

Đơn vị: ms

| Cấu hình | N=1 triệu | N=10 triệu | N=50 triệu |
|---|---:|---:|---:|
| Sequential | 0.5418 | 6.8747 | 38.3425 |
| OpenMP 1 | 0.5940 | 7.0165 | 39.4672 |
| OpenMP 2 | 1.2199 | 6.0367 | 25.8409 |
| OpenMP 4 | 1.0257 | 6.2607 | 25.5138 |
| OpenMP 8 | 1.2710 | 5.9721 | 25.4013 |
| OpenMP 16 | 1.5010 | 6.0755 | 25.7808 |
| OpenMP 22 | 1.4856 | 6.4352 | 23.6431 |

Nhận xét:

- Với N=1 triệu, phiên bản tuần tự nhanh nhất.
- Với N=10 triệu, OpenMP 8 luồng có median compute
  time thấp nhất trong các cấu hình đã đo.
- Với N=50 triệu, OpenMP 22 luồng có median compute
  time thấp nhất, speedup khoảng 1.62 lần.
- Thời gian tổng chịu ảnh hưởng lớn của việc
  cấp phát và khởi tạo dữ liệu.

Kết quả chi tiết và độ phân tán nằm trong CSV.

## 14. Hạn chế

- Chưa kiểm soát hoàn toàn lịch phân phối luồng CPU.
- CPU sử dụng kiến trúc lõi lai.
- Mỗi cấu hình mới được đo 5 lần.
- Kết quả có thể bị ảnh hưởng bởi hệ điều hành,
  chế độ nguồn, nhiệt độ và tiến trình nền.
- Chưa kiểm thử đầy đủ các vấn đề đồng thời
  như race condition ngoài những trường hợp đã chạy.

## 15. Tài liệu bổ sung

- docs/PCAM.md: Thiết kế thuật toán.
- docs/ENVIRONMENT.md: Môi trường thực nghiệm.
- AI_USAGE.md: Nhật ký sử dụng AI.
- CONTRIBUTIONS.md: Đóng góp thành viên.

## 16. Cam kết

Mã nguồn cần được kiểm tra trước khi nộp.
Các số liệu benchmark được lấy từ chương trình thực tế.

Không sử dụng AI để tạo số liệu thực nghiệm giả.
Việc sử dụng AI được công khai trong AI_USAGE.md.
EOF
