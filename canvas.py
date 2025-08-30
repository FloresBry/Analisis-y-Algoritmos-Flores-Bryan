import tkinter as tk
window=tk.Tk()
window.geometry("600x500")
window.title('Canvas')
canvas=tk.Canvas(window, bg= 'lightblue')
canvas.pack()
canvas.create_rectangle((50,20,200,200),fill='red',width=2,dash=(10,6),outline='white')
canvas.create_line(0,0,150,100,fill="black")
canvas.create_oval(300,10,200,80,fill='green')
canvas.create_polygon(50,0,100,200,200,50,fill='white')
canvas.create_arc(300,10,200,80, 
                  fill='red', 
                  start=45,
                  extent=140,
                  style=tk.CHORD, 
                  outline='yellow',
                  width=3)
canvas.create_text(0,0, text="Hola")
window.mainloop()