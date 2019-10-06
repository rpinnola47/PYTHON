def genLista():
    lista = []
    cantidad=int(input("ingrese la cantidad de elementos de la lista "))
    cont=1
    while cont<=(cantidad):
        nro = int(input("Ingrese un numero "))
        lista.append(nro)
        cont=cont+1
    return lista


def boole(a):
    listaboole=[]
    largolista=len(a)-1
    for i in range(largolista):
       if a[i]<=(a[i+1]):
           veracidad=True
       else:
           veracidad=False
       listaboole.append(veracidad)    
    return listaboole             

resultado=genLista()
print(resultado)
resultadofinal=boole(resultado)
print(resultadofinal)