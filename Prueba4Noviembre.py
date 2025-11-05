
#Ejercicio DNI Valido

#Primera forma

LETRAS = "TRWAGMYFPDXBNJZSQVHLCKE"

def es_dni_valido(dni):
    valido = False

    if 8<=len(dni)<=9: # len(dni)>=8 and len(dni)<=9
        resto = int(dni[:-1])%23
        letra = LETRAS[resto]
        valido = letra==dni[-1]

    return valido

#Tests

assert(not es_dni_valido("11111111L"))
assert(not es_dni_valido("11111L"))
assert(es_dni_valido("11111111H"))


#Segunda forma

def es_dni_valido_refactor(dni):
    return 8<=len(dni)<=9 and LETRAS[int(dni[:-1])%23]==dni[-1]

#Tests

assert(not es_dni_valido_refactor("11111111L"))
assert(not es_dni_valido_refactor("11111L"))
assert(es_dni_valido_refactor("11111111H"))

