#Criarei um programa onde ele ira calcular a largura e altura de uma parede e depois ira calcular quanta tinta sera necessária para pintar a parede, sabendo que cada balde de tinta tem 5 litros e cada litro pinta uma área de 2m^2
import math

l= int(input('Digite a largura da sua parede: '))
a= int(input('Agora digite a altura da sua parede: '))
a= l*a
lt= (a/2)
b = math.ceil(lt/5)


print('A área da sua parde é de {} Metros Quadrados, sendo necessário {} baldes de tinta ou {} litros de tinta'.format(a,b,lt))

