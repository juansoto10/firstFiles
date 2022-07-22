# ***PRUEBAS DE CAJA DE CRISTAL***

# Se basan en el flujo del programa.
# Prueba todos los caminos posibles de una función. Ramificaciones, bucles for y while, recursión.
# Se usa en Regression testing o mocks.

# EJEMPLO 1

import unittest


def es_mayor_de_edad(edad):
    if edad >= 18:
        return True
    else:
        return False


class PruebaDeCristalTest(unittest.TestCase):
    
    def test_es_mayor_de_edad(self):
        edad = 20

        resultado = es_mayor_de_edad(edad)

        self.assertEqual(resultado, True)

    def test_es_menor_de_edad(self):
        edad = 15

        resultado = es_mayor_de_edad(edad)

        self.assertEqual(resultado, False)


if __name__ == '__main__':
    unittest.main()

# Nos saldría en consola algo como esto: {
# ..
# ---------------------------------------------------
# Ran 2 tests in 0.000s

# OK
# }


# EJEMPLO 2

# import unittest


# def es_mayor_de_edad(edad):
#     if edad >= 18:
#         return False  # Cambiamos 'accidentalmente' el True a False para provocar un error.
#     else:
#         return False


# class PruebaDeCristalTest(unittest.TestCase):
    
#     def test_es_mayor_de_edad(self):
#         edad = 20

#         resultado = es_mayor_de_edad(edad)

#         self.assertEqual(resultado, True)

#     def test_es_menor_de_edad(self):
#         edad = 15

#         resultado = es_mayor_de_edad(edad)

#         self.assertEqual(resultado, False)


# if __name__ == '__main__':
#     unittest.main()

# En este caso nos saldría un error: AssertionError: False != True por el error de poner en ambos casos de la función False.