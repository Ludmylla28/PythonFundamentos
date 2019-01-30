largura = float(input('digite a largura da parede '))
altura = float(input('digite a altura da parede '))
m2 = altura * largura
tinta = m2/2
print('Sua parede tem {} de altura, {} de largura, {} metros quadrados e precisara de {} litros de tinta para pintar a parede'.format(altura,largura, m2, tinta))