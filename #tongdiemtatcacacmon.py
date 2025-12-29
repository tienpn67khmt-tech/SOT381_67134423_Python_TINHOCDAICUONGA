n =int(input("nhap diem mon toan: "))
m = int(input("nhap diem mon van: "))
p = int(input("nhap diem mon anh: "))
tong = n + m + p
if tong >= 15   and n >= 4 and m >= 4 and p >= 4:
    print("Dau")
    if n > 5 and m > 5 and p > 5:
        print("Hoc deu tat ca cac mon")
    else:
        print("Hoc khong deu tat ca cac mon")
else:
    print("Rot")
