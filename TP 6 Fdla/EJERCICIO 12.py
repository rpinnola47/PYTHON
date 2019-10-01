#EJERCICIO 12 TP 6 FUNDAMENTOS

def extraerdigito(a,b):
    digito=0
    for i in range(0,(b+1)):
        resto=a%10
        numeroresto=a//10
        a=numeroresto
        digito=resto
    if digito==0 and a==0:
        digito=-1
    return digito   
   
   
num1=int(input("ingrese un numero "))
num2=int(input("ingrese la cifra que desea obtener "))
resultado=extraerdigito(num1,num2)
print(resultado)