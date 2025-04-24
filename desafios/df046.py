#Programa que faz a contagem regressiva para o estouro de fogos de artifícios, indo de 10 até 0
from time import sleep
print('Íniciando a contagem regressiva para o lançamento dos fogos!')
for c in range(10, -1, -1):
    print(c)
    sleep(0.5)
print('Fim')