def bubble_sort_giam_dan_do_dai(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if len(arr[j]) < len(arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
def main():
    arr = []
    for i in range(5):
        s = input(f"Nhập chuỗi {i+1}: ")
        arr.append(s)
    bubble_sort_giam_dan_do_dai(arr)
    print("Danh sách sau khi sắp xếp (giảm dần độ dài):")
    for s in arr:
        print(s)
if __name__ == "__main__":
    main()