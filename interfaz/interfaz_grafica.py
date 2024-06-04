import tkinter
import os
from PIL import Image, ImageTk
import customtkinter as ctk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import math


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
        self.simulando=False

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
        self.unidad_dict["Masa"] = ["M/gr", "M/Kgr"]
        self.unidad_dict["Presion"] = ["P/Pa", "P/hPa", "P/kPa"]
        self.unidad_dict["Temperatura"] = ["T/°C", "T/K", "T/°F"]
        self.unidad_dict["Iluminancia"] = ["Ev/lx"]
        self.unidad_dict["Longitud"] = ["L/m", "L/cm"]
        
        self.unidad_2 = {}
        self.unidad_2["Voltaje"] = ["V/v","V/mv","V/uv"]
        self.unidad_2["Corriente"] = ["I/uA", "I/mA", "I/A"]

        self.bandera_discretizador=True
       

        # Configuración frame principal
        self.button_instrumento1 = ctk.CTkButton(self.menu, text="Instrumento", image=self.instrumento1, width=220, command=self.instrumento_config)
        self.button_sensor = ctk.CTkButton(self.menu, text="Sensor", image=self.isensor, width=220, command=self.sensor_config)
        self.button_acondicionador = ctk.CTkButton(self.menu, text="Acondicionador", image=self.iacondicionador, width=220, command=self.acondiconador_config)
        self.button_discretizador = ctk.CTkButton(self.menu, text="Discretizador", image=self.idiscretizador, width=220, command=self.discretizador_config)
        self.button_emulador = ctk.CTkButton(self.menu, text="Emulador", image=self.iemulador, width=220, command=self.emodulador_config)

        self.button_simular = ctk.CTkButton(self.menu, text="Simular", image=self.play, font=("Arial", 15), corner_radius=32, border_width=1.5,command=self.simular_config)
        self.button_simular.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

        self.button_instrumento1.pack(side=ctk.TOP)
        self.button_sensor.pack(side=ctk.TOP)
        self.button_acondicionador.pack(side=ctk.TOP)
        self.button_discretizador.pack(side=ctk.TOP)
        self.button_emulador.pack(side=ctk.TOP)

        # Configurar las columnas de la cuadrícula para que se expandan
        for i in range(5):
            self.principal.grid_columnconfigure(i, weight=1)

        self.root.mainloop()

    def seleccionar_magnitud(self,eleccion):
        print('Prueba')
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



    def guardari_datos(self):
        self.magnitud = self.magnitud_var.get()
        self.unidad = self.combobox_unidad.get()
        self.rangoma = self.rango_max_var.get()
        self.rangomi = self.rango_min_var.get()
        self.salto = self.iteracion_var.get()
        
        
   
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
        
        self.label_iteracion = ctk.CTkLabel(self.principal, text="Puntos:", font=("Arial", 15), pady=30)
        self.label_iteracion.grid(row=17, column=0)
        
        self.iteracion_var = ctk.StringVar(value="0")  
        self.entry_iteracion = ctk.CTkEntry(self.principal, textvariable=self.iteracion_var, font=("Arial", 12))
        self.entry_iteracion.grid(row=17, column=3)
        
        self.aceptar_button = ctk.CTkButton(self.principal, text="Aceptar", command=self.guardari_datos)
        self.aceptar_button.grid(row=18, column=3, columnspan=3, pady=20)

        if(self.simulando==True):
            
            
            

            # Crear una figura de Matplotlib
            fig_instrumento = Figure(figsize=(8, 4), dpi=100)
            plt_instrumento = fig_instrumento.add_subplot(111)
            plt_instrumento.grid(True)

            plt_instrumento.plot(self.mesurando, self.emulador, marker='o', linestyle='')
            
            plt_instrumento.set_xlabel(f'Mesurando:{self.unidad}')
            plt_instrumento.set_ylabel(f'Función Compuesta: bD/CTAS')
            
            self.prueba = ctk.CTkLabel(self.principal, text=self.ecu_instumento, font=("Arial", 15), pady=30)
            self.prueba.grid(row=22, column=3)
            

            # # Crear un canvas para la figura de Matplotlib y agregarlo a la ventana de customtkinter
            canvas = FigureCanvasTkAgg(fig_instrumento, master=self.principal)
            canvas.draw()
            canvas.get_tk_widget().grid(row=19, column=0, columnspan=5, padx=10, sticky="nsew")

            # # Crear la barra de herramientas de navegación de Matplotlib y agregarla a la ventana de customtkinter
            toolbar_frame = ctk.CTkFrame(self.principal)
            toolbar_frame.grid(row=20, column=0, columnspan=5, padx=10, sticky="ew")
            toolbar = NavigationToolbar2Tk(canvas, toolbar_frame)
            toolbar.update()
    


    def seleccionar_mag(self, choice):
        print(f"Magnitud seleccionada: {choice}")
        # Actualiza las unidades en función de la magnitud seleccionada
        if choice == "Voltaje":
            self.combobox_unidads.configure(values=["Vs/V", "Vs/mV"])
        elif choice == "Corriente":
            self.combobox_unidads.configure(values=["Is/A", "Is/mA","Is/uA"])

    def guardar_datos(self):
        self.magnitud_seleccionada = self.magsensor_var.get()
        self.unidad_seleccionada = self.combobox_unidads.get()
        self.sensibilidad_sensor = self.ss_var.get()
        self.valor_inicial = self.vis_var.get()
        
    

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



        if(self.simulando==True):
            self.label_ecuacion_sensor = ctk.CTkLabel(self.principal, text=self.ecu_sensor, font=("Arial", 15), pady=30)
            self.label_ecuacion_sensor.grid(row=6, column=0, columnspan=5)

            # Crear una figura de Matplotlib
            fig_sensor = Figure(figsize=(5, 4), dpi=100)
            plt_sensor = fig_sensor.add_subplot(111)
            plt_sensor.grid(True)
       
            
            plt_sensor.plot(self.mesurando, self.sensor, marker='o', linestyle='-')
           
            plt_sensor.set_xlabel(f'Mesurando:{self.unidad}')
            plt_sensor.set_ylabel(f'Sensor: {self.unidad_seleccionada}')
       

            # Crear un canvas para la figura de Matplotlib y agregarlo a la ventana de customtkinter
            canvas = FigureCanvasTkAgg(fig_sensor, master=self.principal)
            canvas.draw()
            canvas.get_tk_widget().grid(row=7, column=0, columnspan=5, padx=10, sticky="nsew")

            # Crear la barra de herramientas de navegación de Matplotlib y agregarla a la ventana de customtkinter
            toolbar_frame = ctk.CTkFrame(self.principal)
            toolbar_frame.grid(row=8, column=0, columnspan=5, padx=10, sticky="ew")
            toolbar = NavigationToolbar2Tk(canvas, toolbar_frame)
            toolbar.update()

            




    def seleccionar_maga(self, choice):
        print(f"Magnitud seleccionada: {choice}")
        # Actualiza las unidades en función de la magnitud seleccionada
        if choice == "Voltaje":
            self.combobox_unidada.configure(values=["Va/V", "Va/mV"])
        elif choice == "Corriente":
            self.combobox_unidada.configure(values=["Ia/A", "Ia/mA","Ia/uA"])

    def guardar3_datos(self):
        self.magnitud_seleccionadac = self.magac_var.get()
        self.unidad_seleccionadac = self.combobox_unidada.get()
        self.sensibilidad_ac = self.sa_var.get()
        self.valor_iniciala = self.via_var.get()
        
        print(f"Magnitud: {self.magnitud_seleccionadac}, Unidad: {self.unidad_seleccionadac}, Sensibilidad: {self.sensibilidad_ac}, Valor inicial: {self.valor_iniciala}")
        
        

