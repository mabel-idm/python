"""
DICCIONARIOS
   - Se definen con {}
   - Pueden contener elementos de cualquier tipo
   - Mutables: se puede agregar, eliminar o cambiar elementos, sin necesidad de crear un nuevo diccionario
   - Desordenadas: no se buscan por su índice, para buscar se  usa la clave
"""

# PRÁCTICA 1
# Crea un diccionario llamado mi_dic que almacene la siguiente información de una persona:
# nombre: Karen
# apellido: Jurgens
# edad: 35
# ocupacion: Periodista

mi_dic = { 
    'nombre': 'Karen',
    'apellido': 'Jurgens',
    'edad': 35,
    'ocupacion': 'Periodista'
}

#............................................................................................
# PRÁCTICA 2
# Crea una función print que devuelva el segundo ítem de la lista llamada points.
# Si el valor 300 cambiara en el futuro, el código debería funcionar igual para devolver el valor que se encuentre en esa misma posición. Para ello, deberás hacer referencia a los nombres de las claves y/o índices según corresponda.

other_dic = {
    'clave_uno':'valor_uno', 
    'clave_dos':'valor_dos', 
    'clave_tres':'valor_tres', 
    'points':[100, 200, 300]  # Las listas dentro de los diccionarios, NO se colocan con comillas
}

indice_en_la_lista = other_dic['points'][2] # Se usa [] para decir, "Quiero que tomes esta clave"
print(indice_en_la_lista)

#............................................................................................
# PRÁCTICA 3
# Actualiza la información de nuestro diccionario llamado mi_dic (reasignando nuevos valores a las claves según corresponda), y agrega una nueva clave llamada "pais" (sin tilde). Los nuevos datos son:
# nombre: Karen
# apellido: Jurgens
# edad: 36
# ocupacion: Editora
# pais: Colombia
# Para ello, no debes cambiar la línea de código ya escrita, sino actualizar los valores mediante métodos de diccionarios.

new_data_to_dic = {'edad': 36, 'ocupación': 'Editora', 'pais':'Colombia'}
mi_dic.update(new_data_to_dic)

print(mi_dic)