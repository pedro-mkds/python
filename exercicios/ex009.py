num = [5, 4, 3, 9, 0]
num[3] = 8
num.append(7)
num.insert(2, 5)

print(num)

num.sort()
print(num)
num.sort(reverse = True)
print(num)
num.pop(3)
print(f'A lista: {num}, possui {len(num)} itens')