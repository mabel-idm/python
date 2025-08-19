""" INTERACCIÓN ENTRE FUNCIONES """

# PRÁCTICA 1
# Crea una función (lanzar_dados) que arroje dos dados al azar y devuelva sus resultados (valores entre 1 y 6). La función no debe requerir argumentos y generará internamente los valores aleatorios. Luego, proporciona el resultado de estos dos dados a una segunda función llamada evaluar_jugada (que reciba dos argumentos) y que retorne un mensaje según la suma de estos valores:
# Si la suma es menor o igual a 6: "La suma de tus dados es {suma_dados}. Lamentable"
# Si la suma es mayor a 6 y menor a 10: "La suma de tus dados es {suma_dados}. Tienes buenas chances"
# # Si la suma es mayor o igual a 10: "La suma de tus dados es {suma_dados}. Parece una jugada ganadora".

from random import randint, choice

def lanzar_dados():
    dado_uno = randint(1,6)
    dado_dos = randint(1,6)
    suma_dados = dado_uno + dado_dos
    return suma_dados

def evaluar_jugada():

    resultado = lanzar_dados()

    if resultado <= 6:
        print(f"La suma de tus dados es {resultado}. Lamentable.")
    elif 6 < resultado < 10:
        print(f"La suma de tus dados es {resultado}. Tienes buenas chances.")
    elif resultado >= 10:
        print(f"La suma de tus dados es {resultado}. Parece una jugada ganadora.")

evaluar_jugada()

#...........................................................................................
# PRÁCTICA 2
# Crea una función llamada reducir_lista() que tome una lista como argumento (crea también la variable lista_numeros) y devuelva la misma lista pero eliminando duplicados (dejando solo un ejemplar de cada número) y eliminando el valor más alto. El orden de los elementos puede modificarse.
# Por ejemplo:
# Si se proporciona la lista [1, 2, 15, 7, 2] debe devolver [1, 2, 7].
# Crea también una función llamada promedio() que reciba como argumento la lista devuelta por la función anterior y calcule el promedio de sus valores. Debe devolver el resultado, sin imprimirlo.

def reducir_lista():

    lista_numeros = [1,2,3,4,4,5] 
    lista_reducida = []

    for number in lista_numeros:
        if number not in lista_reducida:
            lista_reducida.append(number)
    return lista_reducida

def promedio(lista):
    prom = sum(lista) / len(lista)
    return prom

print(promedio(reducir_lista()))

#...........................................................................................
# PRÁCTICA 3
# Crea una función llamada lanzar_moneda que devuelva el resultado de lanzar una moneda (al azar), pudiendo ser "Cara" o "Cruz", sin recibir argumentos.
# Crea una segunda función llamada probar_suerte que reciba dos argumentos:
# El resultado del lanzamiento de la moneda.
# Una lista de números cualquiera (crea una lista con valores y asígnala a la variable lista_numeros).
# Reglas:
# Si el primer argumento es "Cara", mostrar "La lista se autodestruirá" y devolver la lista vacía [].
# Si es "Cruz", mostrar "La lista fue salvada" y devolver la lista intacta.

def lanzar_moneda():
    return choice(["Cara", "Cruz"])

def probar_suerte(resultado, lista):

    if resultado == "Cara":
        lista.clear()
        print(f"La lista se autodestruirá: {lista}")
    else:
        print(f"La lista quedo intacta: {lista}")

probar_suerte(lanzar_moneda(), [1,2,3])