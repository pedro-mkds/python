from random import randint

minha_tupla = (randint(1,100), randint(1,100), randint(1,100), randint(1,100), randint(1,100),)
    
maior_valor = max(minha_tupla)
menor_valor = min(minha_tupla)

print(minha_tupla)
print(f'Maior valor: {maior_valor}')
print(f'Menor valor: {menor_valor}')