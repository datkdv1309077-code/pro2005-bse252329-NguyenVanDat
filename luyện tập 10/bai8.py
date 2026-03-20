def bai8():
    arr = []
    for i in range(5):
        s = input(f"Nhập chuỗi {i+1}: ")
        arr.append(s)

    n = len(arr)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if len(arr[j]) < len(arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

                print(f"Bước {i},{j}: {arr}")

    print("Kết quả:", arr)