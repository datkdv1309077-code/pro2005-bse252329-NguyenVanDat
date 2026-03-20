def main():
    while True:
        print("\n===== MENU =====")
        print("6. Đảo chuỗi")
        print("7. Mật khẩu")
        print("8. Bubble sort")
        print("9. Class")
        print("10. Bubble sort")
        print("0. Thoát")
        chon = input("Chọn bài: ")
        if chon == "6":
            bai6()
        elif chon == "7":
            bai7()
        elif chon == "8":
            bai8()
        elif chon == "9":
            bai9()
        elif chon == "10":
            bai10()
        elif chon == "0":
            print("Thoát!")
            break
        else:
            print("Sai lựa chọn!")
if __name__ == "__main__":
    main()