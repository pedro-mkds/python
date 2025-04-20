#calculadora de desconto
import math
vt= float(input('Quanto seu produto custa? '))
d= float(input('Qual o valor do desconto que esse produto ira sofrer? '))

up=vt/100

vd=up*d
vf=math.ceil(vt-vd)

print('Se seu produto custa R${} e sofre um desconto de {}, ele passara a custar {}. \n Resumo \n Valor do Produto: {} \n Desconto: {} \n Valor final: {}'.format(vt,d,vf,vt,vd,vf))