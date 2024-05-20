import os
import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv
import requests

# Cargar las variables de entorno del archivo .env
load_dotenv()

def connect_to_database():
    """Conecta a la base de datos PostgreSQL y retorna la conexión y el cursor."""
    try:
        conn = psycopg2.connect(
            dbname=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASS'),
            host=os.getenv('DB_HOST'),
            port=os.getenv('DB_PORT')
        )
        cur = conn.cursor()
        print("Conexión a la base de datos exitosa")
        return conn, cur
    except psycopg2.OperationalError as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None, None

def fetch_data_from_supabase():
    """Realiza una petición GET a la API de Supabase."""
    url = os.getenv('SUPABASE_URL') + "/rest/v1/projects"  # Ajusta esto según la URL correcta de tu API
    headers = {
        "apikey": os.getenv('SUPABASE_KEY'),
        "Authorization": f"Bearer {os.getenv('SUPABASE_KEY')}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print("Datos recibidos de Supabase:", response.json())
    else:
        print("Error al recibir datos de Supabase:", response.status_code, response.text)

def main():
    # Conectar a la base de datos
    conn, cur = connect_to_database()

    # Si la conexión fue exitosa, haz algo con ella, por ejemplo, una consulta básica
    if conn is not None and cur is not None:
        try:
            # Ejecutar una consulta SQL simple (ajusta esto según tu esquema de base de datos)
            cur.execute("SELECT * FROM your_table_name LIMIT 5;")
            results = cur.fetchall()
            for row in results:
                print(row)
        except psycopg2.Error as e:
            print(f"Error al ejecutar la consulta: {e}")
        finally:
            cur.close()
            conn.close()

    # Hacer una llamada a la API de Supabase
    fetch_data_from_supabase()

if __name__ == "__main__":
    main()
