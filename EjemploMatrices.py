
#Ejemplo Matrices

"""
matriz = [ [9,0,0], [0,5,0], [0,0,7] ]

for fila in matriz:
    linea = ""
    for n in fila:
        linea = linea + str(n) + " "
    print(linea)
"""

#Ejemplo Matrices Resuelto Clase

def imprimir_matriz(matriz):
    matriz_final = ""

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz_final += str(matriz[i][j]) + " "
        matriz_final += "\n"
    return matriz_final[:-1]

#print(imprimir_matriz([[9,0,0,4],[0,5,0,1,1],[0,0,7]]))


#Ejemplo Suma

matriz1 = [[9, 0, 0], [0, 5, 0], [0, 0, 7]]
matriz2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def sumar_matrices(m1, m2):
    matriz_suma = []

    i = 0
    while i < len(m1):
        fila = []
        j = 0
        while j < len(m1[i]):
            fila.append(m1[i][j] + m2[i][j])
            j = j + 1
        matriz_suma.append(fila)
        i = i + 1

    return matriz_suma


resultado = sumar_matrices(matriz1, matriz2)
print(imprimir_matriz(resultado))