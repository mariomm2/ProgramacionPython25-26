
#Ejercicio Cifrado Cesar

def cifrado_cesar(palabra, desplazamiento):
    abecedario= "abcdefghijklmnopqrstuvwxyz"
    palabra = palabra.lower()
    palabra_cifrada = ""
    
    for letra in palabra:
        if letra in abecedario:
            nueva_posicion = (abecedario.index(letra)) + desplazamiento % 26
            palabra_cifrada += abecedario[nueva_posicion]
        else: 
            palabra_cifrada += letra
    
    return palabra_cifrada

print(cifrado_cesar("CASADO",3))
print(cifrado_cesar("Mario",6))


def equivalentes (palabra1, palabra2):
    iguales = True
    i = 0
    while i < len(palabra1):
        if palabra2[i:i+1] == "" or palabra1[i] != palabra2[i]:
            iguales= False
    return iguales



#print(equivalentes("Mario", "Maario"))