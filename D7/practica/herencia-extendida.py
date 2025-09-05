""" Herencia Extendida"""

# PRÁCTICA 1
# Si la clase Hija ha heredado de su padre la forma de reir, y de su madre la vocación, y hoy tienen el mismo trabajo en la Fiscalía, crea la herencia múltiple que le permita a esta clase heredar correctamente de Padre y Madre.

class Padre:
    def __init__(self, reir):
        self.reir = reir

class Madre:
    def __init__(self, vocacion):
        self.vocacion = vocacion

class Hija(Padre, Madre):
    def __init__(self, reir, vocacion):
        Padre.__init__(self, reir)
        Madre.__init__(self, vocacion)

#...........................................................................................
# PRÁCTICA 2
# Crea una clase Ornitorrinco que herede de otras clases: Vertebrado, Pez, Reptil, Ave y Mamifero, tal que "construyas" un animal que tiene los siguientes métodos y atributos:
# - poner_huevos()
# - tiene_pico = True
# - vertebrado = True
# - venenoso = True
# - nadar() 
# - caminar()
# - amamantar()

class Vertebrado:
    vertebrado = True

class Pez(Vertebrado):
    def nadar(self):
        pass

    def poner_huevos(self):
        pass

class Reptil(Vertebrado):
    venenoso = True

class Ave(Vertebrado):
    tener_pico = True

    def poner_huevos(self):
        pass

    def caminar(self):
        pass
    
class Mamifero(Vertebrado):
    def amamantar(self):
        pass

class Ornitorrinco(Pez, Reptil, Ave, Mamifero):
    pass

#...........................................................................................
# PRÁCTICA 3
# Un hijo ha heredado de su padre todas sus características, sin embargo, tienen diferentes hobbies. Logra que la clase Hijo herede de Padre todos sus métodos y atributos, sobreescribiendo el método hobby() para que se devuelva: "Juego videojuegos en mi tiempo libre"

class PadreDos:
    def __init__(self, color_ojos, estatura):
        self.color_ojos = color_ojos
        self.estatura = estatura
    
    def hobby(self):
        return "Visito museos en mi tiempo libre."

class HijoDos(PadreDos):
    def hobby(self):
        return "Juego videojuegos en mi tiempo libre."