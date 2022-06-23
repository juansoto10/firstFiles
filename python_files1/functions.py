print(dir())
# --> ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']

def f():
    pass

print(f()) # --> None (Because whe have not defined nothing in the function)
print(f) # --> <function f at 0x7f1af2007d90>

print(dir()) # --> ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'f']
# Now -dir- includes the function 'f'.


# Now let's create a function that actually does something.

def ping():
    return 'Ping!'

print(ping()) # --> Ping!

# Since we did not assign this to a variable, Python printed it to the terminal. But we can also store the return value to a variable:
x = ping()
print(x) # --> Ping!

# If we call the directory function -dir- again we will see the function ping and the variable x listed:
print(dir()) # --> ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'f', 'ping', 'x']


# Example

import math
print(dir(math))
# --> ['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc', 'ulp']


def sphere_volume(r):
    """Returns the volume of a sphere with radius r."""
    v = (4.0/3.0) * math.pi * r**3
    return v


print(sphere_volume(2)) 
# --> 33.510321638291124


def triangle_area(b, h):
    """Returns the area of a triangle with base b and height h"""
    return 0.5 * b * h


print(triangle_area(3, 6))
# --> 9.0


# Functions in Python can accept another kind of arguments called "keyword arguments" f.i.:

def height_in_cm(feet = 0, inches = 0):
    """Converts a length from -ft- and -in- to -cm-."""

    feet_to_cm = feet * 12 * 2.54
    inches_to_cm = inches * 2.54
    
    return feet_to_cm + inches_to_cm


print(height_in_cm(feet = 5)) # --> 152.4 
print(height_in_cm(5)) # --> 152.4 (It's the same that previous line)
print(height_in_cm(5, 8)) # --> 172.72
print(height_in_cm(feet = 6, inches = 1)) # --> 185.42
print(height_in_cm(inches = 11, feet = 5)) # --> 180.34 (we can introduce the inputs in different order like this)

#Python also calls 'keyword arguments' -> 'default arguments'.


# When writing a function we can use both kind of arguments (keyword and required arguments). If we do this, the keyword arguments must come last. F.i.:

# def g(x = 0, y):
#     return x + y

# print(g())
# --> File "/home/juansoto23/personalProjects/firstFiles/python_files1/functions.py", line 77
#     def g(x = 0, y):
#                  ^
# SyntaxError: non-default argument follows default argument

# The correct way to do this is to list the non-default arguments first (required arguments -since they are required-).

def g(y, x = 0):
    return x + y

print(g(5)) # --> 5 (Note that if we do not provide a value for x, the default value is used)

# If we want to pass in a value for the keyword argument, then we must specify it by its name.
# Required arguments are not given a name. They are determined by their postition.