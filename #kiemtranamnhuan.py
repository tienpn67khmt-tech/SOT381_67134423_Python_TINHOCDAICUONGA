#kiemtranamnhuan.py 
nam = int(input("Nhập năm bạn muốn kiểm tra: "))

if (nam % 400 == 0) or ((nam % 4 == 0) and (nam % 100 != 0)):
    print(f"Năm {nam} LÀ năm nhuận (Có 366 ngày). ✅")
else:
    print(f"Năm {nam} KHÔNG PHẢI năm nhuận (Có 365 ngày). ❌")
