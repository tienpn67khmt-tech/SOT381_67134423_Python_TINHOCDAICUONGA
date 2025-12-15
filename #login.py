while True:
    chon=input("bạn có muốn tiếp tục (y/n):")
    if chon=='y' or chon=='Y':
        print("login successful")
    elif chon=='n' or chon=='N':
        print("login falled, vui lòng nhập lại")
        break
    else:
        print("login falled, vui lòng nhập lại")
