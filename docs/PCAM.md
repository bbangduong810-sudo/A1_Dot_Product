# Thiet ke PCAM - A1

## 1. Bai toan

Tinh tich vo huong cua hai vector A va B
co cung N phan tu.

S = sum(A[i] * B[i]), voi i = 0,...,N-1.

## 2. Partitioning

- Chia N phan tu thanh cac nhom cong viec.
- Moi nhom tinh tich A[i] * B[i].
- Cac phep nhan doc lap va co the thuc hien song song.

## 3. Communication

- Cac luong doc hai mang A va B.
- Moi luong tinh tong cuc bo rieng.
- Su dung OpenMP reduction de gop cac tong.
- Khong can trao doi du lieu trong vong lap.

## 4. Agglomeration

- Gom nhieu phan tu vao moi tac vu.
- Giam chi phi tao va quan ly tac vu.
- Su dung mot vung parallel for cho phep tinh.

## 5. Mapping

- Su dung OpenMP tren CPU da loi.
- Phan phoi cac vong lap cho nhieu luong.
- Thu nghiem so luong luong khac nhau.
- Su dung schedule(static) lam phuong an ban dau.

## 6. Danh gia

- So sanh thoi gian tuan tu va song song.
- Tinh Speedup = T_seq / T_par.
- Tinh Efficiency = Speedup / P.
- Thu nghiem toi thieu 3 kich thuoc vector.
- Moi cau hinh chay it nhat 5 lan.
- Bao cao median va do phan tan.
- Kiem tra tinh dung dan cua ket qua.
