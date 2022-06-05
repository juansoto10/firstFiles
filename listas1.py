# ***LISTAS Y MUTABILIDAD***

# Secuencia de objetos -mutable-.
# Cuando se modifica una lista pueden surgir efectos secundarios (side effects).
#  Cuando se muta una estructura de datos como una lista tendríamos una posible fuente de posibles bugs en el programa (hay que darle manejo a estos detalles).
# Para modificar una lista podemos asignar vía índice (my_list[0] = 5) o utilizar los métodos de las listas(append, pop, remove, insert, etc.)


# my_list = [1, 2, 3] **Lista original

# print(my_list[0]) --> 1
# print(my_list[1:]) --> [2, 3]
# my_list.append(4) --> [1, 2, 3, 4]

# Para modificar lo que está en el índice 0:
# my_list[0] = 'a'
# print(my_list) ---> ['a', 2, 3, 4]

# my_list.pop() --> 4  Elimina el último elemento.
# print(my_list) --> [1, 2, 3]


# *EFECTOS SECUNDARIOS*

# Suponiendo que creo una lista -a- y otra -b- a la que le asigno el valor de -a-:
# a = [1, 2, 3]
# b = a
# id(a) --> 136962733760256
# id(b) --> 136962733760256;  es decir, los IDs están apuntando al mismo lugar, son la misma lista para Python.
# En el momento que se desee agregar un elemento a la lista -a- por ejemplo (a.append(5)), dicho elemento se agregaría también en la lista -b- por los side effects mencionados previamente.


# Se puede hacer una lista de listas(usando las listas inmediatamente anteriores e ignorando el cambio agregado a las mismas):
# c = [a, b]
# print(c) --> [[1, 2, 3], [1, 2, 3]]


# *CLONACIÓN*

# Nos ayuda a evitar side effects.
# Casi siempre es mejor clonar una lista que modificarla.
# Para clonar una lista podemos usar -slices- o la función -list-.


# a = [1, 2, 3]
# Si hacemos p.ej. <b = a>;  Esto nos dejaría estas dos listas asociadas al mismo ID, como vimos previamente.

# Para evitar esos efectos secundarios:
# c = list(a)

# Otra forma de hacerlo es:
# d = a[::] 
# print(d) --> [1, 2, 3]

# Ahora, a pesar de tener el mismo valor, las listas se guardan en diferentes objetos de memoria (distintos ID | -id(d)- p.ej.) y al modificarlas no vamos a sufrir (xd) los efectos secundarios que mencionamos anteriormente.


# *LIST COMPREHENSION*

# Una forma concisa de aplicar operaciones a los valores de una secuencia.
# También se pueden aplicar condiciones para filtrar.


# my_list = list(range(10)) --> Lista un rango del 0 al 9.

# Si queremos duplicar los valores de la lista p. ej.:

# double = [i * 2 for i in my_list]
# print(double) --> [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]


# Si por ejemplo solo queremos que muestre los números pares:

# pares = [i for i in my_list if i % 2 == 0]
# print(pares) --> [0, 2, 4, 6, 8]
# Si queremos sacar el 0 habría que hacer los ajustes respectivos (and, or).