cores = (
    '\033[m',         # 0 - Sem cor
    '\033[0;30;44m',  # 1 - Azul
    '\033[0;30;42m',  # 2 - Verde
    '\033[0;30;46m',  # 3 - Ciano
    '\033[1;37;41m',  # 4 - Vermelho claro (para saída)
)

def ajuda(com):
    titulo(f"Acessando o manual do comando '{com}'", 3)
    print(cores[0], end='')  # Reset
    help(com)

def titulo(msg, cor=1):
    tam = len(msg) + 4
    print(cores[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(cores[0], end='')  # Reset


# Programa Principal
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('\033[0;32mFunção ou Biblioteca > \033[m')).strip()
    if comando.upper() == 'FIM':
        titulo('ATÉ LOGO!', 4)
        break
    else:
        ajuda(comando)
