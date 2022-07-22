# ***MANEJO DE EXCEPCIONES***

# Son muy comunes en la programación. No son excepcionales xD.
# Las excepciones en Python normalmente se relacionan con errores de semántica.
# Se pueden crear excepciones propias.
# Cuando una excepción no se maneja (unhandled exception) el programa termina en error.
# Las excepciones se manejan con los keywords: try, except, finally.
# Se pueden utilizar para ramificar programas.
# No deben manejarse de manera silenciosa (por ejemplo, con print statements).
# Para crear tu propia excepción utiliza el keyword -raise-.


# EJEMPLO 1

# def divide_elementos_de_lista(lista, divisor):
#     return [i / divisor for i in lista]


# lista = list(range(10))
# divisor = 2

# print(divide_elementos_de_lista(lista, divisor))

# En este caso nos saldría en consola  --> [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5]


# EJEMPLO 2

# def divide_elementos_de_lista(lista, divisor):
#     return [i / divisor for i in lista]


# lista = list(range(10))
# divisor = 0

# print(divide_elementos_de_lista(lista, divisor))

# En este caso nos saldría en consola un error --> ZeroDivisionError: division by zero

# EJEMPLO 3 
# *Vamos a darle manejo al error anterior*

def divide_elementos_de_lista(lista, divisor):
    try:
        return [i / divisor for i in lista]
    except ZeroDivisionError as e:
        print(e)
        return lista


lista = list(range(10))
divisor = 0

print(divide_elementos_de_lista(lista, divisor))

# En este caso como pusimos un try - except y se ejecutó una división entre 0 al ejecutarse el programa nos muestra la lista sin alterar:
# --> division by zero
# --> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]