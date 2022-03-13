#mostrando a parte inteira de um numero       

'''#Primeiro metodo

num = float(input('Digite um numero:'))
print ('o Numero tem a parte inteira de {:.0f}'.format(num))'''

'''Segundo metodo

from math import trunc
num = float(input('Digite um numero'))
print ('O numero tem a parte inteira de {}'.format (trunc (num)))'''

#terceiro metodo
num = float(input('Digite um numero'))
print ('O numero tem a parte inteira de {}'.format ( int(num)))


