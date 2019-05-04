# zip 

# criando uma lista
x = [1,2,3]
y = [4,5,6]

# perceba que zip retorna tuplas. 
# Neste caso, uma lista de tuplas

list(zip(x,y))

#atenção quando as sequencias tiverem tamanhos 
# diferentes eles a lista zip é do tamanho da menor 

list(zip('abcd','xy'))

#criando uma lista 
a = [1,2,3]
b = [4,5,6,7,8]

list(zip(a,b))

# criando 2 dicionarios 
d1 = {'a':1,'b':2}
d2 = {'c':3,'d':4}

# o zip vai unir as chaves 
list(zip(d1,d2))

# o zip pode unir a chave de um dicionario 
# com o valor do outro
list(zip(d1,d2.values()))

# criando uma função pra 
# trocar os valores do dicionario
def trocarValores(d1, d2):
    dicTemp = {}

    for d1key , d2val in zip (d1, d2.values()):
        dicTemp[d1key] = d2val

    return dicTemp

trocarValores(d1,d2)
