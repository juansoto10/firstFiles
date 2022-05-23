# El usuario deberá poder escoger con qué método se calculará la raíz cuadrada de un número escogido por él mismo.

def raiz_busq_binaria(numero):
    epsilon = 0.01
    bajo = 0.0
    alto = max(1.0, numero)
    respuesta = (alto + bajo) / 2

    while abs(respuesta**2 - numero) >= epsilon:
        print(f'bajo={bajo}, alto={alto}, respuesta={respuesta}')
        if respuesta**2 < numero:
            bajo = respuesta
        else:
            alto = respuesta

        respuesta = (alto + bajo) / 2

    print(f'La raíz cuadrada de {numero} es {respuesta}')    


def raiz_aprox_soluciones(numero):
    epsilon = 0.01
    paso = epsilon**2
    respuesta = 0.0

    while abs(respuesta**2 - numero) >= epsilon and respuesta <= numero:
        print(abs(respuesta**2 - numero), respuesta)
        respuesta += paso

    if abs(respuesta**2 - numero) >= epsilon:
        print(f'No se encontró La raíz cuadrada de {numero}')
    else:
        print(f'La raíz cuadrada de {numero} es {respuesta}')


def raiz_enumeracion_exhaustiva(numero):
    respuesta = 0

    while respuesta**2 < numero:
        print(respuesta)
        respuesta += 1

    if respuesta**2 == numero:
        print(f'La raíz cuadrada de {numero} es {respuesta}')
    else:
        print(f'El número {numero} no tiene raíz cuadrada exacta')


menu_1 = """
Bienvenido a la calculadora de raíces cuadradas😉🤑

Elige un número por ahora solamente 😎 : """

menu_2 = """
Estos son los métodos que dispones para calcular la raíz, cada uno tarda un tiempo distinto:

1-Búsqueda binaria.
2-Aproximación de soluciones.
3-Enumeración exhaustiva (🛑 Solo calcula raíces exactas). 

👽 Elige qué método usar mor:
"""

objetivo = int(input(menu_1))


def run():
    metodo = int(input(menu_2))

    if metodo == 1:
        raiz_busq_binaria(objetivo)
    elif metodo == 2:
        raiz_aprox_soluciones(objetivo)
    elif metodo == 3:
        raiz_enumeracion_exhaustiva(objetivo)
    else:
        print('Ingresa una opción válida por favor')


if __name__ == '__main__':
    run()