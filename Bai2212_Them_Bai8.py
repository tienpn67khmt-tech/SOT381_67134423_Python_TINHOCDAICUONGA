
def tinh_Fibonacci(n):
    day_so = []
    a = 0
    b = 1
    
    
    for i in range(n):
        day_so.append(a)
     
        a, b = b, a + b
        
   
    return day_so

n = int(input("Nhập số nguyên dương n: "))


ket_qua_list = tinh_Fibonacci(n)


tong_S = sum(ket_qua_list)


print(f"Dãy số Fibonacci: {ket_qua_list}")
print(f"Tổng của dãy số = {tong_S}")
