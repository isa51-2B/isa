def sort_and_search(arr, target):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    left, right = 0, n - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
arr = [64, 34, 25, 12, 22, 11, 90]
target = 22
index = sort_and_search(arr, target)
if index != -1:
    print(f"Элемент найден в индексе {index}")
else:
    print("Элемент не найден")
