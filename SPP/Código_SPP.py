import numpy as np
import random 
from time import time
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

## importar librerias y herramientas

random.seed(0)
np.random.seed(0)

##iniciar semilla random

def dibujar(HA_ik,Productos,Dimensiones):
##graficar resultados

    fig = plt.figure()
## crear figura

##definir las 8 vertices una caja

    x0=HA_ik[:, [0]] #0= dimension x

    y0=HA_ik[:, [1]] #1=dimension y

    z0=HA_ik[:, [2]] #2=dimension z
    

    x1=HA_ik[:, [0]]+Dimensiones[:,[0]]

    y1=HA_ik[:, [1]]

    z1=HA_ik[:, [2]]
    

    x2=HA_ik[:, [0]]+Dimensiones[:,[0]]

    y2=HA_ik[:, [1]]+Dimensiones[:,[1]]

    z2=HA_ik[:, [2]]
    

    x3=HA_ik[:, [0]]

    y3=HA_ik[:, [1]]+Dimensiones[:,[1]]

    z3=HA_ik[:, [2]]
    

    x4=HA_ik[:, [0]]

    y4=HA_ik[:, [1]]

    z4=HA_ik[:, [2]]+Dimensiones[:,[2]]
    

    x5=HA_ik[:, [0]]+Dimensiones[:,[0]]

    y5=HA_ik[:, [1]]

    z5=HA_ik[:, [2]]+Dimensiones[:,[2]]
    

    x6=HA_ik[:, [0]]+Dimensiones[:,[0]]

    y6=HA_ik[:, [1]]+Dimensiones[:,[1]]

    z6=HA_ik[:, [2]]+Dimensiones[:,[2]]
    

    x7=HA_ik[:, [0]]

    y7=HA_ik[:, [1]]+Dimensiones[:,[1]]

    z7=HA_ik[:, [2]]+Dimensiones[:,[2]]



    ax1 = fig.add_subplot(111, projection='3d')
#grafica fondo con cuadratura
#definir contorno de la figura, es decir se dibuja el contenedor

    ax1.plot((0,0),(0,150),(0,0),color="black")

    ax1.plot((MX[0],MX[0]),(0,150),(0,0),color="black")

    ax1.plot((0,MX[0]),(150,150),(0,0),color="black")

    ax1.plot((MX[0],MX[0]),(150,150),(0,215),color="black")

    ax1.plot((0,0),(150,150),(0,215),color="black")

    ax1.plot((0,MX[0]),(150,150),(215,215),color="black")

    ax1.plot((0,0),(0,150),(215,215),color="black")

    ax1.plot((0,MX[0]),(0,0),(0,0),color="black")

    ax1.plot((MX[0],MX[0]),(0,150),(215,215),color="black")

    ax1.plot((0,MX[0]),(0,0),(215,215),color="black")

    ax1.plot((MX[0],MX[0]),(75,75),(0,215),color="black")

    ax1.plot((MX[0],MX[0]),(0,0),(0,215),color="black")

    ax1.plot((0,0),(0,0),(0,215),color="black")

#se grafica los objetos de cada cliente con un color diferente, se grafica cada arista por separado
    for k in range(Clientes):
        for i in range(Productos):
            if Dimensiones[i][3]==k+1:
                ax1.plot((x0[i][0],x1[i][0]),(y0[i][0],y1[i][0]),(z0[i][0],z1[i][0]), color=colores[k])

                ax1.plot((x1[i][0],x2[i][0]),(y1[i][0],y2[i][0]),(z1[i][0],z2[i][0]), color=colores[k])

                ax1.plot((x2[i][0],x3[i][0]),(y2[i][0],y3[i][0]),(z2[i][0],z3[i][0]), color=colores[k])

                ax1.plot((x0[i][0],x4[i][0]),(y0[i][0],y4[i][0]),(z0[i][0],z4[i][0]), color=colores[k])

                ax1.plot((x4[i][0],x5[i][0]),(y4[i][0],y5[i][0]),(z4[i][0],z5[i][0]), color=colores[k])
            
                ax1.plot((x5[i][0],x6[i][0]),(y5[i][0],y6[i][0]),(z5[i][0],z6[i][0]), color=colores[k])

                ax1.plot((x6[i][0],x7[i][0]),(y6[i][0],y7[i][0]),(z6[i][0],z7[i][0]), color=colores[k])

                ax1.plot((x4[i][0],x7[i][0]),(y4[i][0],y7[i][0]),(z4[i][0],z7[i][0]), color=colores[k])

                ax1.plot((x0[i][0],x3[i][0]),(y0[i][0],y3[i][0]),(z0[i][0],z3[i][0]), color=colores[k])

                ax1.plot((x2[i][0],x6[i][0]),(y2[i][0],y6[i][0]),(z2[i][0],z6[i][0]), color=colores[k])

                ax1.plot((x3[i][0],x7[i][0]),(y3[i][0],y7[i][0]),(z3[i][0],z7[i][0]), color=colores[k])

                ax1.plot((x1[i][0],x5[i][0]),(y1[i][0],y5[i][0]),(z1[i][0],z5[i][0]), color=colores[k])

   
#se muestra la figura final
    plt.show()
  
    

Dimensiones=np.genfromtxt('R08-2.csv', dtype=int ,delimiter=',')
#importa dimenciones de los objetos

Ceros=np.genfromtxt('CerosR08-2.csv', dtype=int,delimiter=',')
#importa posiciones inicializadas en 0


#variables
Guarda_todo=[]

Guarda_Optimo=[]

tiempo_optimo=[]

tiempo_no_optimo=[]

HA_ik = [] #coordenadas de los objetos

MatrizOptima=[]

MatrizOptima2=[]

MX=[]

MX=[485,150,215]#dimensiones camión

Harmonica=[]


#valores iniciales
Optimo = 0

elapsed_time = 0

iteracion = 0


r_acept =0.7 # Probabilidad en Paper 0.7-0.95

r_pa = 0.1 # Probabilidad en Paper 0.1-0.5

sp=0.5#fragilidad

sa=0.5#apoyo


Productos =len(Dimensiones) #N° de cajas
Clientes=max(Dimensiones[:,3]) #N° de cliente

#se muestra en consola
print ("Rpa y Raccept",r_pa,r_acept)

TiempoDeComputo = int(input ("Tiempo de ejecución: "))
#TiempoDeComputo = 20000 #tiempo usado en instancias finales

print("considerando ",Productos," productos y ",Clientes," clientes")

colores=["red","grey","magenta","c","yellow","blue","green","peru","darkviolet","indigo","orange","lime","maroon","pink","gold"]#maximo 15 clientes

starting_point = time()


MA=np.zeros(Productos)


#inicio sol inicial


SI=Ceros

maxx=[0]
maxy=[0]
fin=0

for k in range (Clientes):
    for i in range (Productos):
        if i==0:
            SI[0][0]=0
            SI[0][1]=0
            SI[0][2]=0
            if k==0:
                maxx.append(Dimensiones[i][0])
                maxy.append(Dimensiones[i][1])
        else:
            
            if Dimensiones[i][3]==k+1:

                if Dimensiones[i][3]!=Dimensiones[i-1][3]:
                    SI[i][0]=fin
                    SI[i][1]=0
                    SI[i][2]=0
                    maxx.append(Dimensiones[i][0])
                    maxy.append(Dimensiones[i][1])
                
                else:
                    
                    if SI[i-1][1]+Dimensiones[i-1][1]+Dimensiones[i][1]<=MX[1]:      #para x 
                        SI[i][0]=SI[i-1][0]
                        maxx.append(Dimensiones[i][0])
                    elif SI[i-1][2]+Dimensiones[i-1][2]+Dimensiones[i][2]<=MX[2]:
                        SI[i][0]=SI[i-1][0]
                        maxx.append(Dimensiones[i][0])
                    else:
                        SI[i][0]=SI[i-1][0]+max(maxx)
                        maxx=[Dimensiones[i][0]]
                
                
                    if SI[i-1][1]+Dimensiones[i-1][1]+Dimensiones[i][1]>MX[1]:      #para y
                        if SI[i-1][2]+Dimensiones[i-1][2]+Dimensiones[i][2]>MX[2]:
                            SI[i][1]=0
                            maxy.append(Dimensiones[i][1])
                        else:
                            SI[i][1]=SI[i-1][1]
                            maxy.append(Dimensiones[i][1])
                    elif SI[i-1][2]+Dimensiones[i-1][2]+Dimensiones[i][2]>MX[2]:
                        SI[i][1]=SI[i-1][1]+max(maxy)
                        maxy=[Dimensiones[i][1]]
                    else:
                        SI[i][1]=SI[i-1][1]
                        maxy.append(Dimensiones[i][1])
                    
                    
                    if SI[i-1][2]+Dimensiones[i-1][2]+Dimensiones[i][2]>MX[2]:      #para z 
                        SI[i][2]=0
                    else:
                        SI[i][2]=SI[i-1][2]+Dimensiones[i-1][2]
                
                
                if SI[i][0]+Dimensiones[i][0]>fin:
                    maxx.append(Dimensiones[i][0])
                    fin=SI[i][0]+max(maxx)
                    maxx.remove(Dimensiones[i][0])
    
    maxx=[0]
    maxy=[0]
    MX[0]=fin #para graficar el limite del camión
    
#fin crear solucion inicial


Hik = Ceros

HA_ik = SI

HA = SI 

nc=np.zeros(Clientes)
cc=np.zeros(Clientes)
   
#se obtienen las cajas por cliente
for k in range (Clientes):
    for i in range (Productos):
        if Dimensiones[i][3]==k+1:
            nc[k]=nc[k]+1
    if nc[k]==1:
        cc[k]=k+1

for k in range (Clientes):
    print(k+1, " Cliente tiene ",nc[k]," cajas",cc) 



def Volumen(HA_ik,Dimensiones,k):#calcula volumen entre parte trasera del que esta mas atras con la parte trasera del que esta mas adelante...falta la parte delantera del que esta mas adelante/como saber cuas es el i que hay que sumarle la dimension????????
    vk=0
    xa=[]
    xb=[]
    ya=[]
    yb=[]
    za=[]
    zb=[]
    for i in range(Productos):
        if Dimensiones[i][3]==k+1:
            xa.append(HA_ik[i][0])
            xb.append(HA_ik[i][0]+Dimensiones[i][0])
            ya.append(HA_ik[i][1])
            yb.append(HA_ik[i][1]+Dimensiones[i][1])
            za.append(HA_ik[i][2])
            zb.append(HA_ik[i][2]+Dimensiones[i][2])
            
    vk=((max(xb)-min(xa))*(max(yb)-min(ya))*(max(zb)-min(za)))
    return vk

#se calculan dotos de volumen de sol inicial
v0=0
vi=np.zeros(Clientes)
vm=np.zeros(Clientes)

for k in range(Clientes):#se invoca Volumen
    vi[k]=Volumen(SI,Dimensiones,k)
    v0=v0+vi[k]



def MoverCaja2(HA_ik,k,i,r,t,u):
#intercambiar pares de objetos, para funcion overlap
    while True:

        A=random.choice([0,1])
        
        B=random.choice([0,1])

        C=random.choice([0,1])

        if A+B+C==1:

            break


    HA_ik[i][k]=(HA_ik[u][k]+Dimensiones[u][k])*A+HA_ik[i][k]*(1-A)

    HA_ik[i][t]=(HA_ik[u][t]+Dimensiones[u][t])*B+HA_ik[i][t]*(1-B)

    HA_ik[i][r]=(HA_ik[u][r]+Dimensiones[u][r])*C+HA_ik[i][r]*(1-C) 


    if MX[k]-Dimensiones[i][k]<HA_ik[i][k]:

        HA_ik[i][k]=MX[k]-Dimensiones[i][k]

        WA=random.choice([0,1])

        HA_ik[i][r]=(min(HA_ik[:Productos,r]))*WA+HA_ik[i][r]*(1-WA)

        HA_ik[i][t]=(min(HA_ik[:Productos,t]))*(1-WA)+HA_ik[i][t]*WA


    if MX[t]-Dimensiones[i][t]<HA_ik[i][t]:

        HA_ik[i][t]=MX[t]-Dimensiones[i][t]

        WA=random.choice([0,1])

        HA_ik[i][r]=(min(HA_ik[:Productos,r]))*WA+HA_ik[i][r]*(1-WA)

        HA_ik[i][k]=(min(HA_ik[:Productos,k]))*(1-WA)+HA_ik[i][k]*WA


    if MX[r]-Dimensiones[i][r]<HA_ik[i][r]:

        HA_ik[i][r]=MX[r]-Dimensiones[i][r]

        WA=random.choice([0,1])

        HA_ik[i][k]=(min(HA_ik[:Productos,k]))*WA+HA_ik[i][k]*(1-WA)

        HA_ik[i][t]=(min(HA_ik[:Productos,t]))*(1-WA)+HA_ik[i][t]*WA    


    return HA_ik




