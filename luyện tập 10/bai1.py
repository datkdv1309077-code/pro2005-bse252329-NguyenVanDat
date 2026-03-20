import os
def lay_ten_file(duong_dan):
    return os.path.basename(duong_dan)
def lay_ten_bai_hat(duong_dan):
    return os.path.splitext(os.path.basename(duong_dan))[0]
def main():
    while True:
        print("\n===== MENU =====")
        print("1. Trích xuất tên file")
        print("2. Trích xuất tên bài hát")
        print("3. Thoát")
        chon = input("Nhập lựa chọn: ")
        if chon == "1":
            path = input("Nhập đường dẫn: ")
            print("Tên file:", lay_ten_file(path))
        elif chon == "2":
            path = input("Nhập đường dẫn: ")
            print("Tên bài hát:", lay_ten_bai_hat(path))
        elif chon == "3":
            print("Thoát chương trình!")
            break
        else:
            print("Lựa chọn không hợp lệ, thử lại!")
if __name__ == "__main__":
    main()