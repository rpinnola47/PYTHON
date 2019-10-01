def fibonacci(a):
   acum=1
   for i in range(1,(a)):
       acum=acum+i
   return acum    
       
def fibonacci2(a,b):
    acum=1
    acum2=1
    for i in range(1,(b)):
        acum=acum+i
        if a>=i:
            acum2=acum+i
           
    return acum2       
     
    
    
    
    
        


num1=int(input("ingrese un numero "))
num2=int(input("ingrese un numero "))

resultado=fibonacci2(num1,num2)
print(resultado)

        