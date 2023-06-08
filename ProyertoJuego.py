import random, os 
'''El proyecto se trata de tomar el concepto del juego "Piedra, Papel, Tijeras" 
y llevarlo a un nuevo nivel agregando una seleccion de personajes quienens 
tendran resistencias y debilidades. 
Propongo remplazar la piedra, papel o tijeras por ataques de fuego, agua y tierra
donde el fuego le gana a la tierra, la tierra al agua y el agua al fuego. Agrego
una potencia o fuerza de daño base a cada ataque que defino en 100 puntos y sumo 
una interaccion entre ellos, que segun la combinacion de ambos sus valoresde 
fuerza se modificaran. Esto esta definido en la funcion "ChoqueDeAtaques" y determina
con que potencia impacta el ataque enemigo a los personajes:
ATAQUES IGUALES=  La potencia de ambos se reduce a la mitad 
AGUA con FUEGO= AGUA conserva 100 puntos, FUEGO se modifica a 0 puntos de ataque
FUAGO con TIERRA= FUEGO conserva 100 puntos, TIERRA se modifica a 0 puntos de ataque
TIERRA con AGUA= TIERRA conserva 100 puntos, AGUA se modifica a 0 puntos de ataque.

Pero a la vez creo a tres personajes (que para un fin comico les doy profesiones)
quienes seran el Plomero, el Gasista y el Jardinero. Donde el Plomero al trabajar 
con agua (podriamos presumir que ese es su elemento) tiene una resistencia del 
100% al elemento fuego, una resistencia media o del 50% al elemento agua y una 
resistencia nula o 0% al elemento tierra. de ingual manera los otros dos personajes
quedando el configurado el cuadro siguiente:
Plomero       |Gasista        |Jardinero
res AGUA   50%|res AGUA     0%|res AGUA  100%
res FUEGO 100%|res FUEGO   50%|res FUEGO   0%
res TIERRA  0%|res TIERRA 100%|res TIERRA 50%

De esta manera las posibilidades de recibir daño en cada jugada son tres (25,50 o 100)
este daño se descontara de la salud inicial del personaje que definí en 300 puntos.
'''
#__________________________________________Defino valores de Personajes
personajeJugador=["Profesion neutra",300]
personajeEnemigo=["Profesion neutra",300]
#_____________________________________________Defino valores de Ataques
ataquej=["ELEMENTO",100]
ataqueE=["ELEMENTO",100]
#____________________________________________Defino potencia de Ataques
def ChoqueDeAtaques(ataque1, ataque2):
    if ataque1[0]==ataque2[0]:
        ataque1[1]=ataque1[1]/2
        ataque2[1]=ataque2[1]/2
    elif ataque1[0]=="AGUA" and ataque2[0]=="FUEGO":
        ataque2[1]=0
    elif ataque1[0]=="FUEGO" and ataque2[0]=="TIERRA":
        ataque2[1]=0
    elif ataque1[0]=="TIERRA" and ataque2[0]=="AGUA":
        ataque2[1]=0
    else:
        ataque1=0
#___________________________Defino potencia de Debilidades y Fortalezas
def plomero(ataque, salud):
    salud=int()
    if ataque[0]=="AGUA":
        salud=salud-(ataque[1]/2)
    elif ataque[0]=="TIERRA":
        salud=salud-ataque[1]
    else:
        return int(salud)    
def Gasista(ataque, salud):
    salud=int()
    if ataque[0]=="AGUA":
        salud=salud-(ataque[1]/2)
    elif ataque[0]=="TIERRA":
        salud=salud-ataque[1]
    else:
        return int(salud)
def jardinero(ataque, salud):
    salud=int()
    if ataque[0]=="AGUA":
        salud=salud-(ataque[1]/2)
    elif ataque[0]=="TIERRA":
        salud=salud-ataque[1]
    else:
        return int(salud)
#_______________________________________________Asignacion de profesion
def Profesion(jugador):
    if jugador==1:
        profesion="Plomero"
    elif jugador==2:
        profesion="Gasista"
    elif jugador==3:
        profesion="Jardinero" 
    return profesion  
def Ataque(OP):
    if OP==1:
        ataque="AGUA"
    elif OP==2:
        ataque="FUEGO"
    elif OP==3:
        ataque="TIERRA" 
    return ataque 
#_____________________________Defino muestra de estado de los Jugadores
def EstadoJugadores():
    print("_____________________________________________________________________")
    print(f"Tu {personajeJugador[0]} tiene {personajeJugador[1]} puntos de salud")
    print(f"El {personajeEnemigo[0]} tiene {personajeEnemigo[1]} puntos de salud")
    print("_____________________________________________________________________")
def MenuPersonajes():
    print("_________________PERSONAJE_")
    print("1 - Plomero________________")
    print("2 - Gasista________________")
    print("3 - Jardinero______________")
    print("___________________________")
def MenuAtaques():
    print("_____________________ATAQUE_")
    print("1 - AGUA____________________")
    print("2 - FUEGO___________________")
    print("3 - TIERRA__________________")
    print("____________________________")
#____________________________________________Seleccionamos el personaje
while True:
    sJ=personajeJugador[1]
    sE=personajeEnemigo[1]
    sJ=int() 
    sE=int()
    if sJ>=0 or sE>=0:
        EstadoJugadores()
        MenuPersonajes()
        jugador=int(input(print("elija a un jugador: ")))
        personajeJugador[0]=Profesion(jugador)
        pEnemigo=int(random.randrange(0,3)//1+1)
        personajeEnemigo[0]=Profesion(pEnemigo)
        os.system("cls")
        print(f"La batalla será entre El {personajeJugador[0]} y El {personajeEnemigo[0]}")
        #______________________________________________Seleccionamos el ataque
        EstadoJugadores()
        MenuAtaques()
        ataque=int(input(print("elija un ataque:")))
        ataquej[0]=Ataque(ataque)
        aEnemigo=int(random.randrange(0,3)//1+1)
        ataqueE[0]=Ataque(aEnemigo)
        os.system("cls")
        print(f"El {personajeJugador[0]} atacó con {ataquej[0]}")
        print(f"El {personajeEnemigo[0]} atacó con {ataqueE[0]}")
        #__________________________________Comparamos fortalezas y Debilidades
        ChoqueDeAtaques(ataquej,ataqueE)
        if personajeJugador[0]=="Plomero":
            personajeJugador[1]=plomero(ataqueE,personajeJugador[1])
        elif personajeJugador[0]=="Gasista":
            personajeJugador[1]=Gasista(ataqueE,personajeJugador[1])
        elif personajeJugador[0]=="Jardinero":
            personajeJugador[1]=jardinero(ataqueE,personajeJugador[1])

        if personajeEnemigo[0]=="Plomero":
            personajeEnemigo[1]=plomero(ataqueE,personajeEnemigo[1])
        elif personajeEnemigo[0]=="Gasista":
            personajeEnemigo[1]=Gasista(ataqueE,personajeEnemigo[1])
        elif personajeEnemigo[0]=="Jardinero":
            personajeEnemigo[1]=jardinero(ataqueE,personajeEnemigo[1])
    else:
        break  
#___________________________________Muestra de resultado de la partida
if personajeJugador[1]==personajeEnemigo[1]:
    print("Wow! es una empate!")
elif personajeJugador[1]==0:
    ganador=personajeEnemigo[0]
    print(f"El ganador es el {ganador}!")
else:
    ganador=personajeJugador[1]
    print(f"El ganador es el {ganador}!")