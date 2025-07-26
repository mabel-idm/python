"""
TUPLAS
   - Se definen con (), o sin nada, igual funcionan
   - Pueden contener elementos de cualquier tipo
   - Inmutables
   - Ordenadas: Se pueden buscar por su índice
"""

# PRÁCTICA 1
# Utiliza un método de tuplas para contar la cantidad de veces que aparece el valor 2 en la siguiente tupla, y muestra el resultado (integer) en pantalla:

mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)

print(mi_tupla.count(2)) # El método 'count', devuelve un integer de la coincidencias

#............................................................................................
# PRÁCTICA 2
# Convierte a lista la siguiente tupla, y almacénala en una variable llamada mi_lista:

mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2)

mi_lista = list(mi_tupla)
print(type(mi_lista))

#............................................................................................
# PRÁCTICA 3
# Extrae los elementos de la siguiente tupla en cuatro variables: a, b, c, d

mi_tupla = (1, 2, 3, 4)

a,b,c,d = mi_tupla  # Este método se llama 'unpacking' y esta es una de las formas de hacerlo
print(a)