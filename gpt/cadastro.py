import re

def ler_nome():
    while True:
        nome = input("Nome completo: ").strip()
        if nome.replace(' ', '').isalpha():
            return nome.title()
        print("❌ Nome inválido. Use apenas letras e espaços.")

def ler_sexo():
    while True:
        sexo = input("Sexo [M/F]: ").strip().upper()
        if sexo in ['M', 'F']:
            return sexo
        print("❌ Sexo inválido. Digite apenas 'M' ou 'F'.")

def ler_idade():
    while True:
        try:
            idade = int(input("Idade: ").strip())
            if 18 <= idade <= 100:
                return idade
            elif idade < 18:
                print("❌ O cliente deve ter no mínimo 18 anos.")
            else:
                print("❌ Idade acima do permitido.")
        except ValueError:
            print("❌ Digite um número válido.")

def ler_email():
    while True:
        email = input("E-mail: ").strip()
        if re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return email.lower()
        print("❌ E-mail inválido.")

def ler_telefone():
    while True:
        telefone = input("Telefone (somente números): ").strip()
        if telefone.isdigit() and 10 <= len(telefone) <= 11:
            return telefone
        print("❌ Telefone inválido. Digite 10 ou 11 dígitos.")

def ler_cpf():
    while True:
        cpf = input("CPF (somente números): ").strip()
        if cpf.isdigit() and len(cpf) == 11:
            return cpf
        print("❌ CPF inválido. Deve conter 11 dígitos numéricos.")

def exibir_cliente(cliente):
    print("\n📝 DADOS DO CLIENTE")
    print(f"Nome    : {cliente['nome']}")
    print(f"Sexo    : {'Masculino' if cliente['sexo'] == 'M' else 'Feminino'}")
    print(f"Idade   : {cliente['idade']} anos")
    print(f"E-mail  : {cliente['email']}")
    print(f"Telefone: {cliente['telefone']}")
    print(f"CPF     : {cliente['cpf']}")
    print("-" * 40)

def main():
    clientes = []
    print('-=' * 20)
    print(f'{"CADASTRO PROFISSIONAL DE CLIENTES":^40}')
    print('-=' * 20)

    while True:
        cliente = {
            'nome': ler_nome(),
            'sexo': ler_sexo(),
            'idade': ler_idade(),
            'email': ler_email(),
            'telefone': ler_telefone(),
            'cpf': ler_cpf()
        }
        clientes.append(cliente)
        exibir_cliente(cliente)

        continuar = input("Deseja cadastrar outro cliente? [S/N]: ").strip().upper()
        if continuar == 'N':
            break

    print(f"\n📋 {len(clientes)} cliente(s) cadastrados com sucesso.")
    print("Encerrando o programa.")

if __name__ == "__main__":
    main()
