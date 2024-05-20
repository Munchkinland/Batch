import psycopg2
import os

def get_connection():
    return psycopg2.connect(
        dbname='postgres',
        user='postgres',
        password=os.getenv('SUPABASE_KEY'),
        host=os.getenv('SUPABASE_URL'),
        port=5432  # El puerto estándar para PostgreSQL
    )

def insert_data(data):
    conn = get_connection()
    cur = conn.cursor()
    for record in data:
        cur.execute("""
            INSERT INTO flights (icao24, callsign, origin_country, time_position, last_contact,
            longitude, latitude, baro_altitude, on_ground, velocity, true_track, vertical_rate, sensors,
            geo_altitude, squawk, spi, position_source) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, record)
    conn.commit()
    cur.close()
    conn.close()

