# Filter 
# tambem recebe uma função e uma sequencia 
# a função passada para a filter deve retornar true ou false
# a filter retornara apenas a lista com os verdadeiros 


#criando função 
def verificarPar(num):
    if num % 2 == 0:
        return True
    else:
        return False

# chamando a função 
verificarPar(30)

#criando uma lista 
lista = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(lista)

#usando uma filter
filter(verificarPar,lista)

list(filter(verificarPar,lista))

#verifica se é par
list(filter(lambda x: x%2==0, lista))

#verifica se é maior que 8
list(filter(lambda num: num>8, lista))