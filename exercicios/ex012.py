#calculando desconto na promoção
preço= float(input('Qual é o preço do sue produto R$'))
# Porcentagem é valor do produto vezez o nivel da porcentagem dividido por cem
novo = preço - (preço * 5 / 100)
print('Opreço com 5%, de desconte fica em {:.2f}'.format(novo))



