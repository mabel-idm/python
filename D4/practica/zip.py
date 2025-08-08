""" ZIP """

# PRÁCTICA 1
# Muestra en pantalla frases como la del siguiente ejemplo: La capital de Alemania es Berlín
# Utiliza la función zip(), loops, y las siguientes listas para resolverlo de forma rápida y eficiente:

capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

for capital, pais in list(zip(capitales, paises)):
    print(f"La capital de {pais} es {capital}")


print()
#...........................................................................................
# PRÁCTICA 2
# Crea un objeto zip formado a partir de listas con un conjunto de marcas y productos que tú prefieras.
# Almacena el resultado en la variable mi_zip.

marca = ["Samsung", "Apple"]
producto = ["Galaxy", "iPhone"]

mi_zip = list(zip(marca, producto))

print(mi_zip)


print()
#...........................................................................................
# PRÁCTICA 3
# Crea el zip con las traducciones de los números del 1 al 5 en español, portugués e inglés (en el mismo orden), y convierte el objeto generado en una lista almacenada en la variable numeros:
# uno / um / one
# dos / dois / two
# tres / três / three
# cuatro / quatro / four
# cinco / cinco / five

number_spanish = ["uno", "dos", "tres", "cuatro", "cinco"]
number_english = ["um", "dois", "três", "quatro", "cinco"]
number_portuguese = ["one", "two", "three", "four", "five"]

number_translate = list(zip(number_spanish, number_english, number_portuguese))

print(number_translate)