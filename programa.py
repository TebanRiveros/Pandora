import tkinter as tk
from tkinter import PhotoImage


#Ventana analogo
def abrir_ventanaa(titulo):
    nueva_ventanaa= tk.Toplevel()
    nueva_ventanaa.title(titulo)
    nueva_ventanaa.geometry("1000x400")
    etiqueta = tk.Label(nueva_ventanaa, text=f"Estás en la sección de {titulo}", wraplength=600, justify="center", font=("Arial", 20))
    texto_ina = tk.Label(nueva_ventanaa, text=f"En el instrumento análogo podrás simular o diseñar recuerda que en esta sección no se tiene uso de discretizador por lo tanto te invitamos a observar el diagrama", wraplength=600, justify="left")
    imagen_path_analogo = r"C:\Users\David Ricardo\OneDrive\Escritorio\Instrumentación\Pandora\diagramaanalogo.png"
    imagen_analogo = PhotoImage(file=imagen_path_analogo)
    imagen_analogo = imagen_analogo.subsample(3, 3)  # Reducir tamaño

    # Etiqueta para la imagen de la sección digital
    etiqueta_imagen_analogo = tk.Label(nueva_ventanaa, image=imagen_analogo)
    etiqueta_imagen_analogo.pack(side="right", padx=10, pady=20)
    etiqueta.pack(pady=10)
    texto_ina.pack(pady=40, padx=20, anchor="w")
   
    
    
#Ventana digital
def abrir_ventanad(titulo):
    nueva_ventanad = tk.Toplevel()
    nueva_ventanad.title(titulo)
    nueva_ventanad.geometry("1000x400")
    etiqueta = tk.Label(nueva_ventanad, text=f"Estás en la sección de {titulo}", wraplength=600, justify="center", font=("Arial", 20))
    texto_ind = tk.Label(nueva_ventanad, text=f"En el instrumento digital podrás simular o diseñar recuerda que en esta sección si se tiene uso de discretizador por lo tanto te invitamos a observar el diagrama", wraplength=600, justify="left")
    etiqueta.pack(pady=10)
    texto_ind.pack(pady=40, padx=20, anchor="w")
    imagen_path_digital = r"C:\Users\David Ricardo\OneDrive\Escritorio\Instrumentación\Pandora\diagramadigital.png"
    imagen_digital = PhotoImage(file=imagen_path_digital)
    imagen_digital = imagen_digital.subsample(3, 3)  # Reducir tamaño

    # Etiqueta para la imagen de la sección digital
    etiqueta_imagen_digital = tk.Label(nueva_ventanad, image=imagen_digital)
    etiqueta_imagen_digital.pack(side="right", padx=20, pady=7)
    
# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Bienvenido al programa Pandora")



# Texto para la ventana principal
texto_titulo = "Programa Pandora de Instrumentación Industrial"
texto_principal = "Este programa tiene como propósito diseñar y simular instrumentos ya sea analógicos o digitales. Cabe recordar que su diferencia radica en el discretizador. Los instrumentos digitales están compuestos por: Sensor, Acondicionador, Discretizador y Emulador. Los instrumentos análogos estan compuestos por: Sensor, Acondicionador y Emulador. En este programa en la parte de diseño podrá calcular los diferentes aspectos ya sea acondicionador, discretizador y/o emulador por medio de la resolución (Es el mínimo valor del salto del valor de la medida, perceptible en la indicación), código CAD (n que es el níumero de bits al que trabajará el discretizador) y voltaje de referencia para encontrar la sensibilidad del discretizador"

# Etiqueta para el texto principal
etiqueta_titulo = tk.Label(ventana, text=texto_titulo, wraplength=600, justify="center", font=("Arial", 20))
etiqueta_principal = tk.Label(ventana, text=texto_principal, wraplength=600, justify="left")
etiqueta_titulo.pack(pady=40)
etiqueta_principal.pack(pady=10, padx=20, anchor="w")  # anchor="w" alinea el texto a la izquierda

# Cargar la imagen
imagen_path = r"C:\Users\David Ricardo\OneDrive\Escritorio\Instrumentación\Pandora\siminstrumento.png"  # Ruta con cadena de texto cruda
imagen = PhotoImage(file=imagen_path)
imagen = imagen.subsample(3, 3)

# Etiqueta para la imagen
etiqueta_imagen = tk.Label(ventana, image=imagen)
etiqueta_imagen.pack(side="right", padx=20, pady=7)  # Mostrar la imagen al lado derecho

color_boton_analogo = "#66c2ff"  # Azul claro
color_boton_digital = "#ff9999"  # Rosa claro

# Crear botón 'Análogo' que abre una nueva ventana
boton_analogo = tk.Button(ventana, text="Instrumento Análogo", command=lambda: abrir_ventanaa("Instrumento Análogo"), bg=color_boton_analogo)
boton_analogo.pack(pady=40)

# Crear botón 'Digital' que abre una nueva ventana
boton_digital = tk.Button(ventana, text="Instrumento Digital", command=lambda: abrir_ventanad("Instrumento Digital"), bg=color_boton_digital)
boton_digital.pack(pady=30)

# Iniciar el bucle de eventos
ventana.mainloop()