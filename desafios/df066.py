c = s = 0
while True:
    n = int(input('Digite um valor [999 para parar]: '))
    if n == 999:
        break 
    c += 1
    s += n
print(f'Fim do programa! Você digitou {c} número e a soma deles é de {s}')
