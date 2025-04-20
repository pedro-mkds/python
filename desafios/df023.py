#Programa que le quantas vezes a letra 'A' aparece, a posição em que ele aparece por primeiro e depois por último

verf = str(input('Digite algo: ')).strip()

print('Verificando a frase: {} '.format(verf))
print('A letra A aparece {}x na frase {}'.format(verf.lower().count('a') , verf))
print('A posição em que a primeira letra A aparece é: {}'.format(verf.find('a')+1))
print('A posição em que a última letra A aparece é: {}'.format(verf.rfind('a')+1))