frase = str(input('Digite uma frase:')).upper().strip()
print ('a letra A aparece {} vezes na frase'.format(frase.count('A')))
print ('A Primeira letra  A apareceu na posição {}'.format(frase.find('A')+1))
print ('A ultima letra A apare na posiçõa {}'.format(frase.rfind('A')+1))
