conjunto = list() 
while True:
    dados = []
    dados.append(str(input('Aluno: ')).strip().title())
    n1 = int(input('1º Nota: '))
    dados.append(n1)
    n2 = int(input('2º Nota: '))
    dados.append(n2)
    n3 = int(input('3º Nota: '))
    dados.append(n3)
    media = (n1 + n2 + n3) / 3
    dados.append(media)
    conjunto.append(dados)
    cont = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if cont == 'N':
        break

print('-=' * 30 )
print('Boletim dos Alunos')
print('-=' * 30 )

for v, i in enumerate(conjunto):
    print(f'{v} - {i[0]} | Média: {i[4]:.2f}')

while True:
    puxar = int(input('Mostrar notas de qual aluno? [999 para parar] '))
    if puxar == 999:
        break
    print(f'O aluno {conjunto[puxar][0]}, tirou as seguintes notas: {conjunto[puxar][1:4]}')
print('\nPrograma finalizado! Volte sempre.')
