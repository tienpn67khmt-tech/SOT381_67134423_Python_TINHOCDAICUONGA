#insotu1den100chiahetcho3va5.py
n = float(input("nhap so tu 1 den 100: "))
if n >= 1 and n <= 100:
    if n%3==0 and n%5==0:
        print("so",n,"chia het cho 3 va 5")
    else:
        print("so",n,"khong chia het cho 3 va 5")
else:
    print("so ban nhap khong hop le")
