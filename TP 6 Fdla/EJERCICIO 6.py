def multiplo(a,b):
    if a%b==0:
        multiplo=True
    else:
        multiplo=False
    return multiplo    
        
num1=int(input("ingrese un numero "))
num2=int(input("ingrese e el otro numero "))
resultado=multiplo(num1,num2)
print(resultado)