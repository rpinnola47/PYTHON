def lista():
    num=int(input("ingrese un numero "))
    lista=[]
    while num!=-1:
        lista.append(num)
        num=int(input("ingrese un numero "))
    return lista

l1=lista()
print(l1)
cantidad=len(l1)
def sumalista(a):
    acum=0
    for i in range(0,(cantidad)):
        l2=a[i]
        acum=acum+l2
    return acum    
        
resultadofinal=sumalista(l1)
print(resultadofinal)
