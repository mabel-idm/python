""" CONSOLA DE TURNOS """


from numbers import perfumeria, farmacia, cosmetica

perf = perfumeria()
farm = farmacia()
cosm = cosmetica()

def elegir_area():

    area = input('A que área te diriges: ')
    if area == 'Perfumería':
        print(next(perf))
    elif area == 'Farmacia':
        print(next(farm))
    elif area == 'Cosmética':
        print(next(cosm))

while True:
    elegir_area()

    otro_turno = input("¿Quieres otro turno? (Si/No): ")
    if otro_turno != "Si":
        break