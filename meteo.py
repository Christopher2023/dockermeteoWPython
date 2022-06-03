import requests
import os

api_key = os.environ["API_KEY"]

url = "http://api.openweathermap.org/data/2.5/weather?"

url = url + "lat=" + os.environ["LAT"] + "&lon=" + os.environ["LONG"] + "&appid=" + api_key

response = requests.get(url).json()

if response["cod"] != "404":
    print(response)
else:
    print("Coordonnees invalides")