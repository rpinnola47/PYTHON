import random
def genListaproductos():
    listaproductos = []
    stock=[]
    repetido=0
    producto = int(input("Ingrese un numero "))
    while producto<1000 or producto>9999:
        producto = int(input("reingrese un numero "))
    while producto!=-1:
        while producto<1000 or producto>9999:
            producto = int(input("reingrese un numero "))
        
        for i in range(0,len(listaproductos)):
            if listaproductos[i]==producto:
                repetido=1
        if repetido==1:
            print("el numero ya fue ingresado")
        else:
            listaproductos.append(producto)
            nrostock=random.randint(0,20)
            stock.append(nrostock)
        
        producto = int(input("Ingrese un numero "))
        repetido=0
    return listaproductos,stock

def minimostock(a):
    contminimo=0
    for i in range(0,len(a)):
        if a[i]<5:
            contminimo=contminimo+1
    return contminimo        
        
def maximolista(a):
    maximo=0
    for i in range(0,len(a)):
        if a[i]>maximo:
            maximo=a[i]
    return maximo        


def maximocodigo(a,b,c):
    listamaximos=[]
    for i in range(0,len(a)):
        if a[i]==b:
            listamaximos.append(c[i])
    return listamaximos        
        
def validezenlalista(a,b):
    cont=0
    for i in range(0,len(a)):
        if b==a[i]:
            cont=cont+1
        
    return cont       

def renovarstock(a,b,c,d):
    for i in range(0,len(a)):
        if b==a[i]:
            posicion=i
    for j in range(0,len(c)):
         if j==posicion:
             auxiliar=c[posicion]
             c[posicion]=(c[posicion])-d
             requerimiento=c[posicion]
             if requerimiento<0:
                 stockrenovado=c[j]
                 print("no hay stock suficiente")
                 c[posicion]=auxiliar
             
             if requerimiento>=0:
                 stockrenovado=c[j]
                 print("el stock renovado queda en:",stockrenovado)
         
             
    
    return stockrenovado             
             
#programa principal        
listacod,listastock=genListaproductos()
print(listacod)
print(listastock)
for i in range(0,len(listacod)):
    print(listacod[i],":",listastock[i])
stockminimo=minimostock(listastock)
print("la cantidad de productos que no cumplen con el stock minimo es:",stockminimo)
maximo=maximolista(listastock)
listamaximo=maximocodigo(listastock,maximo,listacod)
print("el maximo de stock es de:",maximo,". y los productos con dicho stock son:",listamaximo)

nroproducto=int(input("ingrese el codigo de producto "))
while nroproducto!=-1:
    while nroproducto<1000 or nroproducto>9999:
        nroproducto=int(input("dato invalido,reingrese el codigo de producto "))
    siesvalido=validezenlalista(listacod,nroproducto)
    if siesvalido==0:
        listacod.append(nroproducto)
        nrostock=random.randint(0,20)
        listastock.append(nrostock)
        print(listacod)
        print(listastock)
        for i in range(0,len(listacod)):
            print(listacod[i],":",listastock[i])        
            
    
    if siesvalido>=1:
        nroventa=int(input("ingrese la cantidad vendida "))
        cuentafinal=renovarstock(listacod,nroproducto,listastock,nroventa)
        if cuentafinal>=0:
            print("lista con sus stocks ACTUALIZADOS")
            for i in range(0,len(listacod)):
                print(listacod[i],":",listastock[i])  
        
    nroproducto=int(input("ingrese el codigo de producto "))
           
print("ha finalizado el programa")    


