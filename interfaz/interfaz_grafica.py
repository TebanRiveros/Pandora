import tkinter
import os
from PIL import Image, ImageTk
import customtkinter as ctk

carpeta_principal = os.path.dirname(__file__)
carpeta_imagenes = os.path.join(carpeta_principal, "imagenes")
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class Login:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.geometry("400x300")
        self.root.title('Pandora')
        ##self.root.resizable(False, False)

        label = ctk.CTkLabel(self.root, text="P A N D O R A", font=("Arial Black", 20))
        label.place(relx=0.5, rely=0.1, anchor="center")

        # Load the image
        imageninicio = ctk.CTkImage(light_image=Image.open(os.path.join(carpeta_imagenes, "instrumento.png")),dark_image=Image.open(os.path.join(carpeta_imagenes, "instrumento.png")), size=(150, 60))

        # Display the image
        image_label = ctk.CTkLabel(self.root, text="", image=imageninicio)
        image_label.place(relx=0.5, rely=0.35, anchor=tkinter.CENTER)

        def simulation_button_function():
            print("Simulation button pressed")
            self.root.destroy()
            ventanasimu = VentanaSimulacion()

        def design_button_function():
            print("Design button pressed")
            self.root.destroy()
            ventanadis = VentanaDiseno()

        simulation_button = ctk.CTkButton(master=self.root, text="Simulación", font=("Arial", 15),command=simulation_button_function, corner_radius=32, border_color="#FFCC70", border_width=1.5)
        simulation_button.place(relx=0.3, rely=0.7, anchor=tkinter.CENTER)

        design_button = ctk.CTkButton(master=self.root, text="Diseño", command=design_button_function, font=("Arial", 15),corner_radius=32, border_color="#FFCC70", border_width=1.5)
        design_button.place(relx=0.7, rely=0.7, anchor=tkinter.CENTER)

        wtotal = self.root.winfo_screenwidth()
        htotal = self.root.winfo_screenheight()

        wventana = 400
        hventana = 300

        pwidth = round(wtotal/2 - wventana/2)
        pheight = round(htotal/2 - hventana/2)

        self.root.geometry(str(wventana) + "x" + str(hventana) + "+" + str(pwidth) + "+" + str(pheight))
        self.root.mainloop()


