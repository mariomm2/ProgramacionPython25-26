
#Prueba 20 Octubre
#Ejercicio pares y nones 

maxApuestas=1
victoriasJ1=0
victoriasJ2=0

while maxApuestas <=5:

    print("Ronda numero ", maxApuestas)
        
    apuesta1=input("Introduce tu eleccion J1 (p/n)").lower()
    while apuesta1 !="p" and apuesta1 !="n":
        apuesta1=input("Introduce tu eleccion de nuevo J1, debe ser (p/n)").lower()

    apuesta2=input("Introduce tu eleccion J2 (p/n)").lower()
    while apuesta2 !="p" and apuesta2 !="n":
        apuesta2=input("Introduce tu eleccion de nuevo J2, debe ser (p/n)").lower()

    dedos1=int(input("Muestra los dedos J1 (Max 10)"))
    while dedos1<0 or dedos1>10:   
        dedos1=int(input("Muestra los dedos de nuevo J1 (Max 10)"))

    dedos2=int(input("Muestra los dedos J2 (Max 10)"))
    while dedos2<0 or dedos2>10:        
        dedos2=int(input("Muestra los dedos de nuevo J2 (Max 10)"))

    suma=dedos1+dedos2

    if suma%2==0 and apuesta1=="p":
        print("Apuesta ganada por jugador 1.")
        victoriasJ1+=1
    elif suma%2==0 and apuesta2=="p":
        print("Apuesta ganada por jugador 2.")
        victoriasJ2+=1
    elif suma%2!=0 and apuesta1=="n":
        print("GanApuesta ganada por jugador 1.")
        victoriasJ1+=1
    elif suma%2!=0 and apuesta2=="n":
        print("Apuesta ganada por jugador 2.")
        victoriasJ2+=1
    
    maxApuestas+=1

if victoriasJ1>victoriasJ2:
    print("El jugador 1 ha ganado la partida. Gano",victoriasJ1, "veces.")
else:
    print("El jugador 2 ha ganado la partida. Gano",victoriasJ2, "veces.")    