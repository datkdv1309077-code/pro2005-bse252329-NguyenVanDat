d = {
    "name": "Dat",
    "age": 20,
    "city": "Ha Noi"
}
key = input("Nhập key cần kiểm tra: ")
if key in d:
    print(f" Key '{key}' tồn tại trong dictionary")
else:
    print(f" Key '{key}' không tồn tại")