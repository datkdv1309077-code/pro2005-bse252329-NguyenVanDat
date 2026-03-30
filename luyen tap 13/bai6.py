def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
       
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

a = [5, 2, 9, 1, 3]
print("Mảng sau khi sắp xếp:", selection_sort(a))