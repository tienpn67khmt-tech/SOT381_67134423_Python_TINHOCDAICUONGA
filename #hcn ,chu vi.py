print("Chương trình tính hình chữ nhật (0 <= w, h <= 100)")

while True:
    
    w = float(input("Nhập độ dài cạnh w: "))
    h = float(input("Nhập độ dài cạnh h: "))

    if 0.0 <= w <= 100.0 and 0.0 <= h <= 100.0:
        break 
    else:
       
        print("Dữ liệu sai! w và h phải từ 0 đến 100. Nhập lại nhé.")

chu_vi = (w + h) * 2
dien_tich = w * h

print(f"Chu vi: {chu_vi:.2f}")
print(f"Diện tích: {dien_tich:.2f}")
