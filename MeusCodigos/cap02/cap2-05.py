#isso é uma lista 
familia = ["luan", "luana", "lady", "dulci", "emerson"]
print(familia)

#isso é um dicionario
familiaIdade = {"Luan": 12, "Luana": 12, "lady": 5, "Dulcy": 43, "Emerson": 45 }
print(familiaIdade)

print(familiaIdade["lady"])

#limpar dicionario
familiaIdade.clear()
print(familiaIdade)

#deletar o dicionario 
del familiaIdade

#criando novo dicionario
estudante = {"Aline": 1, "Amanda": 2, "Bruna": 3, "Bernardo": 4}
print(estudante)

#contando quantidade do dicionario
print(len(estudante))

#coletando apenas uma informação (key, value ou itens)
print(estudante.keys())
print(estudante.values())
print(estudante.items())

#criando novo dicionario 
estudantesNovos = {"Clarice": 5, "Denise": 6, "Ellena": 7, "Fernanda": 8}
print(estudantesNovos)

# Atualizando um dicionario usando outro dicionario 
estudante.update(estudantesNovos)
print(estudante)

# Inclui coisas no dicionario 
estudante["Giovanna"] = 9
print(estudante)

## Chave e valor podem ser iguais mas responderam de formas diferentes

# É possivel criar uma lista dentro do dicionario 

pessoas = {"familia": ["luan", "luana", "lady", "dulci", "emerson"], "trabalho": ["tiago", "felipe", "carol"]}
print(pessoas)

print(pessoas["familia"][1].upper())

# dicionarios aninhados 

dicio = {"key": {"key1": {"key2":[1,10,19,33,59]}}}
print(dicio["key"]["key1"]["key2"][1] - 2)
