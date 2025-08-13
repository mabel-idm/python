""" Crear Funciones"""

# PRÁCTICA 1
# Declara una función llamada saludar, que cada vez que sea llamada imprima en pantalla "¡Hola mundo!".

def saludar ():
    print("¡Hola mundo!")

saludar ()


print()
#...........................................................................................
# PRÁCTICA 2
# Declara una función llamada bienvenida, que tome como argumento el nombre de una persona, y que cada vez que sea llamada imprima en pantalla "¡Bienvenido {nombre_persona}!".
# Crea la variable nombre_persona, y almacena dentro de la misma el nombre que prefieras.

def bienvenida (nombre_persona):
    print(f"¡Bienvenid@ {nombre_persona}!")

bienvenida('Lili')


print()
#...........................................................................................
# PRÁCTICA 3
# Declara una función llamada cuadrado, que tome como argumento un número cualquiera, y que cada vez que sea llamada, imprima en pantalla el cuadrado de dicho número 
# El nombre del argumento que debe tomar dicha función es un_numero. Crea dicha variable y asígnale un número cualquiera.

def cuadrado (un_numero):
    print(un_numero**2)

cuadrado(2)