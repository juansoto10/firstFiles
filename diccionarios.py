# ***DICCIONARIOS***

# Son como listas, pero usan llaves en lugar de índices.
# No tienen orden interno.
# Son mutables.
# Pueden iterarse


my_dictionary = {
    'Claudia': 48,
    'Juan': '24',
    'Luis': 59,
    'Zuri': 23,
}

print(my_dictionary['Juan'])
print(my_dictionary['Luis'])

# Cuando queremos buscar por llave en un diccionario y no sabemos si esa llave existe y queremos evitar un error:

# P. ej. buscamos una llave que en este caso no existe:
# my_dictionary.get('Arturo', 30) --> 30 ; retornaría el mismo número que ingresamos.

# my_dictionary.get('Juan', 30) --> 24 ; daría el valor de la llave Juan que SÍ existe en este caso.


# *Para reasignar un valor*

# my_dictionary['Juan'] = 25 ; reasigna el valor de la llave existente.


# *Para crear una nueva llave*

# my_dictionary['Amanda'] = 67 --> Me agregaría al dicc. la llave -Amanda- con valor 67.


# *Para borrar una llave*

# del my_dictionary['Amanda'] --> Me sacaría la llave Amanda del dicc.


# *PARA ITERAR EN UN DICCIONARIO*

# Se puede iterar a lo largo de las llaves, los valores o ambos al tiempo.

for llave in my_dictionary.keys():
    print(llave)

for valor in my_dictionary.values():
    print(valor)

for llave, valor in my_dictionary.items():
    print(llave, valor)

print('Luis' in my_dictionary)  # --> True

print('Miguel' in my_dictionary)  # --> False