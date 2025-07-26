"""SINTÁXIS: string.index(valor, desde donde, hasta donde )
   - valor: el string o letra que quieres encontrar
   - desde donde: es el índice(número), se incluye en el conteo
   - hasta donde: es el índice(número), se incluye en el conteo
"""

# PRÁCTICA 1
# Encuentra y muestra en pantalla qué caracter ocupa la quinta posición dentro de la siguiente palabra: "ordenador"

word =  "odernador"
indice = word[5]

print(indice)

#............................................................................................
# PRÁCTICA 2
# Encuentra y muestra en pantalla el índice de la primera aparición de la palabra "práctica" en la siguiente frase:
# "En teoría, la teoría y la práctica son lo mismos. En la práctica, no lo son."

word = "En teoría, la teoría y la práctica son lo mismos. En la práctica, no lo son."
indice = word.index("práctica")

print(indice)

#............................................................................................
# PRÁCTICA 3
# Encuentra y muestra en pantalla el índice de la última aparición de la palabra "práctica" en la siguiente frase:
# "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."

word = "En teoría, la teoría y la práctica son lo mismos. En la práctica, no lo son."
indice = word.rindex("práctica")

print(indice)
