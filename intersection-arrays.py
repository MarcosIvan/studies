def intersection(array1, array2):
    dict = {}
    size = max(len(array1),len(array2))

    for i in range(0,size):
        if i < len(array1):
            if array1[i] in dict:
                dict[array1[i]] += 1
            else:
                dict[array1[i]] = 1
        
        if i < len(array2):
            if array2[i] in dict:
                dict[array2[i]] += 1
            else:
                dict[array2[i]] = 1
    
    result = [num for num, count in dict.items() if count > 1]
    return result


array1 = [3, 7, 12, 18, 25, 30, 42, 55, 67, 81]
array2 = [5, 12, 18, 29, 35, 42, 60, 74, 85, 90]
a = intersection(array1, array2)
print (a)