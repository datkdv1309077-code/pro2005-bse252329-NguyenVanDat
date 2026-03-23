ds = {}
n = int(input("Nhập số lượng người: "))
for i in range(n):
    ten = input(f"Nhập tên người thứ {i+1}: ")
    tuoi = int(input(f"Nhập tuổi của {ten}: "))
    ds[ten] = tuoi
print("\nDanh sách:", ds)
tong = sum(ds.values())
tuoi_tb = tong / n if n > 0 else 0

print("Tuổi trung bình là:", tuoi_tb)