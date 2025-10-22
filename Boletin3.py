

#Boletin 1 Python

#Ejercicio 1

numero=int(input("Introduce un numero: "))

if numero%2==0:
    print("El numero es par.")
else:
    print("El numero es impar.")
    

#Ejercicio 2

numero1=int(input("Introduce el primer numero: "))
numero2=int(input("Introduce el segundo numero: "))

if numero1==numero2:
    print("Ambos numeros son iguales.")
elif numero1>numero2:
    print("El primer numero es mayor que el segundo")
else:
    print("El primer numero es menor que el segundo")


#Ejercicio 3

numero=int(input("Introduce un numero: "))

if numero % 5 == 0:
    print("El numero", numero, "es multiplo de 5.")
if numero % 7 == 0:
    print("El numero", numero, "es multiplo de 7.")
else:
    print("")


#Ejercicio 4

edad=int(input("Introduce tu edad (entre 0 y 50 años): "))

if edad==0:
    print("Aun no has nacido")
elif 1<=edad<=6:
    print("Educacion infantil.")
elif 7<=edad<=11:
    print("Educacion primaria.")
elif 12<=edad<=16:
    print("Educacion secundaria obligatoria.")
elif 17<=edad<=50:
    print("Enseñanza post-obligatoria.")
else:
    print("La edad introducida no es valida")

    
#Ejercicio 5

numero1=int(input("Introduce el primer numero: "))
numero2=int(input("Introduce el segundo numero: "))
numero3=int(input("Introduce el tercer numero: "))
numero4=int(input("Introduce el cuarto numero: "))

media = (numero1+numero2+numero3+numero4) / 4
contador = 0
superior = ""

if numero1 > media:
    contador +=1
    superior+= str(numero1) + " "
if numero2 > media:
    contador +=1
    superior+= str(numero2) + " "
if numero3 > media:
    contador +=1
    superior+= str(numero3) + " "
if numero4 > media:
    contador +=1
    superior+= str(numero4) + " "

print ("La media de los numeros ", numero1, (","), numero2, (","), numero3, ("y"), numero4, "es:", media, 
"y hay", contador, "numeros superiores a la media que son: ", superior)


#Ejercicio 6

numero1= int(input("Introduce el primer numero: "))
numero2= int(input("Introduce el segundo numero: 15"))

if numero1%numero2==0:
    print("Los numeros", numero1, "y", numero2, "son multiplos entre si.")
else:
    print("Los numeros", numero1, "y", numero2, "no son multiplos entre si.")


#Ejercicio 7

caracter = input("Introduce un caracter: ")
caracter_mayus = caracter.upper()

if caracter_mayus == "A":
    print("Es la primera vocal (A)")
elif caracter_mayus == "E":
    print("Es la segunda vocal (E)")
elif caracter_mayus == "I":
    print("Es la tercera vocal (I)")
elif caracter_mayus == "O":
    print("Es la cuarta vocal (O)")
elif caracter_mayus == "U":
    print("Es la quinta vocal (U)")
else:
    print("El caracter introducido no es una vocal")


#Ejercicio 8

estado_civil = input("Introduce tu estado civil (S, C, V, D): ").lower()
edad = int(input("Introduce tu edad: "))
if (estado_civil == "s" or estado_civil == "d") and edad < 35:
    print("El porcentaje de retención es del 12%")
elif edad > 50:
    print("El porcentaje de retención es del 8.5%")
elif (estado_civil == "c" or estado_civil == "v") and edad < 35:
    print("El porcentaje de retención es del 11.3%")
else:
    print("El porcentaje de retención es del 10.5%")

    
# Ejercicio 9

dia = int(input("Introduce el dia de la semana (1 al 7): "))

if dia == 1:
    print("Lunes")
elif dia == 2:
    print("Martes")
elif dia == 3:
    print("Miercoles")
elif dia == 4:
    print("Jueves")
