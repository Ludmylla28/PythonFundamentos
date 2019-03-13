## Modulo datetime 

import datetime

#buscando a data atual
agora = datetime.datetime.now()
print(agora)

dir(datetime)

#buscando o dia atual
dia = datetime.date.today()

print(dia)
print('ctime :', dia.ctime())
print('Ano :', dia.year)
print('Mes :', dia.month)
print('Dia :', dia.day)

#buscando hora atual
t = datetime.time(7,52,00)

print(t)
print('hora :', t.hour)
print('minuto :', t.minute  )
print('segundo :', t.second )
print('microsegundo :', t.microsecond)


# definindo data 
d1 = datetime.date(2018, 6, 28)
print(d1)

d2 = d1.replace(year=2019)
print('d2 :', d2)

print(d1-d2)

