

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


"""
lista = [[1,2,3,4,5],[6,7,8,9,10]]
numero_eliminado = lista[0].remove(8)
numero_eliminado = lista[1].pop()

lista[0].append(11)
lista[1].insert(2,12)

print("/n")

"""