# o importante do enumereite é que ele coloca 
# nos valores um indice, usado como uma forma de 
# filtrar os elementos. 
seq = ['a','b','c']

list(enumerate(seq))

# imprimindo os valores de uma lista com a 
# função enumerate() e seus respectivos indices
for indice, valor in enumerate(seq):
    print(indice,valor)

# printando o valor ate 2
for indice, valor in enumerate(seq):
    if indice >= 2:
        break
    else:
        print(valor)

#criando uma lista 
lista = ['marketing', 'tecnologia', 'business', 'direito'] 

#imprimindo o item e o indice 
for i , item in enumerate(lista):
    print(i,item)

#tambem funciona para strings
#neste caso eu estou printando apenas o indice
for i, item in enumerate('Eu me amo mais que tudo'):
    print(i)

#serve tambem para range
for i, item in enumerate(range(10)):
    print(i,item)
