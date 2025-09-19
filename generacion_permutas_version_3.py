import tkinter as tk
from PIL import ImageTk, Image
import random
ANCHO_FOTO=150
ALTO_FOTO=150
ANCHO_FOTO_MINIATURA=70
ALTO_FOTO_MINIATURA=70
POSICION_INICIAL=0
lista_posiciones = [[0,0],[0,1],[1,0],[1,1],[2,0],[2,1]] 
lista_imagenes=[]
permutas = []
def factorial(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado
def fisher_yates_shuffle(lista):

    n = len(lista)
    for i in range(n - 1, 0, -1):
        j = random.randint(0, i)
        lista[i], lista[j] = lista[j], lista[i]

def generador_permutas_fuerza_bruta(lista):
    global permutas
    n = len(lista)
    permutas.append(list(lista))
    while len(permutas) < factorial(n):
        nueva_lista = list(lista)
        fisher_yates_shuffle(nueva_lista)
        
        if nueva_lista not in permutas:
            permutas.append(nueva_lista)
            print(f"Permutación encontrada: {nueva_lista}") 
            
    
def generar_posicion_opciones(posicion_inicial):
    global POSICION_INICIAL
    global permutas
    global lista_imagenes

    if POSICION_INICIAL ==0:
        frame_opcion_1.grid_forget()
        frame_no_disponible.grid(column=0,row=0, sticky="nsew")
        etiqueta_no_disponible.pack()
        
    else:
        if POSICION_INICIAL==1:
            frame_no_disponible.grid_forget()
            frame_opcion_1.grid(column=0,row=0)
            
        lista_imagenes[0].grid(column=permutas[posicion_inicial-1][0][0],row=permutas[posicion_inicial-1][0][1])
        lista_imagenes[1].grid(column=permutas[posicion_inicial-1][1][0],row=permutas[posicion_inicial-1][1][1])
        lista_imagenes[2].grid(column=permutas[posicion_inicial-1][2][0],row=permutas[posicion_inicial-1][2][1])
        lista_imagenes[3].grid(column=permutas[posicion_inicial-1][3][0],row=permutas[posicion_inicial-1][3][1])
        lista_imagenes[4].grid(column=permutas[posicion_inicial-1][4][0],row=permutas[posicion_inicial-1][4][1])
        lista_imagenes[5].grid(column=permutas[posicion_inicial-1][5][0],row=permutas[posicion_inicial-1][5][1])
        #imagen_1_opcion_1.grid(column=permutas[posicion_inicial-1][0][0],row=permutas[posicion_inicial-1][0][1])
        #imagen_2_opcion_1.grid(column=permutas[posicion_inicial-1][1][0],row=permutas[posicion_inicial-1][1][1])
        #imagen_3_opcion_1.grid(column=permutas[posicion_inicial-1][2][0],row=permutas[posicion_inicial-1][2][1])
        #imagen_4_opcion_1.grid(column=permutas[posicion_inicial-1][3][0],row=permutas[posicion_inicial-1][3][1])
        #imagen_5_opcion_1.grid(column=permutas[posicion_inicial-1][4][0],row=permutas[posicion_inicial-1][4][1])
        #imagen_6_opcion_1.grid(column=permutas[posicion_inicial-1][5][0],row=permutas[posicion_inicial-1][5][1])
        

    
    label_imagen.grid(column=permutas[posicion_inicial][0][0],row=permutas[posicion_inicial][0][1])
    label_imagen_1.grid(column=permutas[posicion_inicial][1][0],row=permutas[posicion_inicial][1][1])
    label_imagen_2.grid(column=permutas[posicion_inicial][2][0],row=permutas[posicion_inicial][2][1])
    label_imagen_3.grid(column=permutas[posicion_inicial][3][0],row=permutas[posicion_inicial][3][1])
    label_imagen_4.grid(column=permutas[posicion_inicial][4][0],row=permutas[posicion_inicial][4][1])
    label_imagen_5.grid(column=permutas[posicion_inicial][5][0],row=permutas[posicion_inicial][5][1])
    imagen_1_opcion_2.grid(column=permutas[posicion_inicial][0][0],row=permutas[posicion_inicial][0][1])
    imagen_2_opcion_2.grid(column=permutas[posicion_inicial][1][0],row=permutas[posicion_inicial][1][1])
    imagen_3_opcion_2.grid(column=permutas[posicion_inicial][2][0],row=permutas[posicion_inicial][2][1])
    imagen_4_opcion_2.grid(column=permutas[posicion_inicial][3][0],row=permutas[posicion_inicial][3][1])
    imagen_5_opcion_2.grid(column=permutas[posicion_inicial][4][0],row=permutas[posicion_inicial][4][1])
    imagen_6_opcion_2.grid(column=permutas[posicion_inicial][5][0],row=permutas[posicion_inicial][5][1])
    
    
    if POSICION_INICIAL==len(permutas):
        frame_opcion_3.grid_forget()
        frame_no_disponible.grid(column=2,row=0, sticky="nsew")
        etiqueta_no_disponible.pack()
    else:
        if POSICION_INICIAL==len(permutas)-1:
            
            frame_no_disponible.grid_forget()
            frame_opcion_3.grid(column=2,row=0)
        
        imagen_1_opcion_3.grid(column=permutas[posicion_inicial+1][0][0],row=permutas[posicion_inicial+1][0][1])
        imagen_2_opcion_3.grid(column=permutas[posicion_inicial+1][1][0],row=permutas[posicion_inicial+1][1][1])
        imagen_3_opcion_3.grid(column=permutas[posicion_inicial+1][2][0],row=permutas[posicion_inicial+1][2][1])
        imagen_4_opcion_3.grid(column=permutas[posicion_inicial+1][3][0],row=permutas[posicion_inicial+1][3][1])
        imagen_5_opcion_3.grid(column=permutas[posicion_inicial+1][4][0],row=permutas[posicion_inicial+1][4][1])
        imagen_6_opcion_3.grid(column=permutas[posicion_inicial+1][5][0],row=permutas[posicion_inicial+1][5][1])

    
def siguiente():
    global POSICION_INICIAL
    POSICION_INICIAL=POSICION_INICIAL+1
    generar_posicion_opciones(POSICION_INICIAL)
def anterior():
    global POSICION_INICIAL
    if POSICION_INICIAL-1>=0:
        POSICION_INICIAL=POSICION_INICIAL-1
    generar_posicion_opciones(POSICION_INICIAL)
def realizar_permutas():
    global permutas
    global lista_posiciones
    boton_anterior.grid(column=1, row=0)
    boton_siguiente.grid(column=3, row=0)
    generador_permutas_fuerza_bruta(lista_posiciones)
    label_anterior.grid(column=0,row=0)
    label_siguiente.grid(column=4,row=0)
    frame_opcion_1.grid(column=1, row=0)
    frame_opcion_2.grid(column=2, row=0)
    frame_opcion_3.grid(column=3, row=0)
    generar_posicion_opciones(POSICION_INICIAL)  
    print("\n---")
    print(f"Total de permutaciones encontradas: {len(permutas)}")  



    


#todas_las_permutaciones = generador_permutas_fuerza_bruta(mi_lista)
root=tk.Tk()
root.geometry("800x600")
root.title("Permutaciones")

frame_fotos=tk.Frame(pady=15)
frame_fotos.pack()
frame_opciones_fotos=tk.Frame(pady=10, padx=10)
frame_opciones_fotos.pack()
frame_botones=tk.Frame(pady=10)
frame_botones.pack()
frame_opcion_1=tk.Frame(frame_opciones_fotos, width=210,height=210,padx=10)
frame_opcion_2=tk.Frame(frame_opciones_fotos,width=210,height=210,padx=30, highlightbackground='blue', highlightthickness=3)
frame_opcion_3=tk.Frame(frame_opciones_fotos,width=210,height=210,padx=20)
frame_no_disponible=tk.Frame(frame_opciones_fotos,width=210,height=210,padx=10)
etiqueta_no_disponible=tk.Label(frame_no_disponible, text="NO DISPONIBLE", height=10, width=28,padx=10)
imagen=Image.open("imagenes/foto_1.jpg")
imagen=imagen.resize((ANCHO_FOTO, ALTO_FOTO), Image.LANCZOS)
imagen_tk=ImageTk.PhotoImage(imagen)
label_imagen=tk.Label(frame_fotos, image=imagen_tk)
label_imagen.grid(column=lista_posiciones[0][0],row=lista_posiciones[0][1])
imagen_1=Image.open("imagenes/foto_2.webp" )
imagen_1=imagen_1.resize((ANCHO_FOTO, ALTO_FOTO), Image.LANCZOS)
imagen_tk_1=ImageTk.PhotoImage(imagen_1)
label_imagen_1=tk.Label(frame_fotos, image=imagen_tk_1)
label_imagen_1.grid(column=lista_posiciones[1][0],row=lista_posiciones[1][1])
imagen_2=Image.open("imagenes/foto_3.jpeg" )
imagen_2=imagen_2.resize((ANCHO_FOTO, ALTO_FOTO), Image.LANCZOS)
imagen_tk_2=ImageTk.PhotoImage(imagen_2)
label_imagen_2=tk.Label(frame_fotos, image=imagen_tk_2 )
label_imagen_2.grid(column=lista_posiciones[2][0],row=lista_posiciones[2][1])
imagen_3=Image.open("imagenes/foto_4.jpeg")
imagen_3=imagen_3.resize((ANCHO_FOTO, ALTO_FOTO), Image.LANCZOS)
imagen_tk_3=ImageTk.PhotoImage(imagen_3)
label_imagen_3=tk.Label(frame_fotos, image=imagen_tk_3)
label_imagen_3.grid(column=lista_posiciones[3][0],row=lista_posiciones[3][1])
imagen_4=Image.open("imagenes/foto_5.webp" )
imagen_4=imagen_4.resize((ANCHO_FOTO, ALTO_FOTO), Image.LANCZOS)
imagen_tk_4=ImageTk.PhotoImage(imagen_4)
label_imagen_4=tk.Label(frame_fotos, image=imagen_tk_4)
label_imagen_4.grid(column=lista_posiciones[4][0],row=lista_posiciones[4][1])
imagen_5=Image.open("imagenes/foto_6.webp" )
imagen_5=imagen_5.resize((ANCHO_FOTO, ALTO_FOTO), Image.LANCZOS)
imagen_tk_5=ImageTk.PhotoImage(imagen_5)
label_imagen_5=tk.Label(frame_fotos, image=imagen_tk_5)
label_imagen_5.grid(column=lista_posiciones[5][0],row=lista_posiciones[5][1])
label_anterior=tk.Label(frame_botones,text="Opcion Anterior")
label_siguiente=tk.Label(frame_botones,text="Opcion siguiente")
boton_anterior=tk.Button(frame_botones,text="<<", command=anterior)
boton_siguiente=tk.Button(frame_botones,text=">>", command=siguiente)
boton_permutas=tk.Button(frame_botones,text="Realizar Permutas", command=realizar_permutas)
boton_permutas.grid(column=2, row=0)

lista_imagenes.append(tk.Label(frame_opcion_1, image=imagen_tk, width=ANCHO_FOTO_MINIATURA, height=ALTO_FOTO_MINIATURA))
imagen_2_opcion_1=tk.Label(frame_opcion_1, image=imagen_tk_1, width=ANCHO_FOTO_MINIATURA, height=ALTO_FOTO_MINIATURA)
imagen_3_opcion_1=tk.Label(frame_opcion_1, image=imagen_tk_2, width=ANCHO_FOTO_MINIATURA, height=ALTO_FOTO_MINIATURA)
imagen_4_opcion_1=tk.Label(frame_opcion_1, image=imagen_tk_3, width=ANCHO_FOTO_MINIATURA, height=ALTO_FOTO_MINIATURA)
imagen_5_opcion_1=tk.Label(frame_opcion_1, image=imagen_tk_4, width=ANCHO_FOTO_MINIATURA, height=ALTO_FOTO_MINIATURA)
imagen_6_opcion_1=tk.Label(frame_opcion_1, image=imagen_tk_5, width=ANCHO_FOTO_MINIATURA, height=ALTO_FOTO_MINIATURA)
imagen_1_opcion_2=tk.Label(frame_opcion_2, image=imagen_tk, width=ANCHO_FOTO_MINIATURA, height=ALTO_FOTO_MINIATURA)
imagen_2_opcion_2=tk.Label(frame_opcion_2, image=imagen_tk_1, width=ANCHO_FOTO_MINIATURA, height=ALTO_FOTO_MINIATURA)
imagen_3_opcion_2=tk.Label(frame_opcion_2, image=imagen_tk_2, width=ANCHO_FOTO_MINIATURA, height=ALTO_FOTO_MINIATURA)
imagen_4_opcion_2=tk.Label(frame_opcion_2, image=imagen_tk_3, width=ANCHO_FOTO_MINIATURA, height=ALTO_FOTO_MINIATURA)
imagen_5_opcion_2=tk.Label(frame_opcion_2, image=imagen_tk_4, width=ANCHO_FOTO_MINIATURA, height=ALTO_FOTO_MINIATURA)
imagen_6_opcion_2=tk.Label(frame_opcion_2, image=imagen_tk_5, width=ANCHO_FOTO_MINIATURA, height=ALTO_FOTO_MINIATURA)
imagen_1_opcion_3=tk.Label(frame_opcion_3, image=imagen_tk, width=ANCHO_FOTO_MINIATURA, height=ALTO_FOTO_MINIATURA)
imagen_2_opcion_3=tk.Label(frame_opcion_3, image=imagen_tk_1, width=ANCHO_FOTO_MINIATURA, height=ALTO_FOTO_MINIATURA)
imagen_3_opcion_3=tk.Label(frame_opcion_3, image=imagen_tk_2, width=ANCHO_FOTO_MINIATURA, height=ALTO_FOTO_MINIATURA)
imagen_4_opcion_3=tk.Label(frame_opcion_3, image=imagen_tk_3, width=ANCHO_FOTO_MINIATURA, height=ALTO_FOTO_MINIATURA)
imagen_5_opcion_3=tk.Label(frame_opcion_3, image=imagen_tk_4, width=ANCHO_FOTO_MINIATURA, height=ALTO_FOTO_MINIATURA)
imagen_6_opcion_3=tk.Label(frame_opcion_3, image=imagen_tk_5, width=ANCHO_FOTO_MINIATURA, height=ALTO_FOTO_MINIATURA)

root.mainloop()

#print(f"Permutaciones finales: {todas_las_permutaciones}")