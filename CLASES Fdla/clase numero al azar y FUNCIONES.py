
"""
import random
numero=random.randint(1,30)
print(numero)
"""


"""
#ejercicio del ppt

numero=int(input("ingrese la cantidad de numeros al azar "))
cont=0
acum=0
while cont<=numero:
    import random
    azar=random.randint(1,9)
    print(azar)
    cont=cont+1
    acum=acum+azar
    
print(acum)

"""
"""
#2)ejercicio con FOR
#el rango es siempre uno menos del que se pone, si pongo 10,es hasta 9

for numero in range(10):
    print(numero)
"""


"""
#hacer el ejercicio 1) con FOR
#el desde SI LO INCLUYE PERO EL HASTA NO

numero=int(input("ingrese la cantidad al azar "))
acum=0
for numero in range(0,numero):
    import random
    azar=random.randint(1,10)
    print(azar)
    acum=acum+azar
    
print(acum)
"""
"""
#QUE VAYA DE 2 EN 2

numero=int(input("ingrese la cantidad al azar "))
acum=0
for numero in range(0,numero,2):
    import random
    azar=random.randint(1,10)
    print(azar)
    acum=acum+azar
"""
"""
#generar la secuencia de 5 en 5 del 5 al 25

for numero in range(5,30,5):
    print(numero)
"""

"""
#ejercicio calcular promedio, diapositiva 22
#CREO LA FUNCION:
#def + el nombre de la variable que voy a crear

def calcularpromedio(a,b):
    prom=(a+b)/ 2
    return prom
#programa principal:
nro1=int(input("ingrese un numero "))
nro2=int(input("ingrese un numero "))
resultado=calcularpromedio(nro1,nro2) #ya creada la funcion,ponemos el range y seguimos
print(resultado)
"""






    



    


