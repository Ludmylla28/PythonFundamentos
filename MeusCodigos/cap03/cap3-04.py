# Range, o ultimo numero é exclusivo 
for i in range(50, 101, 2):
    print(i)

print("-" * 30)

for i in range(3,6):
    print(i)

print("-" * 30)

for i in range(0, -20, -2):
    print(i)

print("-" * 30)

lista = ['mogango', 'banana', 'abacaxi', 'chuchu']
lista_tamanho = len(lista)

for i in range(0, lista_tamanho):
    print(lista[i])
    
print("-" * 30)

print(type(range(0,3)))