#Aluguel de carro
dias = int(input("Quantos dias você ficou com ele ? "))
km = float(input("Quantos km rodou ? "))
pago = (dias * 60) + (km * 0.15)
print("O preço a ser pago é R${:.2f}".format(pago))
