def do_dai_chuoi(chuoi):
    return len(chuoi)
def main():
    chuoi = input("Nhập chuỗi: ")
    if chuoi == "":
        print("Lỗi: Bạn đã nhập chuỗi rỗng!")
    else:
        print("Độ dài của chuỗi là:", do_dai_chuoi(chuoi))
if __name__ == "__main__":
    main()