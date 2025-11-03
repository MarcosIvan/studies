#Recebe uma lista de inteiros
#List[0] vai pra first_list[]
#List[1] vai pra second_list[]
#List[i] vai pra lista que tiver a maior quantidade de números maiores que ele
#Se as listas tiverem quantidades iguais de números maiores que ele, ele vai pra menor lista
#Se as listas tiverem o mesmo tamanho, ele vai pra first_list[]
#Retorna uma única lista, contendo os elementos da first_list[] seguidos dos elementos da second_list[]
def solution(list):
    first_list = []
    second_list = []
    i = 2
    first_list.append(list[0])
    second_list.append(list[1])
    while i < len(list):
        count_first = 0
        j = 0
        while j < len(first_list):
            if first_list[j] > list[i]:
                count_first+=1
            j+=1
        
        count_second= 0
        j = 0
        while j < len(second_list):
            if second_list[j] > list[i]:
                count_second+=1
            j+=1

        if count_first == count_second:
            if len(first_list) > len(second_list):
                second_list.append(list[i])
            else:
                first_list.append(list[i])
        elif count_first > count_second:
            first_list.append(list[i])
        else:
            second_list.append(list[i])
        i+=1
    
    lista = first_list + second_list
    return lista



list = [8, 25, 43, 65, 5, 23, 12]
response = solution(list)
print(response)