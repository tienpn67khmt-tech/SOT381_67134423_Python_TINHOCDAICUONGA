def tim_max(a, b , c ):
    max= a
    if b > max:
        max = b
    if c > max:
        max =c
    return max
def tim_min(a, b , c ):
    min= a
    if b < min:
        min = b
    if c < min:
        min =c
    return min
print("Chương trình tìm Max - Min của 3 số a, b, c")
a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
c = float(input("Nhập số c: "))
ket_qua_max = tim_max(a, b, c)
ket_qua_min = tim_min(a, b, c)
print("=" * 30)
print(f"Giá trị lớn nhất (Max): {ket_qua_max}")
print(f"Giá trị nhỏ nhất (Min): {ket_qua_min}")
 




m= float(input("nhap so m: "))
n= float(input("nhap so n: "))
k= float(input("nhap so k: "))
numMax=tim_max(m,n,k)
numMin=tim_min(m,n,k)
print(f"so lon nhat la:{numMax}")
print(f"so nho nhat la:{numMin}")
