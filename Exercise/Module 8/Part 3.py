import mysql.connector
from geopy.distance import geodesic

def get_airport_coordinates(icao_code):
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="1234",
        database="flight_game"
    )
    cursor = conn.cursor()
    query = """
        SELECT latitude_deg, longitude_deg
        FROM airport
        WHERE ident = %s;
    """
    cursor.execute(query, (icao_code,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    if result:
        return (float(result[0]), float(result[1]))
    else:
        return None

def run_airport_distance():

    icao1 = input("Enter the ICAO code of the first airport: ").strip().upper()
    icao2 = input("Enter the ICAO code of the second airport: ").strip().upper()

    coords1 = get_airport_coordinates(icao1)
    coords2 = get_airport_coordinates(icao2)

    if not coords1:
        print(f"Airport with ICAO code {icao1} not found in the database.")
    if not coords2:
        print(f"Airport with ICAO code {icao2} not found in the database.")

    # Only calculate distance if both exist
    if coords1 and coords2:
        distance_km = geodesic(coords1, coords2).kilometers
        print(f"\n\nDistance between {icao1} and {icao2}: {distance_km:.2f} kilometers")

run_airport_distance()
