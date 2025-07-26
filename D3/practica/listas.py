"""
LISTAS
   - Se definen con []
   - Pueden contener elementos de cualquier tipo
   - Mutables: se puede agregar, eliminar o cambiar elementos, sin necesidad de crear una nueva lista
   - Ordenadas
"""

# PRÁCTICA 1
# Crea una lista con 5 elementos, dentro de la variable "mi_lista". Puedes incluir strings, booleanos, números, etc.

mi_lista = ["Perú", 7, 20.25, "Japón", True ]
print(mi_lista)

#............................................................................................
# PRÁCTICA 2
# Agrega el elemento "motocicleta" a la siguiente lista de medios de transporte:

medios_transporte = ["avión", "auto", "barco", "bicicleta"]
medios_transporte.append("motocicleta")    # No se puede incluir esta línea dentro de una variable, porque "append no es un valor que se pueda almacenar, sino una acción que se aplica a la lista"

print(medios_transporte)

#............................................................................................
# PRÁCTICA 3
# Utiliza el método pop() para quitar el tercer elemento de la siguiente lista llamada frutas, y almacénalo en una variable llamada eliminado. 

frutas = ["manzana", "banana", "mango", "cereza", "sandía"]
new_frutas = frutas.pop()

print(frutas)
print(new_frutas)