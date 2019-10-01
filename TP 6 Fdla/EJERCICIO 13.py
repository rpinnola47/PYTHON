#EJERCICIO 13 TP 6 FUNDAMENTOS

def extraerdigito(a,b):
    digito=0
    resto=a%(10**b)
    digito=resto
    return digito    
        
    
num1=int(input("ingrese un numero "))
num2=int(input("ingrese la cifra que desea obtener "))
resultado=extraerdigito(num1,num2)
print(resultado)