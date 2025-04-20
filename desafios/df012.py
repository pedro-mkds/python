#Conversor de temperatura

graus= float(input('Digite quantos °C está em sua cidade":'))

f= graus * 9/5 + 32
#(°F)
k= graus+273.15
#(K)

print('Isso equivale a {}(°F) Fahrenheit e {}(K) Kelvin.'.format(f,k))