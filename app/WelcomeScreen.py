from customtkinter import CTkFrame, CTkLabel, CTkButton

class WelcomeScreen(CTkFrame):

    def __init__(self, parent, **kwargs):
        super().__init__(parent)

        self.data = {
            "button": None
        }

        # Create objects
        self.label = CTkLabel(self, text="Screen 1", font=("Arial", 20))
        self.button = CTkButton(
            self, 
            text="Go to Screen 2", 
            command=lambda: parent.show_frame(self.data.get("button") if self.data.get("button") else self)
        )

    def __call__(self, parent, **kwargs):

        if kwargs.get("button"):
            self.data["button"] = kwargs.get("button")
            self.button.configure(
                command=lambda: parent.show_frame(self.data.get("button") if self.data.get("button") else self)
            )

        # Initialize objects
        self.label.pack(pady=20)
        self.button.pack(pady=10)