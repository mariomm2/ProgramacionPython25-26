
#Examen 1 Python
#Ejercicio 3 (Incompleto)


import random

total_jugador=0
total_banca=0
apuestas_realizadas=0
puede_jugar=True


while puede_jugar == True:
    numero_apostado=int(input("Elige un numero con el que apostar. "))
    
    cantidad=int(input("Introduce la cantidad a aapostar. "))
    numero_ganador = random.randint(0,36)
    print("Ha salido el numero", numero_ganador)

    distancia=(numero_apostado-numero_ganador)
    
    if numero_apostado==numero_ganador:
        ganacia=cantidad*3
        print("Numero acertado, ganas ", ganacia, "€")
        total_jugador+=ganacia
        total_banca-=ganacia
    
    elif distancia<10:
        perdida = cantidad/3
        print("La distancia es menor de 10 puntos, pierdes", perdida, "€")
        total_banca+=perdida
        total_jugador-=perdida
    
    elif distancia>20:
        perdida=cantidad/2
        print("La distancia es mayor de 20 puntos, pierdes", perdida, "€")
        total_banca+=perdida
        total_jugador-=perdida
    
    elif distancia==36:
        print("La distancia maxima, pierdes todo. No puedes volver a jugar.")
        total_banca+=cantidad
        puede_jugar=False
    else:
        print("Sin ganacia")

    apuestas_realizadas+=1

print("El numero de apuestas realizado es de", apuestas_realizadas, "apuestas.")
print("El importe total ganado es de ", total_jugador, "€")
print("El importe total ganado por la banca es de ", total_banca, "€")