from customtkinter import CTkFrame, CTkLabel, CTkButton
from tkinter import filedialog
import pandas as pd
from data import data

class MainScreen(CTkFrame):

    def __init__(self, parent, **kwargs):
        super().__init__(parent)

        self.data = {
            "button": None
        }

        # Create objects
        self.label = CTkLabel(self, text="Screen 1", font=("Arial", 20))
        self.label.pack(pady=10)

        # self.button = CTkButton(
        #     self, 
        #     text="Go to Screen 2", 
        #     command=lambda: parent.show_frame(self.data.get("button") if self.data.get("button") else self)
        # )

        # Button that prints data
        self.button_print = CTkButton(
            self, 
            text="Print Loaded data",
            command=lambda: print(data.get())
        )
        self.button_print.pack(pady=10)

        # Button that opens dialog to load file
        self.load_file_button = CTkButton(
            self, 
            text="Load File", 
            command=self.load_file
        )
        self.load_file_button.pack(pady=10)

        # Button that calculates averages
        self.button_calc_avg = CTkButton(
            self, 
            text="Calculate Averages", 
            command=lambda: print(data.calculate_column_averages())
        )
        self.button_calc_avg.pack(pady=10)
        
        # Button that calculates median
        self.button_calc_med = CTkButton(
            self, 
            text="Calculate Median", 
            command=lambda: print(data.calculate_column_medians())
        )
        self.button_calc_med.pack(pady=10)

        # Button that calculates std dev
        self.button_calc_stddev = CTkButton(
            self, 
            text="Calculate Standard Deviation", 
            command=lambda: print(data.calculate_column_stddev())
        )
        self.button_calc_stddev.pack(pady=10)

        # Button that calculates std dev
        self.button_calc_max = CTkButton(
            self, 
            text="Calculate Maximums", 
            command=lambda: print(data.calculate_column_maximums())
        )
        self.button_calc_max.pack(pady=10)

        # Button that calculates std dev
        self.button_calc_min = CTkButton(
            self, 
            text="Calculate Minimums", 
            command=lambda: print(data.calculate_column_minimums())
        )
        self.button_calc_min.pack(pady=10)

        # Button that checks normality
        self.button_check_norm = CTkButton(
            self, 
            text="Check Normality", 
            command=lambda: print(data.check_normality())
        )
        self.button_check_norm.pack(pady=10)

        # Button that checks symmetry
        self.button_check_symm = CTkButton(
            self, 
            text="Check Symmetry", 
            command=lambda: print(data.check_symmetry())
        )
        self.button_check_symm.pack(pady=10)

        # Button that shows correlation analysis
        self.button_corr_anal = CTkButton(
            self, 
            text="Correlation Analysis", 
            command=lambda: print(data.correlation_analysis())
        )
        self.button_corr_anal.pack(pady=10)

        # Button that shows class distribution
        self.button_class_dist = CTkButton(
            self, 
            text="Class Distribution", 
            command=lambda: print(data.class_distribution())
        )
        self.button_class_dist.pack(pady=10)

        # Button that encodes using label
        self.button_encode_label = CTkButton(
            self, 
            text="Encode using Label", 
            command=lambda: print(data.encode_all_non_numeric(method="label"))
        )
        self.button_encode_label.pack(pady=10)

        # Button that encodes using one-hot
        self.button_encode_oh = CTkButton(
            self, 
            text="Encode using One-Hot", 
            command=lambda: print(data.encode_all_non_numeric(method="one-hot"))
        )
        self.button_encode_oh.pack(pady=10)
        

    def load_file(self):
        file_path = filedialog.askopenfilename(
            title="Select a File", 
            filetypes=(("CSV Files", "*.csv"), ("Text Files", "*.txt"))
        )
        if file_path:
            try:
                if file_path.endswith('.csv'):
                    df = pd.read_csv(file_path)
                elif file_path.endswith('.txt'):
                    df = pd.read_csv(file_path, delimiter="\t")
                else:
                    raise ValueError("Unsupported file type!")

                # Convert DataFrame to array of arrays
                self.loaded_data = df.values.tolist()
                print("Data loaded successfully:", self.loaded_data)
                data(self.loaded_data)
            except Exception as e:
                print("Error loading file:", e)

    def __call__(self, parent, **kwargs): ...

        # if kwargs.get("button"):
        #     self.data["button"] = kwargs.get("button")
        #     self.button.configure(
        #         command=lambda: parent.show_frame(self.data.get("button") if self.data.get("button") else self)
        #     )

        # # Initialize objects
        # self.label.pack(pady=20)
        # self.button.pack(pady=10)