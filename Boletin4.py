
#Boletin 4 Bucles

#Ejercicio 1 

#Con for:

num1 = int(input("Introduce el primer numero: "))
num2 = int(input("Introduce el segundo numero: "))

if num1<num2:
    for i in range(num1+1, num2):
        print(i)
elif num2<num1:
    for i in range(num2+1, num1):
        print(i)
else:
    print("No hay numeros entre ellos.")

#Con while:

num1 = int(input("Introduce el primer numero: "))
num2 = int(input("Introduce el segundo numero: "))

if num1<num2:
    actual = num1+1
    while actual<num2:
        print(actual)
        actual+=1
elif num2<num1:
    actual = num2+1
    while actual<num1:
        print(actual)
        actual+=1
else:
    print("No hay numeros entre ellos.")
    

#Ejercicio 2

numero = int(input("Introduce un numero: "))
i = 1

while i <= 10:
    resultado = numero*i
    print(numero, "por", i, "=", resultado)
    i+=1


#Ejercicio 3    

#Con for

num1 = int(input("Introduce el primer numero: "))
num2 = int(input("Introduce el segundo numero: "))

if num1>num2:
    nuevo = num1
    num1 = num2
    num2 = nuevo
print("Los numeros entre", num1, "y", num2, "multiplos de 11 son:")

for i in range(num1, num2+1):
    if i%11 == 0:
        print(i)

#Con while

num1 = int(input("Introduce el primer numero: "))
num2 = int(input("Introduce el segundo numero: "))

if num1 > num2:
    nuevo = num1
    num1 = num2
    num2 = nuevo

print("Los numeros entre", num1, "y", num2, "multiplos de 11 son:")

actual = num1
while actual<=num2:
    if actual%11 == 0:
        print(actual)
    actual+=1


#Ejercicio 4

contador=0
suma=0
maximo=0
numero = int(input("Introduce el un numero (Del 1 al 10000): "))

while numero>=1 and numero<=10000:
    contador+=1
    suma = suma+numero
    if numero > maximo:
        maximo=numero
    numero = int(input("Introduce un numero (Del 1 al 1000): "))

if contador>0:
    media = suma/contador
    print("Se han introducido", contador, "numeros, siendo el valor maximo", maximo, "y la media", media)
else:
    print("Numero no valido.")


#Ejercicio 5

#Con while

numero = int(input("Introduce un numero: "))

while numero <= 0:
    print("El numero debe ser positivo.")
    numero = int(input("Introduce un numero positivo: "))

suma = 0
contador = 1

while contador <= numero:
    suma = suma + contador
    contador+=1
print("La suma de los numeros del 1 al", numero, "es:", suma)

#Con for

numero = int(input("Introduce un numero positivo: "))

while numero<=0:
    print("El numero debe ser positivo.")
    numero = int(input("Introduce un numero positivo: "))

suma = 0
for i in range(1, numero+1):
    suma+=i
print("La suma de los numeros entre 1 y", numero, "es:", suma)

#Sin bucles

numero=int(input("Introduce un numero positivo: "))

if numero>0:
    suma = numero*(numero+1)//2
    print("La suma de los numeros entre 1 y", numero, "es:", suma)
else:
    print("El numero debe ser positivo.")
 

#Ejercicio 6

num1 = int(input("Introduce el primer numero: "))
while num1 <= 0:
    num1 = int(input("Debe ser positivo. Introduce el primer numero: "))

num2 = int(input("Introduce el segundo numero: "))
while num2 <= 0:
    num2 = int(input("Debe ser positivo. Introduce el segundo numero: "))

if num1 > num2:
    num1, num2 = num2, num1

suma = 0
for i in range(num1, num2+1):
    suma+=i

print("La suma de los numeros entre", num1, "y", num2, "es:", suma)


#Ejercicio 7

numero = int(input("Introduce un numero (menor que 100 termina): "))
mayor = 0

while numero >= 100:
    if numero > mayor:
        mayor = numero
    numero = int(input("Introduce otro numero (menor que 100 termina): "))

print("El numero mayor es:", mayor)


#Ejercicio 8

num1 = int(input("Introduce el primer numero: "))
num2 = int(input("Introduce el segundo numero: "))

resultado=0
signo=1

if num1 < 0:
    num1 = -num1
    signo = signo * -1

if num2 < 0:
    num2 = -num2
    signo = signo * -1

for i in range(num2):
    resultado = resultado+num1

resultado = resultado*signo
print("El resultado es:", resultado)


#Ejercicio 9

num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

if num2 == 0:
    print("No se puede dividir entre cero.")
else:
    resto = num1
    while resto >= num2:
        resto -= num2
    while resto < 0:
        resto += num2
    print("El resto de", num1, "entre", num2, "es:", resto)


#Ejercicio 10

cantidad = int(input("Cantidad de numeros positivos: "))
while cantidad <= 0:
    cantidad = int(input("Debe aer positivo. Introducelo de nuevo: "))

contador = 0
suma = 0
mayor = 0
menor = 0

while contador < cantidad:
    numero = int(input("Introduce un num positivo: "))
    while numero <= 0:
        numero = int(input("DDebe ser positivo. Introducelo de nuevo: "))

    if contador == 0:
        mayor = numero
        menor = numero
    else:
        if numero > mayor:
            mayor = numero
        if numero < menor:
            menor = numero

    suma += numero
    contador += 1

media = suma / cantidad
print("Media:", media, " Mayor:", mayor, " Menor:", menor)


#Ejercicio 11

altura = int(input("Introduce la altura: "))

for i in range(1, altura + 1):
    espacios = altura-i
    estrellas = 2*i-1
    print(" " * espacios + "*" * estrellas)


#Ejercicio 12

num = int(input("Introduce un numero: "))

while num <= 0:
    num = int(input("Debe ser positivo. Introducelo de nuevo: "))

suma = 0
for i in range(1, num):
    if num % i == 0:
        suma += i

if suma == num:
    print(num, "es perfecto")
else:
    print(num, "no es perfecto")


#Ejercicio 13

num = int(input("Introduce el num de terminos: "))

suma = 0

print("Los terminos son:")

for i in range(1, num+1):
    print("1 /", i)
    suma+=1/i

print("La suma hasta", num, "terminos es:", suma)


