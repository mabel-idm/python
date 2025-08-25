""" Crear y Escribir Archivos """

# PRÁCTICA 1
# Abre el archivo llamado "otro_texto.txt", y cambia su contenido por el texto "Nuevo texto".
# Imprime el contenido completo de "otro_texto.txt" al finalizar.

# Abrir, cambiar y cerrar el texto
texto = open('D6/practica/otro_texto.txt', 'w')
cambiar_texto = texto.write('Nuevo Texto')
texto.close()

# Abrir, leer y cerrar el texto
texto = open('D6/practica/otro_texto.txt', 'r')
leer_texto = texto.read()
texto.close()

print(leer_texto)


#...........................................................................................
# PRÁCTICA 2
# Abre el archivo llamado "mi_archivo.txt", y añade una línea al final del mismo que diga: "Nuevo inicio de sesión".
# Imprime el contenido completo de "mi_archivo.txt" al finalizar.

texto = open('D6/practica/otro_texto.txt', 'a')
add_line = texto.write('\nNuevo inicio de sesión')
texto.close()

texto = open('D6/practica/otro_texto.txt', 'r')
leer_texto = texto.read()
texto.close()

print(leer_texto)


#...........................................................................................
# PRÁCTICA 3
# Utiliza el método writelines para escribir los valores de la siguiente lista al final del archivo "otro_texto.txt" . Inserta un tabulador entre cada elemento de la lista para separarlos.

registro_ultima_sesion = ["Federico\n", "20/12/2021\n", "08:17:32 hs\n", "Sin errores de carga\n"]

texto = open('D6/practica/otro_texto.txt', 'w')
add_lista_values = texto.writelines(registro_ultima_sesion)
texto.close()

texto = open('D6/practica/otro_texto.txt', 'r')
leer_texto = texto.read()
texto.close()

print(leer_texto)