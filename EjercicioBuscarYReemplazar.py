
#Ejercicios buscar y reemplazar
#Ejercicio 13

def buscar_y_reemplazar(frase, buscar, reemplazar):
    resultado = ""
    i = 0

    while i < len(frase):
        if frase[i:i+len(buscar)] == buscar:
            resultado += reemplazar
            i += len(buscar)
        else:
            resultado += frase[i]
            i += 1

    return resultado

print(buscar_y_reemplazar("mario martin", "mario", "jose"))

"""
#Ejercicio 17

def ordenar_vocales(cadena):
    consonantes = ""
    vocales = ""
    texto = cadena.lower()

    for c in texto:
        if c >= "a" and c <= "z":
            if c in "aeiou":
                vocales += c
            else:
                consonantes += c

    resultado = consonantes + vocales
    return resultado

"""
# Mario Martin Maldonado