elif dia == 5:
    print("Viernes")
elif dia == 6:
    print("Sabado")
elif dia == 7:
    print("Domingo")
else:
    print("El dia introducido no es correcto")


#Ejercicio 10

hora1 = int(input("Introduce las horas primeras: "))
min1 = int(input("Introduce los minutos primeros: "))
seg1 = int(input("Introduce los segundos primeros: "))
hora2 = int(input("Introduce las horas segundas: "))
min2 = int(input("Introduce los minutos segundos: "))
seg2 = int(input("Introduce los segundos segundos: "))

if hora1 > hora2:
    print("La primera marcacion es mayor:", hora1, ":", min1, ":", seg1)
elif hora1 < hora2:
    print("La segunda marcacion es mayor:", hora2, ":", min2, ":", seg2)
else:  
    if min1 > min2:
        print("La primera marcacion es mayor:", hora1, ":", min1, ":", seg1)
    elif min1 < min2:
        print("La segunda marcacion es mayor:", hora2, ":", min2, ":", seg2)
    else: 
        if seg1 > seg2:
            print("La primera marcacion es mayor:", hora1, ":", min1, ":", seg1)
        elif seg1 < seg2:
            print("La segunda marcacion es mayor:", hora2, ":", min2, ":", seg2)
        else:
            print("Ambas marcaciones son iguales:", hora1, ":", min1, ":", seg1)

            
#Ejercicio 11

tipo_cliente = input("Introduce el tipo de cliente (S, R, O): ").upper()
cantidad = int(input("Introduce la cantidad gastada: "))

if tipo_cliente == "S" and cantidad >= 100:
    cantidad = cantidad - ((cantidad * 15) / 100)
    print("La cantidad final es: ", cantidad)
elif tipo_cliente == "S" and cantidad < 100:
    cantidad = cantidad - ((cantidad * 10) / 100)
    print("La cantidad final es: ", cantidad)
elif tipo_cliente == "R" and cantidad >= 200:
    cantidad = cantidad - ((cantidad * 12) / 100)
    print("La cantidad final es: ", cantidad)
else:
    cantidad = cantidad - ((cantidad * 5) / 100)
    print("La cantidad final es: ", cantidad)


#Ejercicio 12

numero1=int(input("Introduce el primer numero: "))
numero2=int(input("Introduce el segundo numero: "))
caracter=(input("Introduce el caracter: "))
resultado = 0
if caracter == "+":
    resultado = numero1 + numero2
    print("El resultado es: ", resultado)
elif caracter == "-":
    resultado = numero1 - numero2
    print("El resultado es: ", resultado)
elif caracter == "*":
    resultado = numero1 * numero2
    print("El resultado es: ", resultado)
elif caracter == "/":
    if numero2==0
        print("No se puede dividir por 0")
    else:
        resultado = numero1 / numero2
        print("El resultado es: ", resultado)
else:
    print((str)numero1 + caracter + (str)numero2)

#Para concatenar usamos +

#Ejercicio 13

moneda2e = int(input("Introduce las monedas de 2€: "))
moneda1e = int(input("Introduce las monedas de 1€: "))
moneda50c = int(input("Introduce las monedas de 50 cent: "))
moneda20c = int(input("Introduce las monedas de 20 cent: "))
moneda10c = int(input("Introduce las monedas de 10 cent: "))
moneda5c = int(input("Introduce las monedas de 5 cent: "))
moneda2c = int(input("Introduce las monedas de 2 cent: "))
moneda1c = int(input("Introduce las monedas de 1 cent: "))

total = (moneda2e*2) + (moneda1e*1) + (moneda50c*0.5) + (moneda20c*0.2) + (moneda10c*0.1) + (moneda5c*0.05) + (moneda2c*0.02) + (moneda1c*0.01)
print("Tienes un total de:", total, "€")


#Ejercicio 14

