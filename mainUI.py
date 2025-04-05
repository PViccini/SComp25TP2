import requests

def build_url(base_url, country_iso, indicator, year, format_type):
    return f'{base_url}/{country_iso}/indicator/{indicator}?format={format_type}&date={year}'

def fetch_data(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
    except Exception as e:
        print(f"API request failed: {e}")
    return None

def process_data(data):
    if len(data) > 1 and isinstance(data[1], list) and data[1]:
        return data[1][0].get("value")
    return None


import tkinter as tk
from tkinter import ttk
import datetime
from myClient64 import MyClient64

class GiniApp:
    def __init__(self, root):
        self.root = root
        self.root.title("GINI +1")
        self.root.geometry("400x250")
        self.root.configure(bg="white")

        self.countries = sorted([
            "AFG", "ALB", "DZA", "AND", "AGO", "ARG", "ARM", "AUS", "AUT", "AZE",
            "BDI", "BEL", "BEN", "BTN", "BOL", "BIH", "BWA", "BRA", "BRN", "BGR",
            "BFA", "KHM", "CMR", "CAN", "CPV", "CAF", "TCD", "CHL", "CHN", "COL",
            "COM", "COG", "CRI", "HRV", "CUB", "CYP", "CZE", "DNK", "DJI", "DOM",
            "ECU", "EGY", "SLV", "GNQ", "ERI", "EST", "ETH", "FJI", "FIN", "FRA",
            "GAB", "GMB", "GEO", "DEU", "GHA", "GRC", "GRD", "GTM", "GIN", "GNB",
            "GUY", "HTI", "HND", "HUN", "ISL", "IND", "IDN", "IRN", "IRQ", "IRL",
            "ISR", "ITA", "JAM", "JPN", "JOR", "KAZ", "KEN", "KIR", "KWT", "KGZ",
            "LAO", "LVA", "LBN", "LSO", "LBR", "LBY", "LIE", "LTU", "LUX", "MDG",
            "MWI", "MYS", "MDV", "MLI", "MLT", "MHL", "MRT", "MUS", "MEX", "MDA",
            "MNG", "MNE", "MAR", "MOZ", "MMR", "NAM", "NRU", "NPL", "NLD", "NZL",
            "NIC", "NER", "NGA", "PRK", "MKD", "NOR", "OMN", "PAK", "PLW", "PAN",
            "PNG", "PRY", "PER", "PHL", "POL", "PRT", "QAT", "ROU", "RUS", "RWA",
            "WSM", "STP", "SAU", "SEN", "SRB", "SYC", "SLE", "SGP", "SVK", "SVN",
            "SLB", "SOM", "ZAF", "KOR", "SSD", "ESP", "LKA", "SDN", "SUR", "SWZ",
            "SWE", "CHE", "SYR", "TJK", "TZA", "THA", "TLS", "TGO", "TON", "TTO",
            "TUN", "TUR", "TKM", "UGA", "UKR", "ARE", "GBR", "USA", "URY", "UZB",
            "VUT", "VEN", "VNM", "YEM", "ZMB", "ZWE"
        ])
        self.years = list(range(datetime.datetime.now().year, 1949, -1))

        self.selected_country = tk.StringVar()
        self.selected_year = tk.StringVar()
        self.result_text = tk.StringVar(value="Please select values")

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="GINI +1", font=("Arial", 14, "italic"), bg="white").pack(pady=(20, 10))

        frame = tk.Frame(self.root, bg="white")
        frame.pack(pady=10)

        ttk.Label(frame, text="country").grid(row=0, column=0, padx=10)
        country_menu = ttk.Combobox(frame, textvariable=self.selected_country, values=self.countries, state="readonly")
        country_menu.grid(row=1, column=0, padx=10)

        ttk.Label(frame, text="year").grid(row=0, column=1, padx=10)
        year_menu = ttk.Combobox(frame, textvariable=self.selected_year, values=self.years, state="readonly")
        year_menu.grid(row=1, column=1, padx=10)

        ttk.Label(self.root, textvariable=self.result_text, font=("Arial", 12)).pack(pady=20)

        self.selected_country.trace_add("write", self.update_result)
        self.selected_year.trace_add("write", self.update_result)

    def update_result(self, *args):
        country = self.selected_country.get()
        year = self.selected_year.get()

        if not country or not year:
            return

        url = build_url(
            base_url="https://api.worldbank.org/v2/en/country",
            country_iso=country,
            indicator="SI.POV.GINI",
            year=year,
            format_type="json"
        )

        data = fetch_data(url)
        gini_value = process_data(data)

        if gini_value is not None:
            try:
                c = MyClient64()
                c_result = c.ftoi_add1_64(gini_value)
                self.result_text.set(f"GINI +1: {c_result}")
            except Exception as e:
                self.result_text.set(f"Error: {e}")
        else:
            self.result_text.set("No data found.")


# === main.py ===
import tkinter as tk

def main():
    root = tk.Tk()
    app = GiniApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
