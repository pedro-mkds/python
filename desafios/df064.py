#Programa que soma valores mas quando digitar 999 ele para
n = c = s = 0
while n !=  999:
    n = int(input('Digite um valor [999 para parar]: '))
    if n != 999:
        s += n
        c += 1
print('Você digitou {} número e a soma deles é de {}'.format(c, s))

