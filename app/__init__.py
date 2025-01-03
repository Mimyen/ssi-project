import customtkinter as ctk
from app.MainScreen import MainScreen

# Initialize customtkinter (needed for styling and configuration)
ctk.set_appearance_mode("System")  # Modes: "System" (default), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (default), "green", "dark-blue"

class App(ctk.CTk):

    def __init__(self):
        super().__init__()

        # Set the window title and size
        self.title("SSI Project")
        self.geometry("1280x720")

        # Create frames for different screens
        self.screen1 = MainScreen(self)

        # Initialize and display the first screen
        self.screen1(self)
        
        # Show the first screen
        self.show_frame(self.screen1)

    def show_frame(self, frame):
        # Hide all frames
        self.screen1.pack_forget()
        
        # Show the selected frame
        frame.pack(fill="both", expand=True)