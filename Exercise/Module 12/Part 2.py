import requests

api_key = "CK284"
city = input("Enter municipality name: ")

request = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

try:
    response = requests.get(request)
    if response.status_code == 200:
        data = response.json()
        description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        print(f"Weather: {description}")
        print(f"Temperature: {temperature} Celsius")
    else:
        print(f"Error: Failed to fetch weather data. Status code {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Request error: {e}")