#Configuracion acondiconador
    def acondiconador_config(self):
        self.limpiarpanel()
        self.label_instrumento = ctk.CTkLabel(self.principal, text="ACONDICIONADOR", font=("Arial Black", 20), padx=30)
        self.label_instrumento.grid(row=0, column=0, columnspan=5)

        self.label_magnitudac = ctk.CTkLabel(self.principal, text="Magnitud de salida:", font=("Arial", 15), pady=25, padx=10)
        self.label_magnitudac.grid(row=2, column=0)
        
        self.magniac = ["Voltaje", "Corriente"]
        self.magac_var = ctk.StringVar(value=self.magniac[0])
        self.combobox_magniac = ctk.CTkComboBox(self.principal, values=self.magniac, command=self.seleccionar_maga)
        self.combobox_magniac.grid(row=2, column=2)
        
        self.combobox_unidada = ctk.CTkComboBox(self.principal, values=['unidad'])
        self.combobox_unidada.grid(row=2, column=3, padx=10)
        
        self.label_sa = ctk.CTkLabel(self.principal, text="Sensibilidad:", font=("Arial", 15), pady=30)
        self.label_sa.grid(row=3, column=0, pady=5)

        self.sa_var = ctk.StringVar(value="0")  
        self.entry_sa = ctk.CTkEntry(self.principal, textvariable=self.sa_var, font=("Arial", 12))
        self.entry_sa.grid(row=3, column=2)
        
        self.label_via = ctk.CTkLabel(self.principal, text="Valor inicial:", font=("Arial", 15), pady=30)
        self.label_via.grid(row=4, column=0, pady=5)

        self.via_var = ctk.StringVar(value="0")  
        self.entry_via = ctk.CTkEntry(self.principal, textvariable=self.via_var, font=("Arial", 12))
        self.entry_via.grid(row=4, column=2)
        
        self.aceptar3_button = ctk.CTkButton(self.principal, text="Aceptar", command=self.guardar3_datos)
        self.aceptar3_button.grid(row=5, column=0, columnspan=3, pady=20)

        if self.simulando:
            self.label_ecuacion_acondiconador = ctk.CTkLabel(self.principal, text=self.ecu_acondicionador, font=("Arial", 15), pady=30)
            self.label_ecuacion_acondiconador.grid(row=6, column=0, columnspan=5)
            
            # Crear una figura de Matplotlib
            fig_acondicionador = Figure(figsize=(5, 4), dpi=100)
            plt_acondicionador = fig_acondicionador.add_subplot(111)
            
            plt_acondicionador.grid(True)
        
            plt_acondicionador.plot(self.sensor, self.acondicionador, marker='o', linestyle='-')
            
            # Agregar nombres a los ejes
            plt_acondicionador.set_xlabel(f'Sensor:{self.unidad_seleccionada}')
            plt_acondicionador.set_ylabel(f'Acondicionador: {self.unidad_seleccionadac}')

            # Crear un canvas para la figura de Matplotlib y agregarlo a la ventana de customtkinter
            canvas = FigureCanvasTkAgg(fig_acondicionador, master=self.principal)
            canvas.draw()
            canvas.get_tk_widget().grid(row=7, column=0, columnspan=5, padx=10, sticky="nsew")

            # Crear la barra de herramientas de navegación de Matplotlib y agregarla a la ventana de customtkinter
            toolbar_frame = ctk.CTkFrame(self.principal)
            toolbar_frame.grid(row=8, column=0, columnspan=5, padx=10, sticky="ew")
            toolbar = NavigationToolbar2Tk(canvas, toolbar_frame)
            toolbar.update()

       
       
    def guardar4_datos(self):
        self.sensibilidad_di = self.sd_var.get()
        self.valor_iniciald = self.vid_var.get()
        print(f"Sensibilidad: {self.sensibilidad_di}, Valor inicial: {self.valor_iniciald}")
        
        
    
    def switch_event(self):
        print("switch toggled, current value:", self.habilitador_var.get())
        if (self.habilitador_var.get()=='off'):
            messagebox.showinfo("Discretizador", "Al desabilitar el discretizador el instrumento sera analogico")
            self.entry_sd.configure(state='disabled')
            self.entry_vid.configure(state='disabled')
            self.bandera_discretizador=False
            
        else:
            self.entry_sd.configure(state='normal')
            self.entry_vid.configure(state='normal')
            self.bandera_discretizador=True
            
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
   
        
        self.aceptar3_button = ctk.CTkButton(self.principal, text="Aceptar", command=self.guardar4_datos)
        self.aceptar3_button.grid(row=6, column=3, columnspan=3)


        if(self.simulando==True and self.bandera_discretizador==True):
            self.label_ecuacion_discretizador = ctk.CTkLabel(self.principal, text=self.ecu_discretizador, font=("Arial", 15), pady=30)
            self.label_ecuacion_discretizador.grid(row=7, column=0, columnspan=5)

            # Crear una figura de Matplotlib
            fig_discretizador = Figure(figsize=(5, 4), dpi=100)
            plt_discretizador = fig_discretizador.add_subplot(111)
            plt_discretizador.grid(True)

            plt_discretizador.plot(self.acondicionador, self.discretizador_int, marker='o', linestyle='')

            plt_discretizador.set_xlabel(f'Acondicionador: {self.unidad_seleccionadac}')
            plt_discretizador.set_ylabel(f'Discretizador: Bd/CTAS')

            # # Crear un canvas para la figura de Matplotlib y agregarlo a la ventana de customtkinter
            canvas = FigureCanvasTkAgg(fig_discretizador, master=self.principal)
            canvas.draw()
            canvas.get_tk_widget().grid(row=8, column=0, columnspan=5, padx=10, sticky="nsew")

            # # Crear la barra de herramientas de navegación de Matplotlib y agregarla a la ventana de customtkinter
            toolbar_frame = ctk.CTkFrame(self.principal)
            toolbar_frame.grid(row=9, column=0, columnspan=5, padx=10, sticky="ew")
            toolbar = NavigationToolbar2Tk(canvas, toolbar_frame)
            toolbar.update()
        
   
        
        
        
