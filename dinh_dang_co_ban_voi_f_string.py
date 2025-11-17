#dinhdangchuoi.py

name = input("Nhập tên của bạn: ")
age = int(float(input("Nhập tuổi của bạn: ")))
score = float(input("Nhập điểm của bạn: "))

# Định dạng cơ bản
print(f"Tên: {name}, Tuổi: {age}, Điểm: {score}")

# Định dạng số
print(f"Điểm làm tròn: {score:.2f}")      # 85.57
print(f"Điểm phần trăm: {score:.1f}")

# Căn chỉnh
print(f"Tên: {name:<20} | Tuổi: {age:>5}")  # Căn trái, căn phải
print(f"Số nhị phân: {age:08b}") 
