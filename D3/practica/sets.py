"""
SETS
   - Son una colección de elementos
   - Se definen con set() o {}
   - Pueden contener elementos de cualquier tipo, excepto listas y diccionarios
   - No aceptan elementos repetidos
   - Desordenados, no se pueden ordenar por índice
   - Inmutables
"""

# PRÁCTICA 1
# Une los siguientes sets en uno solo, llamado mi_set_3:

mi_set_1 = {1, 2, "tres", "cuatro"}
mi_set_2 = {"tres", 4, 5}

mi_set_3 = mi_set_1.union(mi_set_2)
print(mi_set_3)  # El elemento repetido se guarda en cualquier posición

#............................................................................................
# PRÁCTICA 2
# Elimina un elemento al azar del siguiente set, utilizando métodos de sets:

sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
my_sorteo = sorteo.pop()

print(my_sorteo)

#............................................................................................
# PRÁCTICA 3
# Agrega el nombre Damián al siguiente set, utilizando métodos de sets:

sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
sorteo.add("Damián")

print(sorteo)