#Configuracion Emulador
    def emodulador_config(self):
        self.limpiarpanel()
        self.label_instrumento = ctk.CTkLabel(self.principal, text="EMULADOR", font=("Arial Black", 20), padx=30)
        self.label_instrumento.grid(row=0, column=0, columnspan=5)


        if(self.simulando==True):
            self.label_ecuacion_emulador = ctk.CTkLabel(self.principal, text=self.ecu_emulador, font=("Arial", 15), pady=30)
            self.label_ecuacion_emulador.grid(row=1, column=0, columnspan=5)

            


            # Crear una figura de Matplotlib
            fig_emulador = Figure(figsize=(5, 4), dpi=100)
            plt_emulador = fig_emulador.add_subplot(111)
            plt_emulador.grid(True)
            if self.bandera_discretizador == True:
                plt_emulador.plot(self.discretizador_int, self.emulador, marker='o', linestyle='')
                plt_emulador.set_xlabel(f'Discretizador: Bd/CTAS')
                plt_emulador.set_ylabel(f'Emulador: {self.unidad}')
            else:
                plt_emulador.plot(self.acondicionador, self.emulador, marker='o', linestyle='')
                plt_emulador.set_xlabel(f'Acondicionador: {self.unidad_seleccionadac}')
                plt_emulador.set_ylabel(f'Emulador: {self.unidad}')

            



            # # Crear un canvas para la figura de Matplotlib y agregarlo a la ventana de customtkinter
            canvas = FigureCanvasTkAgg(fig_emulador, master=self.principal)
            canvas.draw()
            canvas.get_tk_widget().grid(row=2, column=0, columnspan=5, padx=10, sticky="nsew")

            # # Crear la barra de herramientas de navegación de Matplotlib y agregarla a la ventana de customtkinter
            toolbar_frame = ctk.CTkFrame(self.principal)
            toolbar_frame.grid(row=3, column=0, columnspan=5, padx=10, sticky="ew")
            toolbar = NavigationToolbar2Tk(canvas, toolbar_frame)
            toolbar.update()
        
        
    
    
    #Configuracion Simulador

    def simular_config(self):
        self.simulando=True
        
        # # # Obtener los valores mínimo y máximo del rango
        self.ri = float(self.rangomi)
        self.rf = float(self.rangoma)
        self.salto = int(self.salto)
        self.sensibilidadgono = float(self.sensibilidad_sensor)
        self.inicialgono = float(self.valor_inicial)
        self.sensibilidad_dis = float(self.sensibilidad_di)
        #sensor
        if self.inicialgono > 0:
            self.ecu_sen = '+' + str(self.inicialgono)
        else:
            self.ecu_sen = str(self.inicialgono)
            
            
        self.ecu_sensor = self.unidad_seleccionada+' = '+self.sensibilidad_sensor+' '+self.unidad+self.ecu_sen
        # # # Generación de prueba
        self.mesurando = np.linspace(self.ri, self.rf, num=self.salto)
        self.sensor = (self.mesurando * self.sensibilidadgono) + self.inicialgono
        
      



        self.sensibilidad_acgono = float(self.sensibilidad_ac)
        self.valor_inicial_acgono = float(self.valor_iniciala)
        print(self.sensibilidad_acgono)
        print(self.valor_inicial_acgono)
        self.acondicionador = (self.sensor * self.sensibilidad_acgono) + self.valor_inicial_acgono
        self.instru = (self.sensibilidadgono * self.sensibilidad_acgono * self.sensibilidad_dis)
        self.instru2 = (((self.sensibilidad_acgono * self.inicialgono) + self.valor_inicial_acgono) * self.sensibilidad_dis) + 0.5
        
        
        if self.valor_inicial_acgono > 0:
            self.ecu_acon = '+' + str(self.valor_inicial_acgono)
        else:
            self.ecu_acon = str(self.valor_inicial_acgono)
        
        self.ecu_acondicionador = self.unidad_seleccionadac+' = '+self.sensibilidad_ac+ self.unidad_seleccionada +self.ecu_acon
        
        self.ecu_ins = str(self.instru)
        
        
        
        if self.instru2 > 0:
            self.ecu_ins2 = '+' + str(self.instru2)
        else:
            self.ecu_ins2 = str(self.instru2)
    

        self.ecu_instumento = 'BDAS =' +self.ecu_ins+self.unidad+''+self.ecu_ins2

                
        if self.bandera_discretizador==True:
            self.ecu_discretizador = 'BDAS/CTAS = '+self.sensibilidad_di+self.unidad_seleccionadac+ '+ 0.5'
            self.sensibilidad_digono = float(self.sensibilidad_di)
        
            self.discretizador = (self.acondicionador * self.sensibilidad_digono) + 0.5
        
            # # Convertir los valores de discretizador a enteros
            self.discretizador_int = self.discretizador.astype(int)

            self.sensibilidad_emulador = 1/(self.sensibilidadgono*self.sensibilidad_acgono*self.sensibilidad_digono)
            self.valor_inicial_em = (((((self.inicialgono*self.sensibilidad_acgono)+self.valor_inicial_acgono)*self.sensibilidad_digono)+0.5)/(self.sensibilidadgono*self.sensibilidad_acgono*self.sensibilidad_digono))*(-1)
            print('Aqui vamos')
            print(self.sensibilidad_emulador)
            print(self.valor_inicial_em)
            self.ecu_emulador=str(self.sensibilidad_emulador)+' * (bD/CTAS) + '+str(self.valor_inicial_em)
            self.emulador=(self.discretizador_int*self.sensibilidad_emulador)+self.valor_inicial_em
        else:
            pass
            self.sensibilidad_emulador = 1/(self.sensibilidadgono*self.sensibilidad_acgono)
            self.valor_inicial_em = ((((self.inicialgono*self.sensibilidad_acgono)+self.valor_inicial_acgono))/(self.sensibilidadgono*self.sensibilidad_acgono))*(-1)
            print('Aqui vamos')
            print(self.sensibilidad_emulador)
            print(self.valor_inicial_em)
            self.ecu_emulador=str(self.sensibilidad_emulador)+' * (volataje) + '+str(self.valor_inicial_em)
            self.emulador=(self.acondicionador*self.sensibilidad_emulador)+self.valor_inicial_em



       
        
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
        self.disenando=False
        
        # Frame Principal
        self.principal = ctk.CTkScrollableFrame(self.root, fg_color="#242424")
        self.principal.pack(side=ctk.RIGHT, fill='both', expand=True)
        self.label = ctk.CTkLabel(self.menu, text="\nP A N D O R A\n", font=("Arial Black", 20), padx=30)
        self.label.pack(side=ctk.TOP)
        
        self.instrumento1 = ctk.CTkImage(light_image=Image.open(os.path.join(carpeta_imagenes, "instrumento1.png")),dark_image=Image.open(os.path.join(carpeta_imagenes, "instrumento1.png")), size=(100, 50))

        self.isensor = ctk.CTkImage(light_image=Image.open(os.path.join(carpeta_imagenes, "sensor.png")),dark_image=Image.open(os.path.join(carpeta_imagenes, "sensor.png")), size=(90, 50))

        self.iacondicionador = ctk.CTkImage(light_image=Image.open(os.path.join(carpeta_imagenes, "acondicionador.png")),dark_image=Image.open(os.path.join(carpeta_imagenes, "acondicionador.png")), size=(60, 90))

        self.idiscretizador = ctk.CTkImage(light_image=Image.open(os.path.join(carpeta_imagenes, "discretizador.png")),dark_image=Image.open(os.path.join(carpeta_imagenes, "discretizador.png")), size=(60, 90))

        self.iemulador = ctk.CTkImage(light_image=Image.open(os.path.join(carpeta_imagenes, "imagen1.png")),dark_image=Image.open(os.path.join(carpeta_imagenes, "imagen1.png")), size=(90, 50))
        self.disenar = ctk.CTkImage(light_image=Image.open(os.path.join(carpeta_imagenes, "disenar.png")),dark_image=Image.open(os.path.join(carpeta_imagenes, "disenar.png")), size=(40, 30))

        self.unidad_dict = {}
        self.unidad_dict["Masa"] = ["M/gr", "M/Kgr"]
        self.unidad_dict["Presion"] = ["P/Pa", "P/hPa", "P/kPa"]
        self.unidad_dict["Temperatura"] = ["T/°C", "T/K", "T/°F"]
        self.unidad_dict["Iluminancia"] = ["Ev/lx"]
        self.unidad_dict["Longitud"] = ["L/m", "L/cm"]
        
        self.unidad_2 = {}
        self.unidad_2["Voltaje"] = ["V/v","V/mv","V/uv"]
        self.unidad_2["Corriente"] = ["I/uA", "I/mA", "I/A"]
        
        self.bandera_discretizador=True
        
        #Configuración de los botones
        self.button_instrumento1 = ctk.CTkButton(self.menu, text="Instrumento", image=self.instrumento1, width=220, command=self.instrumento_config)
        self.button_sensor = ctk.CTkButton(self.menu, text="Sensor", image=self.isensor, width=220,command=self.sensor_config)
        self.button_acondicionador = ctk.CTkButton(self.menu, text="Acondicionador", image=self.iacondicionador, width=220,command=self.acondiconador_config)
        self.button_discretizador = ctk.CTkButton(self.menu, text="Discretizador", image=self.idiscretizador, width=220,command=self.discretizador_config)
        self.button_emulador = ctk.CTkButton(self.menu, text="Emulador", image=self.iemulador, width=220,command=self.emodulador_config)

        self.button_disenar = ctk.CTkButton(self.menu, text="Diseñar", image=self.disenar, font=("Arial", 15), corner_radius=32, border_width=1.5,command=self.disenar_config)
        self.button_disenar.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)
        self.button_instrumento1.pack(side=ctk.TOP)
        self.button_sensor.pack(side=ctk.TOP)
        self.button_acondicionador.pack(side=ctk.TOP)
        self.button_discretizador.pack(side=ctk.TOP)
        self.button_emulador.pack(side=ctk.TOP)
        for i in range(5):
            self.principal.grid_columnconfigure(i, weight=1)

        self.root.mainloop()
        
    def seleccionar_magnitud(self,eleccion):
        print('PRUEBA')
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
        
    def guardari_datos(self):
        self.magnitud = self.magnitud_var.get()
        self.unidad = self.combobox_unidad.get()
        self.rangoma = self.rango_max_var.get()
        self.rangomi = self.rango_min_var.get()
        self.resolucion = self.iteracion_var.get()
        self.alcance = self.alcance_var.get()
        self.n = self.codigo_var.get()
        self.vref = self.ref_var.get()
        self.vie = self.vie_var.get()
        