dia = int(input("Introduce el dia: "))
mes = int(input("Introduce el mes: "))
year = int(input("Introduce el año: "))

if (year%4 == 0 and year % 100 != 0) or (year % 400 == 0):
    bisiesto = True
else:
    bisiesto = False

if mes<1 or mes>12:
    print("El mes es incorrecto.")
else:
    if mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12:
        max_dias = 31
    elif mes==4 or mes==6 or mes==9 or mes==11:
        max_dias=30
    elif mes==2:
        if bisiesto:
            max_dias=29
        else:
            max_dias=28
    
    if dia < 1 or dia > max_dias:
        print("La fecha no existe, el día es incorrecto.")
    else:
        print("La fecha es valida.")
        if bisiesto:
            print("El año", year, "es bisiesto.")
        else:
            print("El año", year, "no es bisiesto.")


#Ejercicio 15

base = int(input("Introduce la base: "))
exponente = int(input("Introduce el exponente: "))

if exponente > 0:
    resultado = base ** exponente
elif exponente == 0:
    resultado = 1
else:  
    resultado = 1 / (base ** abs(exponente))

print("La potencia de", base, "elevado a", exponente, "es:", resultado)


#Ejercicio 16

lado1 = int(input("Introduce el primer lado: "))
lado2 = int(input("Introduce el segundo lado: "))
lado3 = int(input("Introduce el tercer lado: "))

if lado1+lado2 > lado3 or lado2+lado3 > lado1 or lado1+lado3>lado2:
    if lado1==lado2==lado3:
        print("El triangulo es equilatero.")
    elif lado1==lado2 or lado2==lado3 or lado3==lado1:
        print("El triangulo es isoscele.")
    elif lado1 !=lado2!=lado3:
        print("El triangulo es escaleno.")
    elif (lado1**2 == lado2**2+lado3**2) or (lado2**2 == lado1**2+lado3**2) or (lado3**2 == lado1**2+lado2**2):
        print("El triangulo es rectangulo.")
    
else:
    print("Los lados introducidos no forman un triangulo valido.")


#Ejercicio 17
numero1= int(input("Introduce el primer numero"))
numero2= int(input("Introduce el segundo numero"))

distancia = abs(numero1-numero2)
print("La distancia entre ellos es de: ", distancia)


#Ejercicio 18

cantidad_alumnos = int(input("Introduce la cantidad de alumnos: "))

if cantidad_alumnos >=100:
    costo_alumno=65
    pago_compania=cantidad_alumnos*costo_alumno
if cantidad_alumnos >=50 and cantidad_alumnos<=99:
    costo_alumno=70
    pago_compania=cantidad_alumnos*costo_alumno
if cantidad_alumnos >=30 and cantidad_alumnos<=49:
    costo_alumno=95
    pago_compania=cantidad_alumnos*costo_alumno
if cantidad_alumnos<30:
    costo_bus=2500
    costo_alumno = 2500/cantidad_alumnos

print("El costo por alumno es de ", costo_alumno, "€ y el pago total a la compañia es de ", pago_compania, "€.")


#Ejercicio 19


#Ejercicio 20

matematicas = int(input("Introduce la nota de Mates: "))
ingles = int(input("Introduce la nota de Ingles: "))
programacion = int(input("Introduce la nota de Programacion: "))
asistencia = int(input("Introduce el porcentaje de asistencia: "))

if matematicas>=50 and ingles>=50 and programacion>=50:
    media = (matematicas + ingles + programacion)/3

    if media >= 85:
        print("El estudiante es admitido con beca.")
    elif 70<=media<=84:
        if asistencia>=75:
            print("El estudiante es admitido sin beca.")
        else:
            print("El estudiante es rechazado por asistencia baja.")
    elif 60<=media<=69:
        print("El estudiante queda en lista de espera.")
    else:
        print("El estudiante es rechazado.")
else:
    print("El estudiante es rechazado por no aprobar examenes.")


