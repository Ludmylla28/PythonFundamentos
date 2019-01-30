real = float(input('Quanto você tem na carteira ? R$'))
dolar = real/4.02
dolarCanadense = real/3.14
print('Com R${:.2f} reais você pode comprar U${:.2f} dolares ou C${:.2f} dolares canadenses'.format(real,dolar,dolarCanadense))