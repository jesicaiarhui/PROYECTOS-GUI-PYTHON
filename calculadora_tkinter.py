from tkinter import *
from math import *
 
#VISUALIZAR LA OPERACION EN LA PANTALLA
def Clik_boton(num):
    global operador
    operador=operador+str(num)
    input_text.set(operador)
 
#CÁLCULO Y MUESTRA DE RESULTADOS.
def resultado():
    global operador
    try:
        opera=str(eval(operador))
        input_text.set(opera)
    except:
        input_text.set("ERROR")
    operador = ""
 
#LIMPIEZA DE PANTALLA.
def clear():
    global operador
    operador=("")
    input_text.set("0")
 
 
ventana=Tk()
ventana.title("CALCULADORA")
ventana.geometry("392x600")
ventana.resizable(0,0) #para expandir
ventana.config(cursor="hand2") #cambio cursor


ventana.configure(background="black")
color_boton=("white")
ventana.iconbitmap("calcu.ico") #cambio de icono de la ventana
 
ancho_boton=11
alto_boton=3
input_text=StringVar()
operador=""
 
Salida=Entry(ventana,font=('arial',20,'bold'),width=22,
textvariable=input_text,bd=20,insertwidth=4,bg="white",justify="right")
Salida.place(x=10,y=60)
 
#AÑADIR BOTONES.
#CREAMOS NUESTROS BOTONES
Button(ventana,text="0",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:Clik_boton(0)).place(x=17,y=180)
Button(ventana,text="1",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:Clik_boton(1)).place(x=107,y=180)
Button(ventana,text="2",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:Clik_boton(2)).place(x=197,y=180)
Button(ventana,text="3",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:Clik_boton(3)).place(x=287,y=180)
Button(ventana,text="4",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:Clik_boton(4)).place(x=17,y=240)
Button(ventana,text="5",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:Clik_boton(5)).place(x=107,y=240)
Button(ventana,text="6",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:Clik_boton(6)).place(x=197,y=240)
Button(ventana,text="7",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:Clik_boton(7)).place(x=287,y=240)
Button(ventana,text="8",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:Clik_boton(8)).place(x=17,y=300)
Button(ventana,text="9",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:Clik_boton(9)).place(x=107,y=300)
Button(ventana,text="π",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:Clik_boton("pi")).place(x=197,y=300)
Button(ventana,text=",",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:Clik_boton(".")).place(x=287,y=300)
Button(ventana,text="+",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:Clik_boton("+")).place(x=17,y=360)
Button(ventana,text="-",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:Clik_boton("-")).place(x=107,y=360)
Button(ventana,text="*",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:Clik_boton("*")).place(x=197,y=360)
Button(ventana,text="/",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:Clik_boton("/")).place(x=287,y=360)
Button(ventana,text="√",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:Clik_boton("sqrt(")).place(x=17,y=420)
Button(ventana,text="(",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:Clik_boton("(")).place(x=17,y=480)
Button(ventana,text=")",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:Clik_boton(")")).place(x=107,y=480)
Button(ventana,text="%",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:Clik_boton("%")).place(x=197,y=480)
Button(ventana,text="=",bg=color_boton,width=ancho_boton,height=alto_boton,command=resultado).place(x=287,y=480)
Button(ventana,text="C",bg=color_boton,width=ancho_boton,height=alto_boton,command=clear).place(x=107,y=420)
Button(ventana,text="^",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:Clik_boton("**")).place(x=197,y=420)
Button(ventana,text="ln",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:Clik_boton("log(")).place(x=287,y=420)
 
clear()
 
ventana.mainloop()