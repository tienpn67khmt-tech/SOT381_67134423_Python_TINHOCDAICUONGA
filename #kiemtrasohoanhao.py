#kiemtrasohoanhao.py
n = int(input("Nhập số cần kiểm tra (ví dụ: 6): "))
tong_uoc = 0
i = 1

while i < n:  # Chỉ duyệt đến n-1 (không tính chính nó)
    if n % i == 0:  # Nếu i là ước số của n (chia hết)
        tong_uoc = tong_uoc + i  # Cộng ước số vào tổng
    i += 1
    
if tong_uoc == n:
    print(f"{n} là SỐ HOÀN HẢO.")
else:
    print(f"{n} KHÔNG phải số hoàn hảo.")
