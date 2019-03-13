# map é uma função built-in
# a programação funcinal é uma programação orientada a expressão
# map recebe 2 argumentos (função, sequencia)

#criando 2 funções
def fahen(T):
    return ((float(9)/5)*T +32)

def cels(T):
    return(float(5)/9)*(T-32)

#criando uma lista
temperatura = [0.0,35.8,30.2,28.0,12.6]

map(fahen,temperatura)
map(cels,temperatura)

list(map(fahen,temperatura))
list(map(cels,temperatura))

for x in map(fahen,temperatura):
    print(x)

#usando lambda com o map
list(map(lambda x : x**2, temperatura))

