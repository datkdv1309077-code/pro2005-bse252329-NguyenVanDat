import random

m = int(input("Nhập số hàng: "))
n = int(input("Nhập số cột: "))

matrix = [[random.randint(1, 100) for j in range(n)] for i in range(m)]

print("Ma trận:")
for row in matrix:
    print(row)

r = int(input("Nhập hàng cần xem: "))
print("Hàng", r, ":", matrix[r-1])

c = int(input("Nhập cột cần xem: "))
print("Cột", c, ":")
for i in range(m):
    print(matrix[i][c-1])

max_value = max(max(row) for row in matrix)
print("Giá trị lớn nhất:", max_value)