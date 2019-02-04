#calculando a hypotenusa
from math import hypot
cat1 = float(input("Qual é o tamanho de um cateto "))
cat2 = float(input("Qual é o tamanho do outro cateto "))
hi = hypot(cat1, cat2)
print("Com base nos catetos {} e {} sua hipotenusa é {}".format(cat1,cat2,hi))
