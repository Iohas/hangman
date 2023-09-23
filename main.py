import random
from os import system, name

letras_erradas = []
def limpa_tela():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def display_hangman(chances):

    stages = [
        """
            ---------
            |       |
            |       0----
            |      \\|/
            |      / \\   
            _       
        """,
        """
            ---------
            |       |
            |       0
            |      \\|/
            |      /   
            _       
        """,
        """
            ---------
            |       |
            |       0
            |      \\|/
            |      
            _       
        """,
        """
            ---------
            |       |
            |       0
            |       |/
            |      
            _       
        """,
        """
            ---------
            |       |
            |       0
            |       |
            |      
            _       
        """,
        """
            ---------
            |       |
            |       0
            |       
            |      
            _       
        """,
        """
            ---------
            |       |
            |       
            |       
            |      
            _       
        """,
        print("\n        Letras erradas:", " ".join(letras_erradas))
    ]
    return stages[chances]

def game():

    score = 0

    while True:
        letras_erradas.clear()
        limpa_tela()
        print("\nBem vindo ao jogo da forca")
        print(" Advinhe a palavra abaixo\n")

        palavras = ['abacate', 'banana', 'caju', 'damasco', 'embu', 'figo', 'groselha', 'jaca', 'kiwi', 'laranja']

        palavra = random.choice(palavras)

        letras_palavras = [letra for letra in palavra]

        tabuleiro = ["_"] * len(palavra)

        chances = 6


        letras_tentativas = []

        while chances > 0:
            print(display_hangman(chances))
            print("Palavra:", tabuleiro)
            print("\n")

            tentativa = input("      Digite uma letra: ")

            if tentativa in letras_tentativas:
                print("\nVocê já tentou essa letra antes, tente outra.\n")
                continue

            letras_tentativas.append(tentativa)

            if tentativa in letras_palavras:

                for indice in range(len(letras_palavras)):
                    if letras_palavras[indice] == tentativa:
                        tabuleiro[indice] = tentativa
                if "_" not in tabuleiro:
                    print("\n   Voce venceu a palavra era: {}".format(palavra))
                    score += 1
                    break
            else:
                print("Essa letra nao esta na palavra")
                letras_erradas.append(tentativa)
                chances -= 1

        if "_" in tabuleiro:
            print(display_hangman(0))
            print("\nVoce perdeu, a palavra era: {}".format(palavra))

        play_again = input("\n   Deseja jogar novamente? (s/n): ").lower()
        if play_again != 's':
            print("   Voce finalizou o jogo com %d pontos" %score)
            break

if __name__ == "__main__":
    game()

