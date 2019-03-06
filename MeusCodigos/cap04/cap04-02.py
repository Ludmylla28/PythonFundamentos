## Manipulando arquivo txt
#criando uma variavel e somando string
texto = "Vamos estudar mais um pouco,"
texto = texto + "pois a minha missão é comprar 2 editoras."
texto += "\n Ou juntar 2 milhões em investimentos, e 1 milhão na poupança."
#printanto a variavel
print(texto)

#Abrindo o arquivo com o os
import os 
arquivo = open(os.path.join("C:/Users/ludmy/Documents/FCD/PythonFundamentos/CodigosDSA/Cap04/Notebooks/arquivos/cientista.txt"),"w")
#salvando cada palavra por vez no documento
for palavras in texto.split():
    arquivo.write(palavras + " ")
arquivo.close()

#Abrindo arquivo para leitura
arquivo = open("C:/Users/ludmy/Documents/FCD/PythonFundamentos/CodigosDSA/Cap04/Notebooks/arquivos/cientista.txt","r")
conteudo = arquivo.read()
arquivo.close()
print(conteudo)

print("-" *100)

## usando a expressão with para ler o conteudo
with open("C:/Users/ludmy/Documents/FCD/PythonFundamentos/CodigosDSA/Cap04/Notebooks/arquivos/cientista.txt","r") as doc :
    conteudo = doc.read()

print(len(conteudo))

print("-" *100)

## usando with para escrever o conteudo
texto = "Ai que loucuda" 
texto += " quero estudar mais e mais" 

with open("C:/Users/ludmy/Documents/FCD/PythonFundamentos/CodigosDSA/Cap04/Notebooks/arquivos/cientista.txt","a") as doc:
    doc.write(texto[:10])
    doc.write('\n')
    doc.write(texto[:30])
    doc.close()

with open("C:/Users/ludmy/Documents/FCD/PythonFundamentos/CodigosDSA/Cap04/Notebooks/arquivos/cientista.txt","r") as doc:
    conteudo = doc.read()
    doc.close()

print(conteudo)

print("-" *100)

# manipulando arquivo csv com o with
import csv 

with open("C:/Users/ludmy/Documents/FCD/PythonFundamentos/CodigosDSA/Cap04/Notebooks/arquivos/numeros.csv","w") as doc:
    writer = csv.writer(doc)
    writer.writerow(('primeiro','segundo','terceiro'))
    writer.writerow((55,56,57,58))
    writer.writerow((20,21,22,23))
    doc.close()

with open("C:/Users/ludmy/Documents/FCD/PythonFundamentos/CodigosDSA/Cap04/Notebooks/arquivos/numeros.csv","r") as doc:
    leitor = csv.reader(doc)
    for x in leitor:
        print("Numero da coluna", len(x))
        print(x)
print("-" *100)
## gerando uma lista com dados do arquivo csv
with open("C:/Users/ludmy/Documents/FCD/PythonFundamentos/CodigosDSA/Cap04/Notebooks/arquivos/numeros.csv","r") as doc:
    leitor = csv.reader(doc)
    dados = list(leitor)
print(dados)

for linha in dados[1:]:
    print(linha)
print("-" *100)
### Manipulando arquivos json

#criando um dicionario 
dict = {'nome': 'Jorge Silva',
'linguagem': 'Python', 
'similar': ['c', 'Modula-3', 'lisp'],
'Users': 3000000}

for k,v in dict.items():
    print(k,v)

#importando o pacote
import json 

#convertendo o dicionario em um objeto json
json.dumps(dict)

#criando um arquivo json
with open("C:/Users/ludmy/Documents/FCD/PythonFundamentos/CodigosDSA/Cap04/Notebooks/arquivos/documento.json","w") as doc:
    doc.write(json.dumps(dict))
    doc.close()

with open("C:/Users/ludmy/Documents/FCD/PythonFundamentos/CodigosDSA/Cap04/Notebooks/arquivos/documento.json","r") as doc:
    texto = doc.read()
    data = json.loads(texto)

print(data)

print(data['nome'])
print("-" *100)
## Documento json importado da internet

from urllib.request import urlopen

response = urlopen("http://vimeo.com/api/v2/video/57733101.json").read().decode('utf8')
data = json.loads(response)[0]

print('Titulo :', data['title'])
print('URL :', data['url'])
print('Duração :', data['duration'])
print('Numeração de Visualisações :', data['stats_number_of_plays'])


## copiando conteudo de um arquivo para outro
import os 

arquivo_fonte = "C:/Users/ludmy/Documents/FCD/PythonFundamentos/CodigosDSA/Cap04/Notebooks/arquivos/documento.json"
arquivo_destino = "C:/Users/ludmy/Documents/FCD/PythonFundamentos/CodigosDSA/Cap04/Notebooks/arquivos/json_data.txt"

#método 1 
with open(arquivo_fonte,'r') as infile:
    text = infile.read()
    with open(arquivo_destino,'w') as onfile:
        onfile.write(text)

#método 2 
open(arquivo_destino,'w').write(open(arquivo_fonte,'r').read())

#leitura de arquivo json
with open("C:/Users/ludmy/Documents/FCD/PythonFundamentos/CodigosDSA/Cap04/Notebooks/arquivos/json_data.txt",'r') as doc:
    texto = doc.read()
    data = json.loads(texto)

print(texto)
print(data)

