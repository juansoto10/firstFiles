# class Snowflake:
#     pass

# flake = Snowflake()

# This list contains some but not all of the special methods and attributes that are available to use. Each one starts and ends with double underscores. F. e. The __eq__ special function is called when you compare two objects for equality. __setattr__ special function is called when you attach an attribute to an object.
# __dict__ is a special attribute, not a special function. It is the dictionary which contains all of the object attributes.

# The docstring is not put in the special dictionary, instead it is stored in a special attribute call __doc___

# print(dir(flake))

# --> ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']


# For instance:

# class Martian:
#     """Someone who lives on Mars"""

#     def __init__(self, fn, ln):
#         self.first_name = fn
#         self.last_name = ln

#     def __setattr__(self, name, value):
#         print(f'>>> You set {name} = {value}')  # Print a simple message to check when this method is called.
#         self.__dict__[name] = value  # To store the attributes in the dictionary __dict__.*1

#     def __getattr__(self, name):
#         print(f">>> Get the '{name}' attribute")  # Print a simple message to check when this method is called.
#         if name == 'full_name':
#             return f'{self.first_name} {self.last_name}'
#         else:
#             raise AttributeError(f'No attribute named {name}')



# ANOTHER WAY TO ADD ATTRIBUTES:

# m1 = Martian()
# m1.first_name = 'Juan'
# m1.last_name = 'Soto'
# print(m1.__dict__)

# This is where Python stores the docstring
# print(Martian.__doc__)

# m = Martian('Juan', 'Soto')


# We can add aditional attributes like in the first way, no matter that you have already added anothers attributes in the __init__ method.

# m.arrival_date = '2037-12-15'

# print(m.__dict__)

# Set and get attributes: When we define a __setattr__ special method we can see the name and values of our class.

# Because we wrote our own setattr method -we- are now responsible for storing attributes.*1


# __getattr__ special method: This method is called when you try to acces an attribute.

# print(f'First name = {m.first_name}')
# print(f'Last name = {m.last_name}')
# print(f'Arrival date = {m.arrival_date}')


# Note that if the attribute is found through the normal mechanism, 'getattr' is not called. This is an intentional asymmetry between 'getattr' and 'setattr'. This is done both for efficiency reasons and because otherwise 'getattr' would have no way to access other attributes of the instance.
# In other words, if all you need is the value of an attribute this special methos is not called. Instead python calls a different special method called '__getattribute__'. For nearly all cases the '__getattr__' method will suffice. 'getattr' special method is particularly useful for returning computed attributes.

# print(m.full_name)


#Finally let us try to access a non-existent attribute to see if an attribute error is raised:

# print(m.martian_name)*2

# This (*2) would return -->

# >>> Get the 'martian_name' attribute
# Traceback (most recent call last):
#   File "/home/juansoto23/personalProjects/firstFiles/python_files1/special_methods.py", line 74, in <module>
#     print(m.martian_name)
#   File "/home/juansoto23/personalProjects/firstFiles/python_files1/special_methods.py", line 33, in __getattr__
#     raise AttributeError(f'No attribute named {name}')
# AttributeError: No attribute named martian_name


# A more natural way to generate the full name would be to override the 'str' special method. This method is called when you convert an object to a string.
# First, let us reduce visual clutter by removing the print line inside the 'setattr' method.
# Now, create a Martian object. Print it and run!


# class Martian:
#     """Someone who lives on Mars"""

#     def __init__(self, fn, ln):
#         self.first_name = fn
#         self.last_name = ln

#     def __setattr__(self, name, value):
#         self.__dict__[name] = value  # To store the attributes in the dictionary __dict__.*1


# m = Martian('Rika', 'Furude')
# print(m)
# print(m.__str__())  # *3
# print(id(m))

# The output would be --> 

#<__main__.Martian object at 0x7f38e7c70550>
# <__main__.Martian object at 0x7f38e7c70550>
# 139882383476048

#This output is the string generated by a call to the special '__str__' method. It displays the object type and the c Python memory address. You can also get this value by explicitly calling the '__str__' method.*3

# A useful fact is that each object in Python is assigned a unique integer you can access its value by calling the 'id' function.

# The memory address inside the standard string representation is a hexadecimal value. (ex. 0x000001E4BDC49FD0) WHILE the 'id' returns a base 10 integer.

# If you run Python and type the hexadecimal value (c Python memory address) it would return the 'id' value which is associated to the hex. value.


# Now that we fully understand the default string representation, let us override the str special method. 
# Instead of returning the memory address we will return the martian's full name.

# class Martian:
#     """Someone who lives on Mars"""

#     def __init__(self, fn, ln):
#         self.first_name = fn
#         self.last_name = ln

#     def __setattr__(self, name, value):
#         self.__dict__[name] = value  # To store the attributes in the dictionary __dict__.*1

