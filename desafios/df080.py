num = list()

for c in range(0,5):
    num.append(int(input('Digite um valor: ')))
    maior = max(num)
    menor = min(num)
    if num < maior and num > menor:
        num.insert(2, num)

print(num)
print(maior, menor)
#num.insert(posição, item)
