def concatenar(a,b):
    a=str(a)
    b=str(b)
    final=a+b
    final=int(final)
    return final

num1=int(input("ingrese un numero "))
num2=int(input("ingrese el otro numero "))
resultado=concatenar(num1,num2)
print("el numero concatenado es:",resultado)
        