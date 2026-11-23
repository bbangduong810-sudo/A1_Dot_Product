
# Môi trường thực nghiệm A1

## 1. Phần cứng

- CPU: Intel Core Ultra 7 155H
- Số lõi vật lý: 16
- Số luồng logic: 22
- RAM khả dụng: 31.61 GB
- RAM trống khi kiểm tra: 18 GB
- GPU: Không sử dụng trong phép tính OpenMP


## 2. Phần mềm

- Hệ điều hành: Windows 11 Home Single Language
- Windows Version: 10.0.26300
- Windows Build: 26300
- Môi trường: MSYS2 UCRT64
- Compiler: GCC/G++ 16.2.0
- Chuẩn ngôn ngữ: C++17
- OpenMP: _OPENMP = 202111
- Python: 3.14.10
- Matplotlib: 3.11.2
- Git: 2.56.1


## 3. Cờ biên dịch

Tuần tự:
g++ -std=c++17 -O2 -Wall -Wextra -pedantic

Song song:
g++ -std=c++17 -O2 -fopenmp -Wall -Wextra -pedantic

## 4. Cấu hình thí nghiệm

Kích thước vector:
- N = 1000000
- N = 10000000
- N = 50000000

Số luồng OpenMP:
- 1, 2, 4, 8, 16, 22

Số lần chạy:
- 5 lần cho mỗi cấu hình
- Có một lần warm-up trước khi đo

## 5. Phương pháp đo

- Đồng hồ: std::chrono::steady_clock
- Compute time: thời gian tính tích vô hướng
- Total time: thời gian cấp phát, khởi tạo
  và tính tích vô hướng
- Thống kê: Median, Min, Max, IQR
- Đánh giá: Speedup và Efficiency
- Kiểm tra kết quả tính toán ở mỗi lần chạy

## 6. Dữ liệu

Hai vector double được sinh theo công thức cố định.
Dữ liệu được khởi tạo trong RAM.

A[i] = i % 100 + 1
B[i] = ((i % 100 + 4) % 100) + 1

## 7. Điều kiện chạy

- Chế độ nguồn: Chưa ghi
- Trạng thái cắm sạc: Chưa ghi
- Các tiến trình nền: Chưa kiểm soát đầy đủ
- CPU affinity: Chưa thiết lập
- Số luồng thực tế của từng lần chạy:
  Chưa được ghi nhận riêng

## 8. Hạn chế

- Mỗi cấu hình mới đo 5 lần.
- CPU sử dụng kiến trúc lõi lai.
- Chưa kiểm soát cố định lịch phân phối luồng.
- Kết quả có thể chịu ảnh hưởng của nhiệt độ,
  chế độ nguồn và tải hệ thống.
EOF
