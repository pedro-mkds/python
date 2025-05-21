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

def cadastro(lista):
    while True:
        pessoa = dict()
        while True:
            nome = input('\033[1;34mNome (até 25 caracteres): \033[m').strip().title()
            if len(nome) == 0:
                print('\033[0;31mERRO! Nome não pode ser vazio.\033[m')
            elif len(nome) > 25:
                print('\033[0;31mERRO! Nome muito longo. Digite no máximo 25 caracteres.\033[m')
            else:
                pessoa['nome'] = nome
                break

        while True:
            sexo = input('\033[1;34mSexo [M/F]: \033[m').strip().upper()
            if sexo in 'MF' and sexo.isalpha():
                pessoa['sexo'] = 'Masculino' if sexo == 'M' else 'Feminino'
                break
            else:
                print('\033[0;31mDigite apenas "M" (masculino) ou "F" (feminino).\033[m')

        while True:
            idade = leiaInt('\033[1;34mIdade: \033[m')
            if idade is None:
                print('\033[0;31mERRO! Idade não informada.\033[m')
                continue
            if idade < 0 or idade > 120:
                print('\033[0;31mERRO! Idade inválida. Digite entre 0 e 120.\033[m')
                continue
            pessoa['idade'] = idade
            break

        lista.append(pessoa)
        print(f'\033[1;32m{pessoa["nome"]} foi cadastrado com sucesso!\033[m')

        while True:
            cont = input('\n\033[1;32mDeseja cadastrar mais uma pessoa? [S/N]: \033[m').strip().upper()
            if cont == 'S':
                break
            elif cont == 'N':
                print('\033[1;31mEncerrando cadastro...\033[m')
                return
            else:
                print('\033[0;31mERRO! Responda apenas com "S" ou "N".\033[m')

def listar(lista):
    if not lista:
        print('\033[0;33mNenhuma pessoa cadastrada.\033[m')
        return

    print('=' * 50)
    print('\033[1;32mPESSOAS CADASTRADAS\033[m'.center(50))
    print('=' * 50)
    print('{:<5} {:<25} {:<12} {:<5}'.format('ID', 'Nome', 'Sexo', 'Idade'))
    print('-' * 50)
    for i, pessoa in enumerate(lista, 1):
        print('{:<5} \033[1;32m{:<25} \033[1;32m{:<12} \033[1;32m{:<5}\033[m'.format(
            i, pessoa["nome"], pessoa["sexo"], pessoa["idade"]))
    print('=' * 50)
