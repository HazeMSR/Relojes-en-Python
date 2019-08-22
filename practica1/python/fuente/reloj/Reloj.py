#!/usr/bin/python3
import tkinter as tk
import time
 
class Clock():
    def actualizar_tiempo(self):
        tiempo_actual = time.strftime("%H:%M:%S")
        txt_tiempo.configure(text=tiempo_actual)
        ventana.after(1000, self.actualizar_tiempo)
 
ventana = tk.Tk()
ventana.wm_title("Clock")
 
txt_tiempo = tk.Label(ventana, text="", font=("Helvetica", 150))
txt_tiempo.pack()
reloj = Clock()
reloj.actualizar_tiempo()

txt_tiempo2 = tk.Label(ventana, text="", font=("Arial", 250))
txt_tiempo2.pack()
reloj2 = Clock()
reloj2.actualizar_tiempo()

ventana.mainloop()
