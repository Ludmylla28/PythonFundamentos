#conversor de petragem e calculador de consumo de gazolina
metros = float(input("Me informe a distancia em metros da sua casa ate o seu serviço "))
decimetros = metros*10
centimetros = metros*100
milimetros = metros*1000
decametros = metros/10
hectometro = metros/100
kilometros = metros/1000
gazolina = (kilometros/8)*4.50
print(" Você percorre {} metro, {} decimetros, {} centimetros, {} milimetros".format(metros, decimetros, centimetros, milimetros)) 
print(" Ou {} decametros, {} hectometro, {}kilometro e consome por viagem {} de gazolina".format(decametros, hectometro, kilometros, gazolina))
