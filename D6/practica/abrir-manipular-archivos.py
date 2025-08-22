""" Abrir y Manipular Archivos """

# PRÁCTICA 1
# Abre el archivo texto.txt e imprime su contenido.

abrir_texto = open('D6/practica/texto.txt')     # modo 'r', está por default, funciona así no se coloque
leer_texto = abrir_texto.read()

print(leer_texto)     # read(), se usa para leer el contenido de un archivo


#...........................................................................................
# PRÁCTICA 2
# Imprime la primera línea del archivo texto.txt

imprimir_first_line = abrir_texto.readline()      # Usa var de la L6

print(imprimir_first_line)


#...........................................................................................
# PRÁCTICA 3
# Abre el archivo texto.txt e imprime únicamente la segunda línea.

imprimir_second_line = abrir_texto.readline()      # Usa var de la L6

print(imprimir_second_line)



abrir_texto.close()     # Para cerrar texto.txt 