#inramanhinhn!(0<n<10).py
n=int(input("nhập số n:"))
tong=0
i= 1
for i in range(1,n+1):
    tong+=i
    if 0<n<10:
        print("tổng các số từ 1 đến",n,"là:",tong)
    else:
        print("vui lòng nhập lại n trong khoảng từ 0 đến 10")
        break
