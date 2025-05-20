import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.met(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando 10%, temos R${moeda.moeda(moeda.aum(p, 10))}')
print(f'Reduzindo 13%, temos R${moeda.moeda(moeda.dim(p, 13))}')
 