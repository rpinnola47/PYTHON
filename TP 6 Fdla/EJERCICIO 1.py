def producto(a,b):
    acum=0
    for i in range(1,(b+1)):
        acum=acum+a
    return acum

num1=int(input("ingrese un numero "))
num2=int(input("ingrese el otro numero "))
resultado=producto(num1,num2)
print(resultado)
        
        