import customtkinter as ctk
from app.WelcomeScreen import WelcomeScreen

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
        self.screen1 = WelcomeScreen(self)
        self.screen2 = ctk.CTkFrame(self)

        # Initialize and display the first screen
        self.screen1(self, button = self.screen2)
        self.initialize_screen2()
        
        # Show the first screen
        self.show_frame(self.screen1)

    def initialize_screen2(self):
        # Elements for Screen 2
        label = ctk.CTkLabel(self.screen2, text="Screen 2", font=("Arial", 20))
        label.pack(pady=20)

        button = ctk.CTkButton(self.screen2, text="Go to Screen 1", command=lambda: self.show_frame(self.screen1))
        button.pack(pady=10)

    def show_frame(self, frame):
        # Hide all frames
        self.screen1.pack_forget()
        self.screen2.pack_forget()
        
        # Show the selected frame
        frame.pack(fill="both", expand=True)