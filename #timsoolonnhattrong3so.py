#timsoolonnhattrong3so.py
a = int(input("Nhập số thứ nhất (a): "))
b = int(input("Nhập số thứ hai (b): "))
c = int(input("Nhập số thứ ba (c): "))

if a >= b and a >= c:
    print(f"Số lớn nhất là a: {a}")
elif b >= a and b >= c:
    print(f"Số lớn nhất là b: {b}")
else:
    print(f"Số lớn nhất là c: {c}")
