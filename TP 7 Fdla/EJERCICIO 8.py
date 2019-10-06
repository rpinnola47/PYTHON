def generarlista():
    #creamos la lsta vacia
    lista=[]
    #pedimos numero
    import random
    azar=random.randint(0,100)
    while azar!=0:
        lista.append(azar)
        azar=random.randint(0,100)
      
    return lista


def minimolista(a):
    minimo=100
    for i in range(len(a)-1):
        if a[i]<=minimo:
            minimo=a[i]
    return minimo    
    

def sacarposicion(a,b):
    posiciones=[]
    i=0
    while i<(len(a)-1):
        if a[i]==b:
            posiciones.append(i)
        i=i+1
        
    if i==(len(a)-1) and posiciones==[]:
        print("el numero no se encuentra en la lista")
    return posiciones

resultado=generarlista()
print(resultado)
sacarelminimo=minimolista(resultado)
resultadofinal=sacarposicion(resultado,sacarelminimo)
print("el minimo de la lista es:",sacarelminimo,"y se encuentra en las posiciones:",resultadofinal)