#Configuración de instrumento
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

        self.rango_max_var = ctk.StringVar(value="0")  
        self.entry_rango_max = ctk.CTkEntry(self.principal, textvariable=self.rango_max_var, font=("Arial", 12))
        self.entry_rango_max.grid(row=16, column=5)

        self.combobox_unidad = ctk.CTkComboBox(self.principal, values=['unidad'])
        self.combobox_unidad.grid(row=6, column=5) 
        
        self.label_iteracion = ctk.CTkLabel(self.principal, text="Resolución:", font=("Arial", 15), pady=30)
        self.label_iteracion.grid(row=17, column=0)
        
        self.iteracion_var = ctk.StringVar(value="0")  
        self.entry_iteracion = ctk.CTkEntry(self.principal, textvariable=self.iteracion_var, font=("Arial", 12))
        self.entry_iteracion.grid(row=17, column=3)
        
        self.label_alcance = ctk.CTkLabel(self.principal, text="Alcance:", font=("Arial", 15), pady=30)
        self.label_alcance.grid(row=18, column=0)
        
        self.alcance_var = ctk.StringVar(value="0")  
        self.entry_alcance = ctk.CTkEntry(self.principal, textvariable=self.alcance_var, font=("Arial", 12))
        self.entry_alcance.grid(row=18, column=3)
        
        self.label_codigo = ctk.CTkLabel(self.principal, text="n:", font=("Arial", 15), pady=30)
        self.label_codigo.grid(row=17, column=4)
        
        self.codigo_var = ctk.StringVar(value="0")  
        self.entry_codigo = ctk.CTkEntry(self.principal, textvariable=self.codigo_var, font=("Arial", 12))
        self.entry_codigo.grid(row=17, column=5)
        
        self.label_ref = ctk.CTkLabel(self.principal, text="Vref:", font=("Arial", 15), pady=30)
        self.label_ref.grid(row=18, column=4)
        
        self.ref_var = ctk.StringVar(value="0")  
        self.entry_ref = ctk.CTkEntry(self.principal, textvariable=self.ref_var, font=("Arial", 12))
        self.entry_ref.grid(row=18, column=5)
        
        self.label_vie = ctk.CTkLabel(self.principal, text="V(0) Emulador:", font=("Arial", 15), pady=30)
        self.label_vie.grid(row=19, column=0)
        
        self.vie_var = ctk.StringVar(value="0")  
        self.vie_ref = ctk.CTkEntry(self.principal, textvariable=self.vie_var, font=("Arial", 12))
        self.vie_ref.grid(row=19, column=3)
        
        self.aceptar_button = ctk.CTkButton(self.principal, text="Aceptar", command=self.guardari_datos)
        self.aceptar_button.grid(row=19, column=5, columnspan=3, pady=20)
        
        
        if(self.disenando==True):
            self.p = ctk.CTkLabel(self.principal, text="Resultados:", font=("Arial", 20), pady=30)
            self.p.grid(row=22, column=0)
            self.prueba = ctk.CTkLabel(self.principal, text=self.resrango, font=("Arial", 15), pady=30)
            self.prueba.grid(row=23, column=0)
            self.prueba1 = ctk.CTkLabel(self.principal, text=self.resresolucion, font=("Arial", 15), pady=30)
            self.prueba1.grid(row=24, column=0)
            self.prueba2 = ctk.CTkLabel(self.principal, text=self.rescodigo, font=("Arial", 15), pady=30)
            self.prueba2.grid(row=23, column=3)
            self.prueba3 = ctk.CTkLabel(self.principal, text=self.resalcance, font=("Arial", 15), pady=30)
            self.prueba3.grid(row=24, column=3)
            self.prueba4 = ctk.CTkLabel(self.principal, text=self.resvref, font=("Arial", 15), pady=30)
            self.prueba4.grid(row=25, column=0)
            


    def seleccionar_mag(self, choice):
        print(f"Magnitud seleccionada: {choice}")
        # Actualiza las unidades en función de la magnitud seleccionada
        if choice == "Voltaje":
            self.combobox_unidads.configure(values=["Vs/V", "Vs/mV"])
        elif choice == "Corriente":
            self.combobox_unidads.configure(values=["Is/A", "Is/mA","Is/uA"])

    def guardar_datos(self):
        self.magnitud_seleccionada = self.magsensor_var.get()
        self.unidad_seleccionada = self.combobox_unidads.get()
        self.sensibilidad_sensor = self.ss_var.get()
        self.valor_inicial = self.vis_var.get()
        
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
        self.aceptar2_button.grid(row=4, column=3, pady=20)



        if(self.disenando==True):
            if(self.sensibilidad_sensor == 0):
                self.label_ecuacion_sensor = ctk.CTkLabel(self.principal, text="Error por favor proporcione valores a la sensibilidad del sensor.", font=("Arial", 15), pady=30)
                self.label_ecuacion_sensor.grid(row=6, column=0, columnspan=5)
            else:
                self.label1 = ctk.CTkLabel(self.principal, text="Resultado: ", font=("Arial", 15), pady=30)
                self.label1.grid(row=6, column=0)
                self.label_ecuacion_sensor = ctk.CTkLabel(self.principal, text=self.ecu_sensor, font=("Arial", 15), pady=30)
                self.label_ecuacion_sensor.grid(row=7, column=0, columnspan=5)



    def seleccionar_maga(self, choice):
        print(f"Magnitud seleccionada: {choice}")
        # Actualiza las unidades en función de la magnitud seleccionada
        if choice == "Voltaje":
            self.combobox_unidada.configure(values=["Va/V", "Va/mV"])
        elif choice == "Corriente":
            self.combobox_unidada.configure(values=["Ia/A", "Ia/mA","Ia/uA"])

    def guardar3_datos(self):
        self.magnitud_seleccionadac = self.magac_var.get()
        self.unidad_seleccionadac = self.combobox_unidada.get()
        
        
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
         
        self.aceptar3_button = ctk.CTkButton(self.principal, text="Aceptar", command=self.guardar3_datos)
        self.aceptar3_button.grid(row=5, column=2, pady=20)



        if(self.disenando==True):
            self.label2 = ctk.CTkLabel(self.principal, text="Resultado: ", font=("Arial", 15), pady=30)
            self.label2.grid(row=6, column=0)
            self.label_ecuacion_acondiconador = ctk.CTkLabel(self.principal, text=self.ressa, font=("Arial", 15), pady=30)
            self.label_ecuacion_acondiconador.grid(row=7, column=0, columnspan=5)

    def switch_event(self):
        print("switch toggled, current value:", self.habilitador_var.get())
        if (self.habilitador_var.get()=='off'):
            messagebox.showinfo("Discretizador", "Al desabilitar el discretizador el instrumento sera analogico")
            self.entry_sd.configure(state='disabled')
            self.entry_vid.configure(state='disabled')
            self.bandera_discretizador=False
            
        else:
            self.entry_sd.configure(state='normal')
            self.entry_vid.configure(state='normal')
            self.bandera_discretizador=True
            
