

#Ejercicio 1

from random import randint

def generar_numeros():
    numeros = []
    for i in range(1000):
        numeros.append(randint(1, 2000))
    return numeros

#Apartado a

def numero_mayor(numeros):
    mayor = numeros[0]
    for n in numeros:
        if n > mayor:
            mayor = n
    return mayor

#Apartado b

def numero_menor(numeros):
    menor = numeros[0]
    for n in numeros:
        if n < menor:
            menor = n
    return menor

#Apartado c

"--------------------------------------"

#Ejercicio 2

def desplazar(lista):
    ultimo = lista[-1]
    nueva = [ultimo]
    i = 0
    while i < len(lista) - 1:
        nueva = nueva + [lista[i]]
        i+=1
    return nueva

nums = [1,2,3,4,5,6,7,8,9,10]
print(desplazar(nums))

#Ejercicio 3

def reverse(lista):
    nueva = []
    i = len(lista)-1
    while i >= 0:
        nueva = nueva + [lista[i]]
        i-=1
    return nueva

print(reverse(["Di", "buen", "dia", "a", "papa"]))

#Ejercicio 4

def esta_ordenada(lista):
    i = 0
    ordenada = True

    while i < len(lista) - 1:
        if lista[i] > lista[i+1]:
            ordenada = False
        i +=1

    return ordenada

print(esta_ordenada([1,2,3,4,5]))
print(esta_ordenada([3,2,1]))

#Ejercicio 5

def encajan(fichas):
    i = 0
    correcto = True

    while i < len(fichas) - 1:
        if fichas[i][-1] != fichas[i+1][0]:
            correcto = False
        i +=1

    return correcto

print(encajan(["34", "45", "56"]))  
print(encajan(["34", "25", "56"]))  


#Ejercicio 6

def intersect(lista1, lista2):
    nueva = []
    for x in lista1:
        if (x in lista2) and (x not in nueva):
            nueva = nueva + [x]
    return nueva

print(intersect([1,2,3,4],[3,4,5,6]))

#Ejercicio 7

def union_listas(lista1, lista2):
    nueva = []
    for x in lista1:
        if x not in nueva:
            nueva = nueva + [x]


#Ejercicio 8

#Ejercicio 9

