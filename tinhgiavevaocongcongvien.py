# tinhgiavevaocongvien.py
tuoi = int(input("Vui lòng nhập tuổi của khách: "))
gia_ve = 0

if tuoi < 6:
    gia_ve = 0
    print("Khách hàng được MIỄN PHÍ.")
elif tuoi <= 18:
    gia_ve = 50000
else:
    gia_ve = 100000
print("Số tiền cần thanh toán là:", gia_ve, "đồng")
