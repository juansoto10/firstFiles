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

welcome_message = '''
                      
'''


def read():
    list_of_words = []
    with open('./files/list.txt', 'r', encoding='utf-8') as file:
        for line in file:
            list_of_words.append((line))
    print(list_of_words)


def normalize():
    pass


def run():
    read()
    print(welcome_message)

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