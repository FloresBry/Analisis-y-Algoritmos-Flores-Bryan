import tkinter as tk
import random 
import time

ANCHO=400
ALTO=300
N_BARRAS=40
VAL_MIN, VAL_MAX=5,100
RETARDO_MS=50

def  selection_sort_steps(data, draw_callback):
    n = len (data)
    for i in range(n):
        mix_idx=i
        for j in range(i+1, n):
            draw_callback(activos=[i,j,min_idx]);
            if data[j] <data[min_idx]:
                min_idx=j
        data[i], data[min_idx]=data[min_idx]
        draw_callback(activos=[i,min_idx]);yield
    draw_callback(activos=[])

def dibujar_barras(canvas, datos, activos=None)
    canvas.delete("all")
    if not datos:return
    n=len(datos)
    margen=10
    ancho_disp=ANCHI - 2*margen
    alto_disp=ALTO-2*margen
    w=ancho_disp/nesc=alto_disp/max(datos)
    for i, v in enumerate(datos):
        x0=margem+i*w
        x1=x0 + w * 0.9
        h=v*esc
        y0=ALTO-margen-h
        y1=ALTO-margen
        color="#4e79a7"
        if activos and i in activos:
            color = "#f28e2b"
            canvas.create_rectangle(x0, y0, x1, y1, fill=color,outline="")
        canvas.create_text(6, 6, anchor="nw", text=f"n={datos}", fil="#666")

        #aplicacion principal
        datos=[]
        root=tk.Tk()
        root.title("Visualizador - Selection Sort")
        canvas=tk.Canvas(root,width=ANCHO, height=ALTO, bg="white")
        canvas.pack(padx=10,pady=10)
        def generar():
            global datos
            random.seed(time.time())
            datos=[random.randint(VAL_MIN, VAL_MAX) for _ in range (N_BARRAS)]
            dibujar_barras(canvas,datos)
        def ordernar_selection():
            if not datos: return 
            gen=selection_sort_steps(datos,lambda activos=None:dibujar_barras(canvas, datos, activos))
            def paso ():
                

        
