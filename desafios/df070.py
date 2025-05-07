maisde1k = cont = menor = total = maior = 0
nomemenor = ''

print('-=' * 20)
print('Lojas Koche')
print('-=' * 20)
while True:
    produto = str(input('Qual produto você comprou? ')).strip()
    preco = int(input('Qual é o valor do produto? R$'))
    cont += 1
    total += preco
    if preco >= 1000:
        maisde1k += 1
    if cont == 1 or preco < menor:
        menor = preco
        nomemenor = produto         
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    if resp == 'N':
        break
print('Fim do programa!')
print(f'O Total da sua compra foi de {total:.2f}')
print(f'Temos {maisde1k} produtos que custam mais de R$1000.00')
print(f'O produto mais barato é: {nomemenor} e custa R${menor:.2f}')