v=0
def adyacente(HA_ik,i,u,r,q,v,Dimensiones):#devuelve 1 si tiene un adyacente del mismo cliente, 0 si no es del mismo
    if ((HA_ik[u][r]>=HA_ik[i][r] and HA_ik[u][r]<=HA_ik[i][r]+Dimensiones[i][r] and HA_ik[u][q]>=HA_ik[i][q] and HA_ik[u][q]<=HA_ik[i][q]+Dimensiones[i][q])
    or (HA_ik[u][r]+Dimensiones[u][r]>=HA_ik[i][r] and HA_ik[u][r]+Dimensiones[u][r]<=HA_ik[i][r]+Dimensiones[i][r] and HA_ik[u][q]+Dimensiones[u][q]>=HA_ik[i][q] and HA_ik[u][q]+Dimensiones[u][q]<=HA_ik[i][q]+Dimensiones[i][q])
    or (HA_ik[u][r]>=HA_ik[i][r] and HA_ik[u][r]<=HA_ik[i][r]+Dimensiones[i][r] and HA_ik[u][q]+Dimensiones[u][q]>=HA_ik[i][q] and HA_ik[u][q]+Dimensiones[u][q]<=HA_ik[i][q]+Dimensiones[i][q])
    or (HA_ik[u][r]+Dimensiones[u][r]>=HA_ik[i][r] and HA_ik[u][r]+Dimensiones[u][r]<=HA_ik[i][r]+Dimensiones[i][r] and HA_ik[u][q]>=HA_ik[i][q] and HA_ik[u][q]<=HA_ik[i][q]+Dimensiones[i][q])):
        if Dimensiones[i][3]==Dimensiones[u][3]:
            v=1#tiene un adyacente del mismo cliente
    return v


def adyacente2(HA_ik,i,u,r,q,v,Dimensiones):#devuelve 1 si tiene un adyacente , 0 eoc.
    v=0
    if ((HA_ik[u][r]>=HA_ik[i][r] and HA_ik[u][r]<=HA_ik[i][r]+Dimensiones[i][r] and HA_ik[u][q]>=HA_ik[i][q] and HA_ik[u][q]<=HA_ik[i][q]+Dimensiones[i][q])
    or (HA_ik[u][r]+Dimensiones[u][r]>=HA_ik[i][r] and HA_ik[u][r]+Dimensiones[u][r]<=HA_ik[i][r]+Dimensiones[i][r] and HA_ik[u][q]+Dimensiones[u][q]>=HA_ik[i][q] and HA_ik[u][q]+Dimensiones[u][q]<=HA_ik[i][q]+Dimensiones[i][q])
    or (HA_ik[u][r]>=HA_ik[i][r] and HA_ik[u][r]<=HA_ik[i][r]+Dimensiones[i][r] and HA_ik[u][q]+Dimensiones[u][q]>=HA_ik[i][q] and HA_ik[u][q]+Dimensiones[u][q]<=HA_ik[i][q]+Dimensiones[i][q])
    or (HA_ik[u][r]+Dimensiones[u][r]>=HA_ik[i][r] and HA_ik[u][r]+Dimensiones[u][r]<=HA_ik[i][r]+Dimensiones[i][r] and HA_ik[u][q]>=HA_ik[i][q] and HA_ik[u][q]<=HA_ik[i][q]+Dimensiones[i][q])):
        v=1#tiene un adyacente 
    return v




