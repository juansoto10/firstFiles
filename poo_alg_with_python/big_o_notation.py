# Ley de la suma

#Ej. 1

def f(n):
    for i in range(n):
        print(i)

    for i in range(n):
        print(i)

# --> O(n) + O(n) = O(n + n) = O(2n) = O(n)


#Ej. 2

def g(n):
    for i in range(n):
        print(i)

    for i in range(n * n):
        print(i)

# --> O(n) + O(n * n) = O(n + n**2) = O(n**2)


# Ley de la multiplicación

#Ej. 3

def h(n):
    for i in range(n):
        for j in range(n):
            print(i, j)

# --> O(n) * O(n) = O(n * n) = O(n**2)


# Recursividad múltiple

#Ej. 3

def fibonacci(n):
    if n == 0 or n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)

# --> O(2**n)