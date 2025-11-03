#Recebe um array de anos em string
#Começa no ano[0] e viaja a partir dali de A para B
#Se A=B, 0 horas
#Se A<B, 1 hora
#Se A>B, 2 horas
def calculate(anos):
    i = 0
    count = 0
    while i < len(anos)-1:
        if int(anos[i]) > int(anos[i+1]):
            count+=2
        elif int(anos[i]) < int(anos[i+1]):
            count+=1
        else:
            count+=0
        i+=1
    return count



anos = ["2000", "1990", "1998", "1998", "2050", "2025"] # => 1+2+0+2+1 = 6
response = calculate(anos)
print(response)