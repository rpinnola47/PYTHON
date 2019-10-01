def signo(a):
    if a>0:
        signo=1
    if a<0:
        signo=-1
    if a==0:
        signo=0
    return signo

num1=int(input("ingrese un numero "))
resultado=signo(num1)
print(resultado)