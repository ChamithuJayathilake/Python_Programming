import mysql.connector

connection = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='flight_game',
         user='root',
         password='1234',
         autocommit=True
)

icao = input("Enter the ICAO code of an airport: ")

cursor = connection.cursor()
sql = "SELECT name, municipality FROM airport WHERE ident=%s"
cursor.execute(sql, (icao,))
result = cursor.fetchone()

if result:
    print(f"Airport name: {result[0]}")
    print(f"Location: {result[1]}")
else:
    print("No airport found with that ICAO code.")