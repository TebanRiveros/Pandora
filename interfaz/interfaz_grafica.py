import tkinter
import os
from PIL import Image, ImageTk
import customtkinter as ctk
from tkinter import messagebox

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
        self.principal = ctk.CTkScrollableFrame(self.root, fg_color="#242424")
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
        
        self.unidad_2 = {}
        self.unidad_2["Voltaje"] = ["mV","v"]
        self.unidad_2["Corriente"] = ["uA", "mA", "A"]
       

        # Configuración frame principal
        self.button_instrumento1 = ctk.CTkButton(self.menu, text="Instrumento", image=self.instrumento1, width=220, command=self.instrumento_config)
        self.button_sensor = ctk.CTkButton(self.menu, text="Sensor", image=self.isensor, width=220, command=self.sensor_config)
        self.button_acondicionador = ctk.CTkButton(self.menu, text="Acondicionador", image=self.iacondicionador, width=220, command=self.acondiconador_config)
        self.button_discretizador = ctk.CTkButton(self.menu, text="Discretizador", image=self.idiscretizador, width=220, command=self.discretizador_config)
        self.button_emulador = ctk.CTkButton(self.menu, text="Emulador", image=self.iemulador, width=220, command=self.emodulador_config)

        self.button_simular = ctk.CTkButton(self.menu, text="Simular", image=self.play, font=("Arial", 15), corner_radius=32, border_width=1.5)
        self.button_simular.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

        self.button_instrumento1.pack(side=ctk.TOP)
        self.button_sensor.pack(side=ctk.TOP)
        self.button_acondicionador.pack(side=ctk.TOP)
        self.button_discretizador.pack(side=ctk.TOP)
        self.button_emulador.pack(side=ctk.TOP)

        self.root.mainloop()

    def seleccionar_magnitud(self,eleccion):
        print('sikas')
        lista_unidades = self.unidad_dict.get(eleccion, [])
        # Ahora unidades_magnitud contendrá las unidades asociadas a la magnitud especificada
        print(lista_unidades)
        self.combobox_unidad.configure(values=lista_unidades)
        
    def seleccionar_mag(self,eleccion):
        print('hola')
        lista_unidad = self.unidad_2.get(eleccion, [])
        # Ahora unidades_magnitud contendrá las unidades asociadas a la magnitud especificada
        print(lista_unidad)
        self.combobox_unidads.configure(values=lista_unidad)
    def seleccionar_maga(self,eleccion):
        print('hola')
        lista_unidada = self.unidad_2.get(eleccion, [])
        # Ahora unidades_magnitud contendrá las unidades asociadas a la magnitud especificada
        print(lista_unidada)
        self.combobox_unidada.configure(values=lista_unidada)


    
   
# Configuración instrumento
    def instrumento_config(self):
        self.limpiarpanel()
        self.label_instrumento = ctk.CTkLabel(self.principal, text="INSTRUMENTO", font=("Arial Black", 20), padx=30)
        self.label_instrumento.grid(row=0, column=0, columnspan=5)

        self.label_magnitud = ctk.CTkLabel(self.principal, text="Magnitud:", font=("Arial", 15),pady=25,padx=10)
        self.label_magnitud.grid(row=6, column=0)

        # Combobox for selecting magnitudes
        self.magnitudes = ["Masa", "Presion", "Temperatura", "Iluminancia", "Longitud"]
        self.magnitud_var = ctk.StringVar(value=self.magnitudes[0])
        self.combobox_magnitudes = ctk.CTkComboBox(self.principal, values=self.magnitudes, command=self.seleccionar_magnitud)
        self.combobox_magnitudes.grid(row=6, column=3)
    # Sección para ingresar rango
        self.label_rango = ctk.CTkLabel(self.principal, text="Rango:", font=("Arial", 15), pady=30)
        self.label_rango.grid(row=16, column=0)

        self.rango_min_var = ctk.StringVar(value="0")  
        self.entry_rango_min = ctk.CTkEntry(self.principal, textvariable=self.rango_min_var, font=("Arial", 12))
        self.entry_rango_min.grid(row=16, column=3)

        self.label_to = ctk.CTkLabel(self.principal, text="a", font=("Arial", 15),padx=10)
        self.label_to.grid(row=16, column=4)

        self.rango_max_var = ctk.StringVar(value="100")  
        self.entry_rango_max = ctk.CTkEntry(self.principal, textvariable=self.rango_max_var, font=("Arial", 12))
        self.entry_rango_max.grid(row=16, column=5)

        self.combobox_unidad = ctk.CTkComboBox(self.principal, values=['unidad'])
        self.combobox_unidad.grid(row=6, column=5)
        
        self.label_iteracion = ctk.CTkLabel(self.principal, text="Saltos:", font=("Arial", 15), pady=30)
        self.label_iteracion.grid(row=17, column=0)
        
        self.iteracion_var = ctk.StringVar(value="0")  
        self.entry_iteracion = ctk.CTkEntry(self.principal, textvariable=self.iteracion_var, font=("Arial", 12))
        self.entry_iteracion.grid(row=17, column=3)
    


    def seleccionar_mag(self, choice):
        print(f"Magnitud seleccionada: {choice}")
        # Actualiza las unidades en función de la magnitud seleccionada
        if choice == "Voltaje":
            self.combobox_unidads.configure(values=["V", "mV"])
        elif choice == "Corriente":
            self.combobox_unidads.configure(values=["A", "mA"])

    def guardar_datos(self):
        magnitud_seleccionada = self.magsensor_var.get()
        unidad_seleccionada = self.combobox_unidads.get()
        self.sensibilidad_sensor = float(self.ss_var.get())
        valor_inicial = self.vis_var.get()
        
        print(f"Magnitud: {magnitud_seleccionada}, Unidad: {unidad_seleccionada}, Sensibilidad: {self.sensibilidad_sensor}, Valor inicial: {valor_inicial}")
        


