import customtkinter as ctk

class StockerHeaderFrame(ctk.CTkFrame):
    
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.configure(height=150) # 15px xpad top and bottom -> 30px xpad total 
        self.pack_propagate(False)

        self.label = ctk.CTkLabel(master=self, text="Stocker", fg_color="transparent")

        self.label.pack()
