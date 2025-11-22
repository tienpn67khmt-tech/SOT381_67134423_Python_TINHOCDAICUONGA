diem = float(input("Nhập điểm thi của bạn: "))

if diem < 0 or diem > 10:
    print("Lỗi: Điểm số không hợp lệ! (Phải từ 0 đến 10)")
elif diem >= 5.0:
    print("Chúc mừng! Bạn đã ĐẬU.")
else:
    print("Rất tiếc, bạn đã RỚT.")
