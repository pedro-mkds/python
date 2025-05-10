produtos = ("Camiseta", 49.90, "Calça Jeans", 129.90, "Tênis", 199.99, "Jaqueta de Couro", 350.00, "Óculos de Sol", 150.00, "Relógio", 450.00, "Perfume", 120.00, "Bolsa de Couro", 250.00, "Fones de Ouvido", 80.00, "Carregador Portátil", 60.00)
print('-' * 40)
print(f'{'LISTAGEM DE PREÇO':^40}')
print('-' * 40)
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end='')
    else:
        print(f'R${produtos[pos]:>7.2f}')
