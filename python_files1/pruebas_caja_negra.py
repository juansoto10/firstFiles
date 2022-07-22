# ***PRUEBAS DE CAJA NEGRA***

# Se basan en la especificación de la función o el programa.
# Prueba inputs y valida outputs.
# Se usa en UNIT TESTING e INTEGRATION TESTING.


# EJEMPLO 1

# import unittest


# class CajaNegraTest(unittest.TestCase):

#     def test_suma_dos_positivos(self):
#         num_1 = 10
#         num_2 = 5

#         resultado = suma(num_1, num_2)

#         self.assertEqual(resultado, 15)


# if __name__ == '__main__':
#     unittest.main()


# En este primer ejemplo la consola nos mostraría un error: suma no está definido.

# Ahora, en el ejemplo 2 a propósito vamos a definir la función -suma- pero no vamos a poner nada más (solo un pass).


# EJEMPLO 2

# import unittest


# def suma():
#     pass


# class CajaNegraTest(unittest.TestCase):

#     def test_suma_dos_positivos(self):
#         num_1 = 10
#         num_2 = 5

#         resultado = suma(num_1, num_2)

#         self.assertEqual(resultado, 15)


# if __name__ == '__main__':
#     unittest.main()

# En este caso nos saldría un error: TypeError; suma() takes 0 positional arguments but 2 were given. Dado a que no escribí argumentos.


# EJEMPLO 3

# import unittest


# def suma(num_1, num_2):
#     pass


# class CajaNegraTest(unittest.TestCase):

#     def test_suma_dos_positivos(self):
#         num_1 = 10
#         num_2 = 5

#         resultado = suma(num_1, num_2)

#         self.assertEqual(resultado, 15)


# if __name__ == '__main__':
#     unittest.main()

# En este caso nos saldría un error: AssertionError: None != 15 dado que no definí ninguna operación en la función.


# EJEMPLO 4 (ciclo 4 del proceso más bien)

# import unittest


# def suma(num_1, num_2):
#     return num_1 + num_2


# class CajaNegraTest(unittest.TestCase):

#     def test_suma_dos_positivos(self):
#         num_1 = 10
#         num_2 = 5

#         resultado = suma(num_1, num_2)

#         self.assertEqual(resultado, 15)


# if __name__ == '__main__':
#     unittest.main()

# En este caso nos haría el test sin problema porque se cumple lo que esperábamos.
# Nos saldría en consola algo como esto: {
# .
# ---------------------------------------------------
# Ran 1 test in 0.000s

# OK
# }


# EJEMPLO 5

import unittest


def suma(num_1, num_2):
    return num_1 + num_2


class CajaNegraTest(unittest.TestCase):

    def test_suma_dos_positivos(self):
        num_1 = 10
        num_2 = 5

        resultado = suma(num_1, num_2)

        self.assertEqual(resultado, 15)

    def test_suma_dos_negativos(self):
        num_1 = -10
        num_2 = -7

        resultado = suma(num_1, num_2)

        self.assertEqual(resultado, -17)


if __name__ == '__main__':
    unittest.main()

# Nos saldría en consola algo como esto: {
# ..
# ---------------------------------------------------
# Ran 2 tests in 0.000s

# OK
# }