class VentanaSimulacion:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.geometry("900x600")
        self.root.title('Pandora Simulación')
        wtotal = self.root.winfo_screenwidth()
        htotal = self.root.winfo_screenheight()

        wventana = 900
        hventana = 600

        pwidth = round(wtotal / 2 - wventana / 2)
        pheight = round(htotal / 2 - hventana / 2)

        self.root.geometry(str(wventana) + "x" + str(hventana) + "+" + str(pwidth) + "+" + str(pheight))

        self.menu = ctk.CTkFrame(self.root, fg_color="#1F6AA5", width=220)
        self.menu.pack(side=ctk.LEFT, fill='both', expand=False)

        # FRAME PRINCIPAL
        self.principal = ctk.CTkScrollableFrame(self.root, fg_color="#003B4A")
        self.principal.pack(side=ctk.RIGHT, fill='both', expand=True)

        self.label = ctk.CTkLabel(self.menu, text="\nP A N D O R A\n", font=("Arial Black", 20), padx=30)
        self.label.pack(side=ctk.TOP)

        self.instrumento1 = ctk.CTkImage(light_image=Image.open(os.path.join(carpeta_imagenes, "instrumento1.png")),dark_image=Image.open(os.path.join(carpeta_imagenes, "instrumento1.png")), size=(100, 50))

        self.isensor = ctk.CTkImage(light_image=Image.open(os.path.join(carpeta_imagenes, "sensor.png")),dark_image=Image.open(os.path.join(carpeta_imagenes, "sensor.png")), size=(90, 50))

        self.iacondicionador = ctk.CTkImage(light_image=Image.open(os.path.join(carpeta_imagenes, "acondicionador.png")),dark_image=Image.open(os.path.join(carpeta_imagenes, "acondicionador.png")), size=(60, 90))

        self.idiscretizador = ctk.CTkImage(light_image=Image.open(os.path.join(carpeta_imagenes, "discretizador.png")),dark_image=Image.open(os.path.join(carpeta_imagenes, "discretizador.png")), size=(60, 90))

        self.iemulador = ctk.CTkImage(light_image=Image.open(os.path.join(carpeta_imagenes, "imagen1.png")),dark_image=Image.open(os.path.join(carpeta_imagenes, "imagen1.png")), size=(90, 50))
        self.play = ctk.CTkImage(light_image=Image.open(os.path.join(carpeta_imagenes, "play.png")),dark_image=Image.open(os.path.join(carpeta_imagenes, "play.png")), size=(37, 30))

        self.unidad_dict = {}
        self.unidad_dict["Masa"] = ["gr", "Kgr"]
        self.unidad_dict["Presion"] = ["Pa", "hPa", "kPa"]
        self.unidad_dict["Temperatura"] = ["°C", "K", "°F"]
        self.unidad_dict["Iluminancia"] = ["lx"]
        self.unidad_dict["Longitud"] = ["m", "cm"]

        # Configuración frame principal
        self.button_instrumento1 = ctk.CTkButton(self.menu, text="Instrumento", image=self.instrumento1, width=220, command=self.instrumento_config)
        self.button_sensor = ctk.CTkButton(self.menu, text="Sensor", image=self.isensor, width=220)
        self.button_acondicionador = ctk.CTkButton(self.menu, text="Acondicionador", image=self.iacondicionador, width=220)
        self.button_discretizador = ctk.CTkButton(self.menu, text="Discretizador", image=self.idiscretizador, width=220)
        self.button_emulador = ctk.CTkButton(self.menu, text="Emulador", image=self.iemulador, width=220)

        self.button_simular = ctk.CTkButton(self.menu, text="Simular", image=self.play, font=("Arial", 15), corner_radius=32, border_width=1.5)
        self.button_simular.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

        self.button_instrumento1.pack(side=ctk.TOP)
        self.button_sensor.pack(side=ctk.TOP)
        self.button_acondicionador.pack(side=ctk.TOP)
        self.button_discretizador.pack(side=ctk.TOP)
        self.button_emulador.pack(side=ctk.TOP)

        self.root.mainloop()

    def seleccionar_magnitud(self):
        # Limpiar cualquier widget previamente creado
        for widget in self.principal.winfo_children():
            widget.destroy()

        self.label_magnitud = ctk.CTkLabel(self.principal, text="Magnitud", font=("Arial", 15))
        self.label_magnitud.pack(side=ctk.LEFT, padx=20, pady=10)

        # Obtener la magnitud seleccionada
        magnitud_seleccionada = self.magnitud_var.get()

        # Verificar si la magnitud está en el diccionario
        if magnitud_seleccionada in self.unidad_dict:
            unidades = self.unidad_dict[magnitud_seleccionada]

            # Crear ComboBox para las unidades
            self.label_unidad = ctk.CTkLabel(self.principal, text="Unidad", font=("Arial", 15))
            self.label_unidad.pack(side=ctk.LEFT, padx=20, pady=10)

            self.unidad_var = ctk.StringVar(value=unidades[0])  # Seleccionar la primera unidad por defecto
            self.combobox_unidades = ctk.CTkComboBox(self.principal, values=unidades, variable=self.unidad_var)
            self.combobox_unidades.pack(side=ctk.LEFT, padx=20, pady=10)
        else:
            print("Magnitud no encontrada en el diccionario")
   
# Configuración frame principal
    def instrumento_config(self):
        self.label_instrumento = ctk.CTkLabel(self.principal, text="INSTRUMENTO", font=("Arial Black", 20), padx=30)
        self.label_instrumento.pack(side=ctk.TOP, pady=10)

        self.label_magnitud = ctk.CTkLabel(self.principal, text="Magnitud", font=("Arial", 15))
        self.label_magnitud.pack(side=ctk.LEFT, padx=20, pady=10)

        # Combobox for selecting magnitudes
        self.magnitudes = ["Masa", "Presion", "Temperatura", "Iluminancia", "Longitud"]
        self.magnitud_var = ctk.StringVar(value=self.magnitudes[0])
        self.combobox_magnitudes = ctk.CTkComboBox(self.principal, values=self.magnitudes, variable=self.magnitud_var)
        self.combobox_magnitudes.pack(side=ctk.LEFT, padx=20, pady=10)
        
        
        

    # Sección para ingresar rango
        self.label_rango = ctk.CTkLabel(self.principal, text="Rango", font=("Arial", 15))
        self.label_rango.pack(side=ctk.LEFT, padx=20, pady=10)

        self.rango_min_var = ctk.StringVar(value="0")  
        self.entry_rango_min = ctk.CTkEntry(self.principal, textvariable=self.rango_min_var, font=("Arial", 12))
        self.entry_rango_min.pack(side=ctk.LEFT, padx=10, pady=10)

        self.label_to = ctk.CTkLabel(self.principal, text="a", font=("Arial", 15))
        self.label_to.pack(side=ctk.LEFT, padx=5, pady=10)

        self.rango_max_var = ctk.StringVar(value="100")  
        self.entry_rango_max = ctk.CTkEntry(self.principal, textvariable=self.rango_max_var, font=("Arial", 12))
        self.entry_rango_max.pack(side=ctk.LEFT, padx=10, pady=10)

        self.aceptar_button = ctk.CTkButton(self.principal, text="Aceptar", command=self.seleccionar_magnitud)
        self.aceptar_button.pack(side=ctk.RIGHT, padx=20, pady=100)
        
        



    


