
def calcular_primer_dig(entidad, sucursal):
    pesos_entidad = [4, 8, 5, 10]
    pesos_sucursal = [9, 7, 3, 6]
    suma = 0

    for i in range(4):
        suma += int(entidad[i]) * pesos_entidad[i]

    for i in range(4):
        suma += int(sucursal[i]) * pesos_sucursal[i]

    resto = 11 - (suma % 11)

    digito = resto
    if resto == 11:
        digito = 0
    elif resto == 10:
        digito = 1

    return digito


def calcular_segundo_dig(numero):
    pesos = [1, 2, 4, 8, 5, 10, 9, 7, 3, 6]
    suma = 0

    for i in range(10):
        suma += int(numero[i]) * pesos[i]

    resto = 11-(suma % 11)

    digito = resto
    if resto == 11:
        digito = 0
    elif resto == 10:
        digito = 1

    return digito


def validar_ccc(cuenta):
    es_valida = False

    if len(cuenta) == 20:

        entidad = cuenta[0:4]
        sucursal = cuenta[4:8]
        dc1 = int(cuenta[8])
        dc2 = int(cuenta[9])
        numero = cuenta[10:]

        dc1_calc = calcular_primer_dig(entidad, sucursal)
        dc2_calc = calcular_segundo_dig(numero)

        if dc1 == dc1_calc and dc2 == dc2_calc:
            es_valida = True

    return es_valida


