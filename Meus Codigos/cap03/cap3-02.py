# usando um loop for simples. 
tp = ("ludy", "luan", "luana")
for i in tp:
    print(i)

print("-" * 30)

listaMercado = ["peixe", "tomate", "ervilha"]
for i in listaMercado:
    print(i)

print("-" * 30)

# imprimir valores de 0 a 22 menos o ultimo 
for contador in range(0,22):
    print(contador)

print("-" * 30)

# imprimindo os numeros pares 
listaNumerica = [1,2,3,4,5,6,7,8,9]
for i in listaNumerica:
    if i % 2 == 0:
        print(i)

print("-" * 30)

# imprimimindo numeros pares de 0 a 100 
for i in range(0,100,2):
    print(i)

print("-" * 30) 

#strings tambem são sequenciais
for caracter in "eu amo a familia que eu tenho.":
    print(caracter)

print("-" * 30)

# loop aninhado 
for i in range(0,5):
    for a in range(0,5):
        print(a)

print("-" * 30)

# tentativa de entender o range com o loop
for i in range(0,3):
    print("quero ser rica")

print("-" * 30)

## operando os valores em uma lista com o loop
listaB = [45,43,22,12,12,5]
soma = 0

for i in listaB:
    dobro = i * 2
    soma += dobro

print(soma)

print("-" * 30)

# contando os itens de uma lista 
count = 0

for i in listaB:
    count += 1

print(count)

print("-" * 30)

#pesquisa em lista com loop 
for i in listaB:
    if i == 5:
        print("EURECA EU ACHEI")

print("-" * 30)

# listando chaves de um dicionario
dicio = {"k1": 3, "k2": 1, "k3":2}

for item in dicio:
    print(item)

print("-" * 30)

#imprimindo chave e valor usando o metodo items()
for k,v in dicio.items():
    print(k,v)

