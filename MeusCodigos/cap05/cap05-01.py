#classes são a estrutura basica
#que representa o tipo do objeto
#o objeto é nada mais que uma instancia 
#da classe, que possue caracteristicas proprias

#criando minha primeira classe
class Livro():
    #este metodo vai inicializar cada objeto criado a partir desta classe
    #o nome deste metodo é __init__
    #(self) é uma referencia a cada atributo de um objeto criado a partit desta classe. 

    def __init__(self):
        #o self indica quais são os atributos de cada objeto.
        self.titulo = 'Harry Potter'
        self.isbn = 9988888
        print("Contrutor chamado para criar um objeto desta classe")

    def imprime(self):
        #metodo são funções, qie rece,e, cp,p ára,etrp atributos do objeto criado
        print("foi criado o livro %s e ISBN %d" %(self.titulo, self.isbn))

livro1 = Livro()    

type(livro1)

#atributo do livro1
livro1.titulo
livro1.isbn
livro1.imprime()

#segunda classe 
class LivroNovo():
    def __init__(self, titulo, isnb):
        self.titulo = titulo
        self.isnb = isnb
        print("Construtor chamado para criar um objeto desta classe")
        
    def imprime(self,titulo,isbn):
        print("Estre é o livro %s e ISBN %d" %(titulo, isbn))

livro2 = LivroNovo("Alice no Pais das Maravilhas", 77885598)

livro2.titulo
livro2.imprime(livro2.titulo, livro2.isnb)

#criando uma nova classe 
class Cachorro():
    def __init__(self, raca):
        self.raca = raca
        print("objeto criado com sucesso !")

rex = Cachorro(raca='Labrador')
lady = Cachorro(raca='Pincher')

rex.raca
lady.raca