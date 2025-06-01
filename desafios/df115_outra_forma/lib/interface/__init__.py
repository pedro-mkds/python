def leiaInt(msg):
    while True:
        try:
            n = input(msg).strip()
            if n == '':
                raise ValueError('Entrada vazia.')
            if n.isnumeric():
                return int(n)
            else:
                raise ValueError('Não é um número inteiro válido.')
        except ValueError as e:
            print(f'\033[31mERRO! {e}\033[m')
        except KeyboardInterrupt:
            print('\n\033[31mEntrada cancelada pelo usuário.\033[m')
            return None

def linha(tam = 42):
    return '=' * tam

def linhapeq(tam = 42):
    return '-' * tam

def cabeçalho(txt):
    print(linha())
    print(f'\033[32m{txt.center(42)}\033[m')
    print(linha())

def submenu(txt):
    print(linhapeq())
    print(f'\033[034m {txt.center(42)} \033[m')
    print(linhapeq())
def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'    \033[32m[ {c} ]\033[m - {item}')
        c += 1
    print(linha())
    opc = leiaInt('\033[35mSua Opção: \033[m')
    return opc
