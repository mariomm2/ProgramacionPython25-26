
#Ejercicio Clase AdventOfCode.

file = open("/home/estudiante/Downloads/elfos.txt")

dial_inicio=50
dial_numeros=100
posicion_act=dial_inicio
contador=0

for line in file:
    direccion=line[0]
    pasos=int(line[1:])
    
    if direccion=="L":
        pasos=dial_numeros-pasos
    posicion_act=(posicion_act + pasos) % dial_numeros
    if posicion_act ==0:
        contador+=1
print(contador)

print(line.replace("\n", ""))