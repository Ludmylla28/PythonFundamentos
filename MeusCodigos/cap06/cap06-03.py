# Inserindo dados com variaveis 

# Importanto os modulos a serem usados no codigo 

import sqlite3 as sql
import random as rd
import time 
import datetime as dt
import os 

# Criando variaveis gerais 
nomeDB = 'C:/Users/Ludy/Documents/PythonFundamentos/MeusCodigos/cap06/dsa.db'
nomeTB = 'Produtos'
nova_data = dt.datetime.now()
valor_random = rd.randrange(50,100)
produtos = ['teclado', 'mouse', 'notebook', 'bateria']


# Validando a existencia deste dataset e caso exista é para exclui-lo 
if os.path.exists(nomeDB):
    os.remove(nomeDB)
else:
    None

# Criando uma conexão 
con = sql.connect(nomeDB)

# Criando o cursor 
c = con.cursor()

# Função para criar uma tabela 
def criar_tabela(nomeTB):
    c.execute('CREATE TABLE IF NOT EXISTS nomeTB (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, date TEXT, prod_name TEXT, valor REAL)')

# Função para inserir uma linha 
def inserindo_info(nomeTB, produtos, valor_random, nova_data):
    for prodt in produtos:
        c.execute('INSERT INTO nomeTB (date, prod_name ,valor) VALUES (?, ?, ?)',(nova_data, prodt ,valor_random ))
        con.commit()

# Função para mostrar as informações no banco de dados 
def mostrar_info(nomeTB):
    # Vendo o que tem dentro do Banco de Dados 
    sql_select = 'SELECT * FROM nomeTB'
    c.execute(sql_select)
    dados = c.fetchall()

    # Mostra 
    for linha in dados:
        print(linha)

# Executando Funções 
criar_tabela(nomeTB)
inserindo_info(nomeTB,produtos,valor_random,nova_data)
mostrar_info(nomeTB)