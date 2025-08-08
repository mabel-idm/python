""" 
COMPRENSIÓN DE LISTAS 
    [<expresión> for <elemento> in <iterable> if <condición>]
"""


# PRÁCTICA 1
# Crea una lista llamada valores_cuadrado, formada por los números de la lista valores, elevados al cuadrado.

valores = [1, 2, 3, 4, 5, 6, 9.5]

'''
valores_cuadrado = []

for valor in valores:
    valores_cuadrado.append(valor**2)

print(valores_cuadrado)
'''


valores_cuadrado = [valor**2 for valor in valores]
print(valores_cuadrado)


print()
#...........................................................................................
# PRÁCTICA 2
# Crea una lista valores_pares formada por los números de la lista valores que sean pares.

valores = [1, 2, 3, 4, 5, 6, 9.5]

''' 
valores_pares = []

for valor in valores:
    if valor % 2 == 0:
        valores_pares.append(valor)

print (valores_pares)
'''

valores_pares = [valor for valor in valores if valor % 2 == 0]
print(valores_pares)


print()
#...........................................................................................
# PRÁCTICA 3
# Para la siguiente lista de temperaturas en grados Fahrenheit, expresa estos mismos valores en una nueva lista de temperaturas en grados Celsius usando la fórmula:
# °C = (°F − 32) × (5/9)
# Almacena la nueva lista en una variable llamada grados_celsius.

temperatura_fahrenheit = [32, 212, 275]

'''
grados_celsius = []

for grado_fahrenheit in temperatura_fahrenheit:
    grados_celsius.append((grado_fahrenheit - 32) * (5/9))

print(grados_celsius)
'''

grados_celsisus = [((grado_fahrenheit -32) * (5/9)) for grado_fahrenheit in temperatura_fahrenheit]
print(grados_celsisus)