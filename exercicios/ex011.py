def ler_nome():
    while True:
        nome = input('Nome: ').strip()
        if nome.replace(' ', '').isalpha():
            return nome.title()
        else:
            print('Nome inválido. Digite apenas letras.')

def ler_sexo():
    while True:
        sexo = input('Sexo: [M/F] ').strip().upper()
        if sexo and sexo[0] in 'MF':
            return sexo[0]
        else:
            print('Entrada inválida. Digite apenas M ou F.')

def ler_idade():
    while True:
        try:
            idade = int(input('Idade: '))
            if 18 <= idade < 100:
                return idade
            elif idade < 18:
                print('O cliente não pode ser menor de 18 anos.')
            else:
                print('Você digitou uma idade inválida.')
        except ValueError:
            print('Digite apenas números inteiros.')

def deseja_continuar():
    while True:
        opcao = input('Deseja cadastrar mais um cliente? [S/N] ').strip().upper()
        if opcao in 'SN':
            return opcao == 'S'
        print('Digite apenas S ou N.')

def main():
    print('-=' * 15)
    print(f'{"CADASTRO DE CLIENTES":^30}')
    print('-=' * 15)

    clientes = []
    while True:
        cliente = {
            'nome': ler_nome(),
            'sexo': ler_sexo(),
            'idade': ler_idade()
        }
        clientes.append(cliente)
        if not deseja_continuar():
            break

    print('\n--- CLIENTES CADASTRADOS ---')
    for i, cliente in enumerate(clientes, 1):
        print(f"{i}. Nome: {cliente['nome']}, Sexo: {cliente['sexo']}, Idade: {cliente['idade']}")

if __name__ == "__main__":
    main()
