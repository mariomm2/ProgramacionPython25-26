
#Ejercicio 2. Numeros felices.

def is_happy(numero):
    i=0
    es_feliz=False

    while i<8:
        cadena=str(numero)
        suma=0
        
        j=0
        while j<len(cadena):
            digito = int(cadena[j])
            suma+=digito*digito  #suma=suma+digito*digito
            j+=1

        if suma==1:
            es_feliz=True
        numero=suma
        i+=1
    
    return es_feliz


#Tests

assert(is_happy(7))
assert(is_happy(19))
assert(not is_happy(4))
assert(not is_happy(20))

print("Tests superados")