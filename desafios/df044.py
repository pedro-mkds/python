#Programa que calcula o valor a ser pago por um produto e mostra diferentes formas de pagamento e suas condições
from time import sleep
a = 4500
b = 2000
c = 5000 
d = 2500
e = 1500

print('-==-==-' * 20)
print('{:=^40}'.format(' LOJAS KOCHE '))
print('-==-==-' * 20)
print('Escolha um produto do nosso catalago e veja as formas de pagamento!')
print('''   
    a | TV Smart 4k 75 Polegadas
    b | Telefone 128GB de armazenamento 8gb de ram
    c | Notebook Gamer
    d | Geladeira 
    e | Sofá''')
selecionar = str(input('\nSelecione um produto para saber mais: '))

print('-==-==-' * 20)
sleep(2)
print('Buscando...')
sleep(1)
print('Analisando informações...')
sleep(1)
print('Enviando dados...')
sleep(2)

if selecionar == 'a':
    selecionar = a
    print('A Tv está custando: R$4500,00')
    print('Confira os meios de pagamento:')
    print(' | À vista no dinheiro/pix: R${:.2f} 10% de desconto \n | À vista no cartão: R${:.2f} 5% de desconto \n | Em até 2x no cartão: R${:.2f} preço normal \n | 3x ou mais no cartão: R${:.2f} 20% de juros'.format(a - (a * 0.10), a - (a * 0.05), a, a + (a * 0.30)))
    
    
elif selecionar == 'b':
    selecionar = b
    print('O celular está custando: R$2000,00')
    print('Confira os meios de pagamento:')
    print(' | À vista no dinheiro/pix: R${:.2f} 10% de desconto \n | À vista no cartão: R${:.2f} 5% de desconto \n | Em até 2x no cartão: R${:.2f} preço normal \n | 3x ou mais no cartão: R${:.2f} 20% de juros'.format(b - (b * 0.10), b - (b * 0.05), b, b + (b * 0.30)))
    
elif selecionar == 'c':
    selecionar = c
    print('O Notebook está custando: R$5000,00')
    print('Confira os meios de pagamento:')
    print(' | À vista no dinheiro/pix: R${:.2f} 10% de desconto \n | À vista no cartão: R${:.2f} 5% de desconto \n | Em até 2x no cartão: R${:.2f} preço normal \n | 3x ou mais no cartão: R${:.2f} 20% de juros'.format(c - (c * 0.10), c - (c * 0.05), c, c + (c * 0.30)))
    
elif selecionar == 'd':
    selecionar = d
    print('A Geladeira está custando: R$2500,00')
    print('Confira os meios de pagamento:')
    print(' | À vista no dinheiro/pix: R${:.2f} 10% de desconto \n | À vista no cartão: R${:.2f} 5% de desconto \n | Em até 2x no cartão: R${:.2f} preço normal \n | 3x ou mais no cartão: R${:.2f} 20% de juros'.format(d - (d * 0.10), d - (d * 0.05), d, d + (d * 0.30)))
    
elif selecionar == 'e':
    selecionar = e
    print('O Sofá está custando: R$1500,00')
    print('Confira os meios de pagamento:')
    print(' | À vista no dinheiro/pix: R${:.2f} 10% de desconto \n | À vista no cartão: R${:.2f} 5% de desconto \n | Em até 2x no cartão: R${:.2f} preço normal \n | 3x ou mais no cartão: R${:.2f} 20% de juros'.format(e - (e * 0.10), e - (e * 0.05), e, e + (e * 0.30)))
    
else:
    print('#ERRO# \nVocê digitou um valor inválido! Tente novamente.')