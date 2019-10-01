def maximo(a,b):
    if a<=b:
        maximo=b
    else:
        maximo=a
    return maximo
num1=int(input("ingrese un numero "))
num2=int(input("ingrese el otro numero "))
resultado=maximo(num1,num2)
print("el maximo posible es",resultado)