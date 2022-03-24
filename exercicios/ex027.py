nome = str(input('Digite sue nome completo:')).strip()
n = nome.split()
print('Muito prazer em te conhecer! {}'.format(n[0]))
print('Seu primeiro nome é {}'.format(n[0]))
print('Seu ultimo nome é {}'.format(n[len(n)-1]))

