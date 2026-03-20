def bai6():
    s = input("Nhập chuỗi: ")
    dao = ""

    for i in range(len(s) - 1, -1, -1):
        dao += s[i]

    print("Chuỗi đảo ngược:", dao)