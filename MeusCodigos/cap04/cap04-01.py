#abrindo um arquivo
arquivo1 = open('C:/Users/ludmy/Documents/FCD/PythonFundamentos/CodigosDSA/Cap04/Notebooks/arquivos/arquivo1.txt',encoding='utf8')
# lendo um arquivo
print(arquivo1.read())

#contando a quantidade de caracteres
print(arquivo1.tell())

#retornando para o inicio do arquivo
print(arquivo1.seek(0,0))

#lendo apenas os 10 primeirs caracteres
print(arquivo1.read(10))

print("-" * 100)

##gravando arquivos
arq = open('C:/Users/ludmy/Documents/FCD/PythonFundamentos/CodigosDSA/Cap04/Notebooks/arquivos/arquivo1.txt',"w",encoding='utf8')

#colocando algo no documento
arq.write("Aprendendo python junto com a DSA. Foco no futuro")

arq.close()

print("-" * 100)

#lendo o arquivo
arq1 = open('C:/Users/ludmy/Documents/FCD/PythonFundamentos/CodigosDSA/Cap04/Notebooks/arquivos/arquivo1.txt',"r",encoding='utf8')

print(arq1.read())

print("-" * 100)

# acrescentando conteudo no doc
arq2 = open('C:/Users/ludmy/Documents/FCD/PythonFundamentos/CodigosDSA/Cap04/Notebooks/arquivos/arquivo1.txt',"a",encoding='utf8')
arq2.write(" pois quero dar um futuro melhor para meus filhos")
arq2.close()
arq2 = open('C:/Users/ludmy/Documents/FCD/PythonFundamentos/CodigosDSA/Cap04/Notebooks/arquivos/arquivo1.txt',"r",encoding='utf8')
print(arq2.read())

print("-" * 100)

## automatizando o processo de gravação 
#filename = input("Qual o nome do arquivo ?")
#filename = filename + ".txt"

#arq3 = open(filename, "a")
#texto = input("qual o conteudo do arquivo ? ")
#arq3.write(texto)

#arq3.close()
#arq3 = open(filename, "r")
#print(arq3.read())

print("-" * 100)

#abrindo um dataset 

f = open('C:/Users/ludmy/Documents/FCD/PythonFundamentos/CodigosDSA/Cap04/Notebooks/arquivos/salarios.csv',"r",encoding='utf8')
data = f.read()
rows = data.split('\n')
print(rows)

full_data = []

#dividindo o data set em colunas 

for row in rows:
    split_rows = row.split(",")
    full_data.append(split_rows)
    first_row = full_data[0]
print(full_data)

print("-" * 100)
# contando a quantidade de linhas 
count = 0
for i in full_data:
    count += 1
print(count)

print("-" * 100)
#contando a quantidade de colunas 
conta = 0 
for i in first_row:
    conta += 1
print(conta)

print("-" * 100)
## Gravando arquivos 
arquivo2 = open("C:/Users/ludmy/Documents/FCD/PythonFundamentos/CodigosDSA/Cap04/Notebooks/arquivos/teste.txt","r",encoding='utf8')
print(arquivo2.read())
print(arquivo2.read())

arquivo2.seek(0)

print("-" * 100)
#usando o loop for para ler um arquivo 
for line in open("C:/Users/ludmy/Documents/FCD/PythonFundamentos/tentando.txt", "r",encoding='utf8'):
    print(line)

print("-" * 100)

# importando um data set com Pandas
import pandas as pd 
file_name = "C:/Users/ludmy/Documents/FCD/PythonFundamentos/CodigosDSA/Cap04/Notebooks/arquivos/binary.csv"
df = pd.read_csv(file_name)
df.head()


arquivo3 = "C:/Users/ludmy/Documents/FCD/PythonFundamentos/CodigosDSA/Cap04/Notebooks/arquivos/salarios.csv"
df2 = pd.read_csv(arquivo3)
df2.head() 

