## Criando Listas 
listaMercado = ["ovos", "leite", "frango", "tempero", "farinha"]

print(listaMercado)

#printando cada item da lista 
item1 = listaMercado[1]
item2 = listaMercado[2]
item3 = listaMercado[3]

print(item1, item2, item3)

#atualizando um item da lista 
listaMercado[1] = "peixe"

print(listaMercado)

#Deletando um item da lista
## não é possivel deletar um item que não existe na lista 

del listaMercado[3]

print(listaMercado)

#criando listas dentro de listas (ou listas aninhadas)

listaRemedio = [[1,2,3,4], [5,6,9,8], [9,10,11,12]]

print(listaRemedio)

#selecionando uma lista da lista 

a = listaRemedio[1]
print(a)

#pregando um item da lista dentro da linta

b = a[2]
print(b)

#operações com listas 

print(listaRemedio)

##atribui a variavel qualquer item de qualquer lista 

l = listaRemedio[1][1]
print(l) 

f = l * listaRemedio[2][1]
print(f)


#Concatenando listas 

lista_1 = ["Pretel", "Carolina", "Ludmylla"]
lista_2 = ["Dulcineia","Emerson", "Luan", "Luana"]

print(lista_1 + lista_2)

#operador in 
## verifica se o numero ou item esta na lista 

print(10 in listaRemedio[2])
print(100 in listaRemedio[2])

print("Ludmylla" in lista_1)


#função built-in 

## a função len retorna o tamanho da lista
print(len(listaRemedio[0]))

## a função max retorna o maior valor da lista
print(max(listaRemedio[0]))

## a função min retorna o menor valor da lista
print(min(listaRemedio[0]))

## a função adiciona um item na lista 
lista_2.append("Lady")

print(lista_2)


## Criando uma lista vazia 
peixe = []

print(peixe)

# adicionando um item na lista vazia 
peixe.append("salmão")
peixe.append("sardinha")
peixe.append("atum")

print(peixe)

#criando outra lista vazia 
pratos = []
print(pratos)

##copiando os itens de uma lista pra outra 
for item in peixe:
    pratos.append(item)

print(pratos)

# conta quantos itens iguais aquele tem 
print(listaRemedio[0].count(1))

# adicionando varios itens na lista
pratos.extend(["lasanha", "pizza", "macarronada"])
print(pratos)

print(pratos.index("lasanha"))

# adicionando um iten na posição desejada da lista
pratos.insert(2,3)
print(pratos)

#remove um item da lista 
pratos.remove(3)
print(pratos)

#embaralha os itens da lista
pratos.sort()
print(pratos)

#reverte os itens da lista
pratos.reverse()
print(pratos)

