
#Boletin 5 Python
#Bucles avanzado

#Ejercicio 1

terminos = int(input("Introduce el numero de terminos: "))
numero = "9"
cadena = ""
suma = 0

for i in range(terminos):
    cadena+=numero  
    suma+=int(cadena) 
    print(cadena, end=" ")
print("La suma de la serie es:", suma)

#Ejercicio 2

#Opcion binario

altura=int(input("Introduce la altura de la piramide: "))
cadena=""
for i in range  (1, altura+1):
    if i%2==0:
        numero="0"
        cadena = numero+cadena
        print(cadena)
    else:
        numero="1"
        cadena = numero+cadena
        print(cadena)


#Opcion decimal

altura = int(input("Introduce la altura de la pirámide: "))
numero = 1

for i in range(1, altura+1):
    for j in range(i):
        print(numero, end=" ")
        numero+=1
    print()


#Ejercicio 3

numero = int(input("Introduce x: "))
terminos = int(input("Introduce los terminos: "))
suma = 0
signo = 1
potencia = 1

print("Los valores son:")
for i in range(terminos):
    valor = signo*(numero**potencia)
    print(valor)
    suma+=valor
    signo*=-1
    potencia+=2
print("La suma es:", suma)


#Ejercicio 4

terminos = int(input("Introduce los terminos: "))
numero = ""
suma = 0

print("Los valores son:")
for i in range(terminos):
    numero += "1"
    print(numero)
    suma+=int(numero)

print("La suma es:", suma)


#Ejercicio 5

num1 = int(input("Introduce el primer numero: "))
num2 = int(input("Introduce el segundo numero: "))
contador = 0
actual = num1 + 1
print("Los siguientes 10 numeros multiplos de", num2, "a partir de", num1, "son:")

while contador<10:
    if actual % num2==0:
        print(actual)
        contador+=1
    actual+=1


#Ejercicio 6

numero = int(input("Introduce un numero: "))
print("La secuencia es:")
print(numero, end=" ")

while numero != 1:
    if numero%2 == 0:
        numero = numero//2
    else:
        numero = 3 * numero + 1
    print(" - ", numero, end=" ")

print()

