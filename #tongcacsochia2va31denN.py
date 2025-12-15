
tong = 0
for i in range(1, n + 1):
    tong = tong + i

print("Tổng các số từ 1 đến", n, "là:", tong)


if tong % 2 == 0 and tong % 3 == 0:
    print("Kết quả: Tổng này chia hết cho cả 2 và 3.")
else:
    print("Kết quả: Tổng này KHÔNG chia hết cho cả 2 và 3.")
