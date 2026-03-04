import random

def quicksort(arr, begin, end):
    if begin >= end - 1:
        return

    pivot_index = (begin + end) // 2
    pivot = arr[pivot_index]

    arr[pivot_index], arr[end - 1] = arr[end - 1], arr[pivot_index]

    i = begin
    for j in range(begin, end - 1):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[end - 1] = arr[end - 1], arr[i]

    quicksort(arr, begin, i)
    quicksort(arr, i + 1, end)


arr = [random.randint(0, 1000) for _ in range(20)]
print("Antes:", arr)
quicksort(arr, 0, len(arr))
print("Depois:", arr)