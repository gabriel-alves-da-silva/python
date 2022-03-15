#calculando seno cosseno e tangente
from math import radians, cos, tan, sin
an = float(input('Digite o angulo que voce deseja:'))
seno = (radians(an))
print ('O angulo de {} tem o SENO de {:.2f}'.format(an, seno))
cosseno = cos(radians(an))
print('O angulo de {} temo o  COSSENO DE {:.2F} '.format(an, cosseno))
tangente = tan(radians(an))
print ('O angulo de {} tem a TANGENTE DE {:.2F}'.format(an, tangente)) 