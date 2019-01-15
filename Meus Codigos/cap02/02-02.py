var_teste = 2
print(var_teste)

print(type(var_teste))

#Declaração multipla

pessoa1,pessoa2,pessoa3 = "Ludmylla", "Luan", "Luana"

print(pessoa1)
print(pessoa2)

#variavel não começa com numero e nem com as palavras reservadas
# A ordem dos operadores é a mesma seguida na Matemática

## calculo com variavel 
peso = float(input("Qual o seu peso? "))
altura = float(input("Qual a sua altura? "))
altura2 = altura * altura
imc = peso/ altura2
imcIdeal = 22 * altura2

print("Seu peso atual é {} e seu imc é {}, porem seu peso ideal é {}".format(peso, imc, imcIdeal))

#Concatenação de Variáveis
nome = "Ludmylla Bianca "
sobrenome = "da Silva"
print(nome + sobrenome)