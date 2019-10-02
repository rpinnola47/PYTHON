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

def listacapicua(a):
    indices=len(a)-1
    variable1=indices
    variable2=indices//2
    capicua=0
    for i in range(0,variable2):
      if a[i]==a[variable1]:
          capicua=1
      else:
          capicua=0
      variable1=variable1-1
    if capicua==1:
        print("la lista es capicua")
    else:
        print("la lista NO es capicua")

          
resultado=generarlista()
print(resultado)
final=listacapicua(resultado)
