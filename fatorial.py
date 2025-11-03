def fatorial(a, b):
    print("abrindo passada ", b)
    if a == 0:
        return 1
    c = fatorial(a-1, b+1)
    print("fechando passada ", b)
    return a * c


a = fatorial(4, 1)
print(a)