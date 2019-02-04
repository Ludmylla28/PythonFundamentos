#seno, coceno e tangente
from math import radians, sin, cos, tan
angulo = float(input("Me infome o angulo "))
seno = sin(radians(angulo))
coceno = cos(radians(angulo))
tangente = tan(radians(angulo))
print("O angulo é {}, e o seno {:.2f}, coceno {:.2f} e a tangente {:.2f}".format(angulo,seno,coceno,tangente))
