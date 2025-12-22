n = int(input("nhap so bai hat: "))
daybaihat = [] 

for i in range(n):
    tenbaihat = input("nhap ten bai hat: ")
    daybaihat.append(tenbaihat)

print(f"day bai hat da nhap la: {daybaihat}") 


print(" DANH SÁCH IN HOA ")
for i in range(n):
    ten = daybaihat[i]
    print(ten.upper())


print("CÁC BÀI CÓ TỪ 'YÊU' ")
for i in range(n):
    ten = daybaihat[i]
    

    if ten.lower().find("yêu") != -1:
        print(f"Bài {i}: {ten}")


print(" BÀI HÁT DÀI NHẤT ")
bai_dai_nhat = ""
so_tu_max = 0

for i in range(n):
    ten = daybaihat[i]
    so_tu = len(ten.split())
    
    if so_tu > so_tu_max:
        so_tu_max = so_tu
        bai_dai_nhat = ten

print(f"Ket qua: '{bai_dai_nhat}' voi {so_tu_max} tu")
