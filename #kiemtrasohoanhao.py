#kiemtrasohoanhao.py
n = int(input("Nhập số cần kiểm tra (ví dụ: 6): "))
tong_uoc = 0
i = 1

while i < n: 
    if n % i == 0:  
        tong_uoc = tong_uoc + i  
    i += 1
    
if tong_uoc == n:
    print(f"{n} là SỐ HOÀN HẢO.")
else:
    print(f"{n} KHÔNG phải số hoàn hảo.")
