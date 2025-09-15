""" CONSOLA DE TURNOS """


def perfumeria():

    contador_perfumeria = 1

    while True:
        yield f"Tu turno es: P-{contador_perfumeria}"
        contador_perfumeria += 1


def farmacia():

    contador_farmacia = 1

    while True:
        yield f"Tu turno es: F-{contador_farmacia}"
        contador_farmacia += 1


def cosmetica():

    contador_cosmetica = 1

    while True:
        yield f"Tu turno es: C-{contador_cosmetica}"
        contador_cosmetica += 1