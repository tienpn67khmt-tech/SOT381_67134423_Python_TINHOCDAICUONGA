#kiemtraso.py

x = int(input("Nhập một số nguyên: "))

if (x % 2 == 0) and (x > 10) and (x % 3 == 0):
    print("số thỏa mãn đồng thời cả 3 điều kiện:",x)
else:
    print("số không thỏa mãn đồng thời cả 3 điều kiện:",x)
