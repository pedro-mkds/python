from desafios.df115_outra_forma.lib.interface import cabeçalho


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
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com SUCESSO!')

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('ERRO ao ler o arquivo!')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] =  dado[1].replace('\n','')
            print(f'\033[33m{dado[0]:<30}\033[m\033[34m{dado[1]:>3}\033[m anos')
    finally:
        a.close()

def cadastrar(arq, nome= '<deconhecido>', idade = 0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um erro ao abrir o arquivo:')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro na hora de escrever os dados.')
        else:
            print(f'Novo registro {nome} adicionado!')
            a.close()
