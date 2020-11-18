import pandas as pd

import requests
from bs4 import BeautifulSoup

page = requests.get('https://forecast.weather.gov/MapClick.php?lat=37.2057&lon=-93.2971#.Xu-WXJpKjDc')
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup)
week = soup.find(id='seven-day-forecast-body')
print(week)
print()
print()
items= week.find_all(class_='tombstone-container')


print(items[0].find(class_='period-name').get_text())
print(items[0].find(class_='short-desc').get_text())
print(items[0].find(class_='temp').get_text())
print()
print()
print()

period_names=[i.find(class_='period-name').get_text() for i in items]
print(period_names)
short_description=[i.find(class_='short-desc').get_text() for i in items]
print(short_description)
temperature=[i.find(class_='temp').get_text() for i in items]
print(temperature)
print()
print()
print()



weather_stuff= pd.DataFrame({
    'period': period_names,
    'description': short_description,
    'temperature': temperature,
})
print(weather_stuff)
weather_stuff.to_csv('weather.csv')