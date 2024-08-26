import requests

from pprint import pprint

API_key='9cf8af40cebb3f604a056d6ca7b6848c'

base_URL="http://api.openweathermap.org/data/2.5/weather?"

cityId=input("Enter city ID:")

Final_URL=base_URL+"appid="+API_key+"&id="+cityId

weatherData=requests.get(Final_URL).json()

pprint(weatherData)