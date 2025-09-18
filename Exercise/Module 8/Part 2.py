import mysql.connector

def get_airports_by_country(country_code):
    try:
        # Connect to the database
        conn = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="1234",
            database="flight_game"
        )

        cursor = conn.cursor()

        query = """
            SELECT type, COUNT(*)
            FROM airport
            WHERE iso_country = %s
            GROUP BY type
            ORDER BY type;
        """
        cursor.execute(query, (country_code,))
        results = cursor.fetchall()

        cursor.close()
        conn.close()
        return results

    except mysql.connector.Error:
        return None  # Return None if connection fails

def run_country_program():
    country_code = input("Enter the country code (e.g., FI for Finland): ").strip().upper()
    airports = get_airports_by_country(country_code)

    if not airports:
        print(f"No airports found for country code '{country_code}' or database connection failed.")
        return

    print(f"\n\nAirports in {country_code}:")
    for airport_type, count in airports:
        print(f"{count} {airport_type} airports")

run_country_program()
