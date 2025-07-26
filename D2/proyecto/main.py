"""PROYECTO - DÍA 2"""
# Situación: trabajas en una empresa donde los vendedores reciben comisiones
# del 13% por sus ventas totales, y tu jefe quiere que ayudes a los vendedores a calcular sus
# comisiones creando un programa que les pregunte su nombre y cuánto han vendido en este
# mes. Tu programa le va a responder con una frase que incluya su nombre y el monto que le
# corresponde por las comisiones.

name = input("¿Cúal es tu nombre? ")
sale = int(input("¿Cuánto vendiste este mes? "))  # Conversión a integer, fuera del input
commission = round((sale * 0.13), 2)

print(f"Hola {name}, tu comisión es de $ {commission}")