from urllib import response
import requests

api_key = "240aa650f4db4e154a07d0459c30a347"

url = "http://api.openweathermap.org/data/2.5/weather?"

Lon = input("Enter the longitute : ")
Lat = input("Enter latitude : ")
url = url + "lat=" + Lat + "&lon=" + Lon + "&appid=" + api_key

response = requests.get(url).json()

if response["cod"] != "404":
    print(response)
else:
    print("Coordonnees invalides")