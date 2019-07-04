#Criando um banco de dados SQLite 

#Função para remover um arquino no banco de dados SQLite 
nomeDB = 'escola.db'

import os 
os.remove(nomeDB) if os.path.exists(nomeDB) else None 

#Importando o modulo do SQLite
import sqlite3

#Criando uma conexão com o banco de dados 
#Se ele não não existe será criado agora 
con = sqlite3.connect(nomeDB)

#Validando o tipo do banco
type(con)

#Criando um cursor
#O cursor permite que você percorra todos os registros em um cunjunto de dados
cur = con.cursor()

#Validando o tipo do cursor 
type(cur)

#Criando uma instrução em sql 
sql_create = 'create table cursos'\
    '(id integer primary key,'\
    'titulo varchar(100),'\
    'categoria varchar(140))'

#Executando a função de criação no cursor 
cur.execute(sql_create)

#Criando outra sentenca sql para colocar outros registros 
sql_insert = 'insert into cursor values(?,?,?)'

#Primeira remessa de dados
recset = [(1000, 'Ciencias de dados', 'Data Science'),
          (2000, 'Big Data', 'Analise de Dados'),
          (3000, 'Python Fundamentos', 'Analise de dados')]

#Inserindo os registros
for rec in recset:
    cur.execute(sql_insert, rec)