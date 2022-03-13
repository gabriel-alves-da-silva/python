#calculando a hipotenusa
from math import hypot
co = float(input('digite o comprimento do cateto oposto:'))
ca = float(input('Comprimento do cateto adjacente:'))
hi = hypot(co, ca)
print ('a hipotenusa vai medir {}'.format(hi))