
#Ejercicios de prueba de bucles

for i in range(10, -1, -1):
    print(i)

for i in range (11):
    print(10-i)

for i in range (11):
    print(-i+10)

"----------------------------------------"
    
numero = int(input("Introduce un numero: "))

for i in range(1, 11):
    print(numero, "por", i, "=", numero*i)

numero = int(input("Introduce un numero: "))
final=0

for i in range(1, 11): 
    final = final+numero 
    print(numero, "x", i, "=", final)


numero = int(input("Introduce un numero: "))
resultado = numero*1

for i in range(1, 11):
    print(numero, "por", i, "=", resultado)
    resultado = resultado + numero   

for i in range(1, 4):
    print(i)

contador = 1
while contador<=3:
    print(contador)
    contador = contador+1
