import csv
ten = input("Nhập tên nhân viên: ")
tuoi = input("Nhập tuổi: ")
id_nv = input("Nhập ID: ")
with open("nhanvien.txt", "w", encoding="utf-8") as f:
    f.write(f"Tên: {ten}\n")
    f.write(f"Tuổi: {tuoi}\n")
    f.write(f"ID: {id_nv}\n")
print("\n Đã lưu vào file nhanvien.txt")
with open("nhanvien.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Tên", "Tuổi", "ID"])  
    writer.writerow([ten, tuoi, id_nv])
print(" Đã lưu vào file nhanvien.csv")
print("\n📄 Nội dung file TXT:")
with open("nhanvien.txt", "r", encoding="utf-8") as f:
    print(f.read())
print("📄 Nội dung file CSV:")
with open("nhanvien.csv", "r", encoding="utf-8") as f:
    print(f.read())