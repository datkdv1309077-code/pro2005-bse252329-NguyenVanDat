s = input("Nhập chuỗi số: ")

nums = [int(x.strip()) for x in s.split(";")]

for n in nums:
    print(n)

even = sum(1 for n in nums if n % 2 == 0)
negative = sum(1 for n in nums if n < 0)

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

prime = sum(1 for n in nums if is_prime(n))

avg = sum(nums) / len(nums)

print("Số chẵn:", even)
print("Số âm:", negative)
print("Số nguyên tố:", prime)
print("Trung bình:", avg)