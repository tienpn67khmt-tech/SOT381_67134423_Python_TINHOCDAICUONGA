n = int(input("Nhập số cần đảo ngược: "))
so_ban_dau = n 
so_dao_nguoc = 0

while n > 0:
    chu_so_cuoi = n % 10            
    so_dao_nguoc = so_dao_nguoc * 10 + chu_so_cuoi 
    n = n // 10                    

print(f"Số đảo ngược của {so_ban_dau} là: {so_dao_nguoc}")
