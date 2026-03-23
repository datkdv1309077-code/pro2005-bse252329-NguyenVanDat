arr = ["1 3 4 5", "8 9 9 7", "0 9 8 7", "1 2 3 4", "8 9 0 9"]
arr.sort()
print("Danh sách sau khi sắp xếp:")
for i in range(len(arr)):
    print(f"{i}: {arr[i]}")
x = input("\n1 2 3 4: ")
left = 0
right = len(arr) - 1

while left <= right:
    mid = (left + right) // 2
    print(f"Đang xét vị trí {mid}: {arr[mid]}")

    if arr[mid] == x:
        print(f"\n Tìm thấy '{x}' tại vị trí: {mid}")
        break
    elif arr[mid] < x:
        left = mid + 1
    else:
        right = mid - 1
else:
    print(f"\n Không tìm thấy '{x}'")