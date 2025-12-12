
#Ejercicio 3. Cuadrados Magicos.

#Apartado A.

def es_cuadrado_magico(matriz):
    numero=len(matriz)
    es_magico=True
    suma_total=0
    
    j=0
    while j<numero:
        suma_total+=matriz[0][j]
        j+=1


    i=0 
    while i<numero:
        suma_fila=0   
        j=0
        while j<numero:
            suma_fila+=matriz[i][j]
            j+=1
        if suma_fila!=suma_total:
            es_magico= False
        i+=1

    j=0
    while j<numero:
        suma_columna=0
        i=0
        while i<numero:
            suma_columna+=matriz[i][j]
            i+=1
        if suma_columna!=suma_total:
            es_magico=False
        j+=1

    diagonal_principal=0
    i=0    
    while i<numero:
        diagonal_principal+=matriz[i][i]
        i+=1
    if diagonal_principal!=suma_total:
        es_magico=False
    
    diagonal_inversa=0
    i=0
    while i<numero:
        diagonal_inversa+=matriz[i][numero-1-i]
        i+=1
    if diagonal_inversa!=suma_total:
        es_magico=False
    
    return es_magico        


#Apartado B.

#def es_cuadrado_magico_ampliada(matriz):



#Tests

matriz_vale=[[8,1,6],[3,5,7],[4,9,2]]
matriz_no_vale=[[2,7,6],[9,5,1],[4,3,9]]

assert(es_cuadrado_magico(matriz_vale))
assert(not es_cuadrado_magico(matriz_no_vale))

print("Tests superados")