import tkinter as tk #libreria para tkinter para la interfaz grafica

#frame de la aplicacion
ventana = tk.Tk()

#entrada de texto 
entryDisplay = tk.Entry(ventana, width=18, borderwidth=4, font=('arial', 24), justify="left", state="readonly")

primerNumero = 0
segundoNumero = 0
operacion = None

global currentOperation

#estilo de los botones

button_style = {
        "padx": 30,
        "pady": 0,
        "font": ("Arial", 18)
    }

#funciones de los botonos

#botones

#botones numericos

def modificacionDeEntrada(entrada):

    entryDisplay.config(state='normal')
    entryDisplay.insert(tk.END, str(entrada))
    entryDisplay.config(state='readonly')

def getNumbers(numeros):

    modificacionDeEntrada(numeros)

#boton clear
def botonClear():

    entryDisplay.config(state='normal')
    entryDisplay.delete(0, tk.END)
    entryDisplay.insert(tk.END, str(0))
    entryDisplay.config(state='readonly')


#setup

def main():
    #ventana principal de la aplicacion
    
    #windows settings
    ventana.title("Calculadora basica") #titulo de la ventana
    ventana.geometry("350x750") #establece el tamaño de la ventana
    ventana.resizable(False, False) #restringe la redimension de la ventana

    #configuracion de columnas
    ventana.grid_columnconfigure(0, weight=1) #solo tendra dos columnas 
    ventana.grid_columnconfigure(1, weight=1)
    ventana.grid_columnconfigure(2, weight=1)

    #elementos en la pantalla

    #titulo de la calculadora
    tituloCalculadora = tk.Label(ventana, text='Calculadora matematica',
                             font=('Arial', 16, 'bold'),
                             fg='black',
                             padx= 0,
                             pady= 0)
    

    #botones de la calculadora
    #operaciones
    btn_clear = tk.Button(ventana, text="C", command=botonClear, **button_style, width=13) #boton de limpiar
    btn_plus = tk.Button(ventana, text="+", **button_style, width=13) #boton de sumar 
    btn_resta = tk.Button(ventana, text="-", **button_style, width=13) #boton de resta
    btn_mult = tk.Button(ventana, text="*", **button_style, width=13) #boton de limpiar
    btn_divi = tk.Button(ventana, text="/", **button_style, width=13) #boton de sumar 
    btn_igual = tk.Button(ventana, text="=", **button_style, width=13) #boton de sumar 
    
    #numeros
    btn_1 = tk.Button(ventana, text="1",command=modificacionDeEntrada(1) ,**button_style, width=13) #boton de limpiar
    btn_2 = tk.Button(ventana, text="2", **button_style, width=13) #boton de sumar 
    btn_3 = tk.Button(ventana, text="3", **button_style, width=13) #boton de resta
    btn_4 = tk.Button(ventana, text="4", **button_style, width=13) #boton de limpiar
    btn_5 = tk.Button(ventana, text="5", **button_style, width=13) #boton de sumar
    btn_6 = tk.Button(ventana, text="6", **button_style, width=13) #boton de limpiar
    btn_7 = tk.Button(ventana, text="7", **button_style, width=13) #boton de sumar 
    btn_8 = tk.Button(ventana, text="8", **button_style, width=13) #boton de resta
    btn_9 = tk.Button(ventana, text="9", **button_style, width=13) #boton de limpiar
    btn_0 = tk.Button(ventana, text="0", **button_style, width=13) #boton de sumar 


    #visuzalizacion de lso elementos en pantalla
    tituloCalculadora.grid(row=1, column=0, columnspan=3, padx=0, pady=5, sticky="ew") #funcion para hacer que los elementos aparezcan en la pantalla
    entryDisplay.grid(row=2, column=0, columnspan=3, padx=0, pady=5, sticky="ew")
    btn_clear.grid(row=3, column=0, padx=10, pady=5, sticky="ew")
    btn_plus.grid(row=3, column=2, padx=10, pady=5, sticky="ew")
    btn_resta.grid(row=4, column=0, padx=10, pady=5, sticky="ew")
    btn_mult.grid(row=4, column=2, padx=10, pady=5, sticky="ew")
    btn_divi.grid(row=5, column=0, padx=10, pady=5, sticky="ew")
    btn_igual.grid(row=5, column=2, padx=10, pady=5, sticky="ew")
    btn_1.grid(row=6, column=0, padx=10, pady=5, sticky="ew")
    btn_2.grid(row=6, column=2, padx=10, pady=5, sticky="ew")
    btn_3.grid(row=7, column=0, padx=10, pady=5, sticky="ew")
    btn_4.grid(row=7, column=2, padx=10, pady=5, sticky="ew")
    btn_5.grid(row=8, column=0, padx=10, pady=5, sticky="ew")
    btn_6.grid(row=8, column=2, padx=10, pady=5, sticky="ew")
    btn_7.grid(row=9, column=0, padx=10, pady=5, sticky="ew")
    btn_8.grid(row=9, column=2, padx=10, pady=5, sticky="ew")
    btn_9.grid(row=10, column=0, padx=10, pady=5, sticky="ew")
    btn_0.grid(row=10, column=2, padx=10, pady=5, sticky="ew")
    
    #bucle de eventos para mantener la ventana abierta
    #botonClear()
    modificacionDeEntrada(1)
    ventana.mainloop()
main()

