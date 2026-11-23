# AI_USAGE - A1 Dot Product

## Lich su

### 1
- Thoi gian: 2026-11-23
- Nguoi su dung: Bac
- Cong cu/mo hinh: ChatGPT (GPT-6)
- Muc dich: Thiet lap moi truong GCC, OpenMP va Git.
- Prompt hoac tom tat prompt: Huong dan cai dat va sua loi
  bien dich OpenMP tren Windows 11, MSYS2 UCRT64.
- Ket qua: Huong dan cai GCC, libgomp, Git va kiem tra OpenMP.
- Phan da su dung: Cac lenh cai dat va kiem tra moi truong.
- Chinh sua cua nhom: 
- Kiem chung: omp_test.exe chay va tra ve Dot product = 70.
- Commit/issue lien quan: Khong co commit rieng.

### 2
- Thoi gian: 2026-11-23
- Nguoi su dung: Bac
- Cong cu/mo hinh: ChatGPT (GPT-6)
- Muc dich: Thiet ke thuat toan PCAM cho A1.
- Prompt hoac tom tat prompt: Huong dan thiet ke PCAM cho
  bai toan tinh tich vo huong cua hai vector.
- Ket qua: Ban thiet ke PCAM ban dau.
- Phan da su dung: docs/PCAM.md.
- Chinh sua cua nhom:
- Kiem chung: Can tiep tuc doi chieu PCAM voi ma OpenMP.
- Commit/issue lien quan: c10aa47.

### 3
- Thoi gian: 2026-11-23
- Nguoi su dung: Bac
- Cong cu/mo hinh: ChatGPT (GPT-6)
- Muc dich: Goi y chuong trinh C++ tuan tu.
- Prompt hoac tom tat prompt: Viet chuong trinh tinh tich
  vo huong, sinh du lieu va do thoi gian bang C++17.
- Ket qua: Ma nguon src/sequential.cpp.
- Phan da su dung: Chuong trinh tuan tu.
- Chinh sua cua nhom: 
- Kiem chung: Bien dich thanh cong; N=4 cho 70;
  N=1000000 cho 3191500000.
- Commit/issue lien quan: Commit phien ban tuan tu.

## Tuyen bo

Nguoi nop chiu trach nhiem ve tinh dung dan, ban quyen,
so lieu thuc nghiem va moi noi dung da nop.
Khong su dung AI de tao so lieu thuc nghiem gia.

### 4
- Thoi gian: 2026-11-23
- Nguoi su dung: Bac
- Cong cu/mo hinh: ChatGPT (GPT-6)
- Muc dich: Ho tro lap trinh song song bang OpenMP.
- Prompt hoac tom tat prompt: Huong dan xay dung
  phien ban song song tinh tich vo huong hai vector,
  su dung parallel for, reduction va schedule(static).
- Ket qua: Ma nguon src/parallel.cpp.
- Phan da su dung: Chuong trinh OpenMP va lenh bien dich.
- Chinh sua cua nhom: 
- Kiem chung:
  + N=4, threads=2: dot product=70.
  + N=1000000, threads=4: dot product=3191500000.
  + N=1000000, threads=1: dot product=3191500000.
  + Ca ba truong hop deu cho ket qua dung.
  + Chua hoan thanh benchmark va kiem thu day du.
- Commit/issue lien quan: Commit phien ban song song.
### 5
- Thoi gian: 2026-11-23
- Nguoi su dung: Bac
- Cong cu/mo hinh: ChatGPT (GPT-6)
- Muc dich: Ho tro xay dung bo kiem thu tu dong.
- Prompt chinh: Huong dan kiem thu tinh dung dan
  cua chuong trinh tich vo huong tuan tu va OpenMP.
- Ket qua: tests/test_dot_product.py
- Phan da su dung: Ma Python kiem thu.
- Chinh sua: Sua loi dan lenh Bash vao tep Python.
- Kiem chung: 41 PASS, 0 FAIL.
- Gioi han: Chua kiem thu day du race condition
  va cac truong hop loi cap phat bo nho.
- Commit lien quan: Commit bo kiem thu.
### 6. Ho tro benchmark va ve bieu do
- Thoi gian: 2026-11-23
- Nguoi su dung: Bac
- Cong cu/mo hinh: ChatGPT (GPT-6)
- Muc dich: Thiet ke benchmark va phan tich hieu nang.
- Prompt chinh: Huong dan benchmark A1 voi 3 kich
  thuoc du lieu, nhieu cau hinh luong, 5 lan chay.
- Ket qua: scripts/benchmark.py va scripts/plot.py.
- Phan da su dung: Ma Python benchmark, thong ke
  median, IQR, speedup, efficiency va ve bieu do.
- Chinh sua cua nhom: Bo sung cac dieu chinh thuc te.
- Kiem chung:
  + Benchmark hoan tat 105 lan do chinh thuc.
  + Ket qua duoc luu vao CSV.
  + Tao thanh cong 5 bieu do PNG.
  + Moi lan chay duoc doi chieu ket qua tich vo huong.
- Gioi han: Moi cau hinh moi chay 5 lan;
  chua co phan tich y nghia thong ke.
- Commit lien quan: Commit benchmark.

### 7. Ho tro script build va tai lieu moi truong

- Thoi gian: 2026-11-23
- Nguoi su dung: Bac
- Cong cu/mo hinh: ChatGPT (GPT-6)
- Muc dich: Tu dong hoa bien dich va ghi lai
  moi truong thuc nghiem.
- Prompt chinh: Huong dan tao build.sh va
  ENVIRONMENT.md cho project A1.
- Ket qua:
  + scripts/build.sh
  + docs/ENVIRONMENT.md
- Phan da su dung: Script Bash va mau tai lieu.
- Chinh sua cua nhom: 
- Kiem chung:
  + BUILD COMPLETED SUCCESSFULLY.
  + Bo kiem thu: 41 PASS, 0 FAIL.
  + Doi chieu phien ban phan mem voi may thuc te.
- Commit lien quan: Commit script build va moi truong.
