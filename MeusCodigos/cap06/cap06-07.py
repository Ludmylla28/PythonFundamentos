#Criando um banco de dados mongodb

#Importando o modulo do pymongo 
# (lembrar de instalar o modulo)
from pymongo import MongoClient

#Conectando com o mongo local 
conn = MongoClient('localhost', 27017)

#Testando o tipo da variavel 
print(type(conn))

#Criando um banco de dados chamado "cadastrodb"
db = conn.cadastrodb 

#Testando o tipo da variavel
print(type(db))

#Criando a collection no mongo db
collection = db.cadastrodb

#Testando o tipo da variavel
print(type(collection))

#importando modulo
import datetime 

#criando um documento
post1 = {"codigo": "ID - 9987725",
         "prod_name": "Geladeira",
         "mascas":["brastemp","consul","eletrolux"],
         "data_cadastro": datetime.datetime.utcnow()}

print(type(post1))

collection = db.posts 
post_id = collection.insert_one(post1)

post_id.inserted_id

#criando um documento
post2 = {"codigo": "ID - 2823019",
         "prod_name": "Cama",
         "mascas":["madeira madeira","mobly","ortobom"],
         "data_cadastro": datetime.datetime.utcnow()}

post_id = collection.insert_one(post2).inserted_id

post_id

collection.find({"prod_name":"Geladeira"})

for post in collection.find():
    print(post)

db.name
db.collection_names()
