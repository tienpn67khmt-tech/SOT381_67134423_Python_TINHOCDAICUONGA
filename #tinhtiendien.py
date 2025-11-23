#tinhtiendien.py
kwh=float(input("Nhập số kWh tiêu thụ trong tháng: "))
gia_cap1=1000
gia_cap2=1734
gia_cap3=2014
if kwh<=50:
    tien=kwh*gia_cap1  
elif kwh<=100:
    tien=50*gia_cap1+(kwh-50)*gia_cap2
else:
    tien=50*gia_cap1+50*gia_cap2+(kwh-100)*gia_cap3

print(f"Số tiền điện phải trả trong tháng là: {tien} VND")
