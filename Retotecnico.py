import random
archivo=open("juegocarreras.txt", "w")
def datos():
    print("Participantes juego de carreras ")
    archivo=open("juegocarreras.txt", "r")
    with open("juegocarreras.txt") as archivo:
        for contenido in archivo:
            print(contenido.rstrip())
    archivo.close()   
def agregar():
    y='y'
    recorrido=0
    archivo=open("juegocarreras.txt","r")
    parte=archivo.readlines()
    archivo.close()
    archivo=open("juegocarreras.txt","w")
    print("Digite la informacion del jugador: ")
    nombre=input("Ingrese Nombre y apellido: \n")
    jugador=input("Ingrese nombre del jugador: \n")
    color=input("Ingrese color del vehiculo: \n")
    carril=input("Ingrese el carril en el que desea participar: \n")
    parte.append(nombre+"\n")
    for list in parte:
        if list==jugador+"\n":
            print("jugador existente")
            resp=input("Desea cambiar de jugador:? y/n \n")
            if resp == y:
                break
            else:
               jugador=input("Ingrese nombre del jugador: \n")
               break
    parte.append(jugador+"\n")
    parte.append(color+"\n")
    parte.append(carril+"\n")
    parte.append(str(recorrido)+"\n")     
    print("El jugador a sido agregado") 
    for med in parte:
            archivo.write(med)    
    archivo.close()

def iniciara():
    archivo=open("juegocarreras.txt", "r")
    parte=archivo.readlines()
    archivo.close()
    archivo=open("juegocarreras.txt","w")
    metros=0
    while metros<20000:
        x=0
        participante=input("Ingrese el id del jugador a lanzar: \n")
        for dato in parte:
            if dato == participante+"\n":
                x=x+3
                print(random.randrange(6))
                metros=int(parte[x])+((random.randrange(6))*100)
                parte.insert(x,str(metros)+"\n") 
                break
            else:
                x+=1
    t=0
    for sig in parte:

        if sig >="20000":
            print("El jugador "+parte[t]+" es el ganador")
            break
        else:
            t+=1
    for med in parte:
        archivo.write(med)    
    archivo.close()        

def iniciarb():
    archivo=open("juegocarreras.txt", "r")
    parte=archivo.readlines()
    archivo.close()
    archivo=open("juegocarreras.txt","w")
    metros=0
    while metros<30000:
        x=0
        participante=input("Ingrese el id del jugador a lanzar: \n")
        for dato in parte:
            if dato == participante+"\n":
                x=x+3
                print(random.randrange(6))
                metros=int(parte[x])+((random.randrange(6))*100)
                parte.insert(x,str(metros)+"\n") 
                break
            else:
                x+=1
    t=0
    for sig in parte:
        if sig >="30000":
            print("El jugador "+parte[t]+" es el ganador")
            break
        else:
            t+=1
    for med in parte:
        archivo.write(med)    
    archivo.close() 

def iniciarc():
    archivo=open("juegocarreras.txt", "r")
    parte=archivo.readlines()
    archivo.close()
    archivo=open("juegocarreras.txt","w")
    metros=0
    while metros<50000:
        x=0
        participante=input("Ingrese el id del jugador a lanzar: \n")
        for dato in parte:
            if dato == participante+"\n":
                x=x+3
                print(random.randrange(6))
                metros=int(parte[x])+((random.randrange(6))*100)
                parte.insert(x,str(metros)+"\n") 
                break
            else:
                x+=1
    t=0
    for sig in parte:
        if sig >="50000":
            print("El jugador "+parte[t]+" es el ganador")
            break
        else:
            t+=1
    for med in parte:
        archivo.write(med)    
    archivo.close() 

confirmar=1
while confirmar!=6:
    print("Menu Principal")
    print("1.Ver listado de jugadores ")
    print("2.Agregar jugadores        ")
    print("3.Iniciar juego            ")
    print("4.Salir                    ")
    confirmar=int(input("Ingrese opcion: \n"))
    if confirmar==1:
        archivo.close()
        datos()
    elif confirmar==2:
        archivo.close()
        agregar()
    elif confirmar==3:
        inicio=1
        
        while inicio!=4:
            print("Menu pista carrera")
            print("1. 20 kilometros ")
            print("2. 30 kilometros ")
            print("3. 50 kilometros ")
            print("4. Salir")
            inicio=int(input("Ingrese opción: \n"))
            if inicio==1:
                archivo.close()
                iniciara()
            elif inicio==2:
                archivo.close()
                iniciarb()
            elif inicio==3:
                archivo.close()
                iniciarc()
            elif inicio==4:
                break
            else:
                print("Opción incorrecta")
            
    elif confirmar==4:
        break
    else:
        print("Opcion incorrecta")      
print("Hasta luego")
archivo.close()