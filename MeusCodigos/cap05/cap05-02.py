#em python tudo é objeto

#criando uma lista
lst_num = ["Data", "Science", "Academy", "Nota", 10]

#aqui eu verifico o tipo do objeto 
type(lst_num)

lst_num.count(10)

#criando uma classe 
class Carro(object):
    pass

palio = Carro()
print(type(palio))

# Criando uma nova classe
class Estudantes:
    def __init__(self, nome, idade, nota):
        self.nome= nome
        self.idade= idade
        self.nota= nota

estudante1 = Estudantes("Carolina Franco de Oliveira", 32, 8.7)

print("Bom dia %s, sua nota é %d" %(estudante1.nome,estudante1.nota))
estudante1.idade

#criando uma classe 
class Funcionario:
    def __init__(self,nome,salario):
        self.nome = nome
        self.salario = salario
    def listFunc(self):
        print("O nome do funcionário é " + self.nome + " e o salário é R$" + str(self.salario))

#input só da pra ser usado quando no teste de da um F5
#no caso de dar shift + enter ele não funciona
#nome1 = str(input('Qual o nome do funcionario? '))
#salario1 = float(input('Quanto será o salario dele?? R$'))

funcio1 = Funcionario("Ludmylla Bianca",15000)
funcio1.listFunc()

#usando atribitos

hasattr(funcio1, "nome")
hasattr(funcio1, "idade")
setattr(funcio1, "idade", 22)
getattr(funcio1, "idade")