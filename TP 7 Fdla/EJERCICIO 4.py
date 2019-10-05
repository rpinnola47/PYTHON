def genLista():
    #creamos lista vacia
    lista = []
    #pedimos numero
    nro = int(input("Ingrese un numero "))
    while nro != -1:
        #procesar dato
        lista.append(nro)
        nro = int(input("Ingrese un numero(-1 para finalizar): "))
    return lista

def invertirlista(a):
    largo=len(a)
    for i in range(1,largo,2):
        a[i]=a[i]*-1
    return a    
        
resultado=genLista()
print(resultado)
resultadofinal=invertirlista(resultado)
print(resultadofinal)
        