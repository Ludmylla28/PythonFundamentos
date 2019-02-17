# Exercício 1 - Crie uma estrutura que pergunte ao usuário qual o dia da semana. 
# Se o dia for igual a Domingo ou igual a sábado, 
# imprima na tela "Hoje é dia de descanso", 
# caso contrário imprima na tela "Você precisa trabalhar!"

semana = "test"#int(input("Qual o dia da semana: \n(1)Segunda \n(2)Terça \n(3)Quarta \n(4)Quinta \n(5)Sexta \n"))
if (semana == 1):
    print("Que você tenha uma boa segunda-feira")
elif (semana == 2):
    print("A semana mal começou. Boa Terça")
elif (semana == 3):
    print("Metade da semana UHULL. Boa Quarta")
elif (semana == 4):
    print("A sexta esta chegando ai meu Deus. Boa Quinta")
elif (semana == 5):
    print("A semana ACABOU. Boa Sexta")
else:
    print("Não sei que dia é, estou perdido")

print("-" * 30)

# Exercício 2 - Crie uma lista de 5 frutas e verifique se a fruta 'Morango' faz parte da lista

mercado = ['banana', 'laranja', 'pera', 'morango', 'caju']
for i in mercado:
    if i == 'morango':
        print("Amo morango")

print("-" * 30)
# Exercício 3 - Crie uma tupla de 4 elementos, 
# multiplique cada elemento da tupla por 2 e guarde os resultados em uma lista

tupla1 = (1,2,3,4,5)
lista = []
for i in tupla1:
    multip = i *2
    lista.append(multip)
print(lista)

print("-" * 30)

# Exercício 4 - Crie uma sequência de números pares entre 100 e 150 e imprima na tela
for i in range(100,151,2):
    print(i)

print("-" * 30)

# Exercício 5 - Crie uma variável chamada temperatura e atribua o valor 40. 
# Enquanto temperatura for maior que 35, imprima as temperaturas na tela

temperatura = 40

while temperatura >35:
    print(temperatura)
    temperatura -= 1

print("-" * 30)

# Exercício 6 - Crie uma variável chamada contador = 0. 
# Enquanto counter for menor que 100, imprima os valores na tela,
# mas quando for encontrado o valor 23, interrompa a execução do programa

contador = 0 

while contador < 100:
    if contador == 23:
        break
    else:
        print("Numero",contador)
        contador += 1
print("-" * 30)

# Exercício 7 - Crie uma lista vazia e uma variável com valor 4. 
# Enquanto o valor da variável for menor ou igual a 20, 
# adicione à lista, apenas os valores pares e imprima a lista

listaVazia = []
num = 4

while num <= 20:
    listaVazia.append(num)
    num += 2
print(listaVazia)

print("-" * 30)
# Exercício 8 - Transforme o resultado desta função range em uma lista: range(5, 45, 2)

listaNova=[]

for i in range(5, 45, 2):
    listaNova.append(i)
print(listaNova)

print("-" * 30)

# Exercício 9 - Faça a correção dos erros no código abaixo e execute o programa. 
# Dica: são 3 erros.
temperatura = float(input('Qual a temperatura? '))
if temperatura > 30:
    print('Vista roupas leves.')
else:
    print('Busque seus casacos.')

print("-" * 30)

# Exercício 10 - Faça um programa que conte quantas vezes a letra "r" aparece na frase abaixo. 
# Use um placeholder na sua instrução de impressão

frase = "É melhor, muito melhor, contentar-se com a realidade; se ela não é tão brilhante como os sonhos, tem pelo menos a vantagem de existir." 
conter = 0

for i in frase:
    if i == 'r':
        conter += 1
print("o caracter r apareceu %s vezes na frase" %(conter))

