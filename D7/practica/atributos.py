""" Atributos 
    - De clase      ->  Definido directamente en la clase, compartido.
    - De instancia  ->  Definido con self dentro de __init__, único por objeto.
"""

# PRÁCTICA 1
# Crea una clase llamada Casa, y asígnale atributos: color, cantidad_pisos.
# Crea una instancia de Casa, llamada casa_blanca, de color "blanco" y cantidad de pisos igual a 4.

class Casa:

    def __init__(self, color, cantidad_pisos):
        self.color = color                       # Atributo de instancia
        self.cantidad_pisos = cantidad_pisos     # Atributo de instancia

casa_blanca = Casa("blanco", 4)   

#...........................................................................................
# PRÁCTICA 2
# Crea una clase llamada Cubo, y asígnale el atributo de clase: caras = 6
# y el atributo de instancia: color
# Crea una instancia cubo_rojo, de dicho color.

class Cubo:

    caras = 6      # Atributo de clase

    def __init__(self, color):
        self.color = color     # Atributo de instancia
    
cubo_rojo = Cubo("rojo")

#...........................................................................................
# PRÁCTICA 3
# Crea una clase llamada Personaje, y asígnale el siguiente atributo de clase: real = False
# Crea una instancia llamada harry_potter con los siguientes atributos de instancia:
# especie = "Humano"
# magico = True
# edad = 17

class Personaje:
    
    real = False

    def __init__(self,especie, magico, edad):
        self.especie = especie
        self.magico = magico
        self.edad = edad

harry_potter = Personaje("Humano", True, 17)