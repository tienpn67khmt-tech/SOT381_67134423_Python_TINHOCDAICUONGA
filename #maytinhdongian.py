#maytinhdongian.py
a = float(input("Nhập số thứ nhất (a): "))
b = float(input("Nhập số thứ hai (b): "))
phep_tinh = input("Nhập phép tính bạn muốn (+, -, *, /): ")

if phep_tinh == '+':
    ket_qua = a + b
    print(f"Kết quả: {a} + {b} = {ket_qua}")

elif phep_tinh == '-':
    ket_qua = a - b
    print(f"Kết quả: {a} - {b} = {ket_qua}")

elif phep_tinh == '*':
    ket_qua = a * b
    print(f"Kết quả: {a} * {b} = {ket_qua}")

elif phep_tinh == '/':
    if b == 0:
        print("Lỗi: Không thể chia cho số 0! ⛔")
    else:
        ket_qua = a / b
        print(f"Kết quả: {a} / {b} = {ket_qua}")

else:
    print("Lỗi: Phép tính không hợp lệ! Vui lòng chỉ nhập +, -, *, /")
