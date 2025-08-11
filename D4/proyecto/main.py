""" ADIVINA EL NÚMERO"""

# El programa le va a preguntar al usuario su nombre, y luego le dirá “Juan, he pensado un número entre 1 y 100, y tienes solo ocho intentos para adivinar, cuál crees que es el número”. Entonces, en cada intento el jugador dirá un número y el programa puede responder cuatro cosas distintas: 
# - Si el número que dijo el usuario es menor a 1 o superior a 100, le va a decir que ha elegido un número que no está permitido. 
# - Si el número que ha elegido el usuario es menor al que ha pensado el programa, le va a decir que su respuesta es incorrecta y que ha elegido un número menor al número secreto. 
# - Si el usuario eligió un número mayor al número secreto, también se lo hará saber de la misma manera. 
# - Y si el usuario acertó el número secreto, se le va a informar que ha ganado y cuántos intentos le ha tomado.

from random import randint


user_name = input("\nEscribe tu nombre:  ")

print(f"\nHola {user_name}, debes adivinar un número del 1 al 100. Tienes 8 intentos. \n")

number_pc = randint(1, 100)

contador = 0

while contador < 8:

    contador = contador + 1

    number_user = int(input("¿Cuál crees que es el número?  "))

    if number_user < 0:
        print("Número no permitido. \n")
    elif number_user > 100:
        print("Número no permitido. \n")
    elif number_user < number_pc: 
        print("Respuesta incorrecta, el número es mayor. \n")
    elif number_user > number_pc:
        print("Respuesta incorrecta, el número es menor. \n")
    elif number_user == number_pc: 
        print("¡Acertaste! \n")
        break