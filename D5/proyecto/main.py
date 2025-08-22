"""EL AHORCADO"""

# El programa va a elegir una palabra y le va a mostrar al jugador una serie de guiones que representa la cantidad de letras que tiene la palabra. 
# El jugador en cada turno deberá elegir una letra y si la letra se encuentra en la palabra oculta, el sistema le va a mostrar en qué lugares se encuentra. 

from random import choice

lista_palabras = ["mar", "mariposa", "libro", "azul"]
palabra_elegida = choice(lista_palabras)


def palabra_to_guiones():
    return list(len(palabra_elegida) * '_')      # Convertir la palabra en guiones y luego en una lista
    

def elegir_letra(palabra):

    while '_' in palabra:       # Mientras exista al menos un guión en palabra (palabra_to_guiones(), cuando la llame)
        print(' '.join(palabra))
        letra_usuario = input("¿Qué letra crees que conforma la palabra?: ").lower()

        for i, letra in enumerate(palabra_elegida):
            if letra == letra_usuario:
                palabra[i] = letra_usuario

    print("\n¡Felicidades! La palabra era:", palabra_elegida)

elegir_letra(palabra_to_guiones())



#----- ESTO IMPRIME UNA LISTA DE GUIONES Y PIDE AL USER INSERTAR UNA LETRA -----

# from random import choice 

# lista_palabras = ["mar", "mariposa", "libro", "azul"]
# palabra_elegida = list(choice(lista_palabras))

# def imprimir_guiones(*args):

#     for arg in args:
#         guiones = list(len(arg) * '_')  # Cada letra la convierte en un guión
#     return guiones

# print(imprimir_guiones(palabra_elegida))


# def elegir_letra(palabra, espacios_para_letra):

#     letra_usuario = input("¿Qué letra crees que conforma la palabra?: ").lower()

#     for indice, letra in enumerate(palabra):
#         if letra_usuario ==  letra:
#             espacios_para_letra[indice] = letra_usuario

#     return espacios_para_letra

# elegir_letra(palabra_elegida, imprimir_guiones(palabra_elegida))



#----- ESTO IMPRIME LOS GUIONES Y SI LA LETRA ESTÁ EN LA LISTA -----

# from random import choice 

# lista_palabras = ["mar", "mariposa", "libro", "azul"]
# palabra_elegida = list(choice(lista_palabras))

# def imprimir_guiones():
    
#     for letra in palabra_elegida:
#         letra = "-"
#         print(letra)

# imprimir_guiones()


# def elegir_letra():

#     letra_usuario = input("¿Qué letra crees que conforma la palabra?: ").lower()

#     if letra_usuario in palabra_elegida:
#         print(f"La letra {letra_usuario} esta en la lista")
#     elif letra_usuario is not palabra_elegida:
#         print(f"La letra {letra_usuario} no esta en la lista")
    
# elegir_letra()