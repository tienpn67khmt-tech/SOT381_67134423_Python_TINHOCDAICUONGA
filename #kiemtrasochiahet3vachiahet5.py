#kiemtrasochiahet3vachiahet5.py
n = int(input("Nhập một số n: "))

if n % 3 == 0 and n % 5 == 0:
    print(f"{n} chia hết cho cả 3 và 5. ✅")
else:
    print(f"{n} KHÔNG chia hết cho cả 3 và 5. ❌")
