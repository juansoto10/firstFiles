import os
import sys
import ast
import random
from random import randint

# Usar list comprehensions
# Manejo de errores 
# Manejo de archivos
# Usar el archivo data.txt para obtener las palabras
# Crear un selector de lenguaje xd
# Limpiar la pantalla y usar los módulos importados
# ¿Qué es keyboardInterrupt?


TERMINAL_SIZE = os.get_terminal_size()
columns = TERMINAL_SIZE.columns
rows = TERMINAL_SIZE.lines
VERSION = '1.0'
forbidden = ["_", "-", "\\", "/", "|", "+", "*", "{", "}", "[", "]", "=", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "", "@", "!", ",", ".", ";", ":", "#", "$", "%", "^", "&", "~", "`", "?", "'"]


# ------------- Sprites

GAME_TITLE = """██╗░░██╗░█████╗░███╗░░██╗░██████╗░███╗░░░███╗░█████╗░███╗░░██╗
██║░░██║██╔══██╗████╗░██║██╔════╝░████╗░████║██╔══██╗████╗░██║
███████║███████║██╔██╗██║██║░░██╗░██╔████╔██║███████║██╔██╗██║
██╔══██║██╔══██║██║╚████║██║░░╚██╗██║╚██╔╝██║██╔══██║██║╚████║
██║░░██║██║░░██║██║░╚███║╚██████╔╝██║░╚═╝░██║██║░░██║██║░╚███║
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝
                    by Juan Soto"""

SMALL_TITLE = """█░█ ▄▀█ █▄░█ █▀▀ █▀▄▀█ ▄▀█ █▄░█
█▀█ █▀█ █░▀█ █▄█ █░▀░█ █▀█ █░▀█
"""

HANGMAN_PICS = ['''  +---+
  |   |
      |
      |
      |
      |
=========''', '''  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

WIN_MESSAGE = '''        o    .   _     .
          .     (_)         o
   o      ____            _       o
  _   ,-/   /)))  .   o  (_)   .
 (_)  \_\  ( e(     O             _
 o       \/' _/   ,_ ,  o   o    (_)
  . O    _/ (_   / _/      .  ,        o
     o8o/    \\_/ / ,-.  ,oO8/( -TT
    o8o8O | } }  / /   \Oo8OOo8Oo||     O
   Oo(""o8"""""""""""""""8oo""""""")
  _   `\`'                  `'   /'   o
 (_)    \                       /    _   .
      O  \           _         /    (_)
o   .     `-. .----<(o)_--. .-'
   --------(_/------(_<_/--\_)-----------
'''

LOSE_MESSAGE = """                             Z             
                       Z                   
        .,.,        z           
      (((((())    z             
     ((('_  _`) '               
     ((G   \\  |)                 
    (((`   " ,                  
     .((\.:~:          .--------------.    
     __.| `"'.__      | \\              |     
  .~~   `---'   ~.    |  .             :     
 /                `   |   `-.__________)     
|             ~       |  :             :   
|                     |  :  |              
|    _                |     |   [ ##   :   
 \\    ~~-.            |  ,   oo_______.'   
  `_   ( \) _____/~~~~ `--___              
"""

alphabet = {
    'a': '▄▀█\n█▀█',
    'b': '█▄▄\n█▄█',
    'c': '█▀▀\n█▄▄',
    'd': '█▀▄\n█▄▀',
    'e': '█▀▀\n██▄',
    'f': '█▀▀\n█▀░',
    'g': '█▀▀\n█▄█',
    'h': '█░█\n█▀█',
    'i': '░█░\n░█░',
    'j': '░░█\n█▄█',
    'k': '█▄▀\n█░█', 
    'l': '█░░\n█▄▄',
    'm': '╔╗╗\n║║║',
    'n': '▄▄▄\n█ █',
    'o': '█▀█\n█▄█',
    'p': '█▀█\n█▀▀',
    'q': '█▀█\n▀▀█',
    'r': '█▀█\n█▀▄',
    's': '█▀░\n▄█░',
    't': '▀█▀\n░█░',
    'u': '█░█\n█▄█',
    'v': '█░█\n▀▄▀',
    'w': '║║║\n╚╝╝',
    'x': '▀▄▀\n█░█',
    'y': '█▄█\n░█░',
    'z': '▀█░\n█▄░'
}


# ------------- Colors:

def color(color, string):
    color_list = ['purple', 'cyan', 'blue', 'green', 'yellow', 'red']
    if color == '':
        color = random.choice(color_list)
    if color == 'purple':
        style = '\033[95m'
    elif color == 'cyan':
        style = '\033[96m'
    elif color == 'blue':
        style = '\033[94m'
    elif color == 'green':
        style = '\033[92m'
    elif color == 'yellow':
        style = '\033[93m'
    elif color == 'red':
        style = '\033[91m'
    elif color == 'bold':
        style = '\033[1m'
    elif color == 'underline':
        style = '\033[4m'
    return style + string + '\033[0m' 

help_message = f"""{color('bold', "HANGMAN Game, created by Juan Soto")} {color('blue', "@juansoto10")}
Version: {VERSION}
This is an open source project: https://github.com/juansoto10/hangman_game
{color('bold', "hangman -p")}: Play a Hangman Game.
{color('bold', "hangman -h")}: Show the help message.
{color('bold', "hangman -c")}: Will make some config changes.
{color('bold', "hangman -l language")}: Show the word list.
{color('bold', "hangman -a language word")}: Add a word to the word list.
{color('bold', "hangman -d language word")}: Delete a word from the word list."""



# def read():
#     list_of_words = []
#     with open('./files/list.txt', 'r', encoding='utf-8') as file:
#         for line in file:
#             list_of_words.append((line))
#     print(list_of_words)


def normalize():
    pass


def run():
    pass

    # versiones = dict(python = 2.7, zope = 2.13, plone = 5.1)

    # print(versiones)
    # print(versiones.get('plone'))
    # print(versiones.get('php'))

    # for i in range(11):
    #     print(i, end=', ')

    # my_string = 'Hola'
    # my_integer = 4

    # resultado = my_string * my_integer
    # print(resultado)

    # my_list = ['a', 'b']
    # my_list.append('c')
    # print(my_list)

    # my_string = 'hej jag ar en man'
    # print(my_string[0:3:2])

    # print(my_string.capitalize())

    # print(round(10.3456, 2))

    # words_list = ['Carlos', 'Maria', 'Sofia', 'Angela']
    # print(words_list)
    

if __name__ == '__main__':
    run()