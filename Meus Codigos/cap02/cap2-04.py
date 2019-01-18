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