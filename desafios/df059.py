from time import sleep
print('=-=' * 10)
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
opc = 0
sleep(0.5)
print('=-=' * 10)
while opc != 5:
    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa''')
    opc = int(input('>>>>> Qual é a sua opção? '))
    if opc == 1:
        s = n1 + n2
        print('=-=' * 10)
        print('A soma entre {} + {} da: {}.'.format(n1, n2, s))
        print('=-=' * 10)
    elif opc == 2:
        m = n1 * n2
        print('=-=' * 10)
        print('O resultado de {} X {} é: {}.'.format(n1, n2, m))
        print('=-=' * 10)
    elif opc == 3:
        print('=-=' * 10)
        if n1 > n2:
            maior = n1
            print('Entre {} e {}, o maior é {}.'.format(n1, n2, maior))
        else:
            maior = n2
            print('Entre {} e {}, o maior valor é {}.'.format(n1, n2, maior))
        print('=-=' * 10)

    elif opc == 4:
        print('=-=' * 10)
        print('Infome os valores novamente')
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
        print('=-=' * 10)
    elif opc == 5:
        print('=-=' * 10)
        print('Finalizando...')
        print('=-=' * 10)
    else:
        print('=-=' * 10)
        print('Opção inválida. Tente novamente')
        print('=-=' * 10)
sleep(2)
print('Fim do programa! Volte sempre!')
print('=-=' * 10)