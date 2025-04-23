v1 = int(input('Digite um número: '))
v2 = int(input('Digite outro número: '))
#São iguais:
if v1 == v2:
    print('Não existe número maior ou menor, pois os dois são iguais')
    
else:
#Definindo o maior:
    maior = v1
    if v2 > v1:
        maior = v2
    
#Definindo o menor:
    menor = v1
    if v2 < v1:
        menor = v2
    
    print('O maior número é {} e o menor é {}'.format(maior, menor))
    



