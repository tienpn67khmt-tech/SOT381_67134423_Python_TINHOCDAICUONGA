#phanloaitamgiac.py
a=float(input("nhập đọ dài cạnh a:"))
b=float(input("nhập độ dài cạnh b:"))
c=float(input("nhập độ dài cạnh c:"))
if a+b>c and a+c>b and b+c>a:
    if a==b==c:
        print("tam giác đều")
    elif a==b or b==c or a==c:
        print("tam giác cân")
    elif a*a+b*b==c*c or a*a+c*c==b*b or b*b+c*c==a*a:
        print("tam giác vuông")3
        
    else:
        print("tam giác thường")
else:
    print("không phải tam giác")
