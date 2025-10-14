
# Ejercicios de prueba de condicionales

edad = 15

print(18<=edad<=65, edad >=18 and edad <=65, not(edad<18 or edad>65))

"-----------------------------------------------------------------------"

color_semaforo = "M"

print(color_semaforo!="R" and color_semaforo!="V" and color_semaforo!="A")
print(color_semaforo=="R" or color_semaforo=="V" or color_semaforo=="A")

"-----------------------------------------------------------------------"

dia=input("Introduce un dia de la semana: ")

print("El dia introducido es ", dia, type(dia))

dia=input("Introduce un dia de la semana: ")

print(dia+1)

"-----------------------------------------------------------------------"

print("El dia introducido es ", dia, int(dia))

"-----------------------------------------------------------------------"

nota = int(input("Introduce tu nota entre 0 y 10: "))
if 0<=nota<=10: 
    if nota>=5:
        print("Estas aprobado")
    else:
        print("Estas suspenso")
else:
    print("La nota no es valida")
