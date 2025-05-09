lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Hamburguer')
#Tuplas são imutáveis

for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Eu comi pra caramba')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('Eu comi pra caramba')