#Configuracion discretizador
    def discretizador_config(self):
        self.limpiarpanel()
        self.label_instrumento = ctk.CTkLabel(self.principal, text="DISCRETIZADOR", font=("Arial Black", 20), padx=30)
        self.label_instrumento.grid(row=0, column=0, columnspan=5)

        
        
        self.habilitador_var = ctk.StringVar(value="on")
        self.habilitador = ctk.CTkSwitch(self.principal, text="Desabilitar el discretizador", command=self.switch_event,variable=self.habilitador_var, onvalue="on", offvalue="off")
        self.habilitador.grid(row=6,column=0)


        if(self.disenando==True and self.bandera_discretizador==True):
            self.label3 = ctk.CTkLabel(self.principal, text="Resultado: ", font=("Arial", 15), pady=30)
            self.label3.grid(row=7, column=0)
            self.label_ecuacion_discretizador = ctk.CTkLabel(self.principal, text=self.ressd, font=("Arial", 15), pady=30)
            self.label_ecuacion_discretizador.grid(row=8, column=0, columnspan=5)

#Configuracion Emulador
    def emodulador_config(self):
        self.limpiarpanel()
        self.label_instrumento = ctk.CTkLabel(self.principal, text="EMULADOR", font=("Arial Black", 20), padx=30)
        self.label_instrumento.grid(row=0, column=0, columnspan=5)
        
        if(self.disenando==True):
            self.label4 = ctk.CTkLabel(self.principal, text="Resultado: ", font=("Arial", 15), pady=30)
            self.label4.grid(row=1, column=0)
            self.label_ecuacion_emulador = ctk.CTkLabel(self.principal, text=self.resemulador, font=("Arial", 15), pady=30)
            self.label_ecuacion_emulador.grid(row=2, column=0, columnspan=5)

