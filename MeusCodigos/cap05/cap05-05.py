#estudando metodos especiais

#criando a classe livros
class Livros():
    def __init__(self, titulo, autor, paginas):
        print("Livro criado")
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
    
    def __str__(self):
        return "Titulo: %s, autor: %s, %s paginas"\
            %(self.titulo, self.autor, self.paginas)

    def __len__(self):
        return self.paginas
    
    def len(self):
        return print("Paginas do livro:", self.paginas)

tituloLivro = "Harry Potter e a Pedra Filosofal"
autorLivro = "J.K. Rouling"
paginasLivro = 500
livro1 = Livros(tituloLivro,autorLivro,paginasLivro)

#metodo especial 
print(livro1)
len(livro1)
livro1.len()

#quando executa o comando del ele apaga um atributo
#assim como o comando livro1.__delattr__("paginas")
del livro1.paginas
hasattr(livro1,"paginas")
