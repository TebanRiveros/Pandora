import tkinter as tk

def abrir_ventana(titulo):
    nueva_ventana = tk.Toplevel()
    nueva_ventana.title(titulo)
    nueva_ventana.geometry("300x200")
    etiqueta = tk.Label(nueva_ventana, text=f"Estás en la sección de {titulo}")
    etiqueta.pack(padx=20, pady=20)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Bienvenido al programa Pandora")

color_boton_analogo = "#66c2ff"  # Azul claro
color_boton_digital = "#ff9999"  # Rosa claro

# Crear botón 'Análogo' que abre una nueva ventana
boton_analogo = tk.Button(ventana, text="Instrumento Análogo", command=lambda: abrir_ventana("Instrumento Análogo"), bg=color_boton_analogo)
boton_analogo.pack(pady=10)

# Crear botón 'Digital' que abre una nueva ventana
boton_digital = tk.Button(ventana, text="Instrumento Digital", command=lambda: abrir_ventana("Instrumento Digital"), bg=color_boton_digital)
boton_digital.pack(pady=10)

# Iniciar el bucle de eventos
ventana.mainloop()