from lib.interface import  *
from lib.arquivo import *
from time import sleep

arq = 'dados.txt'

if not arquivoExiste(arq):
    print('Arquivo encontrado com sucesso!')

while True:
    resposta = menu(['Listar Pessoas Cadastras', 'Cadastrar Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de listar conteúdo de um arquivo.
        lerArquivo(arq)
    elif resposta == 2:
        # opção de cadastrar uma nova pessoa.
        submenu('NOVO CADASTRO')
        nome = str(input('Nome: ')).strip().title()
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        # opção de sair do programa.
        submenu('Saindo do sistema... Até logo!')
        break
    else:
        # Digitou uma opção errada no menu.
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)