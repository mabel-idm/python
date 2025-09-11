""" Generadores"""

# PRÁCTICA 1
# Crea un generador (almacenado en la variable generador) que sea capaz de devolver una secuencia infinita de números, iniciando desde el 1, y entregando un número consecutivo superior cada vez que sea llamada mediante next.

def numbers():
    number = 1
    while number >= 1:
        yield number
        number += 1
        
generador = numbers()

print(next(generador))
print(next(generador))
print(next(generador))


#...........................................................................................
# PRÁCTICA 2
# Crea un generador (almacenado en la variable generador) que sea capaz de devolver de manera indefinida múltiplos de 7, iniciando desde el mismo 7, y que cada vez que sea llamado devuelva el siguiente múltiplo (7, 14, 21, 28...).

def multiplos_siete():
    number = 7
    while number % 7 == 0:
        yield number
        number += 7
        
generador = multiplos_siete()

print(next(generador))
print(next(generador))
print(next(generador))


#...........................................................................................
# PRÁCTICA 3
# Crea un generador que reste una a una las vidas de un personaje de videojuego, y devuelva un mensaje cada vez que sea llamado:
# "Te quedan 3 vidas"
# "Te quedan 2 vidas"
# "Te queda 1 vida"
# "Game Over"
# Almacena el generador en la variable perder_vida

def juego():
    number = 4
    while number <= 4:
        number -= 1
        yield number

generador = juego()

print(f"Te quedan {next(generador)} vidas.")
print(f"Te quedan {next(generador)} vidas.")
print(f"Te quedan {next(generador)} vidas.")
print('Game Over')