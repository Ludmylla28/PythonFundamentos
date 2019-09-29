#Retornando dado do mongo com o pymongo 

#Importando pacotes necessarios 
import pymongo 
import datetime
import random as rd

#Conectando com o mongo local
client_con = pymongo.MongoClient()

#Verificando dataBases
client_con.database_names()

#Conectando com a conection
db = client_con.cadastrodb

#Vendo os nomes das collections
colection = db.collection_names()

#Criando uma collection 
if "mycollection" in colection:
        print("ta aqui")
else:
        db.create_collection("mycollection")

#Vendo os nomes das collections
db.collection_names()

def inserindo_documentos(titulo,tags):
    db.mycollection.insert_one({
    'titulo': titulo,
    'descricacao': 'Produto oferecido pela Afirmanet',
    'by': 'A firma Net',
    'url':'http://www.afirmanet.com.br',
    'tags':tags,
    'linkes': rd.randrange(50,100)
    })

def coletando_dados():
        print(list(db.mycollection.find()))

titulos = ['Web Site','Redes Socias','IA','Machine learning','Deep Learning']
tags = [['pagina','site'],['facebook','instagram','twitter'],
['Artificial inteligence','maquina inteligente'],['aprendizado de maquina','maquina aprendendo'],
['aprendizado profundo','maquina aprendendo sozinha']]

for i in titulos:
        inserindo_documentos(i,rd.choice(tags))

coletando_dados()
db.mycollection.remove({})