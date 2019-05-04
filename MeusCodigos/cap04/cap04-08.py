# List Comprehension, 
# aplica uma expressão arbitraria, 
# a uma sequencia de elementos.
# é um loop for dentro de uma lista

#Compreenção em lista(list comprehension) é a 
#construção de uma lista inteligente

#primeira lista
lst = [x for x in 'python']
print(lst)
type(lst)

#segunda lista 
lst = [x**2 for x in range(0,11,2)]
print(lst)

# terceira lista
lst = [x for x in range(11) if x % 2 == 0]
print(lst)

#quarta lista
celsius = [0,10,20.1,34.5]
fahrenheit = [((float(9)/5)*temp + 32) for temp in celsius]
print(fahrenheit)

#operações aninhadas 
lst = [x**2 for x in [x**2 for x in range(11)]]
print(lst)