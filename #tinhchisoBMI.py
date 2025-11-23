#tinhchisoBMI.py
x=float(input("Nhập cân nặng (kg);"))
y=float(input("Nhập chiều cao (m):"))
BMI=x/(y**2)
if BMI<18.5:
    print(f"Chỉ số BMI của bạn là {BMI:.2f}, bạn bị thiếu cân.")
elif 18.5<=BMI<24.9:
    print(f"Chỉ số BMI của bạn là {BMI:.2f}, bạn có cân nặng bình thường.")
elif 25<=BMI<29.9:
    print(f"Chỉ số BMI của bạn là {BMI:.2f}, bạn bị thừa cân.")
else:
    print(f"Chỉ số BMI của bạn là {BMI:.2f}, bạn bị béo phì.")
