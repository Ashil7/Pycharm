import requests

from pprint import pprint

Api_key="9cf8af40cebb3f604a056d6ca7b6848c"

base_URL="http://api.openweathermap.org/data/2.5/weather?"

cityName=input("Enter City Name:")

finalUrl=base_URL+"appid="+Api_key+"&q="+cityName

weatherData=requests.get(finalUrl).json()

pprint(weatherData)

print(finalUrl)