class VentanaDiseno:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.geometry("900x600")
        self.root.title('Pandora Diseño')
        wtotal = self.root.winfo_screenwidth()
        htotal = self.root.winfo_screenheight()

        wventana = 900
        hventana = 600

        pwidth = round(wtotal / 2 - wventana / 2)
        pheight = round(htotal / 2 - hventana / 2)

        self.root.geometry(str(wventana) + "x" + str(hventana) + "+" + str(pwidth) + "+" + str(pheight))

        self.menu = ctk.CTkFrame(self.root, fg_color="#1F6AA5", width=220)
        self.menu.pack(side=ctk.LEFT, fill='both', expand=False)

        self.label = ctk.CTkLabel(self.menu, text="\nP A N D O R A\n", font=("Arial Black", 20), padx=30)
        self.label.pack(side=ctk.TOP)

        self.instrumento1 = ctk.CTkImage(light_image=Image.open(os.path.join(carpeta_imagenes, "instrumento1.png")),dark_image=Image.open(os.path.join(carpeta_imagenes, "instrumento1.png")), size=(100, 50))

        self.isensor = ctk.CTkImage(light_image=Image.open(os.path.join(carpeta_imagenes, "sensor.png")),dark_image=Image.open(os.path.join(carpeta_imagenes, "sensor.png")), size=(90, 50))

        self.iacondicionador = ctk.CTkImage(light_image=Image.open(os.path.join(carpeta_imagenes, "acondicionador.png")),dark_image=Image.open(os.path.join(carpeta_imagenes, "acondicionador.png")), size=(60, 90))

        self.idiscretizador = ctk.CTkImage(light_image=Image.open(os.path.join(carpeta_imagenes, "discretizador.png")),dark_image=Image.open(os.path.join(carpeta_imagenes, "discretizador.png")), size=(60, 90))

        self.iemulador = ctk.CTkImage(light_image=Image.open(os.path.join(carpeta_imagenes, "imagen1.png")),dark_image=Image.open(os.path.join(carpeta_imagenes, "imagen1.png")), size=(90, 50))
        self.disenar = ctk.CTkImage(light_image=Image.open(os.path.join(carpeta_imagenes, "disenar.png")),
                                    dark_image=Image.open(os.path.join(carpeta_imagenes, "disenar.png")), size=(40, 30))

        self.button_instrumento1 = ctk.CTkButton(self.menu, text="Instrumento", image=self.instrumento1, width=220)
        self.button_sensor = ctk.CTkButton(self.menu, text="Sensor", image=self.isensor, width=220)
        self.button_acondicionador = ctk.CTkButton(self.menu, text="Acondicionador", image=self.iacondicionador, width=220)
        self.button_discretizador = ctk.CTkButton(self.menu, text="Discretizador", image=self.idiscretizador, width=220)
        self.button_emulador = ctk.CTkButton(self.menu, text="Emulador", image=self.iemulador, width=220)

        self.button_disenar = ctk.CTkButton(self.menu, text="Diseñar", image=self.disenar, font=("Arial", 15), corner_radius=32, border_width=1.5)
        self.button_disenar.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

        self.button_instrumento1.pack(side=ctk.TOP)
        self.button_sensor.pack(side=ctk.TOP)
        self.button_acondicionador.pack(side=ctk.TOP)
        self.button_discretizador.pack(side=ctk.TOP)
        self.button_emulador.pack(side=ctk.TOP)
        self.root.mainloop()


