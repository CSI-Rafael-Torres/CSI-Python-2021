import requests
import bs4
webpage =requests.get ('https://forecast.weather.gov/MapClick.php?lat=42.26341000000008&lon=-71.80218999999994')
soup = bs4.BeautifulSoup(webpage.content,'html.parser')
sevenDay =soup.find(id="seven-day-forecast")
forecast_items = sevenDay.find_all(class_="tombstone-container")
tonight = forecast_items[1]
print(tonight.prettify())
period = tonight.find(class_="period-name").get_text()
print(period)