j=0
def movf(HA_ik,Dimensiones,i):#si es muy pesada o no esta en equilibrio, dejar en el piso
    global j
    j=0  
    for h in range(Productos):#colocar arriba de una caja del mismo cliente
        if h!=i:
            if Dimensiones[i][3]==Dimensiones[h][3]:
                for k in range(Productos):
                    j=0
                    if (h!=k and i!=k):
                        if HA_ik[h][2]+Dimensiones[h][2]==HA_ik[k][2]:
                            j=adyacente2(HA_ik,h,k,0,1,0,Dimensiones)
                            if j==1:
                                break
                if j==0:
                    if Dimensiones[i][4]<=Dimensiones[h][4]:
                        if ((HA_ik[h][2]+Dimensiones[h][2]+Dimensiones[i][2]<=MX[2])and(HA_ik[h][0]+Dimensiones[i][0]<=MX[0])and(HA_ik[h][1]+Dimensiones[i][1]<=MX[1])):
                            for l in range(Productos):
                                if (l!=h and l!=i):
                                    if (((HA_ik[l][2]<=HA_ik[h][2]+Dimensiones[h][2]<HA_ik[l][2]+Dimensiones[l][2])or(HA_ik[l][2]<HA_ik[h][2]+Dimensiones[h][2]+Dimensiones[i][2]<=HA_ik[l][2]+Dimensiones[l][2])or (HA_ik[l][2]<=HA_ik[h][2]+Dimensiones[h][2]<HA_ik[h][2]+Dimensiones[h][2]+Dimensiones[i][2]<=HA_ik[l][2]+Dimensiones[l][2])or (HA_ik[h][2]+Dimensiones[h][2]<=HA_ik[l][2]<HA_ik[l][2]+Dimensiones[l][2]<=HA_ik[h][2]+Dimensiones[h][2]+Dimensiones[i][2]))
                                    and((HA_ik[l][0]<=HA_ik[h][0]<HA_ik[l][0]+Dimensiones[l][0])or (HA_ik[l][0]<HA_ik[h][0]+Dimensiones[i][0]<=HA_ik[l][0]+Dimensiones[l][0])or (HA_ik[l][0]<=HA_ik[h][0]<HA_ik[h][0]+Dimensiones[i][0]<=HA_ik[l][0]+Dimensiones[l][0])or (HA_ik[h][0]<=HA_ik[l][0]<HA_ik[l][0]+Dimensiones[l][0]<=HA_ik[h][0]+Dimensiones[i][0]))
                                    and ((HA_ik[l][1]<=HA_ik[h][1]<HA_ik[l][1]+Dimensiones[l][1])or (HA_ik[l][1]<HA_ik[h][1]+Dimensiones[i][1]<=HA_ik[l][1]+Dimensiones[l][1])or (HA_ik[l][1]<=HA_ik[h][1]<HA_ik[h][1]+Dimensiones[i][1]<=HA_ik[l][1]+Dimensiones[l][1])or (HA_ik[h][1]<=HA_ik[l][1]<HA_ik[l][1]+Dimensiones[l][1]<=HA_ik[h][1]+Dimensiones[i][1]))):
                                        j=1
                                        break
                            if j==0:
                                HA_ik[i][0]=HA_ik[h][0]
                                HA_ik[i][1]=HA_ik[h][1]
                                HA_ik[i][2]=HA_ik[h][2]+Dimensiones[h][2]
                                j=2
                                break
   

    if j!=2:
        for h in range(Productos):#colocar a la derecha de uno del mismo cliente
            if h!=i:
                if Dimensiones[i][3]==Dimensiones[h][3]:
                    for k in range(Productos):
                        j=0
                        if (h!=k and i!=k):
                            if HA_ik[h][1]+Dimensiones[h][1]==HA_ik[k][1]:
                                j=adyacente2(HA_ik,h,k,2,0,0,Dimensiones)
                                if j==1:
                                    break
                    if j==0:
                        if HA_ik[h][2]==0:
                            if ((HA_ik[h][1]+Dimensiones[h][1]+Dimensiones[i][1]<=MX[1])and(HA_ik[h][0]+Dimensiones[i][0]<=MX[0])):              
                                for l in range(Productos):
                                    if (l!=h and l!=i):
                                        if (((HA_ik[l][1]<=HA_ik[h][1]+Dimensiones[h][1]<HA_ik[l][1]+Dimensiones[l][1])or(HA_ik[l][1]<HA_ik[h][1]+Dimensiones[h][1]+Dimensiones[i][1]<=HA_ik[l][1]+Dimensiones[l][1])or (HA_ik[l][1]<=HA_ik[h][1]+Dimensiones[h][1]<HA_ik[h][1]+Dimensiones[h][1]+Dimensiones[i][1]<=HA_ik[l][1]+Dimensiones[l][1])or (HA_ik[h][1]+Dimensiones[h][1]<=HA_ik[l][1]<HA_ik[l][1]+Dimensiones[l][1]<=HA_ik[h][1]+Dimensiones[h][1]+Dimensiones[i][1]))
                                        and((HA_ik[l][2]<=HA_ik[h][2]<HA_ik[l][2]+Dimensiones[l][2])or (HA_ik[l][2]<HA_ik[h][2]+Dimensiones[i][2]<=HA_ik[l][2]+Dimensiones[l][2])or (HA_ik[l][2]<=HA_ik[h][2]<HA_ik[h][2]+Dimensiones[i][2]<=HA_ik[l][2]+Dimensiones[l][2])or (HA_ik[h][2]<=HA_ik[l][2]<HA_ik[l][2]+Dimensiones[l][2]<=HA_ik[h][2]+Dimensiones[i][2]))
                                        and ((HA_ik[l][0]<=HA_ik[h][0]<HA_ik[l][0]+Dimensiones[l][0])or (HA_ik[l][0]<HA_ik[h][0]+Dimensiones[i][0]<=HA_ik[l][0]+Dimensiones[l][0])or (HA_ik[l][0]<=HA_ik[h][0]<HA_ik[h][0]+Dimensiones[i][0]<=HA_ik[l][0]+Dimensiones[l][0])or (HA_ik[h][0]<=HA_ik[l][0]<HA_ik[l][0]+Dimensiones[l][0]<=HA_ik[h][0]+Dimensiones[i][0]))):
                                            j=1
                                            break
                                if j==0:
                                    HA_ik[i][0]=HA_ik[h][0]
                                    HA_ik[i][1]=HA_ik[h][1]+Dimensiones[h][1]
                                    HA_ik[i][2]=HA_ik[h][2]
                                    j=2
                                    break
                      
                                    
    if j!=2:
        for h in range(Productos):#colocar a la izquierda de uno del mismo cliente
            if h!=i:
                if Dimensiones[i][3]==Dimensiones[h][3]:
                    for k in range(Productos):
                        j=0
                        if (h!=k and i!=k):
                            if HA_ik[h][1]==HA_ik[k][1]+Dimensiones[k][1]:
                                j=adyacente2(HA_ik,h,k,2,0,0,Dimensiones)
                                if j==1:
                                    break
                    if j==0:
                        if HA_ik[h][2]==0:
                            if ((HA_ik[h][1]-Dimensiones[i][1]>=0)and(HA_ik[h][0]+Dimensiones[i][0]<=MX[0])):
                                for l in range(Productos):
                                    if (l!=h and l!=i):
                                        if (((HA_ik[l][1]<=HA_ik[h][1]-Dimensiones[i][1]<HA_ik[l][1]+Dimensiones[l][1])or(HA_ik[l][1]<HA_ik[h][1]<=HA_ik[l][1]+Dimensiones[l][1]) or (HA_ik[l][1]<=HA_ik[h][1]-Dimensiones[i][1]<HA_ik[h][1]<=HA_ik[l][1]+Dimensiones[l][1])or (HA_ik[h][1]-Dimensiones[i][1]<=HA_ik[l][1]<HA_ik[l][1]+Dimensiones[l][1]<=HA_ik[h][1]))
                                        and ((HA_ik[l][2]<=HA_ik[h][2]<HA_ik[l][2]+Dimensiones[l][2])or (HA_ik[l][2]<HA_ik[h][2]+Dimensiones[i][2]<=HA_ik[l][2]+Dimensiones[l][2]) or (HA_ik[l][2]<=HA_ik[h][2]<HA_ik[h][2]+Dimensiones[i][2]<=HA_ik[l][2]+Dimensiones[l][2])or (HA_ik[h][2]<=HA_ik[l][2]<HA_ik[l][2]+Dimensiones[l][2]<=HA_ik[h][2]+Dimensiones[i][2]))#revisar esto de abajo
                                        and ((HA_ik[l][0]<=HA_ik[h][0]<HA_ik[l][0]+Dimensiones[l][0])or (HA_ik[l][0]<HA_ik[h][0]+Dimensiones[i][0]<=HA_ik[l][0]+Dimensiones[l][0]) or (HA_ik[l][0]<=HA_ik[h][0]<HA_ik[h][0]+Dimensiones[i][0]<=HA_ik[l][0]+Dimensiones[l][0])or (HA_ik[h][0]<=HA_ik[l][0]<HA_ik[l][0]+Dimensiones[l][0]<=HA_ik[h][0]+Dimensiones[i][0]))):
                                            j=1
                                            break
                                if j==0:
                                    HA_ik[i][0]=HA_ik[h][0]
                                    HA_ik[i][1]=HA_ik[h][1]-Dimensiones[i][1]
                                    HA_ik[i][2]=HA_ik[h][2]
                                    j=2
                                    break
                                
    if j!=2:
        for h in range(Productos):#colocar atras de uno del mismo cliente
            if h!=i:
                if Dimensiones[i][3]==Dimensiones[h][3]:
                    for k in range(Productos):
                        j=0
                        if (h!=k and i!=k):
                            if HA_ik[h][0]==HA_ik[k][0]+Dimensiones[k][0]:
                                j=adyacente2(HA_ik,h,k,2,1,0,Dimensiones)
                                if j==1:
                                    break
                    if j==0:
                        if HA_ik[h][2]==0:
                            if ((HA_ik[h][0]-Dimensiones[i][0]>=0)and(HA_ik[h][1]+Dimensiones[i][1]<=MX[1])):
                                for l in range(Productos):
                                    if (l!=h and l!=i):
                                        if (((HA_ik[l][0]<=HA_ik[h][0]-Dimensiones[i][0]<HA_ik[l][0]+Dimensiones[l][0])or(HA_ik[l][0]<HA_ik[h][0]<=HA_ik[l][0]+Dimensiones[l][0])or (HA_ik[l][0]<=HA_ik[h][0]-Dimensiones[i][0]<HA_ik[h][0]<=HA_ik[l][0]+Dimensiones[l][0])or (HA_ik[h][0]-Dimensiones[i][0]<=HA_ik[l][0]<HA_ik[l][0]+Dimensiones[l][0]<=HA_ik[h][0]))
                                        and ((HA_ik[l][2]<=HA_ik[h][2]<HA_ik[l][2]+Dimensiones[l][2])or (HA_ik[l][2]<HA_ik[h][2]+Dimensiones[i][2]<=HA_ik[l][2]+Dimensiones[l][2])or (HA_ik[l][2]<=HA_ik[h][2]<HA_ik[h][2]+Dimensiones[i][2]<=HA_ik[l][2]+Dimensiones[l][2])or (HA_ik[h][2]<=HA_ik[l][2]<HA_ik[l][2]+Dimensiones[l][2]<=HA_ik[h][2]+Dimensiones[i][2]))
                                        and ((HA_ik[l][1]<=HA_ik[h][1]<HA_ik[l][1]+Dimensiones[l][1])or (HA_ik[l][1]<HA_ik[h][1]+Dimensiones[i][1]<=HA_ik[l][1]+Dimensiones[l][1])or (HA_ik[l][1]<=HA_ik[h][1]<HA_ik[h][1]+Dimensiones[i][1]<=HA_ik[l][1]+Dimensiones[l][1])or (HA_ik[h][1]<=HA_ik[l][1]<HA_ik[l][1]+Dimensiones[l][1]<=HA_ik[h][1]+Dimensiones[i][1]))):
                                            j=1
                                            break
                                if j==0:
                                    HA_ik[i][0]=HA_ik[h][0]-Dimensiones[i][0]
                                    HA_ik[i][1]=HA_ik[h][1]
                                    HA_ik[i][2]=HA_ik[h][2]
                                    j=2
                                    break



    if j!=2:
        for h in range(Productos):#colocar delante de uno del mismo cliente
            if h!=i:
                if Dimensiones[i][3]==Dimensiones[h][3]:
                    for k in range(Productos):
                        j=0
                        if (h!=k and i!=k):
                            if HA_ik[h][0]+Dimensiones[h][0]==HA_ik[k][0]:
                                j=adyacente2(HA_ik,h,k,2,1,0,Dimensiones)
                                if j==1:
                                    break
                    if j==0:
                        if HA_ik[h][2]==0:
                            if ((HA_ik[h][0]+Dimensiones[h][0]+Dimensiones[i][0]<=MX[0])and(HA_ik[h][1]+Dimensiones[i][1]<=MX[1])):
                                for l in range(Productos):
                                    if (l!=h and l!=i):
                                        if (((HA_ik[l][0]<=HA_ik[h][0]+Dimensiones[h][0]<HA_ik[l][0]+Dimensiones[l][0])or(HA_ik[l][0]<HA_ik[h][0]+Dimensiones[h][0]+Dimensiones[i][0]<=HA_ik[l][0]+Dimensiones[l][0])or (HA_ik[l][0]<=HA_ik[h][0]+Dimensiones[h][0]<HA_ik[h][0]+Dimensiones[h][0]+Dimensiones[i][0]<=HA_ik[l][0]+Dimensiones[l][0])or (HA_ik[h][0]+Dimensiones[h][0]<=HA_ik[l][0]<HA_ik[l][0]+Dimensiones[l][0]<=HA_ik[h][0]+Dimensiones[h][0]+Dimensiones[i][0]))
                                        and ((HA_ik[l][2]<=HA_ik[h][2]<HA_ik[l][2]+Dimensiones[l][2])or (HA_ik[l][2]<HA_ik[h][2]+Dimensiones[i][2]<=HA_ik[l][2]+Dimensiones[l][2])or (HA_ik[l][2]<=HA_ik[h][2]<HA_ik[h][2]+Dimensiones[i][2]<=HA_ik[l][2]+Dimensiones[l][2])or (HA_ik[h][2]<=HA_ik[l][2]<HA_ik[l][2]+Dimensiones[l][2]<=HA_ik[h][2]+Dimensiones[i][2]))
                                        and ((HA_ik[l][1]<=HA_ik[h][1]<HA_ik[l][1]+Dimensiones[l][1])or (HA_ik[l][1]<HA_ik[h][1]+Dimensiones[i][1]<=HA_ik[l][1]+Dimensiones[l][1])or (HA_ik[l][1]<=HA_ik[h][1]<HA_ik[h][1]+Dimensiones[i][1]<=HA_ik[l][1]+Dimensiones[l][1])or (HA_ik[h][1]<=HA_ik[l][1]<HA_ik[l][1]+Dimensiones[l][1]<=HA_ik[h][1]+Dimensiones[i][1]))):
                                            j=1
                                            break
                                if j==0:
                                    HA_ik[i][0]=HA_ik[h][0]+Dimensiones[h][0]
                                    HA_ik[i][1]=HA_ik[h][1]
                                    HA_ik[i][2]=HA_ik[h][2]
                                    j=2
                                    break
                                
                                
    if j!=2:
        for h in range(Productos):#colocar arriba de otro cliente
                if h!=i:
                    for k in range(Productos):
                        j=0
                        if (h!=k and i!=k):
                            if HA_ik[h][2]+Dimensiones[h][2]==HA_ik[k][2]:
                                j=adyacente2(HA_ik,h,k,0,1,0,Dimensiones)
                                if j==1:
                                    break
                    if j==0:
                        if Dimensiones[i][4]<=Dimensiones[h][4]:
                            if ((HA_ik[h][2]+Dimensiones[h][2]+Dimensiones[i][2]<=MX[2])and(HA_ik[h][0]+Dimensiones[i][0]<=MX[0])and(HA_ik[h][1]+Dimensiones[i][1]<=MX[1])):
                                for l in range(Productos):
                                    if (l!=h and l!=i):
                                        if (((HA_ik[l][2]<=HA_ik[h][2]+Dimensiones[h][2]<HA_ik[l][2]+Dimensiones[l][2])or(HA_ik[l][2]<HA_ik[h][2]+Dimensiones[h][2]+Dimensiones[i][2]<=HA_ik[l][2]+Dimensiones[l][2])or (HA_ik[l][2]<=HA_ik[h][2]+Dimensiones[h][2]<HA_ik[h][2]+Dimensiones[h][2]+Dimensiones[i][2]<=HA_ik[l][2]+Dimensiones[l][2])or (HA_ik[h][2]+Dimensiones[h][2]<=HA_ik[l][2]<HA_ik[l][2]+Dimensiones[l][2]<=HA_ik[h][2]+Dimensiones[h][2]+Dimensiones[i][2]))
                                        and((HA_ik[l][0]<=HA_ik[h][0]<HA_ik[l][0]+Dimensiones[l][0])or (HA_ik[l][0]<HA_ik[h][0]+Dimensiones[i][0]<=HA_ik[l][0]+Dimensiones[l][0])or (HA_ik[l][0]<=HA_ik[h][0]<HA_ik[h][0]+Dimensiones[i][0]<=HA_ik[l][0]+Dimensiones[l][0])or (HA_ik[h][0]<=HA_ik[l][0]<HA_ik[l][0]+Dimensiones[l][0]<=HA_ik[h][0]+Dimensiones[i][0]))
                                        and ((HA_ik[l][1]<=HA_ik[h][1]<HA_ik[l][1]+Dimensiones[l][1])or (HA_ik[l][1]<HA_ik[h][1]+Dimensiones[i][1]<=HA_ik[l][1]+Dimensiones[l][1])or (HA_ik[l][1]<=HA_ik[h][1]<HA_ik[h][1]+Dimensiones[i][1]<=HA_ik[l][1]+Dimensiones[l][1])or (HA_ik[h][1]<=HA_ik[l][1]<HA_ik[l][1]+Dimensiones[l][1]<=HA_ik[h][1]+Dimensiones[i][1]))):
                                            j=1
                                            break
                                if j==0:
                                    HA_ik[i][0]=HA_ik[h][0]
                                    HA_ik[i][1]=HA_ik[h][1]
                                    HA_ik[i][2]=HA_ik[h][2]+Dimensiones[h][2]
                                    j=2
                                    break
    
    if j!=2:
        for h in range(Productos):#colocar a la derecha de otro cliente
                if h!=i:
                    for k in range(Productos):
                        j=0
                        if (h!=k and i!=k):
                            if HA_ik[h][1]+Dimensiones[h][1]==HA_ik[k][1]:
                                j=adyacente2(HA_ik,h,k,2,0,0,Dimensiones)
                                if j==1:
                                    break
                    if j==0:
                        if HA_ik[h][2]==0:
                            if ((HA_ik[h][1]+Dimensiones[h][1]+Dimensiones[i][1]<=MX[1])and(HA_ik[h][0]+Dimensiones[i][0]<=MX[0])):              
                                for l in range(Productos):
                                    if (l!=h and l!=i):
                                        if (((HA_ik[l][1]<=HA_ik[h][1]+Dimensiones[h][1]<HA_ik[l][1]+Dimensiones[l][1])or(HA_ik[l][1]<HA_ik[h][1]+Dimensiones[h][1]+Dimensiones[i][1]<=HA_ik[l][1]+Dimensiones[l][1])or (HA_ik[l][1]<=HA_ik[h][1]+Dimensiones[h][1]<HA_ik[h][1]+Dimensiones[h][1]+Dimensiones[i][1]<=HA_ik[l][1]+Dimensiones[l][1])or (HA_ik[h][1]+Dimensiones[h][1]<=HA_ik[l][1]<HA_ik[l][1]+Dimensiones[l][1]<=HA_ik[h][1]+Dimensiones[h][1]+Dimensiones[i][1]))
                                        and((HA_ik[l][2]<=HA_ik[h][2]<HA_ik[l][2]+Dimensiones[l][2])or (HA_ik[l][2]<HA_ik[h][2]+Dimensiones[i][2]<=HA_ik[l][2]+Dimensiones[l][2])or (HA_ik[l][2]<=HA_ik[h][2]<HA_ik[h][2]+Dimensiones[i][2]<=HA_ik[l][2]+Dimensiones[l][2])or (HA_ik[h][2]<=HA_ik[l][2]<HA_ik[l][2]+Dimensiones[l][2]<=HA_ik[h][2]+Dimensiones[i][2]))
                                        and ((HA_ik[l][0]<=HA_ik[h][0]<HA_ik[l][0]+Dimensiones[l][0])or (HA_ik[l][0]<HA_ik[h][0]+Dimensiones[i][0]<=HA_ik[l][0]+Dimensiones[l][0])or (HA_ik[l][0]<=HA_ik[h][0]<HA_ik[h][0]+Dimensiones[i][0]<=HA_ik[l][0]+Dimensiones[l][0])or (HA_ik[h][0]<=HA_ik[l][0]<HA_ik[l][0]+Dimensiones[l][0]<=HA_ik[h][0]+Dimensiones[i][0]))):
                                            j=1
                                            break
                                if j==0:
                                    HA_ik[i][0]=HA_ik[h][0]
                                    HA_ik[i][1]=HA_ik[h][1]+Dimensiones[h][1]
                                    HA_ik[i][2]=HA_ik[h][2]
                                    j=2
                                    break

    
    if j!=2:
        for h in range(Productos):#colocar a la izquierda de otro cliente
            if h!=i:
                    for k in range(Productos):
                        j=0
                        if (h!=k and i!=k):
                            if HA_ik[h][1]==HA_ik[k][1]+Dimensiones[k][1]:
                                j=adyacente2(HA_ik,h,k,2,0,0,Dimensiones)
                                if j==1:
                                    break
                    if j==0:
                        if HA_ik[h][2]==0:
                            if ((HA_ik[h][1]-Dimensiones[i][1]>=0)and(HA_ik[h][0]+Dimensiones[i][0]<=MX[0])):
                                for l in range(Productos):
                                    if (l!=h and l!=i):
                                        if (((HA_ik[l][1]<=HA_ik[h][1]-Dimensiones[i][1]<HA_ik[l][1]+Dimensiones[l][1])or(HA_ik[l][1]<HA_ik[h][1]<=HA_ik[l][1]+Dimensiones[l][1]) or (HA_ik[l][1]<=HA_ik[h][1]-Dimensiones[i][1]<HA_ik[h][1]<=HA_ik[l][1]+Dimensiones[l][1])or (HA_ik[h][1]-Dimensiones[i][1]<=HA_ik[l][1]<HA_ik[l][1]+Dimensiones[l][1]<=HA_ik[h][1]))
                                        and ((HA_ik[l][2]<=HA_ik[h][2]<HA_ik[l][2]+Dimensiones[l][2])or (HA_ik[l][2]<HA_ik[h][2]+Dimensiones[i][2]<=HA_ik[l][2]+Dimensiones[l][2]) or (HA_ik[l][2]<=HA_ik[h][2]<HA_ik[h][2]+Dimensiones[i][2]<=HA_ik[l][2]+Dimensiones[l][2])or (HA_ik[h][2]<=HA_ik[l][2]<HA_ik[l][2]+Dimensiones[l][2]<=HA_ik[h][2]+Dimensiones[i][2]))#revisar esto de abajo
                                        and ((HA_ik[l][0]<=HA_ik[h][0]<HA_ik[l][0]+Dimensiones[l][0])or (HA_ik[l][0]<HA_ik[h][0]+Dimensiones[i][0]<=HA_ik[l][0]+Dimensiones[l][0]) or (HA_ik[l][0]<=HA_ik[h][0]<HA_ik[h][0]+Dimensiones[i][0]<=HA_ik[l][0]+Dimensiones[l][0])or (HA_ik[h][0]<=HA_ik[l][0]<HA_ik[l][0]+Dimensiones[l][0]<=HA_ik[h][0]+Dimensiones[i][0]))):
                                            j=1
                                            break
                                if j==0:
                                    HA_ik[i][0]=HA_ik[h][0]
                                    HA_ik[i][1]=HA_ik[h][1]-Dimensiones[i][1]
                                    HA_ik[i][2]=HA_ik[h][2]
                                    j=2
                                    break
                                
    if j!=2:
        for h in range(Productos):#colocar atras de otro cliente
            if h!=i:
                    for k in range(Productos):
                        j=0
                        if (h!=k and i!=k):
                            if HA_ik[h][0]==HA_ik[k][0]+Dimensiones[k][0]:
                                j=adyacente2(HA_ik,h,k,2,1,0,Dimensiones)
                                if j==1:
                                    break
                    if j==0:
                        if HA_ik[h][2]==0:
                            if ((HA_ik[h][0]-Dimensiones[i][0]>=0)and(HA_ik[h][1]+Dimensiones[i][1]<=MX[1])):
                                for l in range(Productos):
                                    if (l!=h and l!=i):
                                        if (((HA_ik[l][0]<=HA_ik[h][0]-Dimensiones[i][0]<HA_ik[l][0]+Dimensiones[l][0])or(HA_ik[l][0]<HA_ik[h][0]<=HA_ik[l][0]+Dimensiones[l][0])or (HA_ik[l][0]<=HA_ik[h][0]-Dimensiones[i][0]<HA_ik[h][0]<=HA_ik[l][0]+Dimensiones[l][0])or (HA_ik[h][0]-Dimensiones[i][0]<=HA_ik[l][0]<HA_ik[l][0]+Dimensiones[l][0]<=HA_ik[h][0]))
                                        and ((HA_ik[l][2]<=HA_ik[h][2]<HA_ik[l][2]+Dimensiones[l][2])or (HA_ik[l][2]<HA_ik[h][2]+Dimensiones[i][2]<=HA_ik[l][2]+Dimensiones[l][2])or (HA_ik[l][2]<=HA_ik[h][2]<HA_ik[h][2]+Dimensiones[i][2]<=HA_ik[l][2]+Dimensiones[l][2])or (HA_ik[h][2]<=HA_ik[l][2]<HA_ik[l][2]+Dimensiones[l][2]<=HA_ik[h][2]+Dimensiones[i][2]))
                                        and ((HA_ik[l][1]<=HA_ik[h][1]<HA_ik[l][1]+Dimensiones[l][1])or (HA_ik[l][1]<HA_ik[h][1]+Dimensiones[i][1]<=HA_ik[l][1]+Dimensiones[l][1])or (HA_ik[l][1]<=HA_ik[h][1]<HA_ik[h][1]+Dimensiones[i][1]<=HA_ik[l][1]+Dimensiones[l][1])or (HA_ik[h][1]<=HA_ik[l][1]<HA_ik[l][1]+Dimensiones[l][1]<=HA_ik[h][1]+Dimensiones[i][1]))):
                                            j=1
                                            break
                                if j==0:
                                    HA_ik[i][0]=HA_ik[h][0]-Dimensiones[i][0]
                                    HA_ik[i][1]=HA_ik[h][1]
                                    HA_ik[i][2]=HA_ik[h][2]
                                    j=2
                                    break



    if j!=2:
        for h in range(Productos):#colocar delante de otro cliente
            if h!=i:
                if Dimensiones[i][3]==Dimensiones[h][3]:
                    for k in range(Productos):
                        j=0
                        if (h!=k and i!=k):
                            if HA_ik[h][0]+Dimensiones[h][0]==HA_ik[k][0]:
                                j=adyacente2(HA_ik,h,k,2,1,0,Dimensiones)
                                if j==1:
                                    break
                    if j==0:
                        if HA_ik[h][2]==0:
                            if ((HA_ik[h][0]+Dimensiones[h][0]+Dimensiones[i][0]<=MX[0])and(HA_ik[h][1]+Dimensiones[i][1]<=MX[1])):
                                for l in range(Productos):
                                    if (l!=h and l!=i):
                                        if (((HA_ik[l][0]<=HA_ik[h][0]+Dimensiones[h][0]<HA_ik[l][0]+Dimensiones[l][0])or(HA_ik[l][0]<HA_ik[h][0]+Dimensiones[h][0]+Dimensiones[i][0]<=HA_ik[l][0]+Dimensiones[l][0])or (HA_ik[l][0]<=HA_ik[h][0]+Dimensiones[h][0]<HA_ik[h][0]+Dimensiones[h][0]+Dimensiones[i][0]<=HA_ik[l][0]+Dimensiones[l][0])or (HA_ik[h][0]+Dimensiones[h][0]<=HA_ik[l][0]<HA_ik[l][0]+Dimensiones[l][0]<=HA_ik[h][0]+Dimensiones[h][0]+Dimensiones[i][0]))
                                        and ((HA_ik[l][2]<=HA_ik[h][2]<HA_ik[l][2]+Dimensiones[l][2])or (HA_ik[l][2]<HA_ik[h][2]+Dimensiones[i][2]<=HA_ik[l][2]+Dimensiones[l][2])or (HA_ik[l][2]<=HA_ik[h][2]<HA_ik[h][2]+Dimensiones[i][2]<=HA_ik[l][2]+Dimensiones[l][2])or (HA_ik[h][2]<=HA_ik[l][2]<HA_ik[l][2]+Dimensiones[l][2]<=HA_ik[h][2]+Dimensiones[i][2]))
                                        and ((HA_ik[l][1]<=HA_ik[h][1]<HA_ik[l][1]+Dimensiones[l][1])or (HA_ik[l][1]<HA_ik[h][1]+Dimensiones[i][1]<=HA_ik[l][1]+Dimensiones[l][1])or (HA_ik[l][1]<=HA_ik[h][1]<HA_ik[h][1]+Dimensiones[i][1]<=HA_ik[l][1]+Dimensiones[l][1])or (HA_ik[h][1]<=HA_ik[l][1]<HA_ik[l][1]+Dimensiones[l][1]<=HA_ik[h][1]+Dimensiones[i][1]))):
                                            j=1
                                            break
                                if j==0:
                                    HA_ik[i][0]=HA_ik[h][0]+Dimensiones[h][0]
                                    HA_ik[i][1]=HA_ik[h][1]
                                    HA_ik[i][2]=HA_ik[h][2]
                                    j=2
                                    break

    
    
    if j!=2: #hacer que i quede en cualquier parte donde haya espacio
        HA_ik[i][0]=random.randrange(MX[0]-Dimensiones[i][0]) 
        HA_ik[i][1]=random.randrange(MX[1]-Dimensiones[i][1]) 
        HA_ik[i][2]=random.randrange(MX[2]-Dimensiones[i][2])
        
    return HA_ik


    
