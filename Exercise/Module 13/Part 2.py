import mysql.connector
from flask import Flask, jsonify

app = Flask(__name__)

def get_airport_by_icao(icao_code: str):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="flight_game"
    )
    cursor = connection.cursor()
    sql = "SELECT name, municipality FROM airport WHERE ident = %s"
    cursor.execute(sql, (icao_code,))
    row = cursor.fetchone()
    cursor.close()
    connection.close()
    return row

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

@app.route("/hello")
def hello():
    return "Flask is working!"

@app.route("/prime_number/<int:number>")
def prime_number(number):
    result = {
        "Number": number,
        "isPrime": is_prime(number)
    }
    return jsonify(result)

@app.route("/airport/<icao>")
def airport_info(icao):
    icao = icao.upper()
    row = get_airport_by_icao(icao)

    if row:
        name, location = row
        result = {
            "ICAO": icao,
            "Name": name,
            "Location": location
        }
    else:
        result = {
            "ICAO": icao,
            "Name": None,
            "Location": None
        }

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)