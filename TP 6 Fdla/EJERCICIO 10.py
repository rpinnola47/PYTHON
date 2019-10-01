def comparar(a,b):
    signo=0
    if a>b:
        signo=1
    if a<b:
        signo=-1
    if a==b:
        signo=signo
    return signo

num=int(input("ingrese un numero "))
num2=int(input("ingrese el otro numero "))
resultado=comparar(num,num2)
print(resultado)
        