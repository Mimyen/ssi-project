import customtkinter as ctk

# Initialize customtkinter (needed for styling and configuration)
ctk.set_appearance_mode("System")  # Modes: "System" (default), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (default), "green", "dark-blue"

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Set the window title and size
        self.title("CustomTkinter Main Window")
        self.geometry("400x300")

        # Add a label
        self.label = ctk.CTkLabel(self, text="Welcome to CustomTkinter", font=("Arial", 20))
        self.label.pack(pady=20)

        # Add an entry field
        self.entry = ctk.CTkEntry(self, placeholder_text="Enter something here...")
        self.entry.pack(pady=10)

        # Add a button
        self.button = ctk.CTkButton(self, text="Submit", command=self.on_submit)
        self.button.pack(pady=10)

    def on_submit(self):
        # Get the text from the entry and update the label
        text = self.entry.get()
        self.label.configure(text=f"You entered: {text}")