#Configuracion Diseñar

    def disenar_config(self):
        try:
            

            self.disenando=True
        
            # # # Obtener los valores mínimo y máximo del rango
            self.ri = float(self.rangomi)
            self.rf = float(self.rangoma)
            self.resolucion1 = float(self.resolucion)
            self.alcance1 = float(self.alcance)
            self.n1 = float(self.n)
            self.vref1 = float(self.vref)
            self.sensibilidadgono = float(self.sensibilidad_sensor)
            self.inicialgono = float(self.valor_inicial)
            self.vie1 = float(self.vie)
        
            
            
            
            
            #sensor
            
            if self.inicialgono > 0:
                self.ecu_sen = '+' + str(self.inicialgono)
            else:
                self.ecu_sen = str(self.inicialgono)
                
            self.ecu_sensor = self.unidad_seleccionada+ ' = '+self.sensibilidad_sensor+' '+self.unidad+self.ecu_sen
            
            
            #Caso 1
            #En este caso tienen que dar: sensor, rango, resolucion y vref
            
            if(self.rf != 0 and self.resolucion1 != 0 and self.vref1 != 0 and self.vie1 == 0):
                #Ecuacion 1
                self.log_2 = math.log2(((1/self.resolucion1)*(self.rf - self.ri)) + 1)
                self.nresul = round(self.log_2)
                #Ecuacion 2
                self.sd = (2**self.nresul)/self.vref1
                #Ecuacion 3
                self.sa = 1/(self.resolucion1 * self.sensibilidadgono * self.sd)
                #Ecuacion 4
                self.inicial_ac = -(0.5/self.sd) - (self.sa * ((self.sensibilidadgono * self.ri) + self.inicialgono))
                #Ecuacion 5
                self.alcanceres = (self.rf - self.ri)
                #Ecuacion Valor inicial emulador según libro
                self.resvie1 = (-(self.sd * self.sa * self.inicialgono)-(self.sd * self.inicial_ac) - 0.5)/(self.sd * self.sa * self.sensibilidadgono)
                
                self.resrango = 'Rango:'+str(self.rf)+' a '+str(self.ri)
                self.resresolucion = 'Resolución:' +self.resolucion
                self.rescodigo = 'Código CAD:' +str(self.nresul)
                self.resalcance = 'Alcance:' +str(self.alcanceres)
                self.resvref = 'Vref:' +self.vref
                self.ressd =  'BDAS/CTAS = ' +str(self.sd)+self.unidad_seleccionadac+ ' + 0.5' 
                if self.inicial_ac > 0:
                    self.ecu_acon = '+' + str(self.inicial_ac)
                else:
                    self.ecu_acon = str(self.inicial_ac)
            
                self.ressa = self.unidad_seleccionadac+' = '+str(self.sa)+self.unidad_seleccionada+self.ecu_acon
                if self.resvie1 > 0:
                    self.ecu_vie = '+' + str(self.resvie1)
                else:
                    self.ecu_vie = str(self.resvie1)
                
                self.resemulador = self.unidad+' = '+self.resolucion+'BDAS/CTAS'+self.ecu_vie
                
            elif(self.rf != 0 and self.n1 != 0 and self.vref1 != 0 and self.vie1 == 0):
                #Caso 2
                #En este caso tienen que dar: sensor, rango, n y vref
                #se coge ecuación 2
                self.sd = (2**self.nresul)/self.vref1
                #Ecuación 6
                self.sa2 = ((2**self.n1)-1)/(self.sd * self.sensibilidadgono * (self.rf - self.ri))
                #Ecuación 7
                self.resolucion2 = 1/(self.sd * self.sa2 * self.sensibilidadgono)
                #Se coge ecuación 4 para el valor inicial del acondicionador
                self.inicial_ac = -(0.5/self.sd) - (self.sa2 * ((self.sensibilidadgono * self.ri) + self.inicialgono))
                #Ecuacion 5
                self.alcanceres = (self.rf - self.ri)
                #Ecuacion Valor inicial emulador según libro
                self.resvie1 = (-(self.sd * self.sa2 * self.inicialgono)-(self.sd * self.inicial_ac) - 0.5)/(self.sd * self.sa * self.sensibilidadgono)
                
                self.resrango = 'Rango: '+self.rangoma+' a '+self.rangomi
                self.resresolucion = 'Resolución:' +str(self.resolucion2)
                self.rescodigo = 'Código CAD:' +self.n
                self.resalcance = 'Alcance:' +str(self.alcanceres)
                self.resvref = 'Vref:' +self.vref
                self.ressd =  'BDAS/CTAS = ' +str(self.sd)+self.unidad_seleccionadac+ ' + 0.5' 
                if self.inicial_ac > 0:
                    self.ecu_acon = '+' + str(self.inicial_ac)
                else:
                    self.ecu_acon = str(self.inicial_ac)
            
                self.ressa = self.unidad_seleccionadac+' = '+str(self.sa)+self.unidad_seleccionada+self.ecu_acon
                if self.resvie1 > 0:
                    self.ecu_vie = '+' + str(self.resvie1)
                else:
                    self.ecu_vie = str(self.resvie1)
                
                self.resemulador = self.unidad+' = '+str(self.resolucion2)+'BDAS/CTAS'+self.ecu_vie
            elif(self.alcance1 != 0 and self.resolucion1 != 0 and self.vref1 != 0 and self.vie1 != 0):
                #Caso 3
                #En este caso tienen que dar: Alcance, resolución, vref, valor inicial emulador y sensor}
                #Ecuación 1
                self.log_2 = math.log2(((1/self.resolucion1)*(self.alcance1)) + 1)
                self.nresul = round(self.log_2)
                #Ecuación 2
                self.sd = (2**self.nresul)/self.vref1
                #Ecuación 3
                self.sa = 1/(self.resolucion1 * self.sensibilidadgono * self.sd)
                #Ecuacion 8
                self.rmin = round(self.vie1)
                #Ecuacion 9
                self.rmax = self.alcance1 + self.rmin
                #Ecuacion 4
                self.inicial_ac = -(0.5/self.sd) - (self.sa * ((self.sensibilidadgono * self.rmin) + self.inicialgono))
                
                self.resrango = 'Rango:'+str(self.rmax)+' a '+str(self.rmin)
                self.resresolucion = 'Resolución:' +self.resolucion
                self.rescodigo = 'Código CAD:' +str(self.nresul)
                self.resalcance = 'Alcance:' +self.alcance
                self.resvref = 'Vref:' +self.vref
                self.ressd =  'BDAS/CTAS = ' +str(self.sd)+self.unidad_seleccionadac+ ' + 0.5' 
                if self.inicial_ac > 0:
                    self.ecu_acon = '+' + str(self.inicial_ac)
                else:
                    self.ecu_acon = str(self.inicial_ac)
            
                self.ressa = self.unidad_seleccionadac+' = '+str(self.sa)+self.unidad_seleccionada+self.ecu_acon
                self.vief = float(self.vie)
                if self.vief > 0:
                    self.ecu_vie = '+' + str(self.vief)
                else:
                    self.ecu_vie = str(self.vief)
                
                self.resemulador = self.unidad+' = '+self.resolucion+'BDAS/CTAS'+self.ecu_vie
            else:
                self.error = 'La información proporcionada no es correcta por lo tanto no se pueden observar los resultados.'
                self.errors = 'Recordar que: Pandora versión 1.0 tiene 3 casos de diseño por favor revisar estos casos.'
                
        
                    
            if self.bandera_discretizador==True:
                
                print('Aqui vamos')
                
            else:
                pass
                self.sensibilidad_emulador = 1/(self.sensibilidadgono*self.sensibilidad_acgono)
                self.valor_inicial_em = ((((self.inicialgono*self.sensibilidad_acgono)+self.valor_inicial_acgono))/(self.sensibilidadgono*self.sensibilidad_acgono))*(-1)
                print('Aqui vamos')
                print(self.sensibilidad_emulador)
                print(self.valor_inicial_em)
                self.ecu_emulador=str(self.sensibilidad_emulador)+' * (volataje) + '+str(self.valor_inicial_em)
                self.emulador=(self.acondicionador*self.sensibilidad_emulador)+self.valor_inicial_em


        except:
            messagebox.showerror("Error!", "Hay un error en los datos")


    def limpiarpanel(self):
        for widget in self.principal.winfo_children():
            widget.destroy()   