#aqui vamos aprender metodos

#criando uma classe chamada Circulo
class Circulo():

    #o valor de pi é constante
    pi = 3.14

    #criando o metodo para definirmos o valor do raio (default)que será executado no inicio 
    def __init__(self, raio = 5):
        self.raio = raio
    
    # criando o metodo para calcular a area do circulo
    def area(self):
        return(self.raio * self.raio) * Circulo.pi
    
    #metodo para criar um novo raio
    def setRaio(self, novoRaio):
        self.raio = novoRaio

    #metodo para obter o raio do circulo 
    def getRaio(self):
        return self.raio

cir = Circulo()
cir.getRaio()
cir.area()

cir1 = Circulo(7)
cir1.getRaio()
cir1.area()
cir1.setRaio(3)

