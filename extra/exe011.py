#Tinta para pintar uma parede
altura = float(input("Me informe a altura da sua parede = "))
largura = float(input("Me informe a largura da sua parede = "))
metrosQuadrados = altura*largura
tinta = metrosQuadrados/2
print("As medidas da sua parede é de {}m de altura, {}m de largura e tem uma área de {:.2f}m2".format(altura,largura,metrosQuadrados))
print("E para isso você precisará de {:.2f} litros de tinta".format(tinta))
