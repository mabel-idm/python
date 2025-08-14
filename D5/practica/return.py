""" Return """

# PRÁCTICA 1
# Crea una función llamada potencia que tome dos valores numéricos como argumentos. Deberá devolver el número que resulte de resolver una potencia, utilizando el primer número como base y el segundo como exponente.

def potencia(num1, num2):
    return num1**num2

resultado = potencia(5,2) 
print(resultado)


print()
#...........................................................................................
# PRÁCTICA 2
# Crea una función llamada usd_a_eur que tome como único parámetro un valor numérico (un monto en dólares estadounidenses) y devuelva como resultado el monto equivalente en euros. A fines de este ejemplo, tomaremos la conversión 1 USD = 0.90 EUR.
# Crea una variable llamada dolares y almacena en ella un monto cualquiera para entregárselo a tu función y evaluar su resultado.

def usd_a_eur(monto):
    return monto * 0.90

dolares =  usd_a_eur(50)
print(dolares)


print()
#...........................................................................................
# PRÁCTICA 3
# Crea una función llamada invertir_palabra que tome los caracteres de una palabra dada como argumento, invierta el orden de sus caracteres y los devuelva de ese modo en mayúsculas.
# También, crea una variable llamada palabra que contenga el string que tú prefieras, para suministrarle como argumento a la función creada.

def invertir_palabra(string):
    return string[::-1].upper()

palabra = invertir_palabra("Python")
print(palabra)