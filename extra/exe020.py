#sorteando uma lista
from random import shuffle 
aluno1 = str(input("Primeiro aluno: "))
aluno2 = str(input("Segundo aluno: "))
aluno3 = str(input("Terceiro aluno: "))
lista = [aluno1, aluno2, aluno3]
shuffle(lista)
print("A ordem de apresentação será {}".format(lista))