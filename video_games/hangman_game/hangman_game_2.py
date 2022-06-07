import random
import time
 
## Listas de Palabras
marcas_de_carros = ["ford", "audi", "nissan", "renault", "chevrolet", "mitsubishi", "cadillac", "suzuki", "subaru", "jaguar", "ferrari", "fiat", "citroen", "volvo", "mitsubishi", "honda", "mazda", "volskwagen", "toyota", "hyundai", "isuzu", "lotus", "porsche", "peugeot", "jeep", "bugatti", "lamborghini", "lexus", "maserati", "tesla", "infiniti", "bentley", "daewoo", "dodge", "pontiac", "mclaren"]
 
nombres_de_paises = ["mexico", "colombia", "canada", "venezuela", "uruguay", "argentina", "guatemala", "panama","ecuador", "dinamarca", "suecia", "islandia", "francia", "italia", "turquia", "rusia", "ucrania", "polonia", "china", "tailandia", "indonesia", "noruega", "belgica", "rumania", "irlanda", "sudafrica", "egipto", "israel", "españa", "portugal", "vietnam", "grecia", "marruecos", "angola", "madagascar", "croacia", "suiza", "austria", "hungria", "estonia", "finlandia", "mongolia", "japon", "filipinas", "siria", "jordania", "libano", "singapur", "malasia", "australia", "belice", "bolivia", "chile", "nicaragua", "surinam"]
 
 
print("Bienvenido al juego del ahorcado")
time.sleep(1)
print("El objetivo del juego es adivinar la palabra secreta letra por letra.")
print("Tienes 5 vidas y pierdes una cada vez que te equivocas. Si te quedas sin vidas pierdes")
time.sleep(3)
 
print("¿Deseas jugar con marcas de carros o nombres de países?")
time.sleep(1)
 
cat_seleccionada = input("Ingresa C para marcas de carros o P para nombres de países: ")
 
while True:
    if cat_seleccionada.lower() == "c":
        print("Has seleccionado marcas de carros")
        palabra_secreta = random.choice(marcas_de_carros)
        break
    elif cat_seleccionada.lower() == "p":
        print("Has seleccionado nombres de países")
        palabra_secreta = random.choice(nombres_de_paises)
        break
 
    else:
        print("Por favor selecciona una categoría válida")
        cat_seleccionada = input("Ingresa C para marcas de carros o P para nombres de países: ")
 
 
 
# Es el numero de veces que se puede eqivocar
vidas = 5
 
lista_letras_adivinadas = []
 
## Imprimimos la palabra sin letras
print('_' * len(palabra_secreta))
 
while True:
 
    while True:
        letra_adivinada = input("Adivina una letra: ")
        if(len(letra_adivinada)!=1 or letra_adivinada.isnumeric()):
            print("Eso no es una letra, intenta con una sola letra.")
        else:
            if letra_adivinada.lower() in lista_letras_adivinadas:
                print("Ya has intentado con esa letra,prueba otra por favor.")
            else:
                lista_letras_adivinadas.append(letra_adivinada)
 
                if letra_adivinada.lower() in palabra_secreta:
                    print("Felicidades, adivinaste una letra")
                    break
                else:
                    vidas = vidas-1
                    print("Te has equivocado. ¡Perdiste una vida!")
                    print("Te quedan " + str(vidas) + " vidas...")
                    break
 
    if vidas==0:
        print("""
 ▐▄▄▄ ▄▄▄·.▄▄ ·  ▌ ▐· ▐▄▄▄ ▄▄▄·.▄▄ ·  ▌ ▐· ▐▄▄▄ ▄▄▄·.▄▄ ·  ▌ ▐·
  ·██▐█ ▄█▐█ ▀. ▪█·█▌  ·██▐█ ▄█▐█ ▀. ▪█·█▌  ·██▐█ ▄█▐█ ▀. ▪█·█▌
▪▄ ██ ██▀·▄▀▀▀█▄▐█▐█•▪▄ ██ ██▀·▄▀▀▀█▄▐█▐█•▪▄ ██ ██▀·▄▀▀▀█▄▐█▐█•
▐▌▐█▌▐█▪·•▐█▄▪▐█ ███ ▐▌▐█▌▐█▪·•▐█▄▪▐█ ███ ▐▌▐█▌▐█▪·•▐█▄▪▐█ ███ 
 ▀▀▀•.▀    ▀▀▀▀ . ▀   ▀▀▀•.▀    ▀▀▀▀ . ▀   ▀▀▀•.▀    ▀▀▀▀ . ▀  
""")
        print("Has perdido 😔. La palabra secreta era: " + palabra_secreta.capitalize())
        break
 
 
    estatus_actual = ""
 
    letras_faltantes = 0
    for letra in palabra_secreta:
 
        if letra in lista_letras_adivinadas:
            estatus_actual = estatus_actual + letra
 
        else:
            estatus_actual = estatus_actual + "_"
            letras_faltantes = letras_faltantes + 1
 
    ## Imprimir palabra con algunas letras
    print(estatus_actual)
 
 
    if letras_faltantes == 0:
        print("""
 ▐▄▄▄ ▄▄▄·.▄▄ ·  ▌ ▐· ▐▄▄▄ ▄▄▄·.▄▄ ·  ▌ ▐· ▐▄▄▄ ▄▄▄·.▄▄ ·  ▌ ▐·
  ·██▐█ ▄█▐█ ▀. ▪█·█▌  ·██▐█ ▄█▐█ ▀. ▪█·█▌  ·██▐█ ▄█▐█ ▀. ▪█·█▌
▪▄ ██ ██▀·▄▀▀▀█▄▐█▐█•▪▄ ██ ██▀·▄▀▀▀█▄▐█▐█•▪▄ ██ ██▀·▄▀▀▀█▄▐█▐█•
▐▌▐█▌▐█▪·•▐█▄▪▐█ ███ ▐▌▐█▌▐█▪·•▐█▄▪▐█ ███ ▐▌▐█▌▐█▪·•▐█▄▪▐█ ███ 
 ▀▀▀•.▀    ▀▀▀▀ . ▀   ▀▀▀•.▀    ▀▀▀▀ . ▀   ▀▀▀•.▀    ▀▀▀▀ . ▀  
""")
        print("Felicidades, ¡has ganado! 😎")
        print("La palabra secreta es: " + palabra_secreta.capitalize())
        break