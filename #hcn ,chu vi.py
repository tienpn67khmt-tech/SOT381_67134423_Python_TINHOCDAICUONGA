w = float(input("Nhập chiều rộng w: "))
h = float(input("Nhập chiều cao h: "))

if 0 <= w <= 100 and 0 <= h <= 100:
    chu_vi = (w + h) * 2
    dien_tich = w * h
    
    print(f"Chu vi: {chu_vi:.2f}")
    print(f"Diện tích: {dien_tich:.2f}")
else:
    print("Vui lòng nhập w và h trong khoảng từ 0.0 đến 100.0")
            
