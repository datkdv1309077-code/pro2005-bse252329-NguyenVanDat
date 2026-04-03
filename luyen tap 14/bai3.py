import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
n = int(input("Nhập số phần tử: "))
arr = []
for i in range(n):
    x = int(input(f"arr[{i}] = "))
    arr.append(x)
odd_numbers = [x for x in arr if x % 2 != 0]
print("Các số lẻ:", *odd_numbers)
print("Tổng số lượng số lẻ:", len(odd_numbers))
prime_numbers = [x for x in arr if is_prime(x)]
print("Các số nguyên tố:", *prime_numbers)