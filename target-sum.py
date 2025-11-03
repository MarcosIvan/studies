def target_sum(array, target):
    dict = {}

    for i in range(0,len(array)):
        dict[array[i]] = target - array[i]

    for i in range(0,len(array)):
        if dict[array[i]] in dict:
            return True
    return False


array1 = [13, 22, 5, 7, 10, 3, 17, 8, 2, 25, 30, 6, 1, 18, 4, 12, 27, 9, 15, 11]
target1 = 28
array2 = [1, 3, 5, 9, 14, 18, 21, 24, 27, 31, 35, 38, 40, 43, 47, 50, 53, 56, 59, 62]
target2 = 1000
print(target_sum(array1,target1))
print(target_sum(array2,target2))