n = int(input("Nhập một số: "))

if n < 0:
    print("Lỗi: số nhập vào phải không âm!")
else:
    print("Phần dư khi chia cho 2 là:", n % 2)