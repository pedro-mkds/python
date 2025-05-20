import moeda

p = float(input('Digite o preço: R$'))
form = str(input('Gostaria de formatar? [S/N] ')).strip()[0].upper()[0]
if form == 'S':
    form = True
elif form == 'N':
    form = False
print(f'A metade de {moeda.moeda(p)} é {moeda.met(p, form)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, form)}')
print(f'Aumentando 10%, temos {moeda.aum(p, 10, form)}')
print(f'Reduzindo 13%, temos {moeda.dim(p, 13, form)}')
