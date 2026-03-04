import random

def merge(left, right):
    resultado = []
    i,j = 0,0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            resultado.append(left[i])
            i+=1
        else:
            resultado.append(right[j])
            j+=1

    while i < len(left):
        resultado.append(left[i])
        i += 1

    while j < len(right):
        resultado.append(right[j])
        j += 1
    
    return resultado

def mergesort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])

    return merge(left, right)


arr = [random.randint(0, 1000) for _ in range(20)]
print("Antes:", arr)
arr_ordenado = mergesort(arr)
print("Depois:", arr_ordenado)