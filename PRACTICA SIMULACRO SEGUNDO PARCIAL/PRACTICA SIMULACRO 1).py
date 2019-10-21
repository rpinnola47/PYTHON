import random

def listanumeros():
    lista=[]
    azar=random.randint(0,10)
    while azar!=0:
        lista.append(azar)
        azar=random.randint(0,10)
    return lista
def promedio(a):
    acum=0
    maximo=1
    for i in range(0,len(a)):
        acum=acum+a[i]
        if a[i]>maximo:
            maximo=a[i]
    if len(a)>1:
        promedio=acum/len(a)
    return promedio    

def mayoresalpromedio(a,b):
    listamayores=[]
    for i in range(0,len(b)):
        if b[i]>a:
            listamayores.append(b[i])
    return listamayores      

def sacarimpares(a):
    contsacados=0
    largo=len(a)-1
    i=0
    while i<len(a):
        if a[i]%2!=0:
            a.pop(i)
            contsacados=contsacados+1
        else:
            i=i+1    
    return contsacados        

listafinal=listanumeros()
print(listafinal)
promedio=promedio(listafinal)
print("el promedio entre los elementos es de: %.2f " %promedio)
mayor=mayoresalpromedio(promedio,listafinal)
print("los elementos mayores al promedio son:",mayor)
cantidad=sacarimpares(listafinal)
print(listafinal)
print("la cantidad de impares eliminados fueron:",cantidad)




