def lista():
    num=int(input("ingrese un numero, ingrese -1 para cerrar la lista "))
    lista=[]
    while num!=-1:
        lista.append(num)
        num=int(input("ingrese un numero "))
    return lista


def eliminar(a,b):
    listafinal=[]
    variable=0
    for i in range(0,len(a)):
            for j in range(0,len(b)):
                if a[i]==b[j]:
                    variable=1
            if variable==0:
                listafinal.append(a[i])
            variable=0    
 
 
          
    return listafinal            
                
  
    

lista1=lista()
lista2=lista()
print(lista1)
print("Los valores a eliminar son:",lista2)
lista3=eliminar(lista1,lista2)
print(lista3)

