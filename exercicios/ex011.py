#calculando area
larg = float(input('Largura da parede'))
altu = float(input('Altura da parede'))
area = larg * altu
print('Sua parede tem dimensão de {} X {} e sua area é de {}m.'.format(larg, altu, area))
tinta = area / 2
print('para pintar sua parede voce vai precisar de {} litros de tinta'.format(tinta))