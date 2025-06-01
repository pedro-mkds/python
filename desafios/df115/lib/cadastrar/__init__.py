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

def cadastro(nome_arquivo):
    while True:
        nome = input('\033[1;34mNome (até 25 caracteres): \033[m').strip().title()
        if not nome or len(nome) > 25:
            print('\033[0;31mERRO! Nome inválido.\033[m')
            continue

        sexo = ''
        while sexo not in ['M', 'F']:
            sexo = input('\033[1;34mSexo [M/F]: \033[m').strip().upper()
            if sexo not in ['M', 'F']:
                print('\033[0;31mDigite apenas M ou F.\033[m')
        sexo_str = 'Masculino' if sexo == 'M' else 'Feminino'

        idade = leiaInt('\033[1;34mIdade: \033[m')
        if idade is None or idade < 0 or idade > 120:
            print('\033[0;31mERRO! Idade inválida.\033[m')
            continue

        try:
            with open(nome_arquivo, 'a', encoding='utf-8') as f:
                f.write(f'{nome};{sexo_str};{idade}\n')
            print(f'\033[1;32m{nome} foi cadastrado com sucesso!\033[m')
        except Exception as e:
            print(f'\033[0;31mErro ao salvar no arquivo: {e}\033[m')

        cont = input('\n\033[1;32mDeseja cadastrar mais uma pessoa? [S/N]: \033[m').strip().upper()
        if cont != 'S':
            print('\033[1;31mEncerrando cadastro...\033[m')
            break



def listar(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as f:
            linhas = f.readlines()

        if not linhas:
            print('\033[0;33mNenhuma pessoa cadastrada.\033[m')
            return

        print('=' * 50)
        print('\033[1;32mPESSOAS CADASTRADAS\033[m'.center(50))
        print('=' * 50)
        print('{:<5} {:<25} {:<12} {:<5}'.format('ID', 'Nome', 'Sexo', 'Idade'))
        print('-' * 50)
        for i, linha in enumerate(linhas, 1):
            nome, sexo, idade = linha.strip().split(';')
            print('{:<5} \033[1;32m{:<25} {:<12} {:<5}\033[m'.format(i, nome, sexo, idade))
        print('=' * 50)
    except FileNotFoundError:
        print('\033[0;31mArquivo de cadastro não encontrado.\033[m')
