""" Métodos, Ayuda y Documentación"""

# PRÁCTICA 1
# Remueve los caracteres , : _ # de la izquierda del texto.
# Utiliza el método lstrip() e imprime el resultado en pantalla.

string = ",:_#,,,,,,:::____##Python_ _Total,,,,,,::#"
new_string = string.lstrip(",:_#")
print (new_string)


print()
#...........................................................................................
# PRÁCTICA 2
# Añade el elemento "naranja" como el cuarto elemento de la lista frutas utilizando el método insert():

frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]
frutas.insert(3, "naranja") 

print(frutas)


print()
#...........................................................................................
# PRÁCTICA 3
# Verifica si los sets a continuación forman conjuntos aislados (es decir, que no tienen elementos en común), utilizando el método isdisjoint(). Almacena dicho resultado en la variable conjuntos_aislados:

marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
marcas_tv = {"Sony", "Philips", "Samsung", "LG"}

conjuntos_aislados = marcas_smartphones.isdisjoint(marcas_tv)

print(conjuntos_aislados)