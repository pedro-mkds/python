#Programa connecta
profissionais = []

while True:
    print('-' * 30)
    profissional = {
        'nome': input('Nome: '),
        'area': input('Área de atuação: '),
        'cidade': input('Cidade: '),
        'idade': int(input('Idade: ')),
        'disponivel': input('Disponível para atendimento? [S/N]: ').strip().upper() == 'S'
    }
    profissionais.append(profissional)
    
    continuar = input('Deseja cadastrar outro profissional? [S/N] ').strip().upper()
    if continuar != 'S':
        break

print('\n--- Profissionais disponíveis ---')
for p in profissionais:
    if p['disponivel']:
        print(f"{p['nome']} - {p['area']} ({p['cidade']})")
