# Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos

# Import
import random

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman:
    tentativa_certa = []
    tentativa_errada = []
    rodada = 0
    palavra_oculta = []
    # Método Construtor
    def __init__(self, word):
       self.word = word
       self.palavra_oculta = self.hide_word()

    # Método para adivinhar a letra
    def guess(self, letter):
        if letter in self.word:
            self.tentativa_certa.append(letter)
            for pos, char in enumerate(self.word):
                if letter == char:
                    self.palavra_oculta[pos] = letter
        else:
            self.tentativa_errada.append(letter)
            self.rodada+=1
            self.hangman_over()

    # Método para verificar se o jogo terminou
    def hangman_over(self):
        if '_' in (self.palavra_oculta) and self.rodada < 6:
            return False
        else:
            return True

    
    # Método para verificar se o jogador venceu
    def hangman_won(self):
        if self.word == ''.join(self.palavra_oculta):
            return True
        else:
            return False
 
    # Método para não mostrar a letra no board
    def hide_word(self):
        hided_word = [c for c in len(self.word) * '_']
        return hided_word

    # Método para checar o status do game e imprimir o board na tela
    def print_game_status(self):
        print(board[self.rodada])
        print('\nPalavra: '+''.join(self.palavra_oculta))
        print('\nLetras erradas:')
        print(*self.tentativa_errada)
        print('\nLetras certas:')
        print(*self.tentativa_certa)
        pass



# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
    with open("D:\\Temp\\PythonFundamentos\\Cap05\\Lab03\\palavras.txt", "rt") as f:
        bank = f.readlines()
    return bank[random.randint(0, len(bank)-1)].strip()


# Função Main - Execução do Programa
def main():

    # Objeto
    game = Hangman(rand_word())

    # Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
    while game.hangman_over()  == False:
        # Verifica o status do jogo
        game.print_game_status()
        letra = input('\nDigite uma letra: ').lower()
        game.guess(letra)
    
    

    # De acordo com o status, imprime mensagem na tela para o usuário
    if game.hangman_won():
        print('\nParabéns! Você venceu!!')
    else:
        print('\nGame over! Você perdeu.')
        print('A palavra era ' + game.word)

    print('\nFoi bom jogar com você! Agora vá estudar!\n')


# Executa o programa
if __name__ == "__main__":
    main()
