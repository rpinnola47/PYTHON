"""
estrucutura de datos:
listas: puede estar conformada por varios elementos, que estan organizados en "fila de cajitas"
        cada cajita tiene un solo valor. cada posicion tiene UN SOLO VALOR A LA VEZ pero todas esta agrupadas en una misma variable
*cada caja tiene su indice(arranca desde cero)


"""
#creando lista
pino=[4,6,3,9,7]
print(pino)#mostrar por pantalla

#seleccionar uno determinado, imprimir uno determnado
print(pino[2])

#agregar valores, uso NOMBRELISTA.APPEND(VALOR)
pino.append(5)
print(pino)

#agregar varios valores a una lista, mas de un solo valor
pino.extend([5,3,6])
print(pino)

#sacar un valor de la lista, desde un indice
pino.remove(4)
print(pino)

#contar los elementos de una lista
cantidad=len(pino)
print(cantidad)
# tambien se puede directamente print(len(pino))

#contar el ultimo indice, el maximo
cantidad=(len(pino))-1
print(cantidad)
#para imprimir el ultimo valor, primero saco el indice max
print(pino[(len(pino)-1)])



