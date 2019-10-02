def generarlista():
    #creamos la lsta vacia
    lista=[]
    #pedimos numero
    nro=int(input("ingrese un numero "))
    while nro!=-1:
        #procesar dato
        if nro>=1 and nro<=20:
            lista.append(nro)
        else:
            print("numero no valido")
        nro=int(input("ingrese un numero "))
    return lista

resultado=generarlista()
print(resultado)
#averiguar la cantidad de elementos
cantidadelementos=len(resultado)
print(cantidadelementos)            
#mostrar la suma de todos los elementos de la lista
"""
#con WHILE
suma=0
i=0
while i<len(resultado):
    suma=suma+resultado[i]
    i=i+1
print(suma)    
"""
#con FOR
suma=0
for i in range(0,len(resultado)):
    suma=suma+resultado[i]
print(suma)    
    
    

    