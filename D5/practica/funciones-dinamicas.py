""" FUNCIONES DINÁMICAS """

# PRÁCTICA 1
# Crea una función llamada todos_positivos que reciba una lista de números como parámetro y devuelva True si todos los valores de la lista son positivos, y False si al menos uno de los valores es negativo.
# Crea una lista llamada lista_numeros con valores positivos y negativos.


def todos_positivos(lista_numeros):

    for numero in lista_numeros:
        if numero > 0:
            return True
        else:
            return False

print(todos_positivos([-1, 8, 45, 67]))


print()
#...........................................................................................
# PRÁCTICA 2
# Crea una función llamada suma_menores que sume los números de una lista (almacenada en la variable lista_numeros) siempre y cuando sean mayores a 0 y menores a 1000, y devuelva el resultado de dicha suma.


def suma_menores(lista_numeros):

    new_list = []

    for numero in lista_numeros:
        if 0 < numero < 1000:
            new_list.append(numero)
    return sum(new_list)

print(suma_menores([1,2,-3,-4,5,10]))


print()
#...........................................................................................
# PRÁCTICA 3
# Crea una función llamada cantidad_pares que cuente la cantidad de números pares que existen en una lista (lista_numeros), y devuelva el resultado de dicha cuenta.

def cantidad_pares(lista_numeros):

    new_list = []

    for numero in lista_numeros:
        if numero % 2 == 0:
            new_list.append(numero)
    return len(new_list)

print(cantidad_pares([1,2,4,-5,8]))