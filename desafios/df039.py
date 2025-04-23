#Programa alistamento
from datetime import date
anoatual = date.today().year
anonascimento = int(input('Digite o ano que você nasceu: '))
idade = anoatual - anonascimento
anoalistamento = anoatual + 18 - idade

print('Programa de alistamento. Saiba se você já pode se alistar!')
print('===' * 20)

if idade < 18:
    print('Você possou menos de 18 anos. Seu alistamento sera feito no ano de {}'.format(anoalistamento))

elif idade == 18:
    print('Você ainda pode se alistar, pois ja possui 18 anos ou ainda irá fazer 18 anos esse ano.')
    
else:
    print('Seu alistamento está atrasado! Você deveria ter feito seu alistamento no ano de {}'.format(anoalistamento))