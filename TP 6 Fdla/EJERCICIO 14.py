def central(a):
    resto=1
    cont=0
    numero=a
    while resto!=0:
        resto=numero//10
        digito=numero%10
        numero=resto
        cont=cont+1
    if cont%2==0:
        digito=-1
    if cont%2!=0:
        cont=(cont//2)+1
        for i in range(0,(cont)):
            resto=a%10
            numeroresto=a//10
            a=numeroresto
            digito=resto
    return digito

num1=int(input("ingrese un numero "))
resultado=central(num1)
print(resultado)


   