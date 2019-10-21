def hospital():
    listaurgencias=[]
    listaturnos=[]
    numerosocio=0
    while numerosocio!=-1:
        numerosocio=int(input("ingrese el numero de socio: "))
        while (numerosocio<1000 or numerosocio>9999) and numerosocio!=-1:
            numerosocio=int(input("dato invalido,ingrese el numero de socio: "))
        
        if numerosocio!=-1:
            estado=int(input(" si entra en urgencia (1), si es turno(0): "))
            if estado==1:
                listaurgencias.append(numerosocio)
            if estado==0:
                listaturnos.append(numerosocio)
         
            
    return listaurgencias,listaturnos

def buscarsocio(a,b,c):
    conturgencias=0
    conturnos=0
    for i in range(0,len(a)):
        if c==a[i]:
            conturgencias=conturgencias+1
    for i in range(0,len(b)):
        if c==b[i]:
            conturnos=conturnos+1
    return conturgencias,conturnos        
        


listadourgencias,listadoturnos=hospital()
print("los socios atendidos por urgencia fueron:",listadourgencias)
print("los socios atendidos por turno fueron:",listadoturnos)
numeroabuscar=int(input("ingrese el numero de socio que desea buscar: "))
while numeroabuscar>9999 and numeroabuscar<1000:
    numeroabuscar=int(input("ingrese el numero de socio que desea buscar: "))

    
buscador1,buscador2=buscarsocio(listadourgencias,listadoturnos,numeroabuscar)
print("la cantidad de veces que se atendio fueron:",(buscador1+buscador2))
print(buscador1,"fueron por urgencias y",buscador2,"fueron por turnos")




    
        
    
    




    