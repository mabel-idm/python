""" ARGS 
        def nombre_función(*args)  
        --> La palabra 'arg' es reemplazable por cualquier otra, lo importante es que vaya acompañada de un *
        --> (*args) es una tupla
"""

# PRÁCTICA 1
# Crea una función llamada suma_cuadrados que tome una cantidad indeterminada de argumentos numéricos, y que retorne la suma de sus valores al cuadrado.

def suma_cuadrados(*args):

    total = 0

    for arg in args:
        total = total + arg**2
    return total
    
print(suma_cuadrados(1,2,3,4,5))

#...........................................................................................
# PRÁCTICA 2
# Crea una función llamada suma_absolutos, que tome un conjunto de argumentos de cualquier extensión, y retorne la suma de sus valores absolutos (es decir, que tome los valores sin signo y los sume, o lo que es lo mismo, los considere a todos -negativos y positivos- como positivos).

def suma_absolutos(*args):

    total = 0

    for arg in args:
        total = total + abs(arg)  # abs() --> Convierte cada argumento en un número absoluto 
    return total

print(suma_absolutos(-1,1,-1,1,-1,1))
    
#...........................................................................................
# PRÁCTICA 3
# Crea una función llamada numeros_persona que reciba, como primer argumento, un nombre, y a continuación, una cantidad indefinida de números.
# La función debe devolver el siguiente mensaje:
# "{nombre}, la suma de tus números es {suma_numeros}"


def numeros_persona(*args):
    primer_argumento = args[0]
    resto_argumentos = args[1:]

    print(f"{primer_argumento}, la suma de tus números es {sum(resto_argumentos)}")

numeros_persona("Hola",1,2,3,4,5)
