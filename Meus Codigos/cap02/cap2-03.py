## Indexando uma string 
s = 'ludy hoje gostaria de agradecer a você por ser essa pessoa tão maravilhosa que você é.'

print(s[0]+" de linda")
print(s[1]+" de unica")
print(s[2]+" de dedicada")
print(s[3]+" de yogurte")

print(s[:2])
print(s[-1])
print(s[:-1])
print(s[::-1])

#Multiplica a letra
letra = "w" 
print(letra*3)

#Deixa as letras maiusculas
print(s.upper())

#Deixa ad letrar minusculas
print(s.lower())

#Separa as palavras
print(s.split())

#Deixa a primeira letra maiuscula
print(s.capitalize())

#conta quantas parecidos tem
print(s.count('a'))

#Encontra a posição da letra 
print(s.find('p'))

#Verifica se tem so numero 
print(s.isalnum())

#Verifica se tem so letra
print(s.isalpha())

#Verifica se é minusculo
print(s.islower())

#Verifica se é espaço vaziu 
print(s.isspace())

#verifica se termina com determinada letra
print(s.endswith('.'))

## Comparação de string 
print("ludy" == "luana")
print("luana" == "luan")
