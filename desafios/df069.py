#Programa cadastro de pessoas
tot18 = tothomem = totM20 = 0
print('-=' * 20)
print('CADASTRE UMA PESSOA')
print('-=' * 20)

idade = 0

while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in ('MmFf'):
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        tothomem += 1
    
    if sexo == 'F' and idade < 20:
        totM20 += 1
        
    continuar = ' ' 
    while continuar not in ('SN'):
        continuar = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    if continuar == 'N':
        break
print('Acabou')
print(f'O total de pessoas com mais de 18 anos é de: {tot18}')
print(f'Ao todo temos {tothomem} homens cadastrados')
print(f'E temos {totM20} mulheres com menos de 20 anos')