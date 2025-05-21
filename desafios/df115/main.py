import cadastrar
import json

def salvar_arquivo(lista, nome_arquivo='dados.json'):
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        json.dump(lista, f, ensure_ascii=False, indent=4)

def carregar_arquivo(nome_arquivo='dados.json'):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

conjunto = carregar_arquivo()

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
        cadastrar.cadastro(conjunto)
        salvar_arquivo(conjunto)
    elif r == 2:
        cadastrar.listar(conjunto)
    elif r == 3:
        print('\033[1;31mSaindo do sistema... Até logo! 👋\033[m')
        break
    else:
        print('\033[0;31mERRO! Opção inválida.\033[m')
