import requests
import ctypes


# Función para construir la URL dinámica
def build_url(base_url, country_iso, indicator, year, format_type):
    return f'{base_url}/{country_iso}/indicator/{indicator}?format={format_type}&date={year}'

# Función para realizar la solicitud a la API
def fetch_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        print('Response OK')
        return response.json()
    else:
        print('Response Failed')
        return None

# Función para procesar los datos de la respuesta
def process_data(data):
    if len(data) > 1 and isinstance(data[1], list):  # Verifica que haya datos en la respuesta
        result = data[1][0].get("value")  # La lista de resultados está en la segunda posición
         
        return result
    else:
        print("No se encontraron datos en la respuesta.")
        return []

# Función principal
def main():
    # Variables dinámicas
    base_url = 'https://api.worldbank.org/v2/en/country'
    country_iso = input("Ingrese el código ISO del país (por ejemplo, ARG): ").strip().upper()
    indicator = 'SI.POV.GINI'  # Indicador
    year = input("Ingrese el año (por ejemplo, 2012): ").strip()
    format_type = 'json'  # Formato de respuesta

    # Construcción de la URL
    url = build_url(base_url, country_iso, indicator, year, format_type)

    # Realiza la solicitud
    data = fetch_data(url)

    # Procesa los datos si la respuesta es válida
    if data:
        result = process_data(data)
        print("Datos extraídos:")
        print(result)

    conversor_adder = ctypes.CDLL('./conversor_adder.so')
    conversor_adder.c_float_to_int_add1.argtypes = (ctypes.c_float,)
    conversor_adder.c_float_to_int_add1.restype = ctypes.c_int
    c_result = conversor_adder.c_float_to_int_add1(result)
    print(c_result)

# Ejecuta la función principal
if __name__ == "__main__":
    main()
