#kiemtrangaythanghople.py
ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))  
nam = int(input("Nhập năm: "))
if thang < 1 or thang > 12:
    print("Tháng không hợp lệ")
elif ngay < 1:
    print("Ngày không hợp lệ")  
elif thang in [1, 3, 5, 7, 8, 10, 12] and ngay > 31:
    print("Ngày không hợp lệ")  
elif thang in [4, 6, 9, 11] and ngay > 30:
    print("Ngày không hợp lệ")      
elif thang == 2:
    if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
        if ngay > 29:
            print("Ngày không hợp lệ")  
        else:
            print("Ngày hợp lệ")  
    else:
        if ngay > 28:
            print("Ngày không hợp lệ")  
        else:
            print("Ngày hợp lệ")    
else:
   print("ngày tháng năm hơp lệ")
