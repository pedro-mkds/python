#Programa que le 6 número inteiros e mostra a soma apenas daqueles que forem pares. Se o valor for impar desconsidere
s = 0
for c in range(1, 7):
    v = int(input('Digite um número inteiro: '))
    if v % 2 == 0:
        s += v
print('A soma dos valores foi de {}'.format(s))