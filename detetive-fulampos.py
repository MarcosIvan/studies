#Código de Marcos Ivan
#Recebe um array de inteiros
#Verifica se de alguma forma consegue somar 150 utilizando duas notas do array

def verifica_lista(lista):
    response = "Não pode ter roubado"
    if len(lista) == 0:
        response = "Lista inválida"
    elif len(lista) == 1 and lista[0] == 150:
        response = "Pode ter roubado"
    elif len(lista) == 2 and lista[0]+lista[1] == 150:
        response = "Pode ter roubado"
    else:
        i = int(len(lista)/2)
        j = i+1
        while i>0 or j<len(lista):
            if lista[i]+lista[j] == 150:
                response = "Pode ter roubado"
                break
            elif lista[i]+lista[j] < 150:
                j += 1
            else:
                i -= 1
    
    return response


lista = [10, 20, 40, 80, 95, 110, 130]
response = verifica_lista(lista)
print(response)