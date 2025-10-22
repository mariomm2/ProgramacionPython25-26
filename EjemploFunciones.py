
#Ejemplo Funciones

#Actividad 22 Octubre 

#Funcion para saber si un anio es bisiesto

def es_bisiesto(anio):
    resultado = False
    if (anio % 4==0 and anio % 100!= 0) or (anio % 400==0):
        resultado = True
    return resultado

# Tests
assert es_bisiesto(2020) == True
assert es_bisiesto(1900) == False
assert es_bisiesto(2000) == True 
assert es_bisiesto(2023) == False


#Funcion para saber si una persona es mayor de edad

def es_mayor_edad(edad):
    resultado = False
    if edad>=18:
        resultado = True
    return resultado

# Tests
assert es_mayor_edad(18) == True     
assert es_mayor_edad(25) == True     
assert es_mayor_edad(17) == False    
assert es_mayor_edad(0) == False     
