""" CONTROL DE FLUJO """

# PRÁCTICA 1
# Utilizando las variables num1 y num2, que se alimentan con el input del usuario:
# Crea una estructura de control de flujo que compare los valores de las variables y arroje un resultado de acuerdo al caso:
# "num1 es mayor que num2"
# "num2 es mayor que num1"
# "num1 y num2 son iguales"
# Debes mostrar en pantalla el valor de las variables ingresadas en lugar de num1 y num2.
# Aclaración: No deben imprimirse strings adicionales a la respuesta del usuario.


num1 = int(input("Ingresa un número: "))
num2 = int(input("Ingresa un número: "))

if num1 > num2:
    print(f"{num1} es mayor que {num2}")
elif num2 > num1:
    print(f"{num2} es mayor que {num1}")    
elif num1 == num2:
    print(f"{num1} es igual que {num2}")


#...........................................................................................
# PRÁCTICA 2
# Las leyes de un país establecen que un adulto puede conducir si tiene licencia para hacerlo, y para optar por una licencia para conducir, debe tener 18 años o más.
# Crea una estructura condicional para verificar si una persona de 16 años sin licencia puede conducir, y muestra el resultado que corresponda en pantalla:
# "Puedes conducir"
# "No puedes conducir aún. Debes tener 18 años y contar con una licencia"
# "No puedes conducir. Necesitas contar con una licencia"


age = int(input("Ingresa tu edad: "))
driver_license = input("¿Tienes licencia? Escribe si o no: ").lower()

if age >= 18 and driver_license == "si":
    print("Puedes conducir")
elif age >= 18 and driver_license == "no":
    print("No puedes conducir. Necesitas contar con una licencia")
elif age < 18:
    print("No puedes conducir aún. Debes tener 18 años y contar con una licencia")


#...........................................................................................
# PRÁCTICA 3
# Para acceder a un determinado puesto de trabajo, el candidato debe ser capaz de programar en Python y tener conocimientos de inglés.
# Crea una estructura condicional para evaluar a un candidato dadas estas condiciones, y muestra el mensaje correspondiente en pantalla:
# "Cumples con los requisitos para postularte"
# "Para postularte, necesitas saber programar en Python y tener conocimientos de inglés"
# "Para postularte, necesitas tener conocimientos de inglés"
# "Para postularte, necesitas saber programar en Python"
# Evalúa a un candidato que sabe inglés, pero no programa en Python.


python = input("¿Sabes programar en python? Escribe si o no: ").lower()
english = input("¿Tienes conocimientos en inglés? Escribe si o no: ").lower()

if python == "si" and english == "si":
    print("Cumples con los requisitos para postularte")
elif python == "no" and english == "no":
    print("Para postularte, necesitas saber programar en Python y tener conocimientos en inglés")
elif python == "si" and english == "no":
    print("Para postularte, necesitas tener conocimientos de inglés")
elif python == "no" and english == "si":
    print("Para postularte, necesitas saber programar en Python")