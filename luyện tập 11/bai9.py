def nhap_ma_tran(m, n, ten):
    matrix = []
    print(f"\nNhập ma trận {ten}:")
    for i in range(m):
        row = []
        for j in range(n):
            while True:
                x = input(f"Phần tử [{i}][{j}]: ")
                if x.strip() == "":
                    print("❌ Lỗi: Không được để trống!")
                    continue
                try:
                    row.append(float(x))
                    break
                except:
                    print("❌ Lỗi: Phải nhập số!")
        
        matrix.append(row)
    
    return matrix
m = int(input("Nhập số hàng: "))
n = int(input("Nhập số cột: "))
A = nhap_ma_tran(m, n, "A")
B = nhap_ma_tran(m, n, "B")
C = []
for i in range(m):
    row = []
    for j in range(n):
        row.append(A[i][j] + B[i][j])
    C.append(row)
print("\nMa trận A:", A)
print("Ma trận B:", B)
print("Ma trận tổng C:", C)