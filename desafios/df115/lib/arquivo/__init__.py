def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro ao criar o arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    try:
        with open(nome, 'rt') as a:
            print('=' * 50)
            print('\033[1;36mPESSOAS CADASTRADAS NO ARQUIVO\033[m'.center(50))
            print('=' * 50)
            for i, linha in enumerate(a, 1):
                nome, sexo, idade = linha.strip().split(';')
                print(f'{i:<3} \033[1;32m{nome:<25} {sexo:<12} {idade:<5}\033[m')
            print('=' * 50)
    except FileNotFoundError:
        print('Arquivo não encontrado.')

