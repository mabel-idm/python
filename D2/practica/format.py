# PRÁCTICA 1
# Necesitamos imprimir el nombre y número de asociado dentro de la siguiente frase:
# Estimado/a (nombre_asociado), su número de asociado es: (numero_asociado)


nombre_asociado = "Sol"
numero_asociado = "10"

print(f"Estimada {nombre_asociado}, su número de asociado es: {numero_asociado}")

#............................................................................................
# PRÁCTICA 2
# Muestra al usuario la cantidad de puntos acumulados dentro de la siguiente frase:
# Has ganado (c) puntos! En total, acumulas (puntos_totales) puntos

puntos_nuevos = 5
puntos_totales = 15 + puntos_nuevos

print (f"Has ganado {puntos_nuevos} puntos! En total, acumulas {puntos_totales} puntos")

#............................................................................................
# PRÁCTICA 3
# Muestra al usuario la cantidad de puntos acumulados dentro de la siguiente frase:
# Has ganado (puntos_nuevos) puntos! En total, acumulas (puntos_totales) puntos
# En esta ocasión, la cantidad de puntos acumulados (totales) será igual a los puntos_anteriores más los puntos_nuevos.

puntos_nuevos = 3
puntos_anteriores = 20
puntos_totales = puntos_anteriores + puntos_nuevos 

print (f"Has ganado {puntos_nuevos} puntos! En total, acumulas {puntos_totales} puntos")