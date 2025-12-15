#tinhtongdayso.py
n = int(input("Nhập số n (ví dụ: 5): "))
tong = 0 
i = 1    
while i <= n:
    tong = tong + i  
    i = i + 1       
print(f"Tổng từ 1 đến {n} là: {tong}")
