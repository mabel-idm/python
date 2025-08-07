""" LOOP WHILE """

# PRÁCTICA 1
# Crea un Loop While que imprima en pantalla los números del 10 al 0, uno a la vez.

contador = 10

while contador >= 0:
    print(contador) # Se imprime el 10 antes de iniciar el Loop
    contador = contador -1


print()    
#...........................................................................................
# PRÁCTICA 2
# Crea un Loop While que reste de uno en uno los números desde el 50 al 0 (ambos números incluidos) con las siguientes condiciones:
# -  Si el número es divisible por 5, mostrar dicho número en pantalla 
# - Si el número no es divisible por 5, continuar ejecutando el loop sin mostrar el valor en pantalla

contador = 50

while contador >= 0:
    if contador % 5 == 0:
        print(contador)
    contador = contador -1


print()
#...........................................................................................
# PRÁCTICA 3
# Crea un loop For a lo largo de la siguiente lista de números, imprimiendo en pantalla cada uno de sus elementos, e interrumpe el flujo en el momento que encuentres un valor negativo:

lista_numeros = [4, 5, 8, 7, 6, 9, 8, 2, 4, 5, 7, 1, 9, 5, 6, -1, -5, 6, -6, -4, -3]

for numero in lista_numeros:
    if numero < 0:
        break
    print(numero)
