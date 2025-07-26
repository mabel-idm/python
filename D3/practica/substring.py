"""SINTÁXIS: string[start:stop:reset]
   - start: índice de inicio del substring (se incluye)
   - stop:  índice del final del sub-string (no se incluye)
   - step:  saltitos
"""

# PRÁCTICA 1
# Extrae la primera palabra de la siguiente frase utilizando slicing, y muéstrala en pantalla:
# "Controlar la complejidad es la esencia de la programación"
# Pista: La palabra "Controlar" tiene un largo de 9 caracteres.

string = "Controlar la complejidad es la esencia de la programación"
slicing = string[0:9]

print(slicing)

#............................................................................................
# PRÁCTICA 2
# Toma cada tercer carácter empezando desde el noveno hasta el final de la frase, e imprime el resultado.
# "Nunca confíes en un ordenador que no puedas lanzar por una ventana"

string = "Nunca confíes en un ordenador que no puedas lanzar por una ventana"
slicing = string[9::3]

print(slicing)

#............................................................................................
# PRÁCTICA 3
# Invierte la posición de todos los caracteres de la siguiente frase y muestra el resultado en pantalla.
# "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"

string = "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"
slicing = string[::-1]

print(slicing)