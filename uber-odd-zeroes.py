#Recebe uma lista de inteiros
#Verificar quantos dígitos 0 existe em cada número
#Se qtde par, faz nada
#Se qtde ímpar, conta +1
#Retorna a qtde
def solution(list):
    i = 0
    count = 0
    while i < len(list):
        number = list[i]
        qtt_zero = 0
        while number > 0:
            if number%10 == 0:
                qtt_zero+=1
            number = int(number/10)
        i+=1
        if qtt_zero%2 != 0:
            count += 1
    return count


list = [8, 11, 13, 1000, 2000, 10, 20300]
response = solution(list)
print(response)