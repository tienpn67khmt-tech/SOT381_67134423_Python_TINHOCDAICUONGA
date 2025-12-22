import math
print("Bai 1: Tinh chu vi va dien tich tam giac nhap a, b, c theo cong thuc Herong dung while true")

while True:
    a = float(input("Nhap vao canh a: "))
    b = float(input("Nhap vao canh b: "))
    c = float(input("nhap vao canh c: "))
    if a >0 and b>0 and c>0 and a + b > c and a + c > b and b + c > a:
        break
    else:
        print("Day khong phai la 3 canh cua tam giac, vui long nhap lai.")

p=(a+b+c)/2
s=math.sqrt(p*(p-a)*(p-b)*(p-c))
print(f"Dien tich tam giac la: {s:.2f}")
print(f"chu vi hinh tam giac la:{p:.2f}")
