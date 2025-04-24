frase = str(input('Digite uma frase: ')).strip().upper().split()
junto = ''.join(frase)
if junto == junto[::-1]:
    print('Está frase é um palíndromo, pois {} fica igual quando invertida: {}'.format(junto, junto[::-1]))
else:
    print('Está frase não é um palíndromo pois {} não fica igual quando invertida: {}'.format(junto, junto[::-1]))