#Configuracion sensor
    def sensor_config(self):
        self.limpiarpanel()
        self.label_instrumento = ctk.CTkLabel(self.principal, text="SENSOR", font=("Arial Black", 20), padx=30)
        self.label_instrumento.grid(row=0, column=0, columnspan=5)
        
        self.label_magnitudsen = ctk.CTkLabel(self.principal, text="Magnitud de salida:", font=("Arial", 15),pady=25,padx=10)
        self.label_magnitudsen.grid(row=2, column=0)
        
        self.magnisensor = ["Voltaje", "Corriente"]
        self.magsensor_var = ctk.StringVar(value=self.magnisensor[0])
        self.combobox_magnisensor = ctk.CTkComboBox(self.principal, values=self.magnisensor, command=self.seleccionar_mag)
        self.combobox_magnisensor.grid(row=2, column=2)
        
        self.combobox_unidads = ctk.CTkComboBox(self.principal, values=['unidad'])
        self.combobox_unidads.grid(row=2, column=3,padx=10)
        
        self.label_ss = ctk.CTkLabel(self.principal, text="Sensibilidad:", font=("Arial", 15), pady=30)
        self.label_ss.grid(row=3, column=0,pady=5)

        self.ss_var = ctk.StringVar(value="0")  
        self.entry_ss = ctk.CTkEntry(self.principal, textvariable=self.ss_var, font=("Arial", 12))
        self.entry_ss.grid(row=3, column=2)
        
        self.label_vis = ctk.CTkLabel(self.principal, text="Valor inicial:", font=("Arial", 15), pady=30)
        self.label_vis.grid(row=4, column=0,pady=5)

        self.vis_var = ctk.StringVar(value="0")  
        self.entry_vis = ctk.CTkEntry(self.principal, textvariable=self.vis_var, font=("Arial", 12))
        self.entry_vis.grid(row=4, column=2)
        
        self.aceptar2_button = ctk.CTkButton(self.principal, text="Aceptar", command=self.guardar_datos)
        self.aceptar2_button.grid(row=5, column=0, columnspan=3, pady=20)




    def seleccionar_maga(self, choice):
        print(f"Magnitud seleccionada: {choice}")
        # Actualiza las unidades en función de la magnitud seleccionada
        if choice == "Voltaje":
            self.combobox_unidada.configure(values=["V", "mV"])
        elif choice == "Corriente":
            self.combobox_unidada.configure(values=["A", "mA"])

    def guardar3_datos(self):
        self.magnitud_seleccionadac = self.magac_var.get()
        self.unidad_seleccionadac = self.combobox_unidada.get()
        self.sensibilidad_ac = float(self.sa_var.get())
        self.valor_iniciala = self.via_var.get()
        
        print(f"Magnitud: {self.magnitud_seleccionadac}, Unidad: {self.unidad_seleccionadac}, Sensibilidad: {self.sensibilidad_ac}, Valor inicial: {self.valor_iniciala}")
        print(self.sensibilidad_sensor*self.sensibilidad_ac)
        

