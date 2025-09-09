""" Manejo de Errores """

# PRÁCTICA 1
# Implementa para la siguiente función suma(), un manejador de errores simple que ante cualquier error, imprima en pantalla el mensaje: "Error inesperado". En caso contrario, deberá limitarse a mostrar el resultado de la suma entre los dos números.

def suma():
    number_one = int(input('Escribe un número: '))
    number_two = int(input('Escribe otro número: '))
    return number_one + number_two

try:
    print(suma())
except:
    print("Error inesperado.")

#...........................................................................................
# PRÁCTICA 2
# Implementa para la siguiente función cociente(), un manejador de errores:
# Ante un error de tipo (ValueError), debe imprimir en pantalla el mensaje: "Los argumentos a ingresar deben ser números"
# Si se generara una división por cero (error del tipo ZeroDivisionError), el mensaje mostrado debe ser: "El segundo argumento no debe ser cero"
# En caso que no se produzca un error, deberá limitarse a imprimir el resultado del cociente entre los dos números entregados como argumento.

def cociente():
    number_one = int(input('Escribe un número: '))
    number_two = int(input('Escribe otro número: '))
    return number_one / number_two

try:
    print(cociente())
except ValueError:   
    print("Los argumentos a ingresar deben ser números")
except ZeroDivisionError:
    print("El segundo argumento no debe ser cero")

#...........................................................................................
# PRÁCTICA 3
# Implementa un manejador de errores dentro de la siguiente función, abrir_archivo():
# En caso de que el archivo que se intenta abrir no pueda ser hallado (FileNotFoundError), mostrar en pantalla el mensaje: "El archivo no fue encontrado"
# En caso de que otro tipo de error ocurra, mostrar el mensaje: "Error desconocido"
# Si no se produce ningún error, imprimir en pantalla: "Abriendo exitosamente"
# En todos los casos, al finalizar, imprimir: "Finalizando ejecución"

def abrir_archivo():
    pass

    try:
        print("Abriendo exitosamente")

    except FileNotFoundError:
        print("El archivo no fue encontrado.")

    except:
        print("Error desconocido")

    finally:
        print("Finalizando ejecucion.")