from data.fetch_data import fetch_data
from db.database import insert_data
from dotenv import load_dotenv
import os

def main():
    load_dotenv()  # Carga las variables de entorno desde .env
    data = fetch_data()
    if data:
        insert_data(data)
    else:
        print("No data fetched from API.")

if __name__ == "__main__":
    main()
