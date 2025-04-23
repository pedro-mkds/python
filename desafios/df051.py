#Programa que le o primeiro termo e a razão de uma PA. No final, mostra os 10 primeiros termos dessa progressão. 
primeiro = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão da PA: "))

for c in range(0, 10):
    termo = primeiro + c * razao
    print(termo)