import random
from math import sqrt
import tkinter as tk
p1=[]
p2=[]
p3=[]
p4=[]
p5=[]
listasPuntos=[]
puntoUno=0
puntoDos=0
distanciaCorta=0
se_generaron_numeros=False
def funcionEuclidiana (p1,p2):
    distancia=sqrt(((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2))
    print(distancia)

def capturarNumeros():
    global p1
    global p2
    global p3
    global p4
    global p5
    global listasPuntos
    p1=[int(entradaP1X.get()),int(entradaP1Y.get())]
    listasPuntos.append(p1)
    p2=[int(entradaP2X.get()),int(entradaP2Y.get())]
    listasPuntos.append(p2)
    p3=[int(entradaP3X.get()),int(entradaP3Y.get())]
    listasPuntos.append(p3)
    p4=[int(entradaP4X.get()),int(entradaP4Y.get())]
    listasPuntos.append(p4)
    p5=[int(entradaP5X.get()),int(entradaP5Y.get())]
    listasPuntos.append(p5)
    
def limpiar():
    root
def encontrarDistanciaCorta():
    global puntoUno
    global puntoDos
    global listasPuntos
    global distanciaCorta
    global se_generaron_numeros
    if se_generaron_numeros==False:
        capturarNumeros()
    distanciaCorta=sqrt(((listasPuntos[0][0]-listasPuntos[1][0])**2)+((listasPuntos[0][1]-listasPuntos[1][1])**2)) 
    print(f"Primera: {distanciaCorta}")
    
    i=1
    puntoUno=i
    puntoDos=i+1
    while i<len(listasPuntos)-1:
        distancia=sqrt(((listasPuntos[i][0]-listasPuntos[i+1][0])**2)+((listasPuntos[i][1]-listasPuntos[i+1][1])**2)) 
        if distancia<distanciaCorta:
            puntoUno=i
            puntoDos=i+1
            distanciaCorta=distancia
            print(f"Segundo: {distanciaCorta}")
        i=i+1
    imprimirResultados()
    se_generaron_numeros=False
    
def imprimirResultados():
    global puntoUno
    global puntoDos
    etiquetaResultados.grid(row=7,column=3)
    etiquetaResultadoNumerico=tk.Label(panel,text=f"Los puntos mas cercanos son  P{puntoUno} y P{puntoDos} \n con una distancia igual a {distanciaCorta}")
    etiquetaResultadoNumerico.grid(row=7,column=4)


def generar():
    global se_generaron_numeros
    global p1
    global p2
    global p3
    global p4
    global p5
    global listasPuntos
    se_generaron_numeros=True
    p1 = [random.randint(0, 100) for _ in range(2)]
    listasPuntos.append(p1)
    p2 = [random.randint(0, 100) for _ in range(2)]
    listasPuntos.append(p2)
    p3 = [random.randint(0, 100) for _ in range(2)]
    listasPuntos.append(p3)
    p4 = [random.randint(0, 100) for _ in range(2)]
    listasPuntos.append(p4)
    p5 = [random.randint(0, 100) for _ in range(2)]
    listasPuntos.append(p5)
    
    entradaP1X.insert(p1[0],f'{p1[0]}')
    entradaP1Y.insert(p1[1],f'{p1[1]}')
    entradaP2X.insert(p2[0],f'{p2[0]}')
    entradaP2Y.insert(p2[1],f'{p2[1]}')
    entradaP3X.insert(p3[0],f'{p3[0]}')
    entradaP3Y.insert(p3[1],f'{p3[1]}')
    entradaP4X.insert(p4[0],f'{p4[0]}')
    entradaP4Y.insert(p4[1],f'{p4[1]}')
    entradaP5X.insert(p5[0],f'{p5[0]}')
    entradaP5Y.insert(p5[1],f'{p5[1]}')
    
    

root = tk.Tk()
root.title("FORMULA euclidiana")
panel = tk.Frame(root)
panel.pack(pady=6)
etiquetaY=tk.Label(panel, text="Y")
etiquetaY.grid(column=2,row=0)
etiquetaX=tk.Label(panel, text="X")
etiquetaX.grid(column=1,row=0)
etiquetaP1=tk.Label(panel, text="P1")
etiquetaP1.grid(column=0,row=1)
etiquetaP2=tk.Label(panel, text="P2")
etiquetaP2.grid(column=0,row=2)
etiquetaP3=tk.Label(panel, text="P3")
etiquetaP3.grid(column=0,row=3)
etiquetaP4=tk.Label(panel, text="P4")
etiquetaP4.grid(column=0,row=4)
etiquetaP5=tk.Label(panel, text="P5")
etiquetaP5.grid(column=0,row=5)
entradaP1X=tk.Entry(panel)
entradaP1X.insert(0,'0')
entradaP1X.grid(column=1,row=1)
entradaP1Y=tk.Entry(panel)
entradaP1Y.insert(0,'0')
entradaP1Y.grid(column=2,row=1)
entradaP2X=tk.Entry(panel)
entradaP2X.insert(0,'0')
entradaP2X.grid(column=1,row=2)
entradaP2Y=tk.Entry(panel)
entradaP2Y.insert(0,'0')
entradaP2Y.grid(column=2,row=2)
entradaP3X=tk.Entry(panel)
entradaP3X.insert(0,'0')
entradaP3X.grid(column=1,row=3)
entradaP3Y=tk.Entry(panel)
entradaP3Y.insert(0,'0')
entradaP3Y.grid(column=2,row=3)
entradaP4X=tk.Entry(panel)
entradaP4X.insert(0,'0')
entradaP4X.grid(column=1,row=4)
entradaP4Y=tk.Entry(panel)
entradaP4Y.insert(0,'0')
entradaP4Y.grid(column=2,row=4)
entradaP5X=tk.Entry(panel)
entradaP5X.insert(0,'0')
entradaP5X.grid(column=1,row=5)
entradaP5Y=tk.Entry(panel)
entradaP5Y.insert(0,'0')
entradaP5Y.grid(column=2,row=5)
boton_Calcular=tk.Button(panel,text="Calcular",command=encontrarDistanciaCorta)
boton_Calcular.grid(column=3,row=1)
boton_Generar_Random=tk.Button(panel,text="Llenar Random",command=generar)
boton_Generar_Random.grid(column=3,row=2)
boton_limpiar=tk.Button(panel,text="Limpiar",command=limpiar)
boton_limpiar.grid(column=3,row=3)

etiquetaResultados=tk.Label(panel,text="Resultados: ")


root.mainloop()

