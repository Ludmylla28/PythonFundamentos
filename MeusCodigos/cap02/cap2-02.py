var_teste = 1 
print(var_teste)

# Se a variavel não foi definida dara erro
# print(my_var)

var_teste = 2 

print(var_teste)
print(type(var_teste))

x = 22 
print(x)

## Declaração multipla 

pessoa1, pessoa2, pessoa3 = "Luan", "Luana", "Ludmylla"

print(pessoa1)
print(pessoa2)
print(pessoa3)

# Fique atenta python é case-sensitive 
# Não mude ao colocar letra maiuscula e depois minuscula para chamar ela
# Pode colocar nomero na variavel mas não no começo 
# Não podemos usar palavras reservadas como nome de variavel 

## Variavel atribuindo outra variavel 
# É possivel fazer operações com variaveis 

peso = 63
altura = 1.58
altura2 = altura * altura 
imc = peso / altura2
imcIdeal = 21.7

print (imc)
print (imcIdeal * altura2)

## Concatenação de variaveis 

nome = "Ludmylla Bianca"
sobreNome = "Silva"

nomeCompleto = nome + " " + sobreNome

print(nomeCompleto)