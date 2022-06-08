# ***SORTING***


# *SORTING ALPHABETICALLY*

# Alkaline earth metals. These are currently sorted by atomic number.

# earth_metals = ['Beryllium', 'Magnesium', 'Calcium', 'Strontium', 'Barium', 'Radium']
# earth_metals.sort()
# print(earth_metals)

# # (a-z)--> 
# # ['Barium', 'Beryllium', 'Calcium', 'Magnesium', 'Radium', 'Strontium']

# earth_metals.sort(reverse=True)
# print(earth_metals)

# (z-a)--> 
# ['Strontium', 'Radium', 'Magnesium', 'Calcium', 'Beryllium', 'Barium']

# print(help(list.sort))

# -->
# Help on method_descriptor:

# sort(self, /, *, key=None, reverse=False)
#    Sort the list in ascending order and return None.
    
#    The sort is in-place (i.e. the list itself is modified) and stable (i.e. the order of two equal elements is maintained).

#    If a key function is given, apply it once to each list item and sort them, ascending or descending, according to their function values.
    
#    The reverse flag can be set to sort in descending order.


# *EXPLORING MORE FEATURES OF THE SORT METHOD*

# ex. format: (name, radius, density, distance from sun)
# Radius: Radius at equator in Km
# Density: Average density in g/cm3
# Distance from sun: Avg. distance to sun in AU (astronomical units)

# List of planets. Ordered by the -distance from the sun-:

planets = [('Mercury', 2440, 5.43, 0.395), ('Venus', 6052, 5.24, 0.723), ('Earth', 6378, 5.52, 1.000), ('Mars', 3396, 3.93, 1.530), ('Jupiter', 71492, 1.33, 5.210), ('Saturn', 60268, 0.69, 9.551), ('Uranus', 25559, 1.27, 19.213), ('Neptune', 24764, 1.64, 30.070)]

# Sorting by size:

# Creating a function that returns the 2nd value in the tuple, the radius:

size = lambda planet: planet[1]
planets.sort(key=size, reverse=True)
print(planets)

# (+-)-->
# [('Jupiter', 71492, 1.33, 5.21), ('Saturn', 60268, 0.69, 9.551), ('Uranus', 25559, 1.27, 19.213), ('Neptune', 24764, 1.64, 30.07), ('Earth', 6378, 5.52, 1.0), ('Venus', 6052, 5.24, 0.723), ('Mars', 3396, 3.93, 1.53), ('Mercury', 2440, 5.43, 0.395)]

# Sorting by density:

# Creating a function that returns the 3rd value in the tuple, the radius:

density = lambda planet: planet[2]
planets.sort(key=density)
print(planets)

# (-+)-->
# [('Saturn', 60268, 0.69, 9.551), ('Uranus', 25559, 1.27, 19.213), ('Jupiter', 71492, 1.33, 5.21), ('Neptune', 24764, 1.64, 30.07), ('Mars', 3396, 3.93, 1.53), ('Venus', 6052, 5.24, 0.723), ('Mercury', 2440, 5.43, 0.395), ('Earth', 6378, 5.52, 1.0)]

# list.sort() changes the list


# When we want to create a sorted copy of the list or sort a tuple there is a built-in function called sorted. The help(sorted) have mor info.

earth_metals = ['Beryllium', 'Magnesium', 'Calcium', 'Strontium', 'Barium', 'Radium']
sorted_earth_metals = sorted(earth_metals) # This will create a sorted copy of the list and does not modify the original list
print(sorted_earth_metals)

# -->
# ['Barium', 'Beryllium', 'Calcium', 'Magnesium', 'Radium', 'Strontium']


# To 'sort' a tuple

data = (7, 2, 5, 6, 1, 3, 9, 10, 4, 8)

# Tuples do not have a sort method because they are immutable and cannot be changed, but if you pass one to the 'sorted' function it returns a sorted list and the original tuple is unaltered.

print(sorted(data))
print(data)

# -->
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# (7, 2, 5, 6, 1, 3, 9, 10, 4, 8)


# To sort a string:

print(sorted('Alphabetical'))

# It returns a list of all the characters in the string sorted alphabetically, with the capital 'A' coming before the lower case 'a'

# -->
# ['A', 'a', 'a', 'b', 'c', 'e', 'h', 'i', 'l', 'l', 'p', 't']