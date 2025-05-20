import moeda

p = int(input('Digite o preço: R$'))
print(f'A metade de R${p} é R$moeda.met(p)}')
print(f'O dobro de R${p} é R${moeda.dobro(p)}')
print(f'Aumentando 10%, temos R${moeda.aum(p, 10)}')
print(f'Reduzindo 13%, temos R${moeda.dim(p, 13)}')
