# Recursividad
# n! = n * (n - 1)!

def factorial(n):
    """Calcula el factorial de n.

    n int > 0
    returns n!
    """
    print(n)
    if n == 1: #se define el caso base
        return 1

    return n * factorial(n - 1)


n = int(input('Escribe un número entero: '))

print(factorial(n))
