def genLista():
    lista = []
    nro = int(input("Ingrese un numero "))
    while nro != -1:
        lista.append(nro)
        nro = int(input("Ingrese un numero(-1 para finalizar): "))
    return lista

print("ingrese los elemento de la lista (1)")
lista1=genLista()
print("ingrese los elementos de la lista (2)")
lista2=genLista()

#item 1: La concatenación de los valores pares de A con los impares de B.*
def concatenar(a,b):
    listaconcatenada=[]
    for i in range(len(a)):
       if a[i]%2==0:
           listaconcatenada.append(a[i])
    for i in range(len(b)):
        if b[i]%2==0:
            listaconcatenada.append(b[i])   
    return listaconcatenada  
       
resultadofinalitem1=concatenar(lista1,lista2)
print("la concatenacion de las dos listas es:",resultadofinalitem1)
#item2:La concatenación de los valores pares de A con el reverso de los valores pares de B. ("valores pares" o "valores impares" se refiere a los elementos propiamente dichos y no a sus posiciones).
def concatenarpares(a,b):
    listapares=[]
    for i in range(0,(len(a))):
      if a[i]%2==0:
          listapares.append(a[i])
    j=len(b)-1
    while j>=0:
         if b[j]%2==0:
             listapares.append(b[j])
         j=j-1
    return listapares    
resultadofinalitem2=concatenarpares(lista1,lista2)
print("la lista resultante del item2 es:",resultadofinalitem2)

#item3:La intercalación de los elementos de A y B.
def intercalar(a,b):
   listaintercaladas=[]
   largototal=(len(a)+len(b))-1
   cont1=0
   cont2=0
   cont3=0
   while cont1<=largototal:
       if cont2<=(len(a)-1):
           listaintercaladas.append(a[cont2])
           cont2=cont2+1
       if cont3<=(len(b)-1):
           listaintercaladas.append(b[cont3])
           cont3=cont3+1
       cont1=cont1+1
   return listaintercaladas    
       
resultadofinalitem3=intercalar(lista1,lista2)
print("la interlacacion entre las dos listas es:",resultadofinalitem3)
       
