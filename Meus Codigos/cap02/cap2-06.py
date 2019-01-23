## Tuplas 
# Criando uma tupla 

tupla = ("ludy", 22, "luana", 12)

#printando a tupla 
print(tupla)

#pegando só o primeiro numero
print(tupla[0])

#vendo qual o tamanho 
print(len(tupla))

#pegando os dois ultimos numeros da tupla
print(tupla[2:])

#convertendo tupla em lista 
lista_tu = list(tupla)

#adicionar uma valor na tupla/lista
lista_tu.append("Luan")

#convertendo a lista em tupla 

t1 = tuple(lista_tu)

print(t1)