""" EXPRESIONES REGULARES """

import re

# PRÁCTICA 1
# Crea una función llamada verificar_email para comprobar si una dirección de email es correcta, que verifique si el email dado como argumento contiene "@" (entre el nombre de usuario y el dominio) y finaliza en ".com"
# Si se encuentra el patrón, la función debe finalizar mostrando en pantalla el mensaje "Ok", pero si detecta que la frase no contiene los elementos indicados, debe informarle al usuario "La dirección de email es incorrecta" imprimiendo el mensaje.

def verificar_email(email):

    patron =  r"\D+\@\D+\.com"

    if re.search(patron,email):
        print ("OK")
    else:
        print("La dirección de email es incorrecta.")
    
un_email = "usuario@gmail.com"
verificar_email(un_email)


#...........................................................................................
# PRÁCTICA 2
# Crea una función llamada verificar_saludo para verificar si una frase entregada como argumento inicia con la palabra "Hola". Si se encuentra el patrón, la función debe finalizar mostrando el mensaje "Ok", pero si detecta que la frase no contiene "Hola", debe informarle al usuario "No has saludado" imprimiendo el mensaje en pantalla.

def verificar_saludo(frase):

    patron = r"^Hola"

    if re.search(patron,frase):
        print("OK")
    else:
        print("No has saludado.")

una_frase = "Hola ¿cómo estás?"
verificar_saludo(una_frase)


#...........................................................................................
# PRÁCTICA 3
# El código postal de una región determinada se forma a partir de dos caracteres alfanuméricos y cuatro numéricos a continuación (ejemplo: XX1234). Crea una función, llamada verificar_cp para comprobar si el código postal pasado como argumento sigue este patrón. Si el patrón es correcto, mostrar al usuario el mensaje "Ok", de lo contrario: "El código postal ingresado no es correcto".

def verificar_cp(codigo_postal):

    patron = r"^[A-Z]{2}\d{4}$"

    if re.search(patron, codigo_postal):
        print("OK")
    else:
        print("El código postal ingresado no es correcto.")

un_codigo_postal = "AZ1234"
verificar_cp(un_codigo_postal)