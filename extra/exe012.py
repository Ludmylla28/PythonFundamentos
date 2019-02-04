#Calculo de desconto
produto = float(input("Me informe o valor do produto desejado = R$"))
desconto10 = produto - (produto * 10 / 100)
desconto25 = produto - (produto * 25 / 100)
desconto50 = produto - (produto * 50 / 100)
print("Esse é o preço do seu produto R${}".format(produto))
print("Esse é o preço do seu produto com 10% de desconto R${}".format(desconto10))
print("Esse é o preço do seu produto com 25% de desconto R${}".format(desconto25))
print("Esse é o preço do seu produto com 50% de desconto R${}".format(desconto50))
