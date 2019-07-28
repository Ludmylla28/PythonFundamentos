# Importando os modulos 
import sqlite3 as sql
import random as rd 
import time as tm 
import datetime as dt 

# Variaveis Globais
nomeDB = 'C:/Users/Ludy/Documents/PythonFundamentos/MeusCodigos/cap06/dsaSelect.db'
nomeTab = 'produtos'
#nova_data = dt.datetime.now()
#novo_valor = rd.randrange(50,150)
novo_produto = ['geladeira', 'fogão', 'maquina', 'cama', 'colchão', 'sofá']


# Criando uma conexão 
con = sql.connect(nomeDB)

# Criando cursos 
c = con.cursor()

# Função para criar uma tabela 
def criando_tabela(nomeTab):
    c.execute('CREATE TABLE IF NOT EXISTS nomeTab (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, date TEXT, prod_nome TEXT, valor REAL)')

# Função para criar dados 
def inserindo_dados(nomeTab, novo_produto):
    for prod in novo_produto:
        c.execute('INSERT INTO nomeTab (date,prod_nome, valor) VALUES (?,?,?)',(dt.datetime.now(), prod, rd.randrange(50,150)))
        con.commit()

# Função para ler todos os dados 
def leitura_todos_dados(nomeTab):
    c.execute('SELECT * FROM nomeTab')
    for linha in c.fetchall():
        print(linha)

# Função para leitura de um registro especifico 
def leitura_registro(nomeTab):
    c.execute('SELECT * FROM nomeTab WHERE valor > 60.0')
    for linha in c.fetchall():
        print(linha)

# Função para ler uma coluna
def leitura_coluna(nomeTab):
    c.execute('SELECT * FROM nomeTab')
    for linha in c.fetchall():
        print(linha[3])

# Função para fechar a conexão 
def fechar_conexao():
    c.close()
    con.close()

# Executando todas as funções 
criando_tabela(nomeTab)
inserindo_dados(nomeTab,novo_produto)
leitura_todos_dados(nomeTab)
leitura_registro(nomeTab)
leitura_coluna(nomeTab)
fechar_conexao()