def Proximidad(HA_ik,i,v,Dimensiones):#asegura que las cajas tengan al menos un adyacente del mismo cliente
    v=0
        
    for u in range(Productos):
        if u!=i:
            if HA_ik[i][2]+Dimensiones[i][2]==HA_ik[u][2]:#revisa si hay adyacente en capa superior(1/6)
                r=0
                q=1
                v=adyacente(HA_ik,i,u,r,q,v,Dimensiones)
                    
            elif (HA_ik[i][2]==HA_ik[u][2]+Dimensiones[u][2]):#revisa si hay adyacente en capa inferior(2/6)
                r=0
                q=1
                v=adyacente(HA_ik,i,u,r,q,v,Dimensiones)
                    
            elif (HA_ik[i][0]==HA_ik[u][0]+Dimensiones[u][0]):#revisa si hay adyacente en capa trasera(3/6)
                r=2
                q=1
                v=adyacente(HA_ik,i,u,r,q,v,Dimensiones)
                    
            elif (HA_ik[i][0]+Dimensiones[i][0]==HA_ik[u][0]):#revisa si hay adyacente en capa delantera(4/6)
                r=2
                q=1
                v=adyacente(HA_ik,i,u,r,q,v,Dimensiones)
                    
            elif (HA_ik[i][1]==HA_ik[u][1]+Dimensiones[u][1]):#revisa si hay adyacente en capa izquierda(5/6)
                r=2
                q=0
                v=adyacente(HA_ik,i,u,r,q,v,Dimensiones)
                    
            elif (HA_ik[i][1]+Dimensiones[i][1]==HA_ik[u][1]):#revisa si hay adyacente en capa derecha(6/6)
                r=2
                q=0
                v=adyacente(HA_ik,i,u,r,q,v,Dimensiones)
            if v==1:
                break
            
    for k in range (Clientes):
        if Dimensiones[i][3]==cc[k]:
            v=1     

    if v==0:
        movf(HA_ik,Dimensiones,i)
        #se mueve la caja ya que no tiene ningun adyacente del mismo cliente
                    
    return HA_ik




g=0

