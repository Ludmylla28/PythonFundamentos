#Tratativa de erro é uma das partes importantes de um sistema 

# Erro 
print('ola')

# Erro
def numdiv(num1,num2):
    resultado = num1/num2
    print(resultado)

numdiv(4,0)

# try, except, finally

#Erro
print(8 + 's')

#usando try e except  para tratar o erro
try: 
    print(8+'s')
except TypeError:
    print('Esta operação não é permitida')

#tentando gravar um documento e ja tratando o erro
try:
    f = open('C:/Users/ludmy/Documents/FCD/PythonFundamentos/CodigosDSA/Cap04/Notebooks/arquivos/testandoerros.txt','w')
    f.write('gravando no arquivo')
except IOError: 
    print('Erro: Arquivo não encontrado ou não pode ser salvo')
else:
    print('conteudo gravado com sucesso!')
    f.close()

#tratando um erro 
try:
    f = open('C:/Users/ludmy/Documents/FCD/PythonFundamentos/CodigosDSA/Cap04/Notebooks/arquivos/testandoerros','r')
except IOError:
    print('erro: arquivo não encontrado ou não pode ser lido')
else:
    print('conteudo gravado com sucesso!')
    f.close()

#tratando outro erro
def numero():
    try:
        val = int((input("Digite um numero: ")))
    except UnboundLocalError: 
        print("Você não digitou um numero!")
    finally:
        print("Obrigado!")
    print(val)

print(numero())