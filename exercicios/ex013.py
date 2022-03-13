#calculando salario
sal = float(input('Digite o salario R$'))
# Porcentagem é valor do produto vezez o nivel da porcentagem dividido por cem
novo = sal + (sal *15 /100)
print('O salario de {:.2f} com 15%, de aumento fica em {:.2f}'.format( sal,novo))

