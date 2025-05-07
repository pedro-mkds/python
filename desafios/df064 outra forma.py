#Programa que soma valores mas quando digitar 999 ele para
n = c = s = 0
n = int(input('Digite um valor [999 para parar]: '))
while n !=  999:
    s += n
    c += 1
    n = int(input('Digite um valor [999 para parar]: '))
print('Você digitou {} número e a soma deles é de {}'.format(c, s))

