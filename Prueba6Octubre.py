
#Prueba 6 Octubre
#Ejercicio piedra, papel, tijera, lagarto y spock.

print("Bienvenido, tiene que elegir entre piedra, papel, tijera, lagarto y spock.")

eleccion1 = input("Jugador 1, introduce tu elección: ")

while not (eleccion1 == "piedra" or eleccion1 == "papel" or eleccion1 == "tijera" or eleccion1 == "lagarto" or eleccion1 == "spock"):
    eleccion1 = input("Eleccion no valida, jugador 1, introduce tu eleccion de nuevo: ")

eleccion2 = input("Jugador 2, introduce tu eleccion: ")

while not (eleccion2 == "piedra" or eleccion2 == "papel" or eleccion2 == "tijera" or eleccion2 == "lagarto" or eleccion2 == "spock"):
    eleccion2 = input("Eleccion no valida, jugador 2, introduce tu eleccion de nuevo: ")
    
if eleccion1 == eleccion2:
    print("Ambos jugadores empatan con la misma eleccion.")

elif eleccion1 == "tijera" and eleccion2== "papel":
    print ("El ganador es el jugador 1, tijera gana a papel.")
elif eleccion1 == "papel" and eleccion2== "tijera":
    print ("El ganador es el jugador 2, papel pierde ante tijera.")

elif eleccion1 == "papel" and eleccion2== "piedra":
    print ("El ganador es el jugador 1, papel gana a piedra.")
elif eleccion1 == "piedra" and eleccion2== "papel":
    print ("El ganador es el jugador 2, piedra pierde ante papel.")

elif eleccion1 == "lagarto" and eleccion2== "spock":
    print ("El ganador es el jugador 1, lagarto gana a spock.")
elif eleccion1 == "spock" and eleccion2== "lagarto":
    print ("El ganador es el jugador 2, spock pierde ante lagarto.")

elif eleccion1 == "spock" and eleccion2== "tijera":
    print ("El ganador es el jugador 1, spock gana a tijera.")
elif eleccion1 == "tijera" and eleccion2== "spock":
    print ("El ganador es el jugador 2, tijera pierde ante spock.")

elif eleccion1 == "tijera" and eleccion2== "lagarto":
    print ("El ganador es el jugador 1,tijera gana a lagarto.")
elif eleccion2 == "lagarto" and eleccion2== "tijera":
    print ("El ganador es el jugador 2, lagarto pierde ante spock.")

elif eleccion1 == "piedra" and eleccion2== "tijera":
    print ("El ganador es el jugador 1, piedra gana a tijera.")
elif eleccion1 == "tijera" and eleccion2== "piedra":
        print ("El ganador es el jugador 2, tijera pierde ante pidera.")

elif eleccion1 == "papel" and eleccion2== "spock":
    print ("El ganador es el jugador 1, papel gana a spock.")
elif eleccion1 == "spock" and eleccion2== "papel":
    print ("El ganador es el jugador 2, spock pierde ante papel.")

elif eleccion1 == "lagarto" and eleccion2== "papel":
    print ("El ganador es el jugador 1, lagarto gana a papel.")
elif eleccion1 == "papel" and eleccion2== "lagarto":
    print ("El ganador es el jugador 2, papel pierde ante lagarto.")

elif eleccion1 == "spock" and eleccion2== "piedra":
    print ("El ganador es el jugador 1, spock gana a piedra.")
elif eleccion1 == "piedra" and eleccion2== "spock":
    print ("El ganador es el jugador 2, piedra pierde ante spock.")