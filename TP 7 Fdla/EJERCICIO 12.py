def genLista():
    lista = []
    cantidad=int(input("ingrese la cantidad de elementos de la lista "))
    cont=1
    while cont<=(cantidad):
        nro = int(input("Ingrese un numero "))
        lista.append(nro)
        cont=cont+1
    return lista

def item1(a):
    acum1=0
    acum2=1
    for i in range(0,len(a),2):
        acum2=acum2*a[i]
    for i in range(1,len(a),2):
        acum1=acum1+a[i]
    if acum1==0:
        print("no se puede realizar la operacion")
        cuentafinal=0
    
    if acum1>0 or acum1<0:
        cuentafinal=acum2/acum1
    return cuentafinal

def item2(a):
    listaitem2=[]
    j=len(a)-1
    acum=0
    largo=len(a)//2
    for i in range(0,largo):
        acum=acum+(a[i]+a[j])
        listaitem2.append(acum)
        j=j-1
        acum=0
    if len(a)%2!=0:
        listaitem2.append(a[(len(a)//2)+1])
    return listaitem2    
        
        
def item3(a):
    listab=[]
    largo=len(a)-2
    for i in range(0,largo):
        if a[i]==a[i+2] and a[i]!=a[i+1]:
            listab.append(a[i+1])
   
    return listab

resultado0=genLista()
resultado1=item1(resultado0)
if resultado1>0:
    print(resultado1)
resultado2=item2(resultado0)
print(resultado2)
resultado3=item3(resultado0)
print(resultado3)
