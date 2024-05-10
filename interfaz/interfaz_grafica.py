import tkinter
import os
from PIL import Image, ImageTk
import customtkinter as ctk

carpeta_principal=os.path.dirname(__file__)
carpeta_imagenes=os.path.join(carpeta_principal, "imagenes")
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
        imageninicio=ctk.CTkImage(light_image=Image.open(os.path.join(carpeta_imagenes, "instrumento.png")),dark_image=Image.open(os.path.join(carpeta_imagenes, "instrumento.png")), size=(150,60))


        # Display the image
        image_label = ctk.CTkLabel(self.root, text="", image=imageninicio)
        #image_label.pack()
        image_label.place(relx=0.5, rely=0.35, anchor=tkinter.CENTER)

        def simulation_button_function():
            print("Simulation button pressed")
            self.root.destroy()
            ventanasimu=VentanaSimulacion()


        def design_button_function():
            print("Design button pressed")
            self.root.destroy()
            ventanadis=VentanaDiseno()

        simulation_button = ctk.CTkButton(master=self.root, text="Simulación", font=("Arial", 15),command=simulation_button_function, corner_radius=32, border_color="#FFCC70", border_width=1.5)
        simulation_button.place(relx=0.3, rely=0.7, anchor=tkinter.CENTER)

        design_button = ctk.CTkButton(master=self.root, text="Diseño", command=design_button_function, font=("Arial", 15), corner_radius=32, border_color="#FFCC70", border_width=1.5)
        design_button.place(relx=0.7, rely=0.7, anchor=tkinter.CENTER)


        wtotal = self.root.winfo_screenwidth()
        htotal = self.root.winfo_screenheight()

        wventana = 400
        hventana = 300

        pwidth = round(wtotal/2-wventana/2)
        pheight = round(htotal/2-hventana/2)

        self.root.geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidth)+"+"+str(pheight))
        self.root.mainloop()


class VentanaSimulacion():
    def __init__(self):
        self.root = ctk.CTk()
        self.root.geometry("900x600")
        self.root.title('Pandora Simulación')
        wtotal = self.root.winfo_screenwidth()
        htotal = self.root.winfo_screenheight()

        wventana = 900
        hventana = 600

        pwidth = round(wtotal/2-wventana/2)
        pheight = round(htotal/2-hventana/2)

        self.root.geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidth)+"+"+str(pheight))

        self.menu = ctk.CTkFrame(self.root, fg_color="#1F6AA5",width=220)
        self.menu.pack(side=ctk.LEFT, fill='both', expand=False)

        self.label = ctk.CTkLabel(self.menu, text="\nP A N D O R A\n", font=("Arial Black", 20), padx=30)

        #label.place(relx=0.5, rely=0.1, anchor="center") 
        self.label.pack(side=ctk.TOP)
        
        
        self.isensor = ctk.CTkImage(light_image=Image.open(os.path.join(carpeta_imagenes, "sensor2.png")), dark_image=Image.open(os.path.join(carpeta_imagenes, "sensor2.png")), size=(100, 50))
        # # Display the image
        # image_sensor = ctk.CTkLabel(self.menu, text="", image=sensor)
        # image_sensor.place(x=2, y=120)
        
        self.iacondicionador = ctk.CTkImage(light_image=Image.open(os.path.join(carpeta_imagenes, "acondicionador.png")), dark_image=Image.open(os.path.join(carpeta_imagenes, "acondicionador.png")), size=(60, 90))
        # # Display the image
        # image_acondicionador = ctk.CTkLabel(self.menu, text="", image=acondicionador)
        # image_acondicionador.place(x=2, y=200)
        
        self.idiscretizador = ctk.CTkImage(light_image=Image.open(os.path.join(carpeta_imagenes, "discretizador.png")), dark_image=Image.open(os.path.join(carpeta_imagenes, "discretizador.png")), size=(60, 90))
        # # Display the image
        # image_discretizador = ctk.CTkLabel(self.menu, text="", image=discretizador)
        # image_discretizador.place(x=2, y=320)
        
        self.iemulador = ctk.CTkImage(light_image=Image.open(os.path.join(carpeta_imagenes, "imagen1.png")), dark_image=Image.open(os.path.join(carpeta_imagenes, "imagen1.png")), size=(100, 50))
        # # Display the image
        # image_label = ctk.CTkLabel(self.menu, text="", image=emulador)
        # image_label.place(x=2, y=450)  # Ajusta las coordenadas (x, y) según sea necesario
        
        self.button_sensor = ctk.CTkButton(self.menu, text="Sensor", image=self.isensor, width=220)
        self.button_acondicionador = ctk.CTkButton(self.menu, text="Acondicionador", image=self.iacondicionador, width=220)
        self.button_discretizador = ctk.CTkButton(self.menu, text="Discretizador", image=self.idiscretizador, width=220)
        self.button_emulador = ctk.CTkButton(self.menu, text="Emulador", image=self.iemulador, width=220)

        self.button_sensor.pack(side=ctk.TOP)
        self.button_acondicionador.pack(side=ctk.TOP)
        self.button_discretizador.pack(side=ctk.TOP)
        self.button_emulador.pack(side=ctk.TOP)

        

        # buttons_info = [
        #     ("Sensor", "\FFCC70", self.button_sensor),
        #     ("Acondicionador", "\FFCC70", self.button_acondicionador),
        #     ("Discretizador", "\FFCC70", self.button_discretizador),
        #     ("Emulador", "\FFCC70", self.button_emulador)
        # ]
        #for text, icon, button in buttons_info: (ver video en el minuto 36:40) 
           # self.configurar_boton_menu1(button, text, icon, )
        
        self.root.mainloop()






