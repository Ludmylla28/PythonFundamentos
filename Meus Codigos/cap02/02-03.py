nova = "A DSA é a melhor escola "
print(nova)

#retorna a primeira letra
print(nova[0])
print(nova[2])

#Retorna todos os elementos da string, começando pela posição (lembre-se que Python começa a indexação pela posição 0),
# até o fim da string.
print(nova[1:])

# le a ultima letra
print(nova[-1])

# le de traz pra frente 
print(nova[::-1])

#retorna de 2 em 2 
print(nova[::2])

#retorna tudo maiusculo 
print(nova.upper())

#retorna tudo minusculo 
print(nova.lower())

#retorna tudo espaçado 
print(nova.split())

#torna com a primeira maiuscula
print(nova.capitalize())

#conta a quantidade de caracteres iguais 
print(nova.count('a'))

#acha a posição da letra 
print(nova.find('m'))

#verifica se é apenas numero 
print(nova.isalnum())

# verifica se é só letra 
print(nova.isalpha())

#verifica se é tudo minusculo 
print(nova.islower())

#verifica se é só espaço 
print(nova.isspace())

#Verifica se termina com a letra ...
print(nova.endswith(' '))

#comparação de string 
velha = "eu amo minha mãe"

print(nova == velha)

print(nova == nova)