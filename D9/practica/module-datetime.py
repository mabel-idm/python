""" MÓDULO DATETIME """

import datetime

# PRÁCTICA 1
# Crea un objeto fecha llamado mi_fecha que almacene el día 3 de febrero de 1999

mi_fecha = datetime.date(1999, 2, 3)

print(mi_fecha)

#...........................................................................................
# PRÁCTICA 2
# Crea un objeto en la variable hoy que siempre almacene la fecha actual cuando sea invocada.

fecha_actual = datetime.date.today()
print(fecha_actual)

#...........................................................................................
# PRÁCTICA 3
# En una variable llamada minutos, almacena únicamente los minutos de la hora actual.
# Por ejemplo, si se ejecutara a las 20:43:17 de la noche, la variable minutos debe almacenar el valor 43

hora_actual = datetime.datetime.today()
minutos = hora_actual.minute
print(minutos)