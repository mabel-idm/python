""" Archivos y Funciones """

# PRÁCTICA 1
# Crea una función llamada abrir_leer() que abra (open) un archivo indicado como parámetro, y devuelva su contenido (read).

def abrir_leer(ruta_texto):
    abrir_texto = open(ruta_texto, 'r')
    leer_texto = abrir_texto.read()
    abrir_texto.close()
    return leer_texto

texto = abrir_leer('D6/practica/otro_texto_dos.txt')
print(texto)


#...........................................................................................
# PRÁCTICA 2
# Crea una función llamada sobrescribir() que abra (open) un archivo indicado como parámetro, y sobrescriba cualquier contenido anterior por el texto "Contenido eliminado."

def sobrescribir(ruta_texto):
    abrir_texto = open(ruta_texto, 'w')
    sobrescribir_texto = abrir_texto.write('Contenido eliminado.')
    abrir_texto.close()
    return sobrescribir_texto

sobrescribir('D6/practica/otro_texto_dos.txt')
texto_sobrescrito = abrir_leer('D6/practica/otro_texto_dos.txt')     # Llama a la fx de arriba -'abrir_leer' - para que muestre el testo sobrescrito 
print(texto_sobrescrito)


#...........................................................................................
# PRÁCTICA 3
# Crea una función llamada registro_error() que abra (open) un archivo indicado como parámetro, y lo actualice añadiendo una línea al final que indique "se ha registrado un error de ejecución". Finalmente, debe cerrar el archivo abierto.

def registro_error(ruta_texto):
    abrir_texto = open(ruta_texto, 'a')
    agregar_texto = abrir_texto.write('\nSe ha registrado un error.')
    abrir_texto.close()
    return agregar_texto

registro_error('D6/practica/otro_texto_dos.txt')
texto_agregado = abrir_leer('D6/practica/otro_texto_dos.txt')     # Igual, llama a 'abrir_leer'
print(texto_agregado)