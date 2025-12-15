#tongcacsoS=1+1/2+1/3+...+1/n.vaS2=10+1/2+2/3+3/4+...+(n-1)/n.py
n=int(input("nhập số n:"))
S=0
S2=0
for i in range(1,n+1):
    S=S+1/i
    S2=S2+(i-1)/i
print("tổng S=",S)
print("tổng S2=",S2)

