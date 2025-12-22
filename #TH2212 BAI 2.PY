print("chuong trinh tim so lon nhat nho nhat trong 3 so")

a=int(input("nhap so a:"))
b=int(input("nhap so b:"))
c=int(input("nhap so c:"))
   
max= a
if b> max:
    max=b
if c> max:
    max=c


min= a
if b< min:
    min=b
if c< min:
    min=c

print("="*50)
print("so nho nhat la:",min)
print("so lon nhat la:", max)
