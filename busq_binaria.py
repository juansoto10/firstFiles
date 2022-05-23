# BÚSQUEDA BINARIA***1

# Si la respuesta se encuentra en un conjunto ordenado se puede usar búsqueda binaria.
# Es altamente eficiente, pues corta el espacio de búsqueda en dos por cada iteración.


def run():
    objetivo = int(input('Escoge un número: '))
    epsilon = 0.01
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto + bajo) / 2

    while abs(respuesta**2 - objetivo) >= epsilon:
        print(f'bajo={bajo}, alto={alto}, respuesta={respuesta}')
        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta

        respuesta = (alto + bajo) / 2

    print(f'La raíz cuadrada de {objetivo} es {respuesta}')


if __name__ == '__main__':
    run()