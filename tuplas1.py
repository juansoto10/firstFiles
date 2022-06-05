# TUPLAS

# Son inmutables
# Solo se puede REASIGNAR su valor.


# my_tuple = ()  Crea una tupla vacía.
# type(my_tuple)  Nos dice el tipo de dato.


# my_tuple = (1,)  Crea una tupla de un solo valor (debe tener la coma al final).


# my_tuple = (1,)
# my_other_tuple = (2, 3, 4)

# my_tuple += my_other_tuple  my_tuple quedaría reasignada con el valor de: (1, 2, 3, 4).


# Para desempaquetar tuplas:
# my_other_tuple = (2, 3, 4)
# x, y, z = my_other_tuple
# print(x) --> 2 
# print(y) --> 3
# print(z) --> 4 


# Cómo regresar varios valores de una función:
# def coordenadas():
#     return (5,4)

# x, y = coordenadas()
# print(x, y) --> 5 4
# print(x) --> 5
# print(y) --> 4
