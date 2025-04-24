#Programa que analisa dados completos de 4 pessoas
#Media de idade do grupo X
#Nome do homem mais velho
#Quantas mulheres tem menos de 20 anos
pessoas = 0
media_idade = 0
maior = 0
menor = 0
nome_homem_mais_velho = ''
mulheres_menos_20 = 0
for d in range(1, 5):
    print('----- {}ª PESSOA -----'.format(d))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    
    media_idade += idade
    
    if d == 1 and sexo == 'M':
        maior = idade
        nome_homem_mais_velho = nome
    if sexo == 'M' and idade > maior:
        maior = idade
        nome_homem_mais_velho = nome
        
    if sexo == 'F' and idade < 20:
        mulheres_menos_20 += 1
        

print('A idade média do grupo é de: {:.0f} anos'.format(media_idade / 4))
if nome_homem_mais_velho != '':
    print('O nome do homem mais velho é {} e possui {} anos'.format(nome_homem_mais_velho, maior))
else:
    print('Não houve nenhum homem no grupo.')
print('Nesse grupo {} mulher(es) possuem menos de 20 anos'.format(mulheres_menos_20))