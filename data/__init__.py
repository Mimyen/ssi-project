import statistics
from scipy.stats import shapiro, skew
import matplotlib.pyplot as plt
import statsmodels.api as sm
import numpy as np
import seaborn as sns
import pandas as pd
from collections import Counter
from sklearn.preprocessing import LabelEncoder
import os
from typing import Literal

class Data:
    data: list[list[any]] | None = None

    def __init__(self):
        pass

    def __call__(self, data: list[list[any]]):
        self.data = data

    def get(self):
        return self.data

    def calculate_column_averages(self) -> list[float | None]:
        if not self.data or len(self.data) == 0:
            return []

        # Transpose the data to get columns
        columns = list(zip(*self.data))

        averages = []
        for col in columns:
            try:
                # Filter out non-numeric values
                numeric_values = [float(value) for value in col if self._is_number(value)]
                # Calculate average if there are numeric values, otherwise append None
                averages.append(sum(numeric_values) / len(numeric_values) if numeric_values else None)
            except ZeroDivisionError:
                averages.append(None)

        return averages
    
    def calculate_column_medians(self) -> list[float | None]:
        if not self.data or len(self.data) == 0:
            return []

        # Transpose the data to get columns
        columns = list(zip(*self.data))

        medians = []
        for col in columns:
            try:
                # Filter out non-numeric values
                numeric_values = [float(value) for value in col if self._is_number(value)]
                # Calculate median if there are numeric values, otherwise append None
                medians.append(statistics.median(numeric_values) if numeric_values else None)
            except statistics.StatisticsError:
                medians.append(None)

        return medians
    
    def calculate_column_stddev(self) -> list[float | None]:
        if not self.data or len(self.data) == 0:
            return []

        # Transpose the data to get columns
        columns = list(zip(*self.data))

        stddevs = []
        for col in columns:
            try:
                # Filter out non-numeric values
                numeric_values = [float(value) for value in col if self._is_number(value)]
                # Calculate standard deviation if there are numeric values, otherwise append None
                stddevs.append(statistics.stdev(numeric_values) if len(numeric_values) > 1 else None)
            except statistics.StatisticsError:
                stddevs.append(None)

        return stddevs
    
    def calculate_column_maximums(self) -> list[float | None]:
        if not self.data or len(self.data) == 0:
            return []

        # Transpose the data to get columns
        columns = list(zip(*self.data))

        maximums = []
        for col in columns:
            try:
                # Filter out non-numeric values
                numeric_values = [float(value) for value in col if self._is_number(value)]
                # Get max value if there are numeric values, otherwise append None
                maximums.append(max(numeric_values) if numeric_values else None)
            except ValueError:
                maximums.append(None)

        return maximums

    def calculate_column_minimums(self) -> list[float | None]:
        if not self.data or len(self.data) == 0:
            return []

        # Transpose the data to get columns
        columns = list(zip(*self.data))

        minimums = []
        for col in columns:
            try:
                # Filter out non-numeric values
                numeric_values = [float(value) for value in col if self._is_number(value)]
                # Get min value if there are numeric values, otherwise append None
                minimums.append(min(numeric_values) if numeric_values else None)
            except ValueError:
                minimums.append(None)

        return minimums
    
    def check_normality(self):
        if not self.data or len(self.data) == 0:
            print("Brak danych.")
            return

        # Transpose to get columns
        columns = list(zip(*self.data))

        for i, col in enumerate(columns):
            numeric_values = [float(value) for value in col if self._is_number(value)]
            if numeric_values:
                # Test Shapiro-Wilka
                stat, p_value = shapiro(numeric_values)
                print(f"Kolumna {i+1}:")
                print(f"  Test Shapiro-Wilka: stat={stat:.4f}, p={p_value:.4f}")
                if p_value > 0.05:
                    print("  Rozkład prawdopodobnie normalny.")
                else:
                    print("  Rozkład nie jest normalny.")

                # QQ plot
                self._qq_plot(numeric_values, i + 1)
            else:
                print(f"Kolumna {i+1}: Brak danych numerycznych.")

    def _qq_plot(self, data, column_index):
        # Konwersja listy na obiekt NumPy
        data_array = np.array(data)
        sm.qqplot(data_array, line='s')
        plt.title(f"QQ Plot - Kolumna {column_index}")
        plt.show()

    def check_symmetry(self):
        if not self.data or len(self.data) == 0:
            print("Brak danych.")
            return

        # Transpose to get columns
        columns = list(zip(*self.data))

        for i, col in enumerate(columns):
            numeric_values = [float(value) for value in col if self._is_number(value)]
            if numeric_values:
                skewness = skew(numeric_values)
                print(f"Kolumna {i+1}: Skośność = {skewness:.4f}")
                if abs(skewness) < 0.5:
                    print("  Rozkład symetryczny.")
                elif skewness > 0:
                    print("  Rozkład skośny prawostronnie (dodatnia skośność).")
                else:
                    print("  Rozkład skośny lewostronnie (ujemna skośność).")
            else:
                print(f"Kolumna {i+1}: Brak danych numerycznych.")


    def correlation_analysis(self, method: Literal["pearson", "spearman", "kendall"]='pearson'):
        """
        Oblicza macierz korelacji i rysuje heatmapę.

        :param method: 'pearson', 'spearman' lub 'kendall' - metoda obliczania korelacji
        """
        if not self.data or len(self.data) == 0:
            print("Brak danych.")
            return

        # Tworzenie DataFrame z danych numerycznych
        df = pd.DataFrame(self.data).apply(pd.to_numeric, errors='coerce')
        correlation_matrix = df.corr(method=method)

        # Wyświetlenie macierzy korelacji
        print(f"Macierz korelacji ({method}):")
        print(correlation_matrix)

        # Rysowanie heatmapy korelacji
        plt.figure(figsize=(10, 8))
        sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="coolwarm", cbar=True)
        plt.title(f"Heatmapa korelacji ({method.capitalize()})")
        plt.show()

    def class_distribution(self, target_column_index: int = -1):
        """
        Analizuje rozkład klas w określonej kolumnie (domyślnie ostatnia kolumna).

        :param target_column_index: indeks kolumny, która zawiera etykiety klas (domyślnie -1)
        """
        if not self.data or len(self.data) == 0:
            print("Brak danych.")
            return

        try:
            # Pobranie kolumny z etykietami klas
            target_column = [row[target_column_index] for row in self.data]

            # Zliczanie liczności klas
            class_counts = Counter(target_column)
            class_df = pd.DataFrame(list(class_counts.items()), columns=["Klasa", "Liczność"])

            # Wyświetlenie liczności klas w konsoli
            print("Rozkład klas:")
            print(class_df)

            # Rysowanie wykresu słupkowego
            plt.figure(figsize=(8, 6))
            sns.barplot(x="Klasa", y="Liczność", data=class_df, palette="viridis")
            plt.title("Rozkład klas")
            plt.xlabel("Klasa")
            plt.ylabel("Liczność")
            plt.show()

        except IndexError:
            print("Błąd: Podany indeks kolumny jest nieprawidłowy.")

    def label_encode(self, column_index: int):
        """
        Koduje zmienną kategoryczną w kolumnie za pomocą Label Encoding.

        :param column_index: indeks kolumny do zakodowania
        :return: DataFrame z zakodowaną kolumną
        """
        if not self.data or len(self.data) == 0:
            print("Brak danych.")
            return

        # Konwersja do DataFrame
        df = pd.DataFrame(self.data)

        try:
            # Label Encoding
            le = LabelEncoder()
            df[column_index] = le.fit_transform(df[column_index])
            print("Label Encoding zakończony.")
            print(df)
            return df
        except Exception as e:
            print(f"Błąd kodowania: {e}")

    def one_hot_encode(self, column_index: int):
        """
        Koduje zmienną kategoryczną w kolumnie za pomocą One-Hot Encoding.

        :param column_index: indeks kolumny do zakodowania
        :return: DataFrame z zakodowaną kolumną
        """
        if not self.data or len(self.data) == 0:
            print("Brak danych.")
            return

        # Konwersja do DataFrame
        df = pd.DataFrame(self.data)

        try:
            # One-Hot Encoding
            column_name = f"col_{column_index}"
            df.columns = [f"col_{i}" for i in range(df.shape[1])]  # Nazwanie kolumn dla jednoznaczności
            one_hot = pd.get_dummies(df[column_name], prefix=column_name)
            df = pd.concat([df.drop(column_name, axis=1), one_hot], axis=1)
            print("One-Hot Encoding zakończony.")
            print(df)
            return df
        except Exception as e:
            print(f"Błąd kodowania: {e}")

    def encode_all_non_numeric(self, method: Literal['label', 'one-hot'] ='label'):
        """
        Koduje wszystkie kolumny nienumeryczne w zbiorze danych i zapisuje wynik w pliku CSV.

        :param method: 'label' dla Label Encoding, 'one-hot' dla One-Hot Encoding
        :return: DataFrame z zakodowanymi kolumnami
        """
        if not self.data or len(self.data) == 0:
            print("Brak danych.")
            return

        # Konwersja do DataFrame
        df = pd.DataFrame(self.data)

        try:
            for col in df.columns:
                # Sprawdzenie, czy kolumna jest numeryczna
                if not pd.api.types.is_numeric_dtype(df[col]):
                    if method == 'label':
                        # Label Encoding
                        le = LabelEncoder()
                        df[col] = le.fit_transform(df[col])
                        print(f"Label Encoding wykonano dla kolumny: {col}")
                    elif method == 'one-hot':
                        # One-Hot Encoding
                        column_name = f"col_{col}"
                        one_hot = pd.get_dummies(df[col], prefix=column_name)
                        df = pd.concat([df.drop(col, axis=1), one_hot], axis=1)
                        print(f"One-Hot Encoding wykonano dla kolumny: {col}")
                    else:
                        print(f"Nieznana metoda kodowania: {method}")
                        return df

            # Zapisanie danych do pliku CSV
            filename = f"encoded-{method}.csv"
            df.to_csv(filename, index=False)
            print(f"Dane zostały zapisane w pliku: {os.path.abspath(filename)}")

            return df

        except Exception as e:
            print(f"Błąd kodowania: {e}")

    @staticmethod
    def _is_number(value):
        try:
            float(value)
            return True
        except (ValueError, TypeError):
            return False


data = Data()