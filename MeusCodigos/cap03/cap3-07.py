### Lambda

# uma função com 3 linhas de codigo

def potencia(num):
    result = num**2
    return result
potencia(5)

print("-" * 30)
# uma função com 2 linhas de codigo

def potencia1(num):
    return num**2
potencia1(5)

print("-" * 30)
# uma função com 1 linha de codigo
def potencia2(num): return num**2
potencia2(5)

#criando a primeira lambrida 
potencia3 = lambda num: num**2
potencia3(5)

#lambda para numero par
par = lambda x: x%2==0
par(3)
par(6)

#lambda para pegar a primera letra 
first = lambda s: s[0]
first('Ludy')

#função lambda para calculo
addNum = lambda x,y : x+y
addNum(6,2)