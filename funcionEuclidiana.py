import random
from math import sqrt
import tkinter as tk
p1=[]
p2=[]
p3=[]
p4=[]
p5=[]
listasPuntos=[]
VAL_MIN=0
VAL_MAX=40
X=0
Y=1
TAMANIO_LISTA=2
puntoUno=0
puntoDos=0
distanciaCorta=0
se_generaron_numeros=False
def imprimirResultados():
    global puntoUno
    global puntoDos
    etiquetaResultados.grid(row=7,column=3)
    etiquetaResultadoNumerico.config(text=f"Los puntos mas cercanos son  P{puntoUno+1}: {listasPuntos[puntoUno]} y P{puntoDos+1} : {listasPuntos[puntoDos]} \n con una distancia igual a {distanciaCorta}")
    etiquetaResultadoNumerico.grid(row=7,column=4)
def insertarListasEnListas():
    listasPuntos.insert(0,p1)
    listasPuntos.insert(1,p2)
    listasPuntos.insert(2,p3)
    listasPuntos.insert(3,p4)
    listasPuntos.insert(4,p5)
def EstablecerEntry0():
    entradaP1X.insert(0,"0")
    entradaP1Y.insert(0,"0")
    entradaP2X.insert(0,"0")
    entradaP2Y.insert(0,"0")
    entradaP3X.insert(0,"0")
    entradaP3Y.insert(0,"0")
    entradaP4X.insert(0,"0")
    entradaP4Y.insert(0,"0")
    entradaP5X.insert(0,"0")
    entradaP5Y.insert(0,"0")
def limpiarEntries():
    entradaP1X.delete(0,tk.END)
    entradaP1Y.delete(0,tk.END)
    entradaP2X.delete(0,tk.END)
    entradaP2Y.delete(0,tk.END)
    entradaP3X.delete(0,tk.END)
    entradaP3Y.delete(0,tk.END)
    entradaP4X.delete(0,tk.END)
    entradaP4Y.delete(0,tk.END)
    entradaP5X.delete(0,tk.END)
    entradaP5Y.delete(0,tk.END)
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
    p2=[int(entradaP2X.get()),int(entradaP2Y.get())]
    p3=[int(entradaP3X.get()),int(entradaP3Y.get())]
    p4=[int(entradaP4X.get()),int(entradaP4Y.get())]
    p5=[int(entradaP5X.get()),int(entradaP5Y.get())]
    insertarListasEnListas()
    
def limpiar():
    limpiarEntries()
    EstablecerEntry0()
    etiquetaResultados.grid_forget()
    etiquetaResultadoNumerico.grid_forget()
def limpiarLista():
    for i in range(len(listasPuntos)):
        listasPuntos.pop()
    
    
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
    puntoUno=0
    puntoDos=1
    for i in range(len(listasPuntos)):
        for j in range(i+1,len(listasPuntos)):
            distancia=sqrt(((listasPuntos[i][X]-listasPuntos[j][X])**2)+((listasPuntos[i][Y]-listasPuntos[j][Y])**2)) 
            if distancia<distanciaCorta:
                puntoUno=i
                puntoDos=j
                distanciaCorta=distancia
                
        
    imprimirResultados()
    se_generaron_numeros=False
    limpiarLista()



def generar():
    global se_generaron_numeros
    global p1
    global p2
    global p3
    global p4
    global p5
    global listasPuntos
    se_generaron_numeros=True
    p1 = [random.randint(VAL_MIN, VAL_MAX) for _ in range(TAMANIO_LISTA)]
    p2 = [random.randint(VAL_MIN, VAL_MAX) for _ in range(TAMANIO_LISTA)]
    p3 = [random.randint(VAL_MIN, VAL_MAX) for _ in range(TAMANIO_LISTA)]
    p4 = [random.randint(VAL_MIN, VAL_MAX) for _ in range(TAMANIO_LISTA)]
    p5 = [random.randint(VAL_MIN, VAL_MAX) for _ in range(TAMANIO_LISTA)]
    insertarListasEnListas()
    limpiarEntries()
    entradaP1X.insert(p1[X],f'{p1[X]}')
    entradaP1Y.insert(p1[Y],f'{p1[Y]}')
    entradaP2X.insert(p2[X],f'{p2[X]}')
    entradaP2Y.insert(p2[Y],f'{p2[Y]}')
    entradaP3X.insert(p3[X],f'{p3[X]}')
    entradaP3Y.insert(p3[Y],f'{p3[Y]}')
    entradaP4X.insert(p4[X],f'{p4[X]}')
    entradaP4Y.insert(p4[Y],f'{p4[Y]}')
    entradaP5X.insert(p5[X],f'{p5[X]}')
    entradaP5Y.insert(p5[Y],f'{p5[Y]}')
    
    

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
entradaP1X.grid(column=1,row=1)
entradaP1Y=tk.Entry(panel)
entradaP1Y.grid(column=2,row=1)
entradaP2X=tk.Entry(panel)
entradaP2X.grid(column=1,row=2)
entradaP2Y=tk.Entry(panel)
entradaP2Y.grid(column=2,row=2)
entradaP3X=tk.Entry(panel)
entradaP3X.grid(column=1,row=3)
entradaP3Y=tk.Entry(panel)
entradaP3Y.grid(column=2,row=3)
entradaP4X=tk.Entry(panel)
entradaP4X.grid(column=1,row=4)
entradaP4Y=tk.Entry(panel)
entradaP4Y.grid(column=2,row=4)
entradaP5X=tk.Entry(panel)
entradaP5X.grid(column=1,row=5)
entradaP5Y=tk.Entry(panel)
EstablecerEntry0()
entradaP5Y.grid(column=2,row=5)
boton_Calcular=tk.Button(panel,text="Calcular",command=encontrarDistanciaCorta)
boton_Calcular.grid(column=3,row=1)
boton_Generar_Random=tk.Button(panel,text="Llenar Random",command=generar)
boton_Generar_Random.grid(column=3,row=2)
boton_limpiar=tk.Button(panel,text="Limpiar",command=limpiar)
boton_limpiar.grid(column=3,row=3)
etiquetaResultadoNumerico=tk.Label(panel)
etiquetaResultados=tk.Label(panel,text="Resultados: ")


root.mainloop()

