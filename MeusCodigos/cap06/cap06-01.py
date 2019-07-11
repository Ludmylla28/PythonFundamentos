#Criando um banco de dados SQLite 

#Função para remover um arquino no banco de dados SQLite 
nomeDB = 'C:/Users/Ludy/Documents/PythonFundamentos/MeusCodigos/cap06/escola.db'

import os 
os.remove(nomeDB) if os.path.exists(nomeDB) else None 
BASE_DIR = os.path.dirname(os.path.abspath(nomeDB))
db_path = os.path.join(BASE_DIR, "escola.db")
#Importando o modulo do SQLite
import sqlite3

#Criando uma conexão com o banco de dados 
#Se ele não não existe será criado agora 
con = sqlite3.connect(db_path)

#Validando o tipo do banco
#print('con : ', type(con))

#Criando um cursor
#O cursor permite que você percorra todos os registros em um cunjunto de dados
cur = con.cursor()

#Validando o tipo do cursor 
#print('cur : ', type(cur))

#Criando uma instrução em sql 
sql_create = 'CREATE TABLE cursos'\
    '(id integer primary key,'\
    'titulo varchar(100),'\
    'categoria varchar(140))'

#Executando a função de criação no cursor 
cur.execute(sql_create)

#Criando outra sentenca sql para colocar outros registros 
sql_insert = 'INSERT INTO cursos VALUES (?, ?, ?)'

#Primeira remessa de dados
recset = [(1000, 'Ciencias de dados', 'Data Science'),
          (2000, 'Big Data', 'Analise de Dados'),
          (3000, 'Python Fundamentos', 'Analise de dados')]

#Inserindo os registros

for rec in recset:
    cur.execute(sql_insert,rec)

#Grava a Transação 
con.commit()

#Criando outra sentença SQL para selecinar registros
sql_select = 'SELECT * FROM cursos'

#Seleciona todos os registros e recupera os registros
cur.execute(sql_select)
dados = cur.fetchall()

#Mostra 
for linha in dados:
    print("Curso Id: %d, Titulo: %s, Categoria %s \n" %linha)
    
# Gerando outros registros 
# Aqui temos um dicionario dentro de uma lista 
recset = [(1003, 'Gestão de Dados com MongoDB', 'Big Data'),
          (1004, ' R Fundamentos', 'Analise de Dados')]

# Inserindo os registros
# Aqui temos um loop for, cuidado com a sintax 
for rec in recset:
    cur.execute(sql_insert,rec)

# Gravando a transação 
con.commit()

# Seleciona todos os registros 
cur.execute('select * from cursos')

# Recupera os resultados 
recset = cur.fetchall()

# Mostra
for rec in recset:
    print("Curso ID: %d, Titulo: %s, Categoria: %s \n" %rec)

# Fechar a Conexão
con.close()