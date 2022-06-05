import random

IMAGES = ['''

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

words = 'hormiga babuino tejon murcielago oso castor camello gato almeja cobra pantera coyote cuervo ciervo perro burro pato aguila huron zorro rana cabra ganso halcon leon lagarto llama topo mono alce raton mula salamandra nutria buho panda loro paloma piton conejo carnero rata cuervo rinoceronte salmon foca tiburon oveja mofeta perezoso serpiente araña cigüeña cisne tigre sapo trucha pavo tortuga comadreja ballena lobo gallina cebra leopardo suricata oruga'.split()


def get_random_word(words_list):
    """Returns a random str from a list used as argument"""
    word_index = random.randint(0, len(words_list) - 1)
    return words_list[word_index]


# print(f'La palabra aleatoria es: {get_random_word(words)}')

def show_board(IMAGESS, wrong_char, right_char, secret_word):
    print(IMAGESS[len(wrong_char)])
    print()

    print('Letras incorrectas: ', end=' ')
    for character in wrong_char:
        print(character, end=' ')
    print()

    empty_spaces= '_' * len(secret_word)

    for i in range(len(secret_word)):
        if secret_word[i] in right_char:
            empty_spaces = empty_spaces[:i] + secret_word[i] + empty_spaces[i+1:]

    for character in empty_spaces:
        print(character, end=' ')
    print()

def get_the_try(tried_letters):
    """Returns the letter entered by the player and verify that the player has entered only one letter"""
    while True:
        print('Di una letra...')
        tries = input()
        tries = tries.lower
        tries_length = len(tries)
        if tries_length != 1:
            print('Por favor ingresa una letra...')
        elif tries in tried_letters:
            print('Ya has probado esa letra. Elige otra...')
        elif tries not in 'abcdefghijklmnñopqrstuvwxyz':
            print('Por favor ingresa una LETRA...')
        else:
            return tries


def play_again():
    """Returns True if the player wants to play again, otherwise returns False"""
    print('¿Quieres jugar de nuevo? (Responde -sí- o -no-)')
    return input().lower().startswith('s')


print('A H O R C A D O')
wrong_letters = ''
right_letters = ''
the_secret_word = get_random_word(words)
finished_game = False


while True:
    show_board(IMAGES, wrong_letters, right_letters, the_secret_word)
    
    intento = get_the_try(wrong_letters + right_letters)

    if intento in the_secret_word:
        right_letters += intento

        founded_all_letters = True
        for i in range(len(the_secret_word)):
            if the_secret_word[i] not in right_letters:
                founded_all_letters = False
                break
        if founded_all_letters:
            print(f'¡Así es! La palabra secreta es: {the_secret_word}. ¡Has ganado!')
            finished_game = True
        else:
            wrong_letters += intento

            if len(wrong_letters) == len(IMAGES) - 1:
                show_board(IMAGES, wrong_letters, right_letters, the_secret_word)
                print(f'Te has quedado sin intentos después de {str(len(wrong_letters))} intentos fallidos y {str(len(right_letters))} aciertos. La palabra era {the_secret_word}.')
                finished_game = True
        
        if finished_game:
            if play_again():
                wrong_letters = ''
                right_letters = ''
                finished_game = False
                the_secret_word = get_random_word(words)
            else:
                break