#     def __str__(self):
#         return f'{self.first_name} {self.last_name}'

# m = Martian('Rika', 'Furude')
# print(m)

# --> Rika Furude


# *Comparing Martians* 'lt' special method.

# Order by name: martian1 < martian2

# To achieve this you can implement the 'lt' special method.

# class Martian:
#     """Someone who lives on Mars"""

#     def __init__(self, fn, ln):
#         self.first_name = fn
#         self.last_name = ln

#     def __setattr__(self, name, value):
#         self.__dict__[name] = value  # To store the attributes in the dictionary __dict__.*1

#     def __str__(self):
#         return f'{self.first_name} {self.last_name}'

#     def __lt__(self, other):
#         if self.last_name != other.last_name:
#             return (self.last_name < other.last_name)
#         else:
#             return (self.first_name < other.first_name)

# m1 = Martian('Rika', 'Furude')
# m2 = Martian('Tolobe', 'Zakaruko')
# m3 = Martian('Juka', 'Zakaruko')
# m4 = Martian('Kalimba', 'Fundazé')
# m5 = Martian('Ptolomeo', 'Sapohp')
# m6 = Martian('Sangunara', 'Rumbazeka')
# m7 = Martian('Gandungara', 'Androella')
# m8 = Martian('Xavi', 'Eljavi')
# m9 = Martian('Carlos', 'Duty')

# martians = [m1, m2, m3, m4, m5, m6, m7, m8, m9]
# martians.sort()
# for m in martians:
#     print(m)

# -->   Gandungara Androella
#       Carlos Duty
#       Xavi Eljavi
#       Kalimba Fundazé
#       Rika Furude
#       Sangunara Rumbazeka
#       Ptolomeo Sapohp
#       Juka Zakaruko
#       Tolobe Zakaruko


# To confirm that our custom 'less than method'-'lt' is being called we can print a message indicating when two martians are being compared:*4

class Martian:
    """Someone who lives on Mars"""

    def __init__(self, fn, ln):
        self.first_name = fn
        self.last_name = ln

    def __setattr__(self, name, value):
        self.__dict__[name] = value  # To store the attributes in the dictionary __dict__.*1

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def __lt__(self, other):
        print(f'>>> Comparing {self} with {other}')
        if self.last_name != other.last_name:
            return (self.last_name < other.last_name)
        else:
            return (self.first_name < other.first_name)

m1 = Martian('Rika', 'Furude')
m2 = Martian('Tolobe', 'Zakaruko')
m3 = Martian('Juka', 'Zakaruko')
m4 = Martian('Kalimba', 'Fundazé')
m5 = Martian('Ptolomeo', 'Sapohp')
m6 = Martian('Sangunara', 'Rumbazeka')
m7 = Martian('Gandungara', 'Androella')
m8 = Martian('Xavi', 'Eljavi')
m9 = Martian('Carlos', 'Duty')

martians = [m1, m2, m3, m4, m5, m6, m7, m8, m9]
martians.sort()
for m in martians:
    print(m)

# This is what we got -->

# >>> Comparing Tolobe Zakaruko with Rika Furude
# >>> Comparing Juka Zakaruko with Tolobe Zakaruko
# >>> Comparing Juka Zakaruko with Tolobe Zakaruko
# >>> Comparing Juka Zakaruko with Rika Furude
# >>> Comparing Kalimba Fundazé with Juka Zakaruko
# >>> Comparing Kalimba Fundazé with Rika Furude
# >>> Comparing Ptolomeo Sapohp with Juka Zakaruko
# >>> Comparing Ptolomeo Sapohp with Rika Furude
# >>> Comparing Sangunara Rumbazeka with Ptolomeo Sapohp
# >>> Comparing Sangunara Rumbazeka with Rika Furude
# >>> Comparing Gandungara Androella with Ptolomeo Sapohp
# >>> Comparing Gandungara Androella with Rika Furude
# >>> Comparing Gandungara Androella with Kalimba Fundazé
# >>> Comparing Xavi Eljavi with Sangunara Rumbazeka
# >>> Comparing Xavi Eljavi with Kalimba Fundazé
# >>> Comparing Xavi Eljavi with Gandungara Androella
# >>> Comparing Carlos Duty with Sangunara Rumbazeka
# >>> Comparing Carlos Duty with Kalimba Fundazé
# >>> Comparing Carlos Duty with Xavi Eljavi
# >>> Comparing Carlos Duty with Gandungara Androella
# Gandungara Androella
# Carlos Duty
# Xavi Eljavi
# Kalimba Fundazé
# Rika Furude
# Sangunara Rumbazeka
# Ptolomeo Sapohp
# Juka Zakaruko
# Tolobe Zakaruko
