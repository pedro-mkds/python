# Programa que lê início, fim e passo, e exibe a contagem correta

print('=' * 30)
print('   CONTADOR PERSONALIZADO   ')
print('=' * 30)

inicio = int(input('Digite o primeiro número: '))
fim = int(input('Digite o último número: '))
passo = int(input('Digite o passo: '))

# Verifica se o passo é 0 e corrige
if passo == 0:
    print('Passo 0 não é válido. Considerando passo 1.')
    passo = 1

# Ajusta o passo para contagem decrescente, se necessário
if inicio > fim and passo > 0:
    passo = -passo

print('=' * 30)
print(f'Contando de {inicio} até {fim} de {abs(passo)} em {abs(passo)}:')
print('=' * 30)

# Ajusta o fim com base na direção da contagem
if passo > 0:
    fim += 1
else:
    fim -= 1

# Executa a contagem
for c in range(inicio, fim, passo):
    print(c, end=' ')
print('FIM')