#Reduce 
#tambem recebe 2 paremetros (função, sequencia)
#aplica a função passada como parametro 
#aos elementos da sequencia ate que resta apenas um elemento 

#importando modulo reduce 
from functools import reduce

#criando uma lista
lista = [22,12,12,43,45]
print(lista)

#criando uma função 
def soma(a,b):
    x = a + b 
    return x
#usando a função reduce
reduce(soma,lista)

#apredentando diagrama de como funciona o reduce
from IPython.display import Image
Image('C:/Users/ludmy/Documents/FCD/PythonFundamentos/CodigosDSA/Cap04/Notebooks/arquivos/reduce.png')

#novo reduce usando lambda
lst = [40,28,22,30]

reduce(lambda x,y: x+y, lst)

#criando função lambda
achar_maximo = lambda a,b: a if (a > b) else bin

#vendo o tipo da variavel
type(achar_maximo)

# executando a função reduce 
reduce(achar_maximo, lst)