#Configuracion acondiconador
    def acondiconador_config(self):
        self.limpiarpanel()
        self.label_instrumento = ctk.CTkLabel(self.principal, text="ACONDICIONADOR", font=("Arial Black", 20), padx=30)
        self.label_instrumento.grid(row=0, column=0, columnspan=5)

        self.label_magnitudac = ctk.CTkLabel(self.principal, text="Magnitud de salida:", font=("Arial", 15),pady=25,padx=10)
        self.label_magnitudac.grid(row=2, column=0)
        
        self.magniac = ["Voltaje", "Corriente"]
        self.magac_var = ctk.StringVar(value=self.magniac[0])
        self.combobox_magniac = ctk.CTkComboBox(self.principal, values=self.magniac, command=self.seleccionar_maga)
        self.combobox_magniac.grid(row=2, column=2)
        
        self.combobox_unidada = ctk.CTkComboBox(self.principal, values=['unidad'])
        self.combobox_unidada.grid(row=2, column=3,padx=10)
        
        self.label_sa = ctk.CTkLabel(self.principal, text="Sensibilidad:", font=("Arial", 15), pady=30)
        self.label_sa.grid(row=3, column=0,pady=5)

        self.sa_var = ctk.StringVar(value="0")  
        self.entry_sa = ctk.CTkEntry(self.principal, textvariable=self.sa_var, font=("Arial", 12))
        self.entry_sa.grid(row=3, column=2)
        
        self.label_via = ctk.CTkLabel(self.principal, text="Valor inicial:", font=("Arial", 15), pady=30)
        self.label_via.grid(row=4, column=0,pady=5)

        self.via_var = ctk.StringVar(value="0")  
        self.entry_via = ctk.CTkEntry(self.principal, textvariable=self.via_var, font=("Arial", 12))
        self.entry_via.grid(row=4, column=2)
        
        self.aceptar3_button = ctk.CTkButton(self.principal, text="Aceptar", command=self.guardar3_datos)
        self.aceptar3_button.grid(row=5, column=0, columnspan=3, pady=20)
       
       
    def guardar4_datos(self):
        sensibilidad_di = self.sd_var.get()
        valor_iniciald = self.vid_var.get()
        print(f"Sensibilidad: {sensibilidad_di}, Valor inicial: {valor_iniciald}")
        
    
        
        

    # def toggle_entries(self):
    #     state = ctk.DISABLED if self.entry_sd.cget("state") == ctk.NORMAL else ctk.NORMAL
    #     self.entry_sd.configure(state=state)
    #     self.entry_via.configure(state=state)
    
    def switch_event(self):
        print("switch toggled, current value:", self.habilitador_var.get())
        if (self.habilitador_var.get()=='off'):
            messagebox.showinfo("Discretizador", "Al desabilitar el discretizador el instrumento sera analogico")
            self.entry_sd.configure(state='disabled')
            self.entry_vid.configure(state='disabled')
        else:
            self.entry_sd.configure(state='normal')
            self.entry_vid.configure(state='normal')

#Configuracion discretizador
    def discretizador_config(self):
        self.limpiarpanel()
        self.label_instrumento = ctk.CTkLabel(self.principal, text="DISCRETIZADOR", font=("Arial Black", 20), padx=30)
        self.label_instrumento.grid(row=0, column=0, columnspan=5)

        self.label_sd = ctk.CTkLabel(self.principal, text="Sensibilidad:", font=("Arial", 15), pady=30)
        self.label_sd.grid(row=2, column=0,pady=5)

        self.sd_var = ctk.StringVar(value="0")  
        self.entry_sd = ctk.CTkEntry(self.principal, textvariable=self.sd_var, font=("Arial", 12))
        self.entry_sd.grid(row=2, column=2,padx=5)
        
        self.label_vid = ctk.CTkLabel(self.principal, text="Valor inicial:", font=("Arial", 15), pady=30)
        self.label_vid.grid(row=4, column=0,pady=5)

        self.vid_var = ctk.StringVar(value="0")  
        self.entry_vid = ctk.CTkEntry(self.principal, textvariable=self.vid_var, font=("Arial", 12))
        self.entry_vid.grid(row=4, column=2)
        
        self.habilitador_var = ctk.StringVar(value="on")
        self.habilitador = ctk.CTkSwitch(self.principal, text="Desabilitar el discretizador", command=self.switch_event,variable=self.habilitador_var, onvalue="on", offvalue="off")
        self.habilitador.grid(row=6,column=0)
        #self.toggle_button = ctk.CTkButton(self.principal, text="Habilitar/Deshabilitar", command=self.toggle_entries)
        #self.toggle_button.grid(row=6, column=0, columnspan=3, pady=20)
        
        self.aceptar3_button = ctk.CTkButton(self.principal, text="Aceptar", command=self.guardar4_datos)
        self.aceptar3_button.grid(row=6, column=3, columnspan=3)
        

        
#Configuracion Emodulador
    def emodulador_config(self):
        self.limpiarpanel()
        self.label_instrumento = ctk.CTkLabel(self.principal, text="EMODULADOR", font=("Arial Black", 20), padx=30)
        self.label_instrumento.grid(row=0, column=0, columnspan=5)
       
        
    def limpiarpanel(self):
        for widget in self.principal.winfo_children():
            widget.destroy()


        
        



    


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
