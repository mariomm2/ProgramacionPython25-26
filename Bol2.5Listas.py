
#Boletin 2.5. Listas

#Ejercicio 1. Sudoku
 
def comprobar_lista_numeros(lista):
    numeros = "123456789"
    i = 0
    correcto = True

    while i < len(numeros):
        if numeros[i] not in lista:
            correcto = False
        i+=1
    return correcto


def comprobar_filas(sudoku):
    i = 0
    correcto = True

    while i < 9:
        fila = ""
        j = 0
        while j < 9:
            fila = fila + str(sudoku[i][j])
            j+=1

        if not comprobar_lista_numeros(fila):
            correcto = False
        i+=1
    return correcto


def comprobar_columnas(sudoku):
    j = 0
    correcto = True

    while j < 9:
        columna = ""
        i = 0
        while i < 9:
            columna = columna + str(sudoku[i][j])
            i+=1

        if not comprobar_lista_numeros(columna):
            correcto = False
        j+=1
    return correcto


def comprobar_bloques(sudoku):
    correcto = True

    fila_bloque = 0
    while fila_bloque < 9:
        columna_bloque = 0

        while columna_bloque < 9:
            bloque = ""
            i = fila_bloque
            while i < fila_bloque + 3:
                j = columna_bloque
                while j < columna_bloque + 3:
                    bloque = bloque + str(sudoku[i][j])
                    j+=1
                i+=1

            if not comprobar_lista_numeros(bloque):
                correcto = False
            columna_bloque+=3
        fila_bloque+=3
    return correcto


def comprobar_sudoku(sudoku):
    resultado = True

    if not comprobar_filas(sudoku):
        resultado = False
    if not comprobar_columnas(sudoku):
        resultado = False
    if not comprobar_bloques(sudoku):
        resultado = False
    return resultado


#Ejercicio 2. Digito Control

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


"""

#Ejemplo Clase 9 Diciembre
lista = [[1,2,3,4,5],[6,7,8,9,10]]
numero_eliminado = lista[0].remove(8)
numero_eliminado = lista[1].pop()

lista[0].append(11)
lista[1].insert(2,12)

print()

"""