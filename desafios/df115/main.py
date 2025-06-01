from desafios.df115.lib import cadastrar
from desafios.df115.lib import arquivo

arq = 'cursoemvideo.txt'
if arquivo.arquivoExiste(arq):
    print('Arquivo encontrado com sucesso!')
else:
    print('Arquivo não encontrado!')
    arquivo.criarArquivo(arq)

while True:

    print('=' * 40)
    print('\033[1;32mMENU PRINCIPAL\033[m'.center(40))
    print('=' * 40 + '\033[m')
    print('🧑‍💻 \033[1;35m[ 1 ]\033[m Cadastrar uma nova pessoa')
    print('📄 \033[1;35m[ 2 ]\033[m Listar pessoas cadastradas')
    print('❌ \033[1;35m[ 3 ]\033[m Sair do sistema')
    print('=' * 40)

    try:
        r = int(input('Escolha uma opção: '))
    except ValueError:
        print('\033[0;31mERRO! Digite um número válido (1, 2 ou 3).\033[m')
        continue

    if r == 1:
        cadastrar.cadastro(arq)
    elif r == 2:
        cadastrar.listar(arq)
    elif r == 3:
        print('\033[1;31mSaindo do sistema... Até logo! 👋\033[m')
        break
    else:
        print('\033[0;31mERRO! Opção inválida.\033[m')
