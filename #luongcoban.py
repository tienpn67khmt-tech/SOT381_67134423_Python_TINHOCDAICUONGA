#tinhluongcobancothue.py
luong=float(input("Nhập lương cơ bản: "))
thue_suat=0
if luong >= 15000000:
    thue_suat=0.3
elif luong >= 7000000:
    thue_suat=0.2
else:
    thue_suat=0.1
thue=luong*thue_suat
print(f"lương nhạn được là={luong-thue}")     
