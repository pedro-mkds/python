#Irei construir um programa onde ele ira ler um número inteiro e mostrar o seu sucessor e antecessor.

v= int(input('Digite um valor e te mostrarei o seu sucessor e antecessor: '))
s= v+1
a= v-1

d= v*2
t= v*3
r= int(v**(1/2))


print('O sucessor de {} é {}, e o antecessor de {} é {}'.format(v,s,v,a))

print('O dobro de {} é {}, seu triplo é {} e sua raiz quadrada é {}'.format(v,d,t,r))


