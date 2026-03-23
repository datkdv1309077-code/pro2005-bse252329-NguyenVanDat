def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
ds = []
print("Danh sách ban đầu:", ds)
n = int(input("Nhập số lượng phần tử: "))
for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i+1}: "))
    ds.append(x)

print("Danh sách sau khi thêm:", ds)
k = int(input("\nNhập giá trị k: "))
count = ds.count(k)
print(f"Số lần xuất hiện của {k} là: {count}")
tong_snt = 0
for num in ds:
    if la_so_nguyen_to(num):
        tong_snt += num
print("Tổng các số nguyên tố là:", tong_snt)
ds.sort()
print("Danh sách sau khi sắp xếp:", ds)
ds.clear()
print("Danh sách sau khi xóa:", ds)