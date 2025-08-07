""" ENUMERATE """

# PRÁCTICA 1
# Imprime en pantalla frases como la siguiente:
# '{nombre} se encuentra en el índice {indice}'
# Donde:
# - Nombre debe ser cada uno de los nombres de la lista a continuación
# - Índice debe obtenerse mediante enumerate()

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for indice, nombre in enumerate(lista_nombres):
    print(f"{nombre} se encuentra en el índice {indice}")


print()
#...........................................................................................
# PRÁCTICA 2
# Crea una lista formada por las tuplas (índice, elemento), obtenidas al aplicar enumerate() sobre cada carácter del string "Python".
# Llama a la lista resultante con el nombre de variable: lista_indices

cadena = "Python"

cadena_enumerada = list(enumerate(cadena))

print(cadena_enumerada)


print()
#...........................................................................................
# PRÁCTICA 3
# Imprime en pantalla únicamente los índices de aquellos nombres de la siguiente lista que empiecen con la letra M:

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for indice, nombre in enumerate(lista_nombres):
    if nombre[0] == "M":
        print(nombre)