import math
ang = float(input('Digite o ângulo que você deseja: '))
sen = math.sin(math.radians(ang))
print('O ângulo de {} tem o SENO de {:.2f}'.format(ang, sen))
coss = math.cos(math.radians(ang))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ang,coss))
tang = math.tan(math.radians(ang))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(ang,tang))
