# ***AFIRMACIONES***

# Para determinar si una función se cumple y poder seguir adelante con la ejecución de un programa o parar dicha ejecución.
# Programación defensiva.
# Pueden utilizarse para verificar que los tipos sean correctos en una función
# También sirven para debuggear.

# *ESTRUCTURA*

# assert <expresion booleana>, <mensaje de error>

# EJEMPLO 1

# def primera_letra(lista_de_palabras):
#     primeras_letras = []

#     for palabra in lista_de_palabras:
#         assert type(palabra) == str, f'{palabra} no es str'
#         assert len(palabra) > 0, 'No se permiten str vacíos'

#         primeras_letras.append(palabra[0])

#     return primeras_letras


# familia = ['Juan', 12, '', 'Claudia', 'Luis', 'Zuri', 'Amanda', 'Arturo', 'Monica', 'Miguel', 'Edwin', 'Camilo',]

# print('Las primeras letras de estas palabras son: ', primera_letra(familia))


# EJEMPLO 2
# *De esta manera le damos mejor manejo y podemos visualizarlo mejor*

def primera_letra(lista_de_palabras):
    primeras_letras = []
    
    for palabra in lista_de_palabras:
        try:
            assert type(palabra) == str, f'{palabra} no es str'
            assert len(palabra) > 0 , 'No se permiten str vacíos'
            primeras_letras.append(palabra[0])
        except AssertionError as e:
            print(e)

    return primeras_letras


familia = ['Juan', 12, '', 'Claudia', True, 'Luis', 'Zuri', 'Amanda', 'Arturo', 'Monica', 'Miguel', 'Edwin', 'Camilo', False,]

print('Las primeras letras (válidas) de estas palabras son: ', primera_letra(familia))

# d = type('Juan') is bool
# print(d)


