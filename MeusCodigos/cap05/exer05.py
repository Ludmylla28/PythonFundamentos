# Exercício 1 - Crie um objeto a partir da classe abaixo, 
# chamado roc1, passando 2 parâmetros e depois faça uma chamada
# aos atributos e métodos
from math import sqrt

class Rocket():
     
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def move_rocket(self, x_increment=0, y_increment=1):
        self.x += x_increment
        self.y += y_increment
        
    def print_rocket(self):
        print(self.x, self.y)

teste1 = Rocket(22,32)
teste1.x
teste1.y
teste1.print_rocket()
teste1.move_rocket(43,45)
teste1.print_rocket()

# Exercício 2 - Crie uma classe chamada Pessoa() com 
# os atributos: nome, cidade, telefone e e-mail. 
# Use pelo menos 2 métodos especiais na sua classe. 
# Crie um objeto da sua classe e faça uma chamada a 
# pelo menos um dos seus métodos especiais

class Pessoa():
    def __init__(self, nome,cidade,telefone,email):
        self.nome = nome
        self.cidade = cidade
        self.telefone = telefone
        self.email = email
        print("Olá %s, prazer em te receber" %(self.nome))
    
    def __str__(self):
        return "Candidato(a) " + self.nome + " mora na cidade " + self.cidade

candidato1 = Pessoa("Carolina Franco de Oliveira", "Osasco", 950855005, "carolbatera@gmail.com")
str(candidato1)

# Exercício 3 - Crie a classe Smartphone com 2 
# atributos, tamanho e interface e crie a classe 
# MP3Player com os atributos capacidade. 
# A classe MP3player deve herdar os atributos da 
# classe Smartphone.

class Smartphone():
    def __init__(self, tamanho, interface):
        self.tamanho = tamanho
        self.interface = interface
        print("Produto identificado")

class MP3Player(Smartphone):
    def __init__(self,capacidade, tamanho = '15 cm', interface = 'Led'):
        self.capacidade = capacidade
        Smartphone.__init__(self,tamanho,interface)

    def printMP3Player(self):