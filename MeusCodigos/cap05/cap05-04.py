#neste documento aprenderemos sobre herança

#criando a classe animal - mãe
class Animal():
    def __init__(self):
        print("Animal Criado")

    def Identif(self):
        print("Animal")
    
    def Comer(self):
        print("Comendo")

#criando a classe cachorro - filha
class Cachorro(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Objeto Cachorro criado")
    
    def Identif(self):
        print("Cachorro")
    
    def latir(self):
        print("Au Au!")

rex = Cachorro()
rex.Identif()
rex.Comer()
rex.latir()
