if 5 > 2:
    print("Eu consegui") 

if 5 < 2:
    print("uuuuuhhhhhhh")
else:
    print("acho")

print(5 > 3)
print(6 == 4)
print(1 < 2)

## condicional aninhada 

idade = 22
nome = "Ludy"

# Com a "condicional" and = e, então se for ... e ... faça ...
if (nome == "Ludy") and (idade == 22):
    print("Olá ludy")
else:
    print("OPA ... Quem é você ?")

# Condicional só aninada
if idade > 18:
    if nome == "Ludy":
        print("URULL você de volta")
    else:
        print("hummmm você é novo")

# Condicional com o or = ou, então se for ... ou se for ... faça ...
if (idade < 10) or (nome == "bla"):
    print("prazer em te conhecer")
else:
    print("bla bla bla pra você")

## ELIF 
dia = "Terça"

if dia == "Segunda":
    print("Hoje fara sol")
elif dia == "Terça":
    print("Hoje é Terça-Feira")
else:
    print("Hoje é dia de beber")

## mais de um tipo de condicional

materia = input("Qual sua materia preferida= ")
notaFinal = int(input("Digite uma nota entre 0 e 10= "))

if materia == "geografia":
    print("você é louco(a)")
elif (materia == "matematica") and (notaFinal <= 6):
    print("que fantastico")
elif (materia == "matematica") and (notaFinal >= 7):
    print("você é otimo nisso") 
else:
    print("hummm que confuso")

