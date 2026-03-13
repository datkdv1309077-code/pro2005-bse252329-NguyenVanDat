sinh_vien = {
    "An": 8,
    "Binh": 7,
    "Chi": 9
}

key = input("Nhập tên sinh viên cần tìm: ")

if key in sinh_vien:
    print("Key tồn tại trong dictionary")
else:
    print("Key không tồn tại")