class VentanaDiseno():
    def __init__(self):
        self.root = ctk.CTk()
        self.root.geometry("900x600")
        self.root.title('Pandora Diseño')
        wtotal = self.root.winfo_screenwidth()
        htotal = self.root.winfo_screenheight()

        wventana = 900
        hventana = 600

        pwidth = round(wtotal/2-wventana/2)
        pheight = round(htotal/2-hventana/2)

        self.root.geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidth)+"+"+str(pheight))
        
        self.menu = ctk.CTkFrame(self.root, fg_color="#003366")
        self.menu.pack(side=ctk.LEFT, fill='both', expand=False)

        label = ctk.CTkLabel(self.menu, text="P A N D O R A", font=("Arial Black", 20))

        label.place(relx=0.5, rely=0.1, anchor="center") 
        
        
        sensor = ctk.CTkImage(light_image=Image.open(os.path.join(carpeta_imagenes, "sensor.png")), dark_image=Image.open(os.path.join(carpeta_imagenes, "sensor.png")), size=(100, 50))
        # Display the image
        image_sensor = ctk.CTkLabel(self.menu, text="", image=sensor)
        image_sensor.place(x=2, y=120)
        
        acondicionador = ctk.CTkImage(light_image=Image.open(os.path.join(carpeta_imagenes, "acondicionador.png")), dark_image=Image.open(os.path.join(carpeta_imagenes, "acondicionador.png")), size=(60, 90))
        # Display the image
        image_acondicionador = ctk.CTkLabel(self.menu, text="", image=acondicionador)
        image_acondicionador.place(x=2, y=200)
        
        discretizador = ctk.CTkImage(light_image=Image.open(os.path.join(carpeta_imagenes, "discretizador.png")), dark_image=Image.open(os.path.join(carpeta_imagenes, "discretizador.png")), size=(60, 90))
        # Display the image
        image_discretizador = ctk.CTkLabel(self.menu, text="", image=discretizador)
        image_discretizador.place(x=2, y=320)
        
        emulador = ctk.CTkImage(light_image=Image.open(os.path.join(carpeta_imagenes, "imagen1.png")), dark_image=Image.open(os.path.join(carpeta_imagenes, "imagen1.png")), size=(100, 50))
        # Display the image
        image_label = ctk.CTkLabel(self.menu, text="", image=emulador)
        image_label.place(x=2, y=450)  # Ajusta las coordenadas (x, y) según sea necesario
        self.root.mainloop()