def fragilidad(HA_ik,i,Dimensiones): #i esta arriba, y reviso los de abajo
    base=0
    g=0
    if HA_ik[i][2]==0:
        g=1

    for u in range(Productos):
        if u!=i:
            if (HA_ik[u][2]+Dimensiones[u][2]==HA_ik[i][2]):
                if ((HA_ik[i][0]>=HA_ik[u][0] and HA_ik[i][0]<=HA_ik[u][0]+Dimensiones[u][0] and HA_ik[i][1]>=HA_ik[u][1] and HA_ik[i][1]<=HA_ik[u][1]+Dimensiones[u][1])
                and (HA_ik[i][0]+Dimensiones[i][0]>=HA_ik[u][0] and HA_ik[i][0]+Dimensiones[i][0]<=HA_ik[u][0]+Dimensiones[u][0] and HA_ik[i][1]+Dimensiones[i][1]>=HA_ik[u][1] and HA_ik[i][1]+Dimensiones[i][1]<=HA_ik[u][1]+Dimensiones[u][1])
                and (HA_ik[i][0]>=HA_ik[u][0] and HA_ik[i][0]<=HA_ik[u][0]+Dimensiones[u][0] and HA_ik[i][1]+Dimensiones[i][1]>=HA_ik[u][1] and HA_ik[i][1]+Dimensiones[i][1]<=HA_ik[u][1]+Dimensiones[u][1])
                and (HA_ik[i][0]+Dimensiones[i][0]>=HA_ik[u][0] and HA_ik[i][0]+Dimensiones[i][0]<=HA_ik[u][0]+Dimensiones[u][0] and HA_ik[i][1]>=HA_ik[u][1] and HA_ik[i][1]<=HA_ik[u][1]+Dimensiones[u][1])): #las 4 puntas de la caja de arriba dentro de la caja de abajo
                    base=1
                    g=2
                    if Dimensiones[u][4]<Dimensiones[i][4]:
                        movf(HA_ik,Dimensiones,i)
                        g=1
                    
                elif ((HA_ik[u][0]>=HA_ik[i][0] and HA_ik[u][0]<=HA_ik[i][0]+Dimensiones[i][0] and HA_ik[u][1]>=HA_ik[i][1] and HA_ik[u][1]<=HA_ik[i][1]+Dimensiones[i][1])
                and (HA_ik[u][0]+Dimensiones[u][0]>=HA_ik[i][0] and HA_ik[u][0]+Dimensiones[u][0]<=HA_ik[i][0]+Dimensiones[i][0] and HA_ik[u][1]+Dimensiones[u][1]>=HA_ik[i][1] and HA_ik[u][1]+Dimensiones[u][1]<=HA_ik[i][1]+Dimensiones[i][1])
                and (HA_ik[u][0]>=HA_ik[i][0] and HA_ik[u][0]<=HA_ik[i][0]+Dimensiones[i][0] and HA_ik[u][1]+Dimensiones[u][1]>=HA_ik[i][1] and HA_ik[u][1]+Dimensiones[u][1]<=HA_ik[i][1]+Dimensiones[i][1])
                and (HA_ik[u][0]+Dimensiones[u][0]>=HA_ik[i][0] and HA_ik[u][0]+Dimensiones[u][0]<=HA_ik[i][0]+Dimensiones[i][0] and HA_ik[u][1]>=HA_ik[i][1] and HA_ik[u][1]<=HA_ik[i][1]+Dimensiones[i][1])): #las 4 puntas abajo de la caja de arriba
                    area1=Dimensiones[i][0]*Dimensiones[i][1]#area caja de arriba
                    area3= Dimensiones[u][0]*Dimensiones[u][1]#area caja de abajo
                    base=base+(area3/area1)#minimo apoyo que necesitan todas las cajas
                    g=2
                    if Dimensiones[u][4]<Dimensiones[i][4]:
                        movf(HA_ik,Dimensiones,i)
                        g=1
                            
                elif ((HA_ik[u][0]>=HA_ik[i][0] and HA_ik[u][0]<=HA_ik[i][0]+Dimensiones[i][0] and HA_ik[u][1]>=HA_ik[i][1] and HA_ik[u][1]<=HA_ik[i][1]+Dimensiones[i][1])
                and (HA_ik[u][1]+Dimensiones[u][1]>=HA_ik[i][1] and HA_ik[u][1]+Dimensiones[u][1]<=HA_ik[i][1]+Dimensiones[i][1])): #1/4 2 puntas de atras bajo la caja de arriba
                    area1=Dimensiones[i][0]*Dimensiones[i][1]#area caja de arriba
                    area2=Dimensiones[u][1]*(HA_ik[i][0]+Dimensiones[i][0]-HA_ik[u][0])#área en contacto
                    area3= Dimensiones[u][0]*Dimensiones[u][1]#area caja de abajo
                    base=base+(area2/area1)#minimo apoyo que necesitan todas las cajas
                    g=2
                    if Dimensiones[u][4]<Dimensiones[i][4]:
                        if (area2/area3)>sp:
                            movf(HA_ik,Dimensiones,i)
                            g=1
                            
                elif ((HA_ik[u][0]>=HA_ik[i][0] and HA_ik[u][0]<=HA_ik[i][0]+Dimensiones[i][0] and HA_ik[u][1]>=HA_ik[i][1] and HA_ik[u][1]<=HA_ik[i][1]+Dimensiones[i][1])
                and (HA_ik[u][0]+Dimensiones[u][0]>=HA_ik[i][0] and HA_ik[u][0]+Dimensiones[u][0]<=HA_ik[i][0]+Dimensiones[i][0])): #2/4 2puntas de la izquierda bajo la caja de arriba
                    area1=Dimensiones[i][0]*Dimensiones[i][1]
                    area2=Dimensiones[u][0]*(HA_ik[i][1]+Dimensiones[i][1]-HA_ik[u][1])
                    area3= Dimensiones[u][0]*Dimensiones[u][1]#area caja de abajo
                    base=base+(area2/area1)#minimo apoyo que necesitan todas las cajas
                    g=2
                    if Dimensiones[u][4]<Dimensiones[i][4]:
                        if (area2/area3)>sp:
                            movf(HA_ik,Dimensiones,i)
                            g=1
                          
                elif ((HA_ik[u][0]+Dimensiones[u][0]>=HA_ik[i][0] and HA_ik[u][0]+Dimensiones[u][0]<=HA_ik[i][0]+Dimensiones[i][0] and HA_ik[u][1]+Dimensiones[u][1]>=HA_ik[i][1] and HA_ik[u][1]+Dimensiones[u][1]<=HA_ik[i][1]+Dimensiones[i][1])
                and (HA_ik[u][0]>=HA_ik[i][0] and HA_ik[u][0]<=HA_ik[i][0]+Dimensiones[i][0])): #3/4 2puntas de la derecha bajo la caja de arriba
                    area1=Dimensiones[i][0]*Dimensiones[i][1]
                    area2=Dimensiones[u][0]*(HA_ik[u][1]+Dimensiones[u][1]-HA_ik[i][1])
                    area3= Dimensiones[u][0]*Dimensiones[u][1]#area caja de abajo
                    base=base+(area2/area1)#minimo apoyo que necesitan todas las cajas
                    g=2
                    if Dimensiones[u][4]<Dimensiones[i][4]:
                        if (area2/area3)>sp:
                            movf(HA_ik,Dimensiones,i)
                            g=1
                            
                elif ((HA_ik[u][0]+Dimensiones[u][0]>=HA_ik[i][0] and HA_ik[u][0]+Dimensiones[u][0]<=HA_ik[i][0]+Dimensiones[i][0] and HA_ik[u][1]+Dimensiones[u][1]>=HA_ik[i][1] and HA_ik[u][1]+Dimensiones[u][1]<=HA_ik[i][1]+Dimensiones[i][1])
                and (HA_ik[u][1]>=HA_ik[i][1] and HA_ik[u][1]<=HA_ik[i][1]+Dimensiones[i][1])): #4/4 2 puntas de adelante bajo la caja de arriba
                    area1=Dimensiones[i][0]*Dimensiones[i][1]
                    area2=Dimensiones[u][1]*(HA_ik[u][0]+Dimensiones[u][0]-HA_ik[i][0])
                    area3= Dimensiones[u][0]*Dimensiones[u][1]#area caja de abajo
                    base=base+(area2/area1)#minimo apoyo que necesitan todas las cajas
                    g=2
                    if Dimensiones[u][4]<Dimensiones[i][4]:
                        if (area2/area3)>sp:
                            movf(HA_ik,Dimensiones,i)
                            g=1
                            
                elif (HA_ik[u][0]>=HA_ik[i][0] and HA_ik[u][0]<=HA_ik[i][0]+Dimensiones[i][0] and HA_ik[u][1]>=HA_ik[i][1] and HA_ik[u][1]<=HA_ik[i][1]+Dimensiones[i][1]):#1/4 una punta dentro, atras e izquierda
                    area1=Dimensiones[i][0]*Dimensiones[i][1]
                    area2=(HA_ik[i][0]+Dimensiones[i][0]-HA_ik[u][0])*(HA_ik[i][1]+Dimensiones[i][1]-HA_ik[u][1])
                    area3= Dimensiones[u][0]*Dimensiones[u][1]#area caja de abajo
                    base=base+(area2/area1)#minimo apoyo que necesitan todas las cajas
                    g=2
                    if Dimensiones[u][4]<Dimensiones[i][4]:
                        if (area2/area3)>sp:
                            movf(HA_ik,Dimensiones,i)
                            g=1
                    
                elif (HA_ik[u][0]+Dimensiones[u][0]>=HA_ik[i][0] and HA_ik[u][0]+Dimensiones[u][0]<=HA_ik[i][0]+Dimensiones[i][0] and HA_ik[u][1]+Dimensiones[u][1]>=HA_ik[i][1] and HA_ik[u][1]+Dimensiones[u][1]<=HA_ik[i][1]+Dimensiones[i][1]):#2/4 una punta dentro, adelante y derecha
                    area1=Dimensiones[i][0]*Dimensiones[i][1]
                    area2=(HA_ik[u][0]+Dimensiones[u][0]-HA_ik[i][0])*(HA_ik[u][1]+Dimensiones[u][1]-HA_ik[i][1])
                    area3= Dimensiones[u][0]*Dimensiones[u][1]#area caja de abajo
                    base=base+(area2/area1)#minimo apoyo que necesitan todas las cajas
                    g=2
                    if Dimensiones[u][4]<Dimensiones[i][4]:
                        if (area2/area3)>sp:
                            movf(HA_ik,Dimensiones,i)
                            g=1
                            
                elif (HA_ik[u][0]>=HA_ik[i][0] and HA_ik[u][0]<=HA_ik[i][0]+Dimensiones[i][0] and HA_ik[u][1]+Dimensiones[u][1]>=HA_ik[i][1] and HA_ik[u][1]+Dimensiones[u][1]<=HA_ik[i][1]+Dimensiones[i][1]):#3/4 una punta dentro, atras y derecha
                    area1=Dimensiones[i][0]*Dimensiones[i][1]
                    area2=(HA_ik[i][0]+Dimensiones[i][0]-HA_ik[u][0])*(HA_ik[u][1]+Dimensiones[u][1]-HA_ik[i][1])
                    area3= Dimensiones[u][0]*Dimensiones[u][1]#area caja de abajo
                    base=base+(area2/area1)#minimo apoyo que necesitan todas las cajas
                    g=2
                    if Dimensiones[u][4]<Dimensiones[i][4]:
                        if (area2/area3)>sp:
                            movf(HA_ik,Dimensiones,i)
                            g=1
                            
                elif (HA_ik[u][0]+Dimensiones[u][0]>=HA_ik[i][0] and HA_ik[u][0]+Dimensiones[u][0]<=HA_ik[i][0]+Dimensiones[i][0] and HA_ik[u][1]>=HA_ik[i][1] and HA_ik[u][1]<=HA_ik[i][1]+Dimensiones[i][1]): #4/4 una punta dentro, delante e izquierda
                    area1=Dimensiones[i][0]*Dimensiones[i][1]
                    area2=(HA_ik[u][0]+Dimensiones[u][0]-HA_ik[i][0])*(HA_ik[i][1]+Dimensiones[i][1]-HA_ik[u][1])
                    area3= Dimensiones[u][0]*Dimensiones[u][1]#area caja de abajo
                    base=base+(area2/area1)#minimo apoyo que necesitan todas las cajas
                    g=2
                    if Dimensiones[u][4]<Dimensiones[i][4]:
                        if (area2/area3)>sp:
                            movf(HA_ik,Dimensiones,i)
                            g=1
                    
                    
                    #6 CASOS NUEVOS, CUANDO LA CAJA DE ARRIBA SOBRESALE
                  
                    
                elif ((HA_ik[i][0]>=HA_ik[u][0] and HA_ik[i][0]<=HA_ik[u][0]+Dimensiones[u][0] and HA_ik[i][1]>=HA_ik[u][1] and HA_ik[i][1]<=HA_ik[u][1]+Dimensiones[u][1])
                and (HA_ik[i][0]+Dimensiones[i][0]>=HA_ik[u][0] and HA_ik[i][0]+Dimensiones[i][0]>=HA_ik[u][0]+Dimensiones[u][0] and HA_ik[i][1]+Dimensiones[i][1]>=HA_ik[u][1] and HA_ik[i][1]+Dimensiones[i][1]<=HA_ik[u][1]+Dimensiones[u][1])):#1/4, 2 de atras de i encima
                    area1=Dimensiones[i][0]*Dimensiones[i][1]#area caja de arriba
                    area2=Dimensiones[i][1]*(HA_ik[u][0]+Dimensiones[u][0]-HA_ik[i][0])#área en contacto
                    area3= Dimensiones[u][0]*Dimensiones[u][1]#area caja de abajo
                    base=base+(area2/area1)#minimo apoyo que necesitan todas las cajas
                    g=2
                    if Dimensiones[u][4]<Dimensiones[i][4]:
                        if (area2/area3)>sp:
                            movf(HA_ik,Dimensiones,i)
                            g=1
                                
                elif ((HA_ik[i][0]>=HA_ik[u][0] and HA_ik[i][0]<=HA_ik[u][0]+Dimensiones[u][0] and HA_ik[i][1]>=HA_ik[u][1] and HA_ik[i][1]<=HA_ik[u][1]+Dimensiones[u][1])
                and (HA_ik[i][0]+Dimensiones[i][0]>=HA_ik[u][0] and HA_ik[i][0]+Dimensiones[i][0]<=HA_ik[u][0]+Dimensiones[u][0] and HA_ik[i][1]+Dimensiones[i][1]>=HA_ik[u][1] and HA_ik[i][1]+Dimensiones[i][1]>=HA_ik[u][1]+Dimensiones[u][1])):#2/4. 2 de la izquierda
                    area1=Dimensiones[i][0]*Dimensiones[i][1]#area caja de arriba
                    area2=Dimensiones[i][0]*(HA_ik[u][1]+Dimensiones[u][1]-HA_ik[i][1])#área en contacto
                    area3= Dimensiones[u][0]*Dimensiones[u][1]#area caja de abajo
                    base=base+(area2/area1)#minimo apoyo que necesitan todas las cajas
                    g=2
                    if Dimensiones[u][4]<Dimensiones[i][4]:
                        if (area2/area3)>sp:
                            movf(HA_ik,Dimensiones,i)
                            g=1

                elif ((HA_ik[i][0]>=HA_ik[u][0] and HA_ik[i][0]<=HA_ik[u][0]+Dimensiones[u][0] and HA_ik[i][1]+Dimensiones[i][1]>=HA_ik[u][1] and HA_ik[i][1]+Dimensiones[i][1]<=HA_ik[u][1]+Dimensiones[u][1])
                and (HA_ik[i][0]+Dimensiones[i][0]>=HA_ik[u][0] and HA_ik[i][0]+Dimensiones[i][0]<=HA_ik[u][0]+Dimensiones[u][0] and HA_ik[i][1]<=HA_ik[u][1] and HA_ik[i][1]<=HA_ik[u][1]+Dimensiones[u][1])): #3/4, 2 de la derecha
                    area1=Dimensiones[i][0]*Dimensiones[i][1]#area caja de arriba
                    area2=Dimensiones[i][0]*(HA_ik[i][1]+Dimensiones[i][1]-HA_ik[u][1])#área en contacto
                    area3= Dimensiones[u][0]*Dimensiones[u][1]#area caja de abajo
                    base=base+(area2/area1)#minimo apoyo que necesitan todas las cajas
                    g=2
                    if Dimensiones[u][4]<Dimensiones[i][4]:
                        if (area2/area3)>sp:
                            movf(HA_ik,Dimensiones,i)
                            g=1

                elif ((HA_ik[i][0]+Dimensiones[i][0]>=HA_ik[u][0] and HA_ik[i][0]+Dimensiones[i][0]>=HA_ik[u][0]+Dimensiones[u][0] and HA_ik[i][1]>=HA_ik[u][1] and HA_ik[i][1]<=HA_ik[u][1]+Dimensiones[u][1])
                and (HA_ik[i][0]>=HA_ik[u][0] and HA_ik[i][0]<=HA_ik[u][0]+Dimensiones[u][0] and HA_ik[i][1]+Dimensiones[i][1]>=HA_ik[u][1] and HA_ik[i][1]+Dimensiones[i][1]<=HA_ik[u][1]+Dimensiones[u][1])):#4/4, 2 de adelante
                    area1=Dimensiones[i][0]*Dimensiones[i][1]#area caja de arriba
                    area2=Dimensiones[i][1]*(HA_ik[u][0]+Dimensiones[u][0]-HA_ik[i][0])#área en contacto
                    area3= Dimensiones[u][0]*Dimensiones[u][1]#area caja de abajo
                    base=base+(area2/area1)#minimo apoyo que necesitan todas las cajas
                    g=2
                    if Dimensiones[u][4]<Dimensiones[i][4]:
                        if (area2/area3)>sp:
                            movf(HA_ik,Dimensiones,i)
                            g=1
                                
                elif ((HA_ik[i][0]<=HA_ik[u][0] and HA_ik[i][0]<=HA_ik[u][0]+Dimensiones[u][0] and HA_ik[i][1]>=HA_ik[u][1] and HA_ik[i][1]<=HA_ik[u][1]+Dimensiones[u][1])
                and (HA_ik[i][0]+Dimensiones[i][0]>=HA_ik[u][0] and HA_ik[i][0]+Dimensiones[i][0]>=HA_ik[u][0]+Dimensiones[u][0] and HA_ik[i][1]+Dimensiones[i][1]>=HA_ik[u][1] and HA_ik[i][1]+Dimensiones[i][1]<=HA_ik[u][1]+Dimensiones[u][1])):#la de arriba en x, el de abajo en y
                    area1=Dimensiones[i][0]*Dimensiones[i][1]#area caja de arriba
                    area2=Dimensiones[i][1]*Dimensiones[u][0]#área en contacto
                    area3= Dimensiones[u][0]*Dimensiones[u][1]#area caja de abajo
                    base=base+(area2/area1)#minimo apoyo que necesitan todas las cajas
                    g=2
                    if Dimensiones[u][4]<Dimensiones[i][4]:
                        if (area2/area3)>sp:
                            movf(HA_ik,Dimensiones,i)
                            g=1
                                
    
                elif ((HA_ik[i][0]>=HA_ik[u][0] and HA_ik[i][0]<=HA_ik[u][0]+Dimensiones[u][0] and HA_ik[i][1]<=HA_ik[u][1] and HA_ik[i][1]<=HA_ik[u][1]+Dimensiones[u][1])
                and (HA_ik[i][0]+Dimensiones[i][0]>=HA_ik[u][0] and HA_ik[i][0]+Dimensiones[i][0]<=HA_ik[u][0]+Dimensiones[u][0] and HA_ik[i][1]+Dimensiones[i][1]>=HA_ik[u][1] and HA_ik[i][1]+Dimensiones[i][1]>=HA_ik[u][1]+Dimensiones[u][1])):#el de arriba en y , el de abajo en x
                    area1=Dimensiones[i][0]*Dimensiones[i][1]#area caja de arriba
                    area2=Dimensiones[i][0]*Dimensiones[i][1]#área en contacto
                    area3= Dimensiones[u][0]*Dimensiones[u][1]#area caja de abajo
                    base=base+(area2/area1)#minimo apoyo que necesitan todas las cajas
                    g=2
                    if Dimensiones[u][4]<Dimensiones[i][4]:
                        if (area2/area3)>sp:
                            movf(HA_ik,Dimensiones,i)
                            g=1
                if g==1:
                    break

    if (g==2 or g==0):
        if base<sa:#mover i, ya que no esta en equilibrio
            movf(HA_ik,Dimensiones,i)

    return HA_ik




