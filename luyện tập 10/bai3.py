def giai_thua(n):
    if n == 0 or n == 1:
        return 1
    return n * giai_thua(n - 1)
def main():
    n = int(input("Nhập số nguyên không âm n: "))
    if n < 0:
        print("Không tồn tại giai thừa cho số âm!")
    else:
        print(f"{n}! =", giai_thua(n))
if __name__ == "__main__":
    main()