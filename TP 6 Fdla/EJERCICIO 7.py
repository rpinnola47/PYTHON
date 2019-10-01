def factorial(a):
   acum=1
   for i in range(1,(a+1)):
       acum=acum*i
   return acum

num1=int(input("ingrese un numero "))
resultado=factorial(num1)
print(resultado)
        
                   