def read():
    numbers = []
    with open('./files/numbers.txt', 'r', encoding='utf-8') as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)


def write():
    names = ['Claudia', 'Lucía', 'Irina', 'Juan', 'Rocío']
    with open ('./files/names.txt', 'a', encoding='utf-8') as f:
        for name in names:
            f.write(name)
            f.write('\n')


def run():
    write()
    # read()


if __name__ == '__main__':
    run()

# -with- es un manejador conceptual, impide que el archivo se rompa si el programa se cierra inesperadamente.

# open(ruta, modo, encoding) --> Sirve para abrir archivos

# write() --> Para escribir una línea en un archivo de texto en Python

# -f- va a ser el 'nombre de la variable' que le damos a nuestro archivo para su uso en Python

# 'a': Modo de escritura sin sobreescribir
# 'w': Modo de escritura sobreescribiendo el archivo
# 'r': Modo de lectura