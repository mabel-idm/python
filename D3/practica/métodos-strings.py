# PRÁCTICA 1
# Imprime el siguiente texto en mayúsculas, empleando el método específico de strings:
# "Especialmente en las comunicaciones electrónicas, la escritura enteramente en mayúsculas equivale a gritar."

string = "Especialmente en las comunicaciones electrónicas, la escritura enteramente en mayúsculas equivale a gritar."
print (string.upper())

#............................................................................................
# PRÁCTICA 2
# Une la siguiente lista en un string, separando cada elemento con un espacio. Utiliza el método apropiado de listas/strings, y muestra en pantalla el resultado.
# ["La", "legibilidad", "cuenta."]

lista = ["La", "legibilidad", "cuenta."]
print(" ".join(lista))

#............................................................................................
# 
# PRÁCTICA 3
# Reemplaza en la siguiente frase:
# "Si la implementación es difícil de explicar, puede que sea una mala idea." los siguientes pares de palabras:
# "difícil" → "fácil"
# "mala" → "buena"

string = "Si la implementación es difícil de explicar, puede que sea una mala idea."
new_string = string.replace("difícil", "fácil").replace("mala", "buena")

print(new_string)