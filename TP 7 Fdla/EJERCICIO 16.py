
def random():
    import random
    azar=random.randint(1000,9999)
    return azar
    
def intentos(a):
    listaintentos=[]
    print("intente descubrir el numero de 4 cifras formado al azar")
    opcion=int(input("ingrese un numero de 4 cifras, ponga -1 cuando se quiera rendir: "))
    while opcion<1000 or opcion>9999:
        opcion=int(input("numero invalido,reingrese un numero de 4 cifras: "))
        
    while opcion!=-1:
        while opcion<1000 or opcion>9999:
            opcion=int(input("numero invalido,reingrese un numero de 4 cifras: "))
        if opcion==a:
            print("FELICITACIONES! la NASA quiere saber tu ubicacion")
            listaintentos.append(opcion)
            opcion=-1
            
        
        else:
            listaintentos.append(opcion)
            if opcion>a:
                print("su numero es mayor al generado")
            if opcion<a:
                print("su numero es menor al generado")
            opcion=int(input("ingrese un numero de 4 cifras, ponga -1 cuando se quiera rendir: "))          
    
    return listaintentos            
        


numeroelegido=random()
condicion=str(input("quiere empezar el juego? ponga (si): "))
maximo=0
listapuntajes=[]
while condicion!="terminar":
    juego=intentos(numeroelegido)
    print("la cantidad de intentos fueron:",len(juego),"y dichos intentos fueron",juego)
    listapuntajes.append(len(juego))
    for i in range(0, len(listapuntajes)-1):
        for j in range(i + 1,len(listapuntajes)):
            if listapuntajes[i] > listapuntajes[j]:
                aux = listapuntajes[i]
                listapuntajes[i] = listapuntajes[j]
                listapuntajes[j] = aux
    m=1
    mejorespuntajes=[]
    largo=len(listapuntajes)-1
    while m<=5:
       if largo>=0:
            mejorespuntajes.append(listapuntajes[largo])
       largo=largo-1
       m=m+1
        
        
    if len(juego)>maximo:
        maximo=len(juego)
        nombre=str(input("ingrese su nombre para el marcador: "))
    print("los 5 mejores puntajes hasta el momento son:",mejorespuntajes)
    condicion=str(input("quiere intentarlo otra vez? ponga (si) sino ponga (terminar): "))

    