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

##gravando arquivos
arq = open('C:/Users/ludmy/Documents/FCD/PythonFundamentos/CodigosDSA/Cap04/Notebooks/arquivos/arquivo1.txt',"w")

#colocando algo no documento
arq.write("Aprendendo python")

arq.close()

#lendo o arquivo
arq1 = open('C:/Users/ludmy/Documents/FCD/PythonFundamentos/CodigosDSA/Cap04/Notebooks/arquivos/arquivo1.txt',"r")

print(arq1.read())