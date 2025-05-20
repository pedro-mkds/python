from utilizadescev import moeda
from utilizadescev import dado

p = dado.leiaDinheiro('Digite o preço: R$')
a = int(input('Digite o aumento: %'))
d = int(input('Digite o desconto: %'))
form = str(input('Gostaria de formatar? [S/N] ')).strip()[0].upper()[0]

moeda.resumo(p, a, d, form)
