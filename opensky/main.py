import requests

def fetch_data():
    url = "https://opensky-network.org/api/states/all"  # Asegúrate de que esta es la URL correcta
    response = requests.get(url)
    print("Status Code:", response.status_code)  # Imprime el código de estado HTTP
    if response.status_code == 200:
        data = response.json()['states']
        if data:
            return data
        else:
            print("No data found in response.")
            return None
    else:
        print("Failed to fetch data:", response.text)  # Imprime el cuerpo de la respuesta si falla
        return None
