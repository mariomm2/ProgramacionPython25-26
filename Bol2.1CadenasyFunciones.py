
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
            numero = numero + c
        else:
            if numero != "":
                total = total + int(numero)
                numero = ""
    if numero != "":
        total = total + int(numero)

    return total

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
"""

#Ejercicio 6

def lowCaseInString(cadena):
    contador = 0
    for c in cadena:
       #if c >= "a" and c <= "z":
        if c.islower():
            contador = contador + 1
    return "Hay " + str(contador) + " letras minúsculas"

print(lowCaseInString("MarioMartin"))

"""
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

def palabra_escondida(texto, palabra):
    i = 0
    for letra in texto:
        if i < len(palabra) and letra == palabra[i]:
            i = i + 1
    
    resultado = False
    if i == len(palabra):
        resultado = True
    
    return resultado

print(palabra_escondida("supercalifragilisticoespialidoso", "rapido"))
print(palabra_escondida("sfragsilicoesiidoso", "rapido"))


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

"""