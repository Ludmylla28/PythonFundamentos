# jogo da forca 

import random

# palavras do jogo
board = ['''
>>>>>>>>>>> JOGO DA FORCA <<<<<<<<<<<<<
     +---+
     |   |
         |
         |
         |
         |
     =========
''','''
     +---+
     |   |
     O   |
         |
         |
         |
     ========= 
''','''
     +---+
     |   |
     O   |
     |   |
         |
         |
     ========= 
''','''
    +---+
    |   |
    O   |
   /|   |
        |
        |
   ==========
''','''
    +---+
    |   |
    O   |
   /|\  |
        |
        |
   ==========
''','''
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
   ==========
''','''
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
   ==========
''','''
>>>>>>>>>>>>>>> VOCÊ MORREU <<<<<<<<<<<<<<<
''']

# Estrutura do jogo  
class Forca :
     # Método construtor
     def __init__(self,palavra):
          self.palavra = palavra
          self.letra_pedida = []
          self.letra_adivinhada = []
     
     # Métoro para adivinhar a letra
     def adivinhar(self,letra):
          if letra in self.palavra and letra not in self.letra_adivinhada:
               self.letra_adivinhada.append(letra)
          elif letra not in self.palavra and letra not in self.letra_pedida:
               self.letra_pedida.append(letra)
          else:
               return False
          return True
     
     # Método para verificar se o jogo terminou
     def forca_acabou(self):
          return self.forca_ganhou() or (len(self.letra_pedida) == 6)
     
     # Método para verificar de o jogador venceu 
     def forca_ganhou(self):
          if '*' not in self.esconder_letra():
               return True
          return False
     
     # Método para não mostrar a letra no board
     def esconder_letra(self):
          rtn = ''
          for i in self.palavra:
               if i not in self.letra_adivinhada:
                    rtn += '*'
               else:
                    rtn += i
          return rtn

     
     # Método para checar o status do game e imprimir o board na tela
     def print_game_status(self):
          print(board[len(self.letra_pedida)])
          print('\nPalavra: ' + self.esconder_letra())
          print('\nLetras erradas: ',)
          for letra in self.letra_pedida:
               print(letra,)
          print()
          print('Letras corretas: ',)
          for letra in self.letra_adivinhada:
               print(letra,)
          print()
     
# Função para ler uma palavra de forma aleatoria do banco de palavras
def palavra_random():
     arquivoPalavras = "C:/Users/Ludy/Documents/PythonFundamentos/MeusCodigos/cap05/lab03/palavrasJogo.txt" 
     with open (arquivoPalavras,"rt") as f:
          bank = list(f)
          palavraDoJogo = random.choice(bank)
          palavraDoJogo = palavraDoJogo.strip('\n')
     return palavraDoJogo

# Função matriz - Execução do Programa
def main():
     
     # Variaveis de textos
     venceu = "\nURULLL Você venceu."
     perdeu = "\n^_^ Fim do jogo. Você perdeu"
     mostra_palavra = "\nA palavra era "
     pedido = "\nDigite uma letra: "

     # Objeto
     game = Forca(palavra_random()) 

     # Enquanto o jogo não tiver terminado, print do status solicita uma letra
     # e faz a leitura do caracter
     while not game.forca_acabou():
          game.print_game_status()
          user_input = input(pedido)
          game.adivinhar(user_input)
     
     # Verificação de status do jogo
     game.print_game_status()

     # De acordo com o status, imprime mensagem na tela para o usuario

     
     if game.forca_ganhou():
          print(venceu)
     else:
          print(perdeu)
          print(mostra_palavra + game.palavra)

# Executando o programa 
if __name__ == "__main__":
     main()