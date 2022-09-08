palavra = "manga"

# ocultando a palavra com a quantidade de caracteres x _
palavra_oculta = [l for l in len(palavra) * '_']

#salvar as letras certas que o usuario digitou
tentativa_certa = []

#salvar letras erradas que o usuario digitou
tentativa_errada = []

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

print(palavra_oculta)
# palavra_oculta[0] = 'm'
# print(palavra_oculta)
# palavra_oculta[1] = 'a'
# print(palavra_oculta)

cont = 0
while cont < 7:
    if ''.join(palavra_oculta) != palavra:
        print(board[cont])
        print('\nPalavra: '+''.join(palavra_oculta))
        print('\nLetras erradas:')
        print(*tentativa_errada)
        print('\nLetras certas:')
        print(*tentativa_certa)
        letra = input('\nDigite uma letra: ')
        if letra in palavra:
            tentativa_certa.append(letra)
            for pos, caractere in enumerate(palavra):
                if letra == caractere:
                    palavra_oculta[pos] = letra
        else:
            tentativa_errada.append(letra)
            cont+=1
    else:
        print(' Parabens voce acertou a palavra!')
        break
else: 
    print(' Fim de Jogo, a palavra era: '+ palavra)