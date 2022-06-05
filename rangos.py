# ***RANGOS***

# Representan una secuencia de enteros.
# Range(comienzo, fin, pasos)
# Son inmutables al igual que los strings y las tuplas.
# Eficientes en uso de memoria y normalmente usados en -for loops-.


# my_range = range(1, 5)
# print(type(my_range)) --> <class 'range'>

# for i in my_range:
#     print(i) --> 1 2 3 4 5 (El display sería distinto -vertical- dado que está dentro de un for)


# my_range = range(0, 7, 2)
# my_other_range = range(0, 8, 2)  Los dos rangos aquí mostrados nos muestran la misma secuencia de números.

# print(my_range == my_other_range) --> True

# *Value equality*
# id(my_range) --> 140319906077984 p.ej.
# id(my_other_range) --> 140319906077936 p.ej. 
# Esto muestra que en memoria se almacenan en lugares distintos a pesar de que su contenido es practicamente el mismo (el límite superior o -fin- no se incluye nunca en los rangos y otros objetos que usen especificaciones parecidas como cuando trabajamos con listas).


# To check object equality (not value equality):
# print(my_range is my_other_range) --> False
# Because they are not the same objects despise they have the same content.