def Overlap(HA_ik,k,i):

    """Se cambia la posicion de las cajas si estan total o parcialmente dentro de otro"""    
    
    for t in range(3):

        if k != t:

            for r in range(3):#revisar todas las cajas comparadas a todas las cajas en todas las posiciones

                if r != t and r != k:

                    for u in range(Productos):

                        if u!=i:

                            while True:

                                if (HA_ik[i][k]<=HA_ik[u][k]<HA_ik[u][k]+Dimensiones[u][k]<HA_ik[i][k]+Dimensiones[i][k] 

                                and HA_ik[u][t]<HA_ik[i][t]<HA_ik[i][t]+Dimensiones[i][t]<HA_ik[u][t]+Dimensiones[u][t] 

                                and HA_ik[u][r]<HA_ik[i][r]<HA_ik[u][r]+Dimensiones[u][r]<HA_ik[i][r]+Dimensiones[i][r]):#dos lineas (1/2)

                                    MoverCaja2(HA_ik,k,i,r,t,u)


                                elif (HA_ik[i][k]<=HA_ik[u][k]<HA_ik[u][k]+Dimensiones[u][k]<HA_ik[i][k]+Dimensiones[i][k] 

                                and HA_ik[u][r]<HA_ik[i][r]<HA_ik[i][r]+Dimensiones[i][r]<HA_ik[u][r]+Dimensiones[u][r]

                                and HA_ik[i][t]<HA_ik[u][t]<HA_ik[i][t]+Dimensiones[i][t]<HA_ik[u][t]+Dimensiones[u][t]):#dos lineas (2/2)

                                    MoverCaja2(HA_ik,k,i,r,t,u)
                                    
                                    
                                elif (HA_ik[i][k]<=HA_ik[u][k] and HA_ik[u][t]<=HA_ik[i][t] and HA_ik[i][r]<=HA_ik[u][r] 
                                
                                and HA_ik[i][t]+Dimensiones[i][t]<=HA_ik[u][t]+Dimensiones[u][t] 
                                
                                and HA_ik[u][r]+Dimensiones[u][r]<=HA_ik[i][r]+Dimensiones[i][r] 
                                
                                and HA_ik[u][k]<HA_ik[i][k]+Dimensiones[i][k]<=HA_ik[u][k]+Dimensiones[u][k]):#4 lineas
                                
                                    MoverCaja2(HA_ik,k,i,r,t,u)



                                elif (HA_ik[u][k]<=HA_ik[i][k]<HA_ik[i][k]+Dimensiones[i][k]<=HA_ik[u][k]+Dimensiones[u][k] 

                                and HA_ik[u][r]<=HA_ik[i][r]<HA_ik[i][r]+Dimensiones[i][r]<=HA_ik[u][r]+Dimensiones[u][r] 

                                and HA_ik[u][t]<=HA_ik[i][t]<HA_ik[i][t]+Dimensiones[i][t]<=HA_ik[u][t]+Dimensiones[u][t]):#8 puntas dentro

                                    MoverCaja2(HA_ik,k,i,r,t,u)


                                elif (HA_ik[u][k]<=HA_ik[i][k]<HA_ik[u][k]+Dimensiones[u][k]<HA_ik[i][k]+Dimensiones[i][k] 

                                and HA_ik[u][t]<=HA_ik[i][t]<HA_ik[i][t]+Dimensiones[i][t]<=HA_ik[u][t]+Dimensiones[u][t] 

                                and HA_ik[u][r]<=HA_ik[i][r]<HA_ik[i][r]+Dimensiones[i][r]<=HA_ik[u][r]+Dimensiones[u][r]):#4 puntas dentro(1/6)

                                    MoverCaja2(HA_ik,k,i,r,t,u)


                                elif (HA_ik[i][k]<HA_ik[u][k]<HA_ik[i][k]+Dimensiones[i][k]<=HA_ik[u][k]+Dimensiones[u][k] 

                                and HA_ik[u][t]<=HA_ik[i][t]<HA_ik[i][t]+Dimensiones[i][t]<=HA_ik[u][t]+Dimensiones[u][t] 

                                and HA_ik[u][r]<=HA_ik[i][r]<HA_ik[i][r]+Dimensiones[i][r]<=HA_ik[u][r]+Dimensiones[u][r]):#4 puntas dentro(2/6)

                                    MoverCaja2(HA_ik,k,i,r,t,u)


                                elif (HA_ik[u][k]<=HA_ik[i][k]<HA_ik[i][k]+Dimensiones[i][k]<=HA_ik[u][k]+Dimensiones[u][k] 

                                and HA_ik[u][t]<=HA_ik[i][t]<HA_ik[u][t]+Dimensiones[u][t]<HA_ik[i][t]+Dimensiones[i][t] 

                                and HA_ik[u][r]<=HA_ik[i][r]<HA_ik[i][r]+Dimensiones[i][r]<=HA_ik[u][r]+Dimensiones[u][r]):#4 puntas dentro(3/6)

                                    MoverCaja2(HA_ik,k,i,r,t,u)


                                elif (HA_ik[u][k]<=HA_ik[i][k]<HA_ik[i][k]+Dimensiones[i][k]<=HA_ik[u][k]+Dimensiones[u][k] 

                                and HA_ik[u][t]<=HA_ik[i][t]<HA_ik[i][t]+Dimensiones[i][t]<=HA_ik[u][t]+Dimensiones[u][t] 

                                and HA_ik[i][r]<HA_ik[u][r]<HA_ik[i][r]+Dimensiones[i][r]<=HA_ik[u][r]+Dimensiones[u][r]):#4 puntas dentro(4/6)

                                    MoverCaja2(HA_ik,k,i,r,t,u)


                                elif (HA_ik[u][k]<=HA_ik[i][k]<HA_ik[i][k]+Dimensiones[i][k]<=HA_ik[u][k]+Dimensiones[u][k] 

                                and HA_ik[u][t]<=HA_ik[i][t]<HA_ik[i][t]+Dimensiones[i][t]<=HA_ik[u][t]+Dimensiones[u][t] 

                                and HA_ik[u][r]<=HA_ik[i][r]<HA_ik[u][r]+Dimensiones[u][r]<HA_ik[i][r]+Dimensiones[i][r]):#4 puntas dentro(5/6)

                                    MoverCaja2(HA_ik,k,i,r,t,u)


                                elif (HA_ik[u][k]<=HA_ik[i][k]<HA_ik[i][k]+Dimensiones[i][k]<=HA_ik[u][k]+Dimensiones[u][k] 

                                and HA_ik[i][t]<HA_ik[u][t]<HA_ik[i][t]+Dimensiones[i][t]<=HA_ik[u][t]+Dimensiones[u][t] 

                                and HA_ik[u][r]<=HA_ik[i][r]<HA_ik[i][r]+Dimensiones[i][r]<=HA_ik[u][r]+Dimensiones[u][r]):#4 puntas dentro(6/6)

                                    MoverCaja2(HA_ik,k,i,r,t,u)


                                elif (HA_ik[u][k]<=HA_ik[i][k]<HA_ik[i][k]+Dimensiones[i][k]<=HA_ik[u][k]+Dimensiones[u][k] 

                                and HA_ik[u][t]<=HA_ik[i][t]<HA_ik[u][t]+Dimensiones[u][t]<HA_ik[i][t]+Dimensiones[i][t] 

                                and HA_ik[u][r]<=HA_ik[i][r]<HA_ik[u][r]+Dimensiones[u][r]<HA_ik[i][r]+Dimensiones[i][r]):#2 puntas 1/12

                                    MoverCaja2(HA_ik,k,i,r,t,u)


                                elif (HA_ik[u][k]<=HA_ik[i][k]<HA_ik[u][k]+Dimensiones[u][k]<HA_ik[i][k]+Dimensiones[i][k] 

                                and HA_ik[u][t]<HA_ik[i][t]<HA_ik[u][t]+Dimensiones[u][t]<=HA_ik[i][t]+Dimensiones[i][t] 

                                and HA_ik[u][r]<=HA_ik[i][r]<HA_ik[i][r]+Dimensiones[i][r]<=HA_ik[u][r]+Dimensiones[u][r]):#2 puntas 2/12

                                    MoverCaja2(HA_ik,k,i,r,t,u)


                                elif (HA_ik[u][k]<=HA_ik[i][k]<HA_ik[u][k]+Dimensiones[u][k]<HA_ik[i][k]+Dimensiones[i][k] 

                                and HA_ik[u][t]<=HA_ik[i][t]<HA_ik[i][t]+Dimensiones[i][t]<=HA_ik[u][t]+Dimensiones[u][t] 

                                and HA_ik[u][r]<=HA_ik[i][r]<HA_ik[u][r]+Dimensiones[u][r]<HA_ik[i][r]+Dimensiones[i][r]):#2 puntas 3/12

                                    MoverCaja2(HA_ik,k,i,r,t,u)


                                elif (HA_ik[u][k]<=HA_ik[i][k]<HA_ik[i][k]+Dimensiones[i][k]<=HA_ik[u][k]+Dimensiones[u][k] 

                                and HA_ik[u][t]<=HA_ik[i][t]<HA_ik[u][t]+Dimensiones[u][t]<HA_ik[i][t]+Dimensiones[i][t] 

                                and HA_ik[i][r]<HA_ik[u][r]<HA_ik[i][r]+Dimensiones[i][r]<=HA_ik[u][r]+Dimensiones[u][r]):#2 puntas 4/12

                                    MoverCaja2(HA_ik,k,i,r,t,u)


                                elif (HA_ik[i][k]<HA_ik[u][k]<HA_ik[i][k]+Dimensiones[i][k]<=HA_ik[u][k]+Dimensiones[u][k] 

                                and HA_ik[u][t]<HA_ik[i][t]<HA_ik[u][t]+Dimensiones[u][t]<=HA_ik[i][t]+Dimensiones[i][t] 

                                and HA_ik[u][r]<=HA_ik[i][r]<HA_ik[i][r]+Dimensiones[i][r]<=HA_ik[u][r]+Dimensiones[u][r]):#2 puntas 5/12

                                    MoverCaja2(HA_ik,k,i,r,t,u)


                                elif (HA_ik[i][k]<=HA_ik[u][k]<HA_ik[i][k]+Dimensiones[i][k]<HA_ik[u][k]+Dimensiones[u][k] 
                                
                                and HA_ik[u][t]<=HA_ik[i][t]<HA_ik[i][t]+Dimensiones[i][t]<=HA_ik[u][t]+Dimensiones[u][t] 

                                and HA_ik[u][r]<=HA_ik[i][r]<HA_ik[u][r]+Dimensiones[u][r]<HA_ik[i][r]+Dimensiones[i][r]):#2 puntas 6/12 /

                                    MoverCaja2(HA_ik,k,i,r,t,u)


                                elif (HA_ik[u][k]<=HA_ik[i][k]<HA_ik[u][k]+Dimensiones[u][k]<HA_ik[i][k]+Dimensiones[i][k] 

                                and HA_ik[u][t]<=HA_ik[i][t]<HA_ik[i][t]+Dimensiones[i][t]<=HA_ik[u][t]+Dimensiones[u][t] 

                                and HA_ik[i][r]<HA_ik[u][r]<HA_ik[i][r]+Dimensiones[i][r]<=HA_ik[u][r]+Dimensiones[u][r]):#2 puntas 7/12 /

                                    MoverCaja2(HA_ik,k,i,r,t,u)


                                elif(HA_ik[i][k]<HA_ik[u][k]<HA_ik[i][k]+Dimensiones[i][k]<=HA_ik[u][k]+Dimensiones[u][k] 

                                and HA_ik[u][t]<=HA_ik[i][t]<HA_ik[i][t]+Dimensiones[i][t]<=HA_ik[u][t]+Dimensiones[u][t] 

                                and HA_ik[i][r]<HA_ik[u][r]<HA_ik[i][r]+Dimensiones[i][r]<=HA_ik[u][r]+Dimensiones[u][r]):#2 puntas 8/12 /

                                    MoverCaja2(HA_ik,k,i,r,t,u)


                                elif (HA_ik[u][k]<=HA_ik[i][k]<HA_ik[i][k]+Dimensiones[i][k]<=HA_ik[u][k]+Dimensiones[u][k] 
                                
                                and HA_ik[i][t]<HA_ik[u][t]<HA_ik[i][t]+Dimensiones[i][t]<=HA_ik[u][t]+Dimensiones[u][t] 

                                and HA_ik[i][r]<HA_ik[u][r]<HA_ik[i][r]+Dimensiones[i][r]<=HA_ik[u][r]+Dimensiones[u][r]):#2 puntas 9/12 /

                                    MoverCaja2(HA_ik,k,i,r,t,u)

                                elif (HA_ik[u][k]<=HA_ik[i][k]<HA_ik[i][k]+Dimensiones[i][k]<=HA_ik[u][k]+Dimensiones[u][k] 

                                and HA_ik[i][t]<HA_ik[u][t]<HA_ik[i][t]+Dimensiones[i][t]<=HA_ik[u][t]+Dimensiones[u][t] 

                                and HA_ik[u][r]<=HA_ik[i][r]<HA_ik[u][r]+Dimensiones[u][r]<HA_ik[i][r]+Dimensiones[i][r]):#2 puntas 10/12 /

                                    MoverCaja2(HA_ik,k,i,r,t,u)


                                elif (HA_ik[u][k]<=HA_ik[i][k]<HA_ik[u][k]+Dimensiones[u][k]<HA_ik[i][k]+Dimensiones[i][k] 

                                and HA_ik[i][t]<HA_ik[u][t]<HA_ik[i][t]+Dimensiones[i][t]<=HA_ik[u][t]+Dimensiones[u][t] 

                                and HA_ik[u][r]<=HA_ik[i][r]<HA_ik[i][r]+Dimensiones[i][r]<=HA_ik[u][r]+Dimensiones[u][r]):#2 puntas 11/12 /

                                    MoverCaja2(HA_ik,k,i,r,t,u)


                                elif (HA_ik[i][k]<HA_ik[u][k]<HA_ik[i][k]+Dimensiones[i][k]<=HA_ik[u][k]+Dimensiones[u][k] 

                                and HA_ik[i][t]<HA_ik[u][t]<HA_ik[i][t]+Dimensiones[i][t]<=HA_ik[u][t]+Dimensiones[u][t] 

                                and HA_ik[u][r]<=HA_ik[i][r]<HA_ik[i][r]+Dimensiones[i][r]<=HA_ik[u][r]+Dimensiones[u][r]):#2 puntas 12/12 /

                                    MoverCaja2(HA_ik,k,i,r,t,u)


                                elif (HA_ik[u][k]<=HA_ik[i][k]<HA_ik[u][k]+Dimensiones[u][k]<HA_ik[i][k]+Dimensiones[i][k] 

                                and HA_ik[u][r]<=HA_ik[i][r]<HA_ik[u][r]+Dimensiones[u][r]<HA_ik[i][r]+Dimensiones[i][r] 

                                and HA_ik[u][t]<=HA_ik[i][t]<HA_ik[u][t]+Dimensiones[u][t]<HA_ik[i][t]+Dimensiones[i][t]):#1 puntas dentro (1/8)

                                    MoverCaja2(HA_ik,k,i,r,t,u)


                                elif (HA_ik[i][k]<HA_ik[u][k]<HA_ik[i][k]+Dimensiones[i][k]<=HA_ik[u][k]+Dimensiones[u][k] 

                                and HA_ik[u][r]<=HA_ik[i][r]<HA_ik[u][r]+Dimensiones[u][r]<HA_ik[i][r]+Dimensiones[i][r] 

                                and HA_ik[u][t]<=HA_ik[i][t]<HA_ik[u][t]+Dimensiones[u][t]<HA_ik[i][t]+Dimensiones[i][t]):#1 puntas dentro (2/8)

                                    MoverCaja2(HA_ik,k,i,r,t,u)


                                elif (HA_ik[u][k]<=HA_ik[i][k]<HA_ik[u][k]+Dimensiones[u][k]<HA_ik[i][k]+Dimensiones[i][k] 

                                and HA_ik[i][r]<HA_ik[u][r]<HA_ik[i][r]+Dimensiones[i][r]<=HA_ik[u][r]+Dimensiones[u][r] 

                                and HA_ik[u][t]<=HA_ik[i][t]<HA_ik[u][t]+Dimensiones[u][t]<HA_ik[i][t]+Dimensiones[i][t]):#1 puntas dentro (3/8)

                                    MoverCaja2(HA_ik,k,i,r,t,u)


                                elif (HA_ik[u][k]<=HA_ik[i][k]<HA_ik[u][k]+Dimensiones[u][k]<HA_ik[i][k]+Dimensiones[i][k] 

                                and HA_ik[u][r]<=HA_ik[i][r]<HA_ik[u][r]+Dimensiones[u][r]<HA_ik[i][r]+Dimensiones[i][r] 

                                and HA_ik[i][t]<HA_ik[u][t]<HA_ik[i][t]+Dimensiones[i][t]<=HA_ik[u][t]+Dimensiones[u][t]):#1 puntas dentro (4/8)

                                    MoverCaja2(HA_ik,k,i,r,t,u)


                                elif (HA_ik[i][k]<HA_ik[u][k]<HA_ik[i][k]+Dimensiones[i][k]<=HA_ik[u][k]+Dimensiones[u][k] 

                                and HA_ik[i][r]<HA_ik[u][r]<HA_ik[i][r]+Dimensiones[i][r]<=HA_ik[u][r]+Dimensiones[u][r] 

                                and HA_ik[u][t]<=HA_ik[i][t]<HA_ik[u][t]+Dimensiones[u][t]<HA_ik[i][t]+Dimensiones[i][t]):#1 puntas dentro (5/8)

                                    MoverCaja2(HA_ik,k,i,r,t,u)


                                elif (HA_ik[i][k]<HA_ik[u][k]<HA_ik[i][k]+Dimensiones[i][k]<=HA_ik[u][k]+Dimensiones[u][k] 

                                and HA_ik[u][r]<=HA_ik[i][r]<HA_ik[u][r]+Dimensiones[u][r]<HA_ik[i][r]+Dimensiones[i][r] 

                                and HA_ik[i][t]<HA_ik[u][t]<HA_ik[i][t]+Dimensiones[i][t]<=HA_ik[u][t]+Dimensiones[u][t]):#1 puntas dentro (6/8)

                                    MoverCaja2(HA_ik,k,i,r,t,u)


                                elif (HA_ik[u][k]<=HA_ik[i][k]<HA_ik[u][k]+Dimensiones[u][k]<HA_ik[i][k]+Dimensiones[i][k] 

                                and HA_ik[i][r]<HA_ik[u][r]<HA_ik[i][r]+Dimensiones[i][r]<=HA_ik[u][r]+Dimensiones[u][r] 

                                and HA_ik[i][t]<HA_ik[u][t]<HA_ik[i][t]+Dimensiones[i][t]<=HA_ik[u][t]+Dimensiones[u][t]):#1 puntas dentro (7/8)

                                    MoverCaja2(HA_ik,k,i,r,t,u)


                                elif (HA_ik[i][k]<HA_ik[u][k]<HA_ik[i][k]+Dimensiones[i][k]<=HA_ik[u][k]+Dimensiones[u][k] 

                                and HA_ik[i][r]<HA_ik[u][r]<HA_ik[i][r]+Dimensiones[i][r]<=HA_ik[u][r]+Dimensiones[u][r] 
                                
                                and HA_ik[i][t]<HA_ik[u][t]<HA_ik[i][t]+Dimensiones[i][t]<=HA_ik[u][t]+Dimensiones[u][t]):#1 puntas dentro (8/8)

                                    MoverCaja2(HA_ik,k,i,r,t,u)


                                elif (HA_ik[i][k]+Dimensiones[i][k]==HA_ik[u][k]+Dimensiones[u][k] 

                                and HA_ik[i][t]+Dimensiones[i][t]==HA_ik[u][t]+Dimensiones[u][t] 

                                and HA_ik[i][r]+Dimensiones[i][r]==HA_ik[u][r]+Dimensiones[u][r]):#no puede ser igual esquina 
                                                                                                  #delantera superior izquierda
                                    MoverCaja2(HA_ik,k,i,r,t,u)


                                elif (HA_ik[i][k]==HA_ik[u][k] 

                                and HA_ik[i][r]==HA_ik[u][r] 

                                and HA_ik[i][t]==HA_ik[u][t]): #no puede ser igual esquina trasera inferior derecha

                                    MoverCaja2(HA_ik,k,i,r,t,u)


                                else:

                                    break

    return HA_ik


