# Criando o Banco de Dados e Inserindo dados 

# Variael com o nome do dataSet
nomeDB = 'C:/Users/Ludy/Documents/PythonFundamentos/MeusCodigos/cap06/dsa.db'

# Importando o modulo do sistema operacional 
import os 

# Validando a existencia deste dataset e caso exista é para exclui-lo 
if os.path.exists(nomeDB):
    os.remove(nomeDB)
else:
    None

# Importando modulo SQLite3 
import sqlite3 as sql

# Criando uma conexão com o banco de dados 
conx = sql.connect(nomeDB)

# Criando um cursor 
c = conx.cursor()

# Função de criar uma tabela 
def criando_tabela():
    c.execute('CREATE TABLE IF NOT EXISTS pessoas (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, date TEXT,'\
        'prod_name TEXT, valor REAL)')

# Função de inserir dados 
def data_insert():
    c.execute("INSERT INTO pessoas VALUES (10, '2018-05-02 14:32:11', 'Teclado', 90 )")
    conx.commit()


# Executando a função de criar tabela
criando_tabela()

# Executando a função de inserir dados 
data_insert()

#vendo o que tem dentro do Banco de Dados 
sql_select = 'SELECT * FROM pessoas'
c.execute(sql_select)
dados = c.fetchall()

#Mostra 
for linha in dados:
    print(linha)

#fechando as conexões 
c.close()
conx.close()

