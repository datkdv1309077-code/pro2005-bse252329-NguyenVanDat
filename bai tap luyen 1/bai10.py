file = "products.txt"

# nhập sản phẩm
code = input("ma: ")
name = input("ten: ")
price = float(input("gia: "))

with open(file, "a", encoding="utf-8") as f:
    f.write(f"{code};{name};{price}\n")

# đọc danh sách
products = []
with open(file, "r", encoding="utf-8") as f:
    for line in f:
        code, name, price = line.strip().split(";")
        products.append((code, name, float(price)))

print("Danh sách sản phẩm:")
for p in products:
    print(p)

# sắp xếp giảm dần theo giá
products.sort(key=lambda x: x[2], reverse=True)

print("Sắp xếp theo giá giảm dần:")
for p in products:
    print(p)