def Gravedad2(HA_ik):
#que las cajas no queden flotando
    
    MA = np.zeros(Productos)

    #productos en cota cero

    for i in range(Productos):

        if HA_ik[i][2] == 0:

            MA[i] = 1

    #productos inmediatamente sobre otros productos que no vuelan

    for i in range(Productos):

        if MA[i] == 0:

            compatibles = []

            for u in range(Productos):

                if i != u and MA[u] == 1:

                    if HA_ik[u][2]+Dimensiones[u][2] == HA_ik[i][2]:#cotas compatibles

                        if( (HA_ik[u][1] <= HA_ik[i][1]<HA_ik[u][1]+Dimensiones[u][1])or(HA_ik[u][1]<HA_ik[i][1]+Dimensiones[i][1]<=HA_ik[u][1]+Dimensiones[u][1])

                        and (HA_ik[u][0] <= HA_ik[i][0]<HA_ik[u][0]+Dimensiones[u][0])or(HA_ik[u][0]<HA_ik[i][0]+Dimensiones[i][0]<=HA_ik[u][0]+Dimensiones[u][0])):

                            MA[i] = 1#la caja i está justo sobre caja u

                            break


                        else:#agrega a lista de compatibles

                            compatibles.append(u)


            if MA[i] == 0 and len(compatibles) != 0:

                for u in compatibles:

                    if ((HA_ik[u][0]+Dimensiones[u][0] > HA_ik[i][0]

                        and HA_ik[u][0] < HA_ik[i][0]+Dimensiones[i][0]

                        and

                        (HA_ik[u][1]+Dimensiones[u][1] > HA_ik[i][1]

                        and HA_ik[u][1] < HA_ik[i][1]+Dimensiones[i][1]))):

                        MA[i] = 1


                        break

                    else:

                        compatibles.remove(u)
    #productos que vuelan

    vuelan = {}#diccionario con producto y altura

    for i in range(Productos):

        if MA[i] == 0:

            vuelan.setdefault(i,HA_ik[i][2])

    for w in sorted(vuelan.items(), key=lambda x:x[1]):

        i = w[0]

        compatibles = []


        for u in range(Productos):

            if i != u and MA[u] == 1:

                if (HA_ik[u][2]+Dimensiones[u][2] < HA_ik[i][2]):#cotas compatibles i está sobre u

                    compatibles.append(u)


        for u in compatibles:

            borrar = []

            if not (HA_ik[u][0]+Dimensiones[u][0] > HA_ik[i][0]

            and HA_ik[u][0] < HA_ik[i][0]+Dimensiones[i][0]

            and HA_ik[u][1]+Dimensiones[u][1] > HA_ik[i][1]

            and HA_ik[u][1] < HA_ik[i][1]+Dimensiones[i][1]):

                borrar.append(u)

            compatibles = list(set(compatibles)-set(borrar))

        #asignar cota al más alto de la proyección XY

        if len(compatibles) != 0:

            cotaMax = -1

            cajaMax = 0

            for u in compatibles:

                if HA_ik[u][2]+Dimensiones[u][2] >= cotaMax:

                    cotaMax = HA_ik[u][2]+Dimensiones[u][2]

                    cajaMax = u

            if cotaMax != -1:

                HA_ik[i][2] = HA_ik[cajaMax][2]+Dimensiones[cajaMax][2]

                MA[i] = 1


        else:

            HA_ik[i][2] = 0

            MA[i] = 1


    return HA_ik





