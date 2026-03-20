def dem_ky_tu(chuoi, ky_tu):
    return chuoi.count(ky_tu)
def main():
    chuoi = input("Nhập chuỗi: ")
    ky_tu = input("Nhập ký tự cần đếm: ")
    if len(ky_tu) != 1:
        print("Vui lòng chỉ nhập 1 ký tự!")
        return
    so_lan = dem_ky_tu(chuoi, ky_tu)
    print(f"Ký tự '{ky_tu}' xuất hiện {so_lan} lần trong chuỗi.")
if __name__ == "__main__":
    main()