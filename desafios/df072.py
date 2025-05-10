extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')



while True:
    num = int(input('Escolha um número de 0 a 20 [999 para sair]: '))
    if num == 999:
        break
    elif num >= 0 and num <= 20:
        print(f'O número {num}, por extenso fica: {extenso[num]}')
    else:
        print('Você digitou um valor inválido! Tente novamente.') 
        
print('Programa Finalizado! Até mais')