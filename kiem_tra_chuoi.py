# kiemtrachuoi.py

chuoi_kiem_tra = input("Nhập một chuỗi bất kỳ: ")

chuoi_da_chuan_hoa = chuoi_kiem_tra.lower()

co_python = "python" in chuoi_da_chuan_hoa
co_programming = "programming" in chuoi_da_chuan_hoa

ket_qua = co_python and co_programming

print(f"Chuỗi của bạn: '{chuoi_kiem_tra}'")
print(f"Có chứa 'python' không? {co_python}")
print(f"Có chứa 'programming' không? {co_programming}")
print(f"Có chứa cả hai từ không? {ket_qua}")
