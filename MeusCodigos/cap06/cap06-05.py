# Update e Delete de dados 
# Importando modulos necessarios 

import sqlite3 as sql 
import os 
import random as rdm
import time 
import datetime as dtm
import matplotlib.pyplot as plt


# Variaveis Globais 
nomeDB = '/home/ludmylla/Documents/PythonFundamentos/MeusCodigos/cap06/dsaUpdat.db'
nomeTab = 'CasaNova'
produtos = ['fogão', 'geladeira', 'mesa', 'sofa', 'cadeira']

# Validando se ja existe o banco de dados 
if os.path.exists(nomeDB):
    os.remove(nomeDB)
else:
    None

# Criando conexão e cursor
con = sql.connect(nomeDB)
c = con.cursor()

# Criando funções para manipulação de dados
def criando_tabela(nomeTab):
    c.execute('CREATE TABLE IF NOT EXISTS nomeTab (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,'\
        'date TEXT, '\
        'prod_name TEXT,'\
        'valor REAL)')

def inserir_dados(nomeTab, produtos):
    c.execute("INSERT INTO nomeTab (date,prod_name,valor) VALUES (?, ?, ?)", (dtm.datetime.now(),produtos,rdm.randrange(50,200)))
    con.commit()

def lendo_todos_dados(nomeTab):
    c.execute("SELECT * FROM nomeTab")
    for linha in c.fetchall():
        print(linha)

def lendo_coluna(nomeTab):
    c.execute("SELECT * FROM nomeTab")
    for i in c.fetchall():
        print(i[3])

def atualizando_doc(nomeTab):
    c.execute("UPDATE nomeTab SET valor = 70.00 WHERE valor = 80.00")
    con.commit()

def delete_doc(nomeTab):
    c.execute("DELETE FROM nomeTab WHERE valor = 70.00")
    con.commit()

# Função para criação de grafico
def criando_graficos(nomeTab):
        c.execute("SELECT id, valor FROM nomeTab")
        ids = []
        valores = []
        dados = c.fetchall()
        for i in dados:
                ids.append(i[0])
                valores.append(i[1])
        plt.bar(ids,valores)
        plt.show()

# Executando as funções 
criando_tabela(nomeTab)
for prod in produtos :
    inserir_dados(nomeTab,prod)
    time.sleep(1)
lendo_todos_dados(nomeTab)
lendo_coluna(nomeTab)
atualizando_doc(nomeTab)
delete_doc(nomeTab)
criando_graficos(nomeTab)