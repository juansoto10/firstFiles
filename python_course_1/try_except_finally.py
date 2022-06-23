import math

# (1)

def palindrome(string):
    return string == string[::-1]


try:
    print(palindrome(1))
except TypeError:
    print('Numbers are not allowed')

# --> Please type a string


# (2)

def palindrome_2(string):
    try:
        if len(string) == 0:
            raise ValueError('Empty strings are not allowed')
        return string == string[::-1]
    except ValueError as ve:
        print(ve)
        return False


try:
    print(palindrome_2(''))
except TypeError:
    print('Numbers are not allowed')

# --> 
# Empty strings are not allowed
# False

# Finally is used when we want to close a file and several other uses with files. Se ejecuta SIEMPRE, haya sido lanzada la excepción o no haya sido lanzada.

def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


try:
    num = int(input('Type a number: '))
    if num < 0:
        raise ValueError('Negative numbers are not allowed')
    if num == 0:
        raise ValueError('The number 0 has infinite divisors')
    # if isinstance(num, str):
    #     raise ValueError('Only numbers are allowed')

    print(divisors(num))
    print(':::My program has ended:::')
except ValueError as ve:
    print(ve)