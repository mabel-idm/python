""" MÓDULO COLLECTIONS"""

from collections import Counter         # P-1
from collections import defaultdict     # P-2
from collections import deque           # P-3


# PRÁCTICA 1
# Aplica un Counter (contador) sobre la lista de números, y almacénalo en una variable llamada contador

lista = [1, 2, 3, 6, 7, 1, 2, 4, 5, 5, 5, 5, 3, 2, 6, 7]

contador = Counter(lista)
print(contador)


#...........................................................................................
# PRÁCTICA 2
# Crea un diccionario llamado mi_diccionario, para el cual, cuando no se halle una palabra clave buscada, se cargue con el string "Valor no hallado".
# Carga el diccionario, al menos, con el siguiente par de datos:
# palabra clave = edad
# valor = 44
# Utiliza el método defaultdict del módulo Collections.

def respuesta_no_hallado():
    return "Valor no hallado"

mi_diccionario = defaultdict(respuesta_no_hallado)
mi_diccionario["edad"] = 44   # Así se definen los default diccionarios

print(mi_diccionario["nombre"])


#...........................................................................................
# PRÁCTICA 3
# Una cola doblemente terminada o deque (del inglés double ended queue) es una estructura de datos lineal que permite insertar y eliminar elementos por ambos extremos.
# Investiga más al respecto en cualquier sitio de documentación, y a continuación implementa una deque a partir del módulo collections. Los elementos iniciales de la lista se brindan a continuación.
# ["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"]
# La lista debe tener la capacidad de incorporar elementos por la izquierda, y recibir el nombre lista_ciudades.

lista_ciudades = ["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"]

lista_deque = deque(lista_ciudades)
lista_deque.appendleft("Seúl")

print(lista_deque)