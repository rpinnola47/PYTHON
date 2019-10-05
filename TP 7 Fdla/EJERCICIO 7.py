año=[0,0,0,0,0,0,0,0,0,0,0,0]
#meses es para el print del final
meses=["Enero","Febrero","Marzo","Abril","Mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]
legajo=int(input("ingrese el numero de legajo"))
maximo=0
while legajo!=-1:
    dia=int(input("ingrese el dia "))
    mes=int(input("ingrese el mes "))
    ano=int(input("ingrese el año "))
   #validar fecha con una funcion aparte
    año[mes-1]=año[mes-1]+1
    if  (año[mes-1])>maximo:
        maximo= año[mes-1]
    legajo=int(input("ingrese el numero de legajo"))
    
for i in range(len(meses)):
    print(meses[i],":",año[i])
for i in range(len(meses)):
    if año[i]==maximo:
        print("el mes con mas cumpleaños es:",meses[i])
    

        
            
            
  
        
            
    