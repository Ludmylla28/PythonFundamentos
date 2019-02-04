#lista de escolhidos (randomica)
from random import choice
aluno1 = str(input("Primeiro aluno: "))
aluno2 = str(input("Segundo aluno: "))
aluno3 = str(input("Terceiro aluno: "))
lista = [aluno1, aluno2, aluno3]
print("O aluno escolhido foi {}".format(choice(lista)))