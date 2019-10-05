#Ejercicio 6: Ídem anterior, utilizando búsqueda binaria sobre una lista ordenada.

#Funcion generarlista:
def genLista():
    #creamos lista vacia
    lista = []
    #pedimos numero
    nro = int(input("Ingrese un numero (-1 para finalizar): "))
    while nro != -1:
        #procesar dato
        lista.append(nro)
        nro = int(input("Ingrese un numero(-1 para finalizar): "))
    return lista

#Funcion ordenamiento por seleccion:
def metodoSeleccion(lista):
    for i in range(0, len(lista)-1):
        for j in range(i + 1,len(lista)):
            if lista[i] > lista[j]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
    return lista

#Funcion busqueda binaria:
def busquedaBinaria(lista,elem):
    p0 = 0
    pf = len(lista)
    for i in range(p0,pf):
        pm = (p0 + pf)//2
        if elem == lista[pm]:
            return pm
        elif elem > lista[pm]:
            p0 = pm + 1
        else:
            pf = pm - 1
    return -1

#Programa Ppal:
numeros = genLista()
numeros = metodoSeleccion(numeros)
print(numeros)
nro = int(input("Ingrese el numero que quiere buscar en la lista: "))
if busquedaBinaria(numeros, nro) == -1:
    print("El numero no se encuentra en la lista")
else:
    print("El numero se encuentra en la posición: ", busquedaBinaria(numeros, nro))
