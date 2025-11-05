
#Ejercicios de prueba de estructuras de datos

cadena = "Hola"

lista_numeros = [1, 3, 5, 7, 9]

for i in range (len(lista_numeros)):
    print(i, lista_numeros[i])

for elemento in lista_numeros:
    print(elemento)

print(lista_numeros[0])


"------------------------------------------------------------------------"

#Primeros 50 numeros pares

lista_pares = []

for i in range(1, 50):
    lista_pares.append(i*2)

print(lista_pares)
