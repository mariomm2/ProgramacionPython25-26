
"""
#Ejercicio 1

def crear_acronimo(frase):
    acronimo = ""
    palabra = ""
    excluir = " de la del y o en a "
    frase = frase + " "

    for c in frase:
        if c != " ":
            palabra = palabra + c
        else:
            if (" " + palabra.lower() + " ") not in excluir:
                acronimo = acronimo + palabra[0].upper()
            palabra = ""

    return acronimo

print(crear_acronimo("Instituto Nacional de Tecnologia Industrial"))


#Ejercicio 2

def a_camel_case(frase):
    resultado = ""
    palabra = ""
    primera = True
    frase = frase + " "

    for c in frase:
        if c != " ":
            palabra = palabra + c
        else:
            if palabra != "":
                if primera:
                    resultado = resultado + palabra.lower()
                    primera = False
                else:
                    resultado = resultado + palabra[0].upper() + palabra[1:].lower()
                palabra = ""

    return resultado

print(a_camel_case("hola mundo cruel"))


#Ejercicio 3

def suma_numeros(cadena):
    total = 0
    numero = ""

    for c in cadena:
        if c >= "0" and c <= "9":
            numero +=c
        else:
            if numero != "":
                total = total + int(numero)
                numero = ""
    if numero != "":
        total = total + int(numero)

    return total

#Con isdigit()
def suma_numeros(cadena):
    total = 0
    numero = ""

    for c in cadena:
        if c.isdigit():            
            numero = numero + c    
        else:
            if numero != "":     
                total = total + int(numero)
                numero = ""        

    if numero != "":              
        total = total + int(numero)

    return total


cadena = "abc12de3fg45"
print("La suma total es:", suma_numeros(cadena))

print(suma_numeros("abc12x3y45"))


#Ejercicio 4

def rotar_cadena(cadena, n):
    longitud =len(cadena)
    n = n%longitud
    nuevaCadena = ""

    for i in range(longitud - n, longitud):
        nueva = nuevaCadena + cadena[i]
    for i in range(0, longitud - n):
        nuevaCadena = nuevaCadena + cadena[i]

    return nuevaCadena

print(rotar_cadena("python", 2))


#Forma sencilla de hacerlo

def rotar_cadena(cadena, n):
    return cadena[n:] + cadena[:n]

rotar_cadena("python", 2)


#Ejercicio 5

def charactersInString(cadena, caracter):
    cadena = cadena.lower()
    caracter = caracter.lower()
    contador = 0

    for c in cadena:
        if c == caracter:
            contador = contador+1

    return "La letra introducida aparece " + str(contador) + " veces"

print(charactersInString("ProgramAcion", "a"))


#Ejercicio 6

def lowCaseInString(cadena):
    contador = 0
    for c in cadena:
       #if c >= "a" and c <= "z":
        if c.islower():
            contador = contador + 1
    return "Hay " + str(contador) + " letras minúsculas"

print(lowCaseInString("MarioMartin"))


#Ejercicio 7

def numberInString(cadena):
    contador = 0
    for c in cadena:
        if c >= "0" and c <= "9":
            contador = contador + 1
    return contador

print(numberInString("abc123x45"))


#Ejercicio 8

def palindromo(cadena):
    cadena = cadena.replace(" ", "").lower()
    invertida = ""
    for i in range(len(cadena) - 1, -1, -1):
        invertida = invertida + cadena[i]

    resultado = False
    if cadena == invertida:
        resultado = True
    return resultado

print(palindromo("reconocer"))
print(palindromo("se o no se"))


#Ejercicio 9

#Resuelto en clase

def buscar_palabra(texto, palabra):
    texto=texto.lower()
    palabra=palabra.lower()
    contador=0
    contador_cp=0
    encontrada=False
    
    while not encontrada and contador_cp<len(texto) and len(palabra)>0:
        if texto[contador_cp]==palabra[contador]:
            contador+=1
        contador_cp+=1
        encontrada=len(palabra)==contador
    


    return encontrada or len(palabra)==0 and len(texto)==0


assert(buscar_palabra("rapidosupercalifragilisticoespialidoso", "rapido"))
assert(buscar_palabra("supercalifragilisticoespialido", "rapido"))
assert(buscar_palabra("",""))
assert(not buscar_palabra("sfragaglistiasdhj", "rapido"))
assert(not buscar_palabra("superfragilisdaeto", "rapido"))
assert(not buscar_palabra("", "rapido"))
assert(not buscar_palabra("supercalifragilisticoespialidoso", ""))
assert(not buscar_palabra("rapi", "rapido"))


#Ejercicio 10

def es_armstrong(numero):
    cadena = str(numero)
    n = len(cadena)
    suma = 0
    for c in cadena:
        digito = int(c)
        potencia = 1
        for i in range(n):
            potencia = potencia * digito
        suma = suma + potencia
    
    resultado = False
    if suma == numero:
        resultado = True
    
    return resultado

num = int(input("Introduce un numero: "))
if es_armstrong(num):
    print(num, "es un numero Armstrong.")
else:
    print(num, "no es un numero Armstrong.")


#Ejercicio 11

#Ejercicio 12


"""
#Ejercicio 13

def buscar_y_reemplazar(frase, buscar, reemplazar):
    nueva = ""
    i = 0

    while i < len(frase):
        if frase[i:i+len(buscar)] == buscar:
            nueva = nueva + reemplazar
            i = i + len(buscar)
        else:
            nueva = nueva + frase[i]
            i = i + 1

    return nueva
"""

    #Ejercicio 17

    def ordenar_vocales(cadena):
    consonantes = ""
    vocales = ""
    texto = cadena.lower()

    for c in texto:
        if c >= "a" and c <= "z":
            if c in "aeiou":
                vocales = vocales + c
            else:
                consonantes = consonantes + c

    resultado = consonantes + vocales
    return resultado

"""