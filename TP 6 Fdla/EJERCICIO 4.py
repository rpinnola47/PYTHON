def par(a):
    if a%2==0:
        par=True
    else:
        par=False
    return par    
        
numero=int(input("ingrese un numero "))    
resultado=par(numero)
if resultado==True:
    print("es un numero par")
if resultado==False:
    print("no es par")
    