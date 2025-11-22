#kiemtraoduongsoam.py
n = int(input("Nhập vào một số nguyên n: "))

if n > 0:
    print(f"{n} là số dương (+)")
elif n < 0:
    print(f"{n} là số âm (-)")
else:
    print("Đây là số 0")
