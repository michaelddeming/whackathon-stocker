import customtkinter as ctk
from PIL import Image


class StockerHeaderFrame(ctk.CTkFrame):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.configure(
            height=150, fg_color="transparent"
        )  # 15px xpad top and bottom -> 30px xpad total
        self.pack_propagate(False)

        light_mode = "app/assets/imgs/stocker_logo_full_dark.png"
        dark_mode = "app/assets/imgs/stocker_logo_full.png"
        self.logo = ctk.CTkImage(
            light_image=Image.open(light_mode),
            dark_image=Image.open(dark_mode),
            size=(750, 120),
        )

        self.logo_label = ctk.CTkLabel(self, image=self.logo, text="")
        self.logo_label.pack(fill="both", expand=True)
