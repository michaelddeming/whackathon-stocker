import customtkinter as ctk

from CustomWidgets.StockerHeaderFrame import StockerHeaderFrame
from CustomWidgets.StockerTabView import StockerTabView


from CustomWidgets.StockerPortfolio import StockerPortfolio

class App(ctk.CTk):

    def __init__(self):
        super().__init__()

        # Window Header Title
        self.title("Stocker Dashboard")
        
        # Window Auto Open Top Level
        self.attributes("-topmost", True)
        
        # Window Geometry 
        self.geometry("1200x900")
        self.resizable(width=False, height=False)


        # add custom widgets as self.widget objects to be included in App()
        self.StockerHeaderFrame = StockerHeaderFrame(master=self)
        self.StockerHeaderFrame.pack(side="top", fill="x", pady=(15,0), padx=15)

        self.StockerTabView = StockerTabView(master=self)
        self.StockerTabView.pack(fill="both", expand=True, padx=15, pady=(0,15))



 


    
if __name__ == "__main__":
    app = App()
    app.mainloop()
    