# definindo uma função 
def primeiraFunc():
    print("hello word")

print("-" * 30)

#printando a função
primeiraFunc()

def segundaFunc(nome):
    print("hello %s" %(nome))

segundaFunc("Ludy")

print("-" * 30)

#brincando com uma função
import random
livros = ["Harry Potter", "Crepusculo", '50 tons de cinza', "Alice no pais das maravilhas"]

def proximoLivro():
    sorteio = random.choice(livros)
    print("O proximo livro a ser lido será ... %s" %(sorteio))

proximoLivro()
## deu certo =) 

print("-" * 30)

#nova funcão 
def funcNumeros():
    for i in range(0,8):
        print("Numero " + str(i))

funcNumeros()

print("-" * 30)

##função para somar os numeros
def addNum(primeiroN, segundoN):
    print("Primeiro numero: " + str(primeiroN))
    print("Segundo numero: " + str(segundoN))
    print("A soma é: ", primeiroN + segundoN)

#chamando a função
addNum(43, 22)

print("-" * 30)

### VARIAVEIS LOCAIS E GLOBAIS
## variavel global
var_global = 10 #essa é uma variavel global

def multiply(num1, num2):
    var_global = num1 * num2 #essa é uma variavel local
    print(var_global)

multiply(
    num1 = int(input("Fale um numero de 0 a 10: ")),
    num2 = int(input("Fale outro numero de 0 a 10: "))
)

print(var_global)

print("-" * 30)

### FUNÇÃO BUILT-IN
print(abs(-22))
print(bool(0))
print(bool(1))

print("-" * 30)

### Função str, int, float
idade = int(input(" Me informe sua idade: "))

if idade > 18:
    print("Seja bem vindo a Afirma Net")
else:
    print("Hummm acho melhor estudar um pouco mais.")

print("-" * 30)

print(int("23"))
print(float("23"))
print(str(23))
print(len([2,25,36]))

array = ["a", "b", "c"]
print(max(array))
print(min(array))

lista1 = [22,43,2]
print(sum(lista1))

print("-" * 30)

## Criando funções usando outras funções
import math

def numPrimo(num):
    if (num % 2) == 0 and num > 2:
        return "este numero não é primo"
    for i in range(3,int(math.sqrt(num)) + 1, 2):
        if (num % i) == 0:
            return "este numero não é primo"
    return "este numero é primo"

numPrimo(541)


print("-" * 30)

### fazendo split dos dados

def split_string(text):
    return text.split(" ")

texto = str(input("o que você acha sobre a temperatura ? "))

# isso divide a string em uma lista
print(split_string(texto))

# atribuindo o output de uma função para uma variavel

token = split_string(texto)
print(token)

print("-" * 30)


# função com numero variavel de argumentos
def printVarInfo(arg1, *vartuple ):
    print("O parâmetro passado foi: ", arg1)

#imprimindo cada valor do segundo argumento
    for item in vartuple:
        print("O parâmetro passado foi: ", item)
    return;

printVarInfo(10)
printVarInfo('chocolate', 'laranja', 'banana', 'tomate')