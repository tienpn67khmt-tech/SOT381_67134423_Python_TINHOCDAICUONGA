tra_loi = ""

while tra_loi != "yes":

    tra_loi = input("Bạn có muốn thoát không? (nhập 'yes' hoặc 'no'): ").lower()

    if tra_loi == "no":
        print("Cảm ơn bạn đã sử dụng chương trình.")
        
    elif tra_loi == "yes":
        print("Thoát thành công!")
        
    else:
        print("Mình không hiểu, vui lòng nhập đúng 'yes' hoặc 'no'.")
