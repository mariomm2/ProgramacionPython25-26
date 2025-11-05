
#Ejercicio 2

hora = int(input("Introduce la hora. "))
minuto = int(input("Introduce los minutos. "))
segundo = int(input("Introduce los segundos. "))

segundo = segundo + 1

if segundo == 60:
    segundo=0
    minuto = minuto + 1

if minuto== 60:
    minuto= 0
    hora =hora + 1

if hora == 24:
    hora = 0

print("Formato 24 horas.")
print(hora, ":", minuto, ":", segundo)

if hora < 12:
    periodo="AM"
else:
    periodo = "PM"


print("Formato 12 horas")
#print(hora12, ":", minuto, ":", segundo, periodo)

