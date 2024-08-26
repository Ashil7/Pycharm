import requests

from pprint import pprint

API_key='182b91931b4e4256b9fee16ab2b7d8b8'

'''baseURL='https://newsapi.org/v2/everything?'

title=input("Enter Topic:")

final_URL=baseURL+'q='+title+"&apiKey="+API_key

NewsData=requests.get(final_URL).json()

pprint(NewsData)
'''

baseURL='https://newsapi.org/v2/top-headlines?'

country=input("Enter Country:")

final_URL=baseURL+'country='+country+"&apiKey="+API_key

NewsData=requests.get(final_URL).json()

pprint(NewsData)


