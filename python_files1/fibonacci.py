# In mathematics, the Fibonacci numbers, commonly denoted Fn, form a sequence, the Fibonacci sequence, in which each number is the sum of the two preceding ones. The sequence commonly starts from 0 and 1, although some authors omit the initial terms and start the sequence from 1 and 1 or from 1 and 2. Starting from 0 and 1, the next few values in the sequence are:[1]

# <0, 1>, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...


def fibonacci(n):
    """Calcula el número de fibonacci para una posición en particular -Las 2 primeras posiciones (0 y 1) no se cuentan como índices de la posición-

    n int > 0
    
    returns número fibonacci para posición n
    """
    print(n)
    if n == 0 or n == 1:
        return 1
    
    return fibonacci(n - 1) + fibonacci(n - 2)


n = int(input('Ingresa un número entero: '))

print(f'El número fibonacci para {n} es: {fibonacci(n)}')