import json
from flask import Flask, Response

app = Flask(__name__)

airports = {
    "EFHK": {"Name": "Helsinki-Vantaa Airport", "Location": "Helsinki"},
    "EGLL": {"Name": "Heathrow Airport", "Location": "London"},
    "KJFK": {"Name": "John F. Kennedy International Airport", "Location": "New York"}
}

@app.route('/airport/<icao>')
def airport_info(icao):
    icao = icao.upper()
    if icao in airports:
        response = {
            "ICAO": icao,
            "Name": airports[icao]["Name"],
            "Location": airports[icao]["Location"],
            "status": 200
        }
        return response
    else:
        response = {
            "message": "Airport not found",
            "status": 404
        }
        json_response = json.dumps(response)
        http_response = Response(response=json_response, status=404, mimetype="application/json")
        return http_response

@app.errorhandler(404)
def page_not_found(error_code):
    response = {
        "message": "Invalid endpoint",
        "status": 404
    }
    json_response = json.dumps(response)
    http_response = Response(response=json_response, status=404, mimetype="application/json")
    return http_response

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)


# Example request http://127.0.0.1:5000/airport/EFHK