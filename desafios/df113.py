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
            print(f'\033[0;31mERRO! {e}\033[m')
        except KeyboardInterrupt:
            print('\n\033[0;31mEntrada cancelada pelo usuário.\033[m')
            return None

def leiaFloat(msg):
    while True:
        try:
            n = input(msg).strip().replace(',', '.')
            if n == '':
                raise ValueError('Entrada vazia.')
            return float(n)
        except ValueError as e:
            print(f'\033[0;31mERRO! {e}\033[m')
        except KeyboardInterrupt:
            print('\n\033[0;31mEntrada cancelada pelo usuário.\033[m')
            return None


# --- Programa principal
i = leiaInt('Digite um número inteiro: ')
r = leiaFloat('Digite um número real: ')

if i is not None and r is not None:
    print(f'\nVocê digitou {i} (inteiro) e {r} (real).')
else:
    print('\n\033[0;33mPrograma encerrado sem valores válidos.\033[m')
