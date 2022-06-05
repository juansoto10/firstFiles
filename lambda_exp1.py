favorite_players = ['Cristiano Ronaldo', 'Lionel Messi', 'Erling Haaland', 'Luis Díaz', 'Zlatan Ibrahimovic', 'R. F. García', 'Kevin d. Bruyne', 'Ronaldo L. N. de Lima']

# favorite_players.sort(key = lambda name: name.split(' ')). 
# <Con esto me organizaría la lista alfabéticamente teniendo en cuenta el primer caracter de la cadena.>

# De esta manera puedo organizar mi lista en orden alfabético a partir de los apellidos.
favorite_players.sort(key = lambda name: name.split(' ')[-1].lower())

print(favorite_players)