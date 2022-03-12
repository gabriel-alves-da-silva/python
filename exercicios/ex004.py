#Dissecando uma variavel
nome = input(('Qual é seu nome?'))
print('Olá {} Esse script de python vai dizer algumas caracteristicas  do valor que voce dizer. [False] Significa Não e [true] Siginifica Sim.\nSe voce é um progamador ou poliglota voce sabe que não significa, Mas aqui siginifica porque essa porra não é uma democracia'.format(nome,))
n1 = input('Digite algo para ver as informações:')
i1 = (n1.isalnum())
i2 = (n1.isspace())
i3 = (n1.isalpha())
i4 = (n1.islower())
i5 = (n1.isupper())
i6 = (type(n1))
print ('Ele é um numero? {}|\nÈ um espaço? {}|\nÈ alfa numerico? {}|\nÈ uma letra minuscula? {}|\nÈ uma letra maiuscula? {}|\nO tipo primitivo é {}|'.format(i1, i2, i3, i4, i5, i6))

print ("Obrigado por testar, {}! Voce é um amigo. Amigo <3".format(nome))
