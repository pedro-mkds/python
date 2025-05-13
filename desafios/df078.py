valores = []
maior = menor = 0

for c in range(0,5):
    valores.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        maior = menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]

print(f'Os valores digitas foram: {valores}')
print(f'O maior valor foi {maior}, que está na posição ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O menor valor foi {menor}, que está na posição ',end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...',end='')
print()
