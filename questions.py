##Comentario: dejo mis comentarios con los enunciados y mi proceso de pensamiento
##para poder estudiar luego.
##Espero no sea molestia.

## fix 1
##El juego tiene un bug. Si el usuario ingresa más de una letra, un número o
##cualquier otro carácter inválido,
##el programa se comporta de manera inesperada. Modificalo para que en ese caso
##muestre el mensaje
##"Entrada no válida" y continúe el juego en la siguiente iteración.

## idea de resolución: controlar que se ingrese un único caracter, y que sea letra.
## devolver "entrada no válida" y pedir un input nuevo.



##fix 2:
##Modificá el juego para que al final de la partida se muestre el puntaje
##del jugador. El puntaje se calcula de la siguiente forma: cada letra
##incorrecta resta 1 punto, adivinar la palabra completa suma 6 puntos,
##y perder deja el puntaje en 0.

##idea de resolución: luego de cada if que comprueba si la letra es correcta
## o no, añadir/restar.
## Mostrar/setear y mostrar puntaje al final.


##fix 3:
##Modificá el juego para que las palabras estén agrupadas por categoría.
##Al inicio de cada partida, mostrar las categorías disponibles y permitir
##que el usuario elija una. Ayuda: utilizá un diccionario donde las claves
##sean los nombres de las categorías y los valores sean listas de palabras.

##idea de resolución: la lista words la tendría que reemplazar por un 
## diccionario de categorías. Un Input que elija la categoría-> que se
## juegue con la categoría elegida.


## fix 4:
##Modificá el juego para que, al jugar varias rondas seguidas, no se
##repita la misma palabra. Investigá la función random.sample() .

##idea de resolución: el random sample hace que no repita palabra. Sacar el break del while
##para poder comprobar si se quiere seguir jugando, seleccionar otra categoría o la misma, y guardar el puntaje.

import random
##diccionario con listas. las listas son las categorias.
categorias = {
    "Programacion":["python", "programa", "variable", "funcion", "bucle", "cadena", "entero", "lista",],
    "Economia":["activos", "pasivos", "oferta", "demanda", "mercado", "utilidad",],
    "Animales":[ "leon", "lobo", "jirafa", "hipopotamo", "delfin", "elefante",]}




print("¡Bienvenido al Ahorcado!")
print()
puntaje = 0 ##inicializo

while True: ##bucle del programa
    
    while True: ##bucle de categorías
        
        print("Categorías: ") ##imprimir las categorias
        for  nombres_categorias in categorias.keys(): ##por: cantidad de categorias en el diccionario
            print(f"- {nombres_categorias}") ##imprime: el nombre de la categoria
        print()

        cat_seleccionada = input("Seleccione una categoria: ").capitalize() ##selecciona. el capitalize es para que la primera letra sea mayuscula.

        if cat_seleccionada in categorias: ##comprueba que la entrada sea válida
            cat_juego = categorias[cat_seleccionada]
            palabras_mezcladas= random.sample(cat_juego, len(cat_juego)) ## random.sample para no repetir palabras
            break ##se rompe el bucle
        else:
            print("Entrada no válida.") ## vuelve al bucle hasta que se haya una entrada válida
    
    
    while True: ##bucle de juego
        if len(palabras_mezcladas) == 0: ##comprueba si hay palabras en la categoría
            print("La categoría ya no tiene palabras.")
            break ##rompe el bucle de juego, vuelve a elegir categorías
        word =  palabras_mezcladas.pop() ## saca una palabra y la elimina de la lista
        guessed = []
        attempts = 6
        while attempts > 0:
            # Mostrar progreso: letras adivinadas y guiones para las que faltan
            progress = ""
            for letter in word:
                if letter in guessed:
                    progress += letter + " "
                else:
                    progress += "_ "
            print(progress)
            # Verificar si el jugador ya adivinó la palabra completa
            if "_" not in progress:
                print("¡Ganaste!")
                print("Puntaje acumulado: ", puntaje) ## mostrar puntaje cuando se gana
                break
            print(f"Intentos restantes: {attempts}")
            print(f"Letras usadas: {', '.join(guessed)}")
            letter = input("Ingresá una letra: ") ##acá el input de letra!!

            if len(letter) != 1 or not letter.isalpha():  ##controlo que sea un solo caracter letra
                print("Entrada no válida.")
                continue  ## vuelve al input
            if letter in guessed:
                print("Ya usaste esa letra.")
            elif letter in word:
                guessed.append(letter)
                puntaje = puntaje + 6 ##se suman 6 por letra correcta
                print("¡Bien! Esa letra está en la palabra.")
            else:
                guessed.append(letter)
                puntaje = puntaje - 1
                attempts -= 1 ##se resta 1 por letra incorrecta
                print("Esa letra no está en la palabra.")
            print()
        else:
            print(f"¡Perdiste! La palabra era: {word}") ##saqué el seteo a 0 del puntaje y el print a "Puntaje acumulado"
            print("Puntaje acumulado: ", puntaje)
            
        continuar = input("Desea seguir jugando? [S/N]").capitalize()
        if continuar != "S":
            break ##terminar el bucle del juego
    break ##terminar el bucle de categorías

print("Fin del juego.")