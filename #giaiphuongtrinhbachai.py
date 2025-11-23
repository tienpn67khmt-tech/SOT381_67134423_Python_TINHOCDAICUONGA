#giaiphuongtrinhbachai.py
a=float(input("nhập hệ số a:"))
b=float(input("nhập hệ số b:"))
c=float(input("nhập hệ số c:")) 
if a==0:            
    if b==0:
        if c==0:
            print("phương trình có vô số nghiệm.")
        else:
            print("phương trình vô nghiệm.")
    else:
        x=-c/b
        print(f"phương trình có một nghiệm x={x}")  
else:
    delta=b**2-4*a*c
    if delta<0:
        print("phương trình vô nghiệm.")
    elif delta==0:
        x=-b/(2*a)
        print(f"phương trình có nghiệm kép x1=x2={x}")
    else:
        x1=(-b+delta**0.5)/(2*a)
        x2=(-b-delta**0.5)/(2*a)
        print(f"phương trình có hai nghiệm phân biệt x1={x1} và x2={x2}")
