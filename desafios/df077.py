palavras = ("amigo", "casa", "carro", "cidade", "computador", "família", "gato", "jogo", "luz", "musica", "novo", "pao", "quadro", "rato", "sol", "tela", "util", "vazio", "xicara", "yogurte", "zona")

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=', ')