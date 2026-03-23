nums = list(map(int, input("Nhập danh sách số: ").split()))
even_numbers = []
tong = 0
for num in nums:
    if num % 2 == 0:
        even_numbers.append(num)
        tong += num
print("Các số chẵn là:", even_numbers)
print("Tổng các số chẵn là:", tong)