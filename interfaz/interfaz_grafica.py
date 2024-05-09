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
        self.root.title('Pandora S')
        wtotal = self.root.winfo_screenwidth()
        htotal = self.root.winfo_screenheight()

        wventana = 900
        hventana = 600

        pwidth = round(wtotal/2-wventana/2)
        pheight = round(htotal/2-hventana/2)

        self.root.geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidth)+"+"+str(pheight))

        self.menu = ctk.CTkFrame(self.root, fg_color="blue")
        self.menu.pack(side=ctk.LEFT, fill='both', expand=False)

        emulador=ctk.CTkImage(light_image=Image.open(os.path.join(carpeta_imagenes, "imagen1.png")),dark_image=Image.open(os.path.join(carpeta_imagenes, "imagen1.png")), size=(150,60))
        # Display the image
        image_label = ctk.CTkLabel(self.menu, text="", image=emulador)
        image_label.pack()


        self.root.mainloop()




class VentanaDiseno():
    def __init__(self):
        self.root = ctk.CTk()
        self.root.geometry("500x400")
        self.root.title('Pandora D')
        wtotal = self.root.winfo_screenwidth()
        htotal = self.root.winfo_screenheight()

        wventana = 400
        hventana = 300

        pwidth = round(wtotal/2-wventana/2)
        pheight = round(htotal/2-hventana/2)

        self.root.geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidth)+"+"+str(pheight))
        self.root.mainloop()