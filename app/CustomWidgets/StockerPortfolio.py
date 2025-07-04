
import customtkinter as ctk

class StockerPortfolio(ctk.CTkFrame):
    
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.pack_propagate(False)

        # Portfolio Frame Left Section
        self.StockerPortfolioLeftSection = ctk.CTkFrame(master=self, width=400, border_color="black", border_width=1)
        self.StockerPortfolioLeftSection.pack_propagate(False)
        self.StockerPortfolioLeftSection.pack(side="left", fill="y", padx=(15, 7.5), pady=(5, 15))



        self.portfolio_left_section_title = "Deming Investments"
        ctk.CTkLabel(self.StockerPortfolioLeftSection, text=f"Portfolio: {self.portfolio_left_section_title}", fg_color="transparent").pack(padx=5, pady=5)

        
        # Portfolio Frame Right Section
        self.StockerPortfolioRightSection = ctk.CTkFrame(master=self, width=710, border_color="black", border_width=1)

        self.StockerPortfolioRightSection.pack(side="right", fill="y", padx=(7.5, 15), pady=(5, 15))

