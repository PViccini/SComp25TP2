import requests
import os
import time

USE_MOCK = os.getenv("USE_MOCK", "false").lower() == "true"
BASE_URL = 'http://localhost:5001/v2/en/country' if USE_MOCK else 'https://api.worldbank.org/v2/en/country'

INDICATOR = 'SI.POV.GINI'
FORMAT = 'json'

def build_url(country_iso, year):
    return f'{BASE_URL}/{country_iso}/indicator/{INDICATOR}?format={FORMAT}&date={year}'

def fetch_data(url):
    try:
        if USE_MOCK:
            start = time.perf_counter()
        response = requests.get(url)
        if USE_MOCK:
            elapsed = time.perf_counter() - start
            print(f"⏱️ API call to {url} took {elapsed:.4f} seconds")
        if response.status_code == 200:
            return response.json()
    except Exception as e:
        print(f"API request failed: {e}")
    return None

def process_data(data):
    if len(data) > 1 and isinstance(data[1], list) and data[1]:
        return data[1][0].get("value")
    return None

try:
    import ttkbootstrap as tb
except ImportError:
    import subprocess
    import sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", "ttkbootstrap"])
    import ttkbootstrap as tb

from ttkbootstrap.constants import *
import datetime
from src.myClient64 import MyClient64

class GiniApp:
    def __init__(self, root):
        self.root = root
        self.root.title("GINI +1")
        self.root.geometry("380x250")
        self.root.resizable(False, False)

        # Country and year data
        self.countries = sorted([
            "AFG", "ALB", "DZA", "AND", "AGO", "ARG", "ARM", "AUS", "AUT", "AZE",
            "BDI", "BEL", "BEN", "BTN", "BOL", "BIH", "BWA", "BRA", "BRN", "BGR",
            "BFA", "BDI", "KHM", "CMR", "CAN", "CPV", "CAF", "TCD", "CHL", "CHN",
            "COL", "COM", "COG", "CRI", "HRV", "CUB", "CYP", "CZE", "DNK", "DJI",
            "DOM", "ECU", "EGY", "SLV", "GNQ", "ERI", "EST", "ETH", "FJI", "FIN",
            "FRA", "GAB", "GMB", "GEO", "DEU", "GHA", "GRC", "GRD", "GTM", "GIN",
            "GNB", "GUY", "HTI", "HND", "HUN", "ISL", "IND", "IDN", "IRN", "IRQ",
            "IRL", "ISR", "ITA", "JAM", "JPN", "JOR", "KAZ", "KEN", "KIR", "KWT",
            "KGZ", "LAO", "LVA", "LBN", "LSO", "LBR", "LBY", "LIE", "LTU", "LUX",
            "MDG", "MWI", "MYS", "MDV", "MLI", "MLT", "MHL", "MRT", "MUS", "MEX",
            "MDA", "MNG", "MNE", "MAR", "MOZ", "MMR", "NAM", "NRU", "NPL", "NLD",
            "NZL", "NIC", "NER", "NGA", "PRK", "MKD", "NOR", "OMN", "PAK", "PLW",
            "PAN", "PNG", "PRY", "PER", "PHL", "POL", "PRT", "QAT", "ROU", "RUS",
            "RWA", "WSM", "STP", "SAU", "SEN", "SRB", "SYC", "SLE", "SGP", "SVK",
            "SVN", "SLB", "SOM", "ZAF", "KOR", "SSD", "ESP", "LKA", "SDN", "SUR",
            "SWZ", "SWE", "CHE", "SYR", "TJK", "TZA", "THA", "TLS", "TGO", "TON",
            "TTO", "TUN", "TUR", "TKM", "UGA", "UKR", "ARE", "GBR", "USA", "URY",
            "UZB", "VUT", "VEN", "VNM", "YEM", "ZMB", "ZWE"
        ])
        self.years = list(range(datetime.datetime.now().year, 1949, -1))

        self.selected_country = tb.StringVar()
        self.selected_year = tb.StringVar()
        self.result = tb.StringVar(value="Select a country and year")

        self._setup_ui()

    def _setup_ui(self):

        # Title
        tb.Label(self.root, text="GINI +1", font=("Helvetica", 16, "italic")).pack(pady=(20, 10))

        # Frame for inputs
        input_frame = tb.Frame(self.root)
        input_frame.pack(pady=5)

        # Country dropdown
        tb.Label(input_frame, text="Country").grid(row=0, column=0, padx=10)
        country_cb = tb.Combobox(input_frame, textvariable=self.selected_country, values=self.countries, width=12, bootstyle="info")
        country_cb.grid(row=1, column=0, padx=10)

        # Year dropdown
        tb.Label(input_frame, text="Year").grid(row=0, column=1, padx=10)
        year_cb = tb.Combobox(input_frame, textvariable=self.selected_year, values=self.years, width=6, bootstyle="info")
        year_cb.grid(row=1, column=1, padx=10)

        # Result label
        tb.Label(self.root, textvariable=self.result, font=("Helvetica", 12), bootstyle="secondary").pack(pady=20)

        # Trace selection changes
        self.selected_country.trace_add("write", self.update_result)
        self.selected_year.trace_add("write", self.update_result)

    def update_result(self, *args):
        country = self.selected_country.get()
        year = self.selected_year.get()

        if not country or not year:
            return

        url = build_url(country, year)
        data = fetch_data(url)

        if data:
            gini = process_data(data)
            if gini is not None:
                client = MyClient64()
                self.result.set(f"GINI + 1 = {client.ftoi_add1_64(gini)}")
            else:
                self.result.set("No data for selected year")
        else:
            self.result.set("Failed to fetch data")


def main():
    root = tb.Window(themename="darkly")  # try "solar", "darkly", "litera", "flaty", etc
    app = GiniApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