def ORDEN(HA_ik,Dimensiones):#se pasa de la parte trasera
    penalizacion=0
    layer=np.zeros(Clientes)
    layer2=[]
    
    for k in range(Clientes):
        layer[k]=0
        
    for k in range(Clientes):
        for i in range (Productos):
            if Dimensiones[i][3]==k+1:
                layer2.append(HA_ik[i][0]+Dimensiones[i][0])
        layer[k]=max(layer2)
        layer2=[]

    for k in range (Clientes):
        for i in range (Productos):
            o=0
            if Dimensiones[i][3]==k+1:
                if k!=0: 
                    if HA_ik[i][0]<layer[k-1]:
                        o=(layer[k-1]-HA_ik[i][0])/(2*MX[0])#penalizacion distancia entre layer y parte trasra de la caja   
            if o!=0:
                penalizacion=penalizacion+o
        
    return penalizacion



def ORDEN2(HA_ik,Dimensiones):#se pasa de la parte delantera
    penalizacion2=0
    layer=np.zeros(Clientes)
    layer2=[]
    
    for k in range(Clientes):
        layer[k]=0
        
    for k in range(Clientes):
        for i in range (Productos):
            if Dimensiones[i][3]==k+1:
                layer2.append(HA_ik[i][0])
        layer[k]=min(layer2)
        layer2=[]

    for k in range (Clientes):
        for i in range (Productos):
            o=0
            if Dimensiones[i][3]==k+1:
                if k!=Clientes-1: 
                    if HA_ik[i][0]+Dimensiones[i][0]>layer[k+1]:
                        o=(HA_ik[i][0]+Dimensiones[i][0]-layer[k+1])/(2*MX[0])#penalizacion distancia entre layer y parte trasra de la caja   
            if o!=0:
                penalizacion2=penalizacion2+o
        
    return penalizacion2                


def movv(HA_ik,Dimensiones):#mover los ultimos de cada cliente
    for j in range (Clientes):
        xmaxv=0                
        for i in range(Productos):
            if Dimensiones[i][3]==j+1:
                if HA_ik[i][0]+Dimensiones[i][0]>xmaxv:
                    xmaxv=HA_ik[i][0]+Dimensiones[i][0]
        nv=[]
        for i in range(Productos):
            if Dimensiones[i][3]==j+1:
                if HA_ik[i][0]+Dimensiones[i][0]==xmaxv:
                    nv.append(i)
        
        for h in range (len(nv)):
            HA_ik[nv[h]][0]=0
            HA_ik[nv[h]][1]=0
            HA_ik[nv[h]][2]=MX[2]+1
        
        for h in range (len(nv)):
            movf(HA_ik,Dimensiones,nv[h])
                       
    return HA_ik
        



"Nueva FO"

#calcular largo maximo xmax
for i in range (Productos):
    if i==0:
        xmax=HA_ik[i][0]+Dimensiones[i][0]
    if i>0:
        if (HA_ik[i][0]+Dimensiones[i][0])>xmax:
            xmax=HA_ik[i][0]+Dimensiones[i][0]
    

pen1=ORDEN(HA_ik,Dimensiones)
pen2=ORDEN2(HA_ik,Dimensiones)
pen0=pen1+pen2

   
"FO"
Optimo=xmax

    
if iteracion==0:
    MatrizOptima2.append(100000000000000000)
Guarda_todo.append(Optimo)

tiempo_no_optimo.append(int(elapsed_time))
F=0
F=int(min(MatrizOptima2))

if (Optimo<F):
    """Se obtiene el minimo de las pruebas"""
    v0=v0
    pen0=pen0
    MX[0]=Optimo
    niter=0
    tiempo=0
    HA=HA_ik.copy()
    Guarda_Optimo.append(Optimo)
    tiempo_optimo.append(int(elapsed_time))
    print ("HA_ik ", iteracion, "es:", HA_ik[0:Productos], "","El optimo es:", Optimo)
    print("volumen de referencia es: ",v0,"pen atras ",pen1,"pen adelante ",pen2,"pen total ",pen0)

else:
    HA_ik=HA.copy()

if (iteracion==0):
    MatrizOptima2=[]
    
MatrizOptima2.append(Optimo)
Optimo=0 
iteracion=iteracion+1
    




while (True):

    """ Aqui empieza La metaheurística "Harmony Search", con sus 3 casos (encontrar una melodia ya utilizada

    , usar una melodia ya utilizada variando siertas notas y usar una melodia con notas totalmente aleatorias.) """

    Harmonica.append(HA_ik)#se agraga a armonica HA_ik

    rand=random.random()

    
    if rand > r_acept:#elegir una aharmonia existente random

        p=random.randrange(len(Harmonica))#crea un p random que se detiene en la longitud de Harmonica

        HA_ik=Harmonica[p]


    elif rand > r_pa:#ajustar la solucion
        
        d=random.choice([0,1])# elegir si mover cajas o no
        
        
        if (d==1):
            f=random.randrange(Productos)#cantidad de productos que se mueven escogido aleatoriamente

            for q in range(f): #moviendo los productos
                x=random.randrange(Productos)
                movf(HA_ik,Dimensiones,x)
                
    else:
        #si no es mayor a ninguna probabilidad, se elige una melodia con notas aleatorias

        
        for i in range(Productos):      

            HA_ik[i][0]=random.randrange(MX[0]-Dimensiones[i][0])      

            HA_ik[i][1]=random.randrange(MX[1]-Dimensiones[i][1])      

            HA_ik[i][2]=random.randrange(MX[2]-Dimensiones[i][2])


# no entrar aca cuando entra en el primer if
    if rand<=r_acept:
                
        Gravedad2(HA_ik)
                
        for i in range(Productos):
            for k in range(3):
                Overlap(HA_ik,k,i)
                            
        for i in range(Productos):#desde aqui se llama la funcion Proximidad
            Proximidad(HA_ik,i,v,Dimensiones)

        Gravedad2(HA_ik)
            
        for i in range(Productos):
            for k in range(3):
                Overlap(HA_ik,k,i)                        
        
        for i in range(Productos):
            fragilidad(HA_ik,i,Dimensiones)# se llama funcion fragilidad
        
        Gravedad2(HA_ik)
                
        for i in range(Productos):
            for k in range(3):
                Overlap(HA_ik,k,i)
                        


        """Mover hacia atras los más externos, para disminuir largo"""             
        movv(HA_ik,Dimensiones)



        Gravedad2(HA_ik)
                            
        for i in range(Productos):
            for k in range(3):
                Overlap(HA_ik,k,i)
                                
                
        for i in range(Productos):#desde aqui se llama la funcion Proximidad
            Proximidad(HA_ik,i,v,Dimensiones)

        Gravedad2(HA_ik)
            
        for i in range(Productos):
            for k in range(3):
                Overlap(HA_ik,k,i)
        
        for i in range(Productos):
            fragilidad(HA_ik,i,Dimensiones)#revisa si tiene algun adyacente solo en la capa inferior, y si se da y tiene un peso mayor lo mueve o gira.....el adyacente supeior se ve cuando se analiza la caja que estaba arriba

        Gravedad2(HA_ik)
                
        for i in range(Productos):
            for k in range(3):
                Overlap(HA_ik,k,i)
                        
        Gravedad2(HA_ik)
        
        
    vt=0
    vm=np.zeros(Clientes)
    for k in range(Clientes):#de aqui se llama
        vm[k]=Volumen(HA_ik,Dimensiones,k)
        vt=vt+vm[k]

    """ Ajuste de espacio vacio entre clientes por movv"""

    x=0
    LT=MX[0]
    while x<=LT:
        h=0
        for i in range(Productos):
            if (HA_ik[i][0]<=x<=HA_ik[i][0]+Dimensiones[i][0]):
                h=1
                break
        if h==0:
            for i in range(Productos):
                if HA_ik[i][0]>x:
                    HA_ik[i][0]=HA_ik[i][0]-1
            
            for i in range (Productos):
                if i==0:
                    xmax=HA_ik[i][0]+Dimensiones[i][0]
                if i>0:
                    if (HA_ik[i][0]+Dimensiones[i][0])>xmax:
                        xmax=HA_ik[i][0]+Dimensiones[i][0]

            LT=xmax
            x=x-1
        x=x+1    
    
    

    "Nueva FO"
        

    pen1=ORDEN(HA_ik,Dimensiones)
    pen2=ORDEN2(HA_ik,Dimensiones)
    pent=pen1+pen2

    
    "FO"
    Optimo=LT

    
    Guarda_todo.append(Optimo)

    tiempo_no_optimo.append(int(elapsed_time))


    F=0

    F=int(min(MatrizOptima2))

    elapsed_time = time() - starting_point

    iteracion=iteracion+1
  
    if (((Optimo<F)and(vt<2*v0)) or ((Optimo==F)and(vt<v0))or((Optimo==F)and(pent<pen0))):

        """Se obtiene el minimo de las pruebas"""
        
        v0=vt#guardar el mejor volumen
        pen0=pent
        
        HA=HA_ik.copy()
        niter=iteracion
        tiempo= time() - starting_point
        
        Guarda_Optimo.append(Optimo)

        tiempo_optimo.append(int(elapsed_time))

        print ("HA_ik ", iteracion, "es:", HA_ik[0:Productos], "","El optimo es:"
               , Optimo, "En ", elapsed_time, "segundos")
        print("con la probabilidad ",rand,"volumen de referencia es: ",vt,
              "pen atras ",pen1,"pen adelante ",pen2,"pen total ",pent)
        

    else:# si no se obtiene un optimo, se continua iterando con la mejor solucion

        HA_ik=HA.copy()


    MatrizOptima2.append(Optimo)

    Optimo=0 


    elapsed_time = time() - starting_point

    
    if elapsed_time>=TiempoDeComputo:

        break



#Largo maximo
for i in range (Productos):
    if i==0:
        xmax=HA[i][0]+Dimensiones[i][0]
    if i>0:
        if (HA[i][0]+Dimensiones[i][0])>xmax:
            xmax=HA[i][0]+Dimensiones[i][0]

MX[0]=xmax
       
print ("Numero de iteraciones", iteracion)

print("en la iteracion: ", niter," y el tiempo ",tiempo)
print("Largo maximo es  ", MX[0])
print("el volumen es  ", v0," la penalizacion es ",pen0)

print ("tiempo", elapsed_time)

print ("la mejor iteración es: ", HA[0:Productos])

#graficar solucion
dibujar(HA,Productos, Dimensiones)
print("considerando ",Productos," productos y ",Clientes," clientes")


#Guardar solucion inicial y final en archivo de texto
archivo = open("spp.txt","w")
for i in range (Productos):
    archivo.write("[")
    archivo.write('%s'%SI[i][0])
    archivo.write(",")
    archivo.write('%s'%SI[i][1])
    archivo.write(",")
    archivo.write('%s'%SI[i][2])
    archivo.write("]")
    archivo.write(",")
archivo.write("\n\n\n\n")
for i in range (Productos):
    archivo.write("[")
    archivo.write('%s'%HA[i][0])
    archivo.write(",")
    archivo.write('%s'%HA[i][1])
    archivo.write(",")
    archivo.write('%s'%HA[i][2])
    archivo.write("]")
    archivo.write(",")
archivo.close() 