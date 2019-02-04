#Conversor de moeda
reais = float(input("Quanto de dinheiro você tem agora ? "))
dolarAmericano = reais/3.73
dolarCanadensse = reais/2.83
print("Com o dinheiro que você tem hoje que é R${:.2f}, você consegue U${:.2f} e CAD${:.2f}".format(reais, dolarAmericano,dolarCanadensse))
