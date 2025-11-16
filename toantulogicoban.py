#toantulogiccoban.py
age = int(input("Nhập tuổi của bạn: "))

input_license = input("Bạn có bằng lái xe không? (gõ 'true' hoặc 'false'): ")
has_license = (input_license.lower() == 'true')


input_employed = input("Bạn có đang đi làm không? (gõ 'true' hoặc 'false'): ")
is_employed = (input_employed.lower() == 'true')


print("---")
print("Bạn đã nhập:")
print("Tuổi:", age)
print("Có bằng lái:", has_license) 
print("Có việc làm:", is_employed) 
print("---")


can_drive = age >= 18 and has_license
print("Có thể lái xe:", can_drive) 

can_get_loan = age >= 18 and is_employed
print("Có thể vay vốn:", can_get_loan)

is_eligible = age >= 65 or is_employed
print("Đủ điều kiện ưu tiên:", is_eligible)

is_unemployed = not is_employed
print("Đang thất nghiệp:", is_unemployed)
