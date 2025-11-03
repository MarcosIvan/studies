def binary_search(list, element, start, end):
    mid = int((start+end)/2)

    if mid >= len(list):
        return end
    
    if list[mid] == element:
        if mid + 1 >= len(list) or list[mid] != list[mid + 1]:
            return mid + 1
        return binary_search(list, element, mid + 1, end)
    
    else:
        if mid - 1 < 0 or list[mid] != list[mid - 1]:
            return mid
        return binary_search(list, element, start, mid - 1)

def histogram(list):
    start = 0
    dict = {}
    while start < len(list):
        quantity = binary_search(list, list[start], start, len(list)-1) - start
        dict[list[start]] = quantity
        start = start + quantity
    print(dict)


list = [1,1,1,1,1,1,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3,3]
histogram(list)