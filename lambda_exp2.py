def build_quadratic_function(a, b, c):
    """Returns the function f(x) = ax^2 + bx +c"""
    return lambda x: a*x**2 + b*x + c

# f = build_quadratic_function(2, 3, -5)
# print(f(0)) #This returns the quadratic function evaluated (using a=2, b=3, c=-5 and <x=0>).

print(build_quadratic_function(3, 0, 1)(2)) # Returns 3x^2 + 1 evaluated for x=2.