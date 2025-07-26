# NOTA:
# Se usa round(número_a_redondear, decimales al costado)
# Si es que no se especifica decimales, Python lo interpreta como "sin decimales"
# Pyhton redondea así: decimal ≥ 5 ∴ redondeo hacia arriba, decimal < 5 ∴ redondeo hacia abajo

# PRÁCTICA 1
# Redondea el resultado de la división 10/3 a un número con 2 decimales, y muestra en pantalla el valor redondeado.

div = 10 / 3
print(round(div))

#............................................................................................
# PRÁCTICA 2
# Redondea el número 10.676767 al entero más próximo, y muestra en pantalla el resultado.

number = 10.676767
print(round(number))

#............................................................................................
# PRÁCTICA 3
# Calcula la raíz cuadrada de 5, y muestra en pantalla el resultado redondeado con 4 posiciones decimales.

root = 5**0.5
print(round(root, 5))