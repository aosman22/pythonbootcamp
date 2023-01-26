from bs4 import BeautifulSoup
import requests
import re

url = 'https://www.live-footballontv.com/chelsea-on-tv.html'

result = requests.get(url)
doc = BeautifulSoup(result.text, 'html.parser')

fixturedate = doc.find(class_="fixture-date")
print(fixturedate.string)

time = doc.find(class_="fixture__time")
print(time.string)

teams = doc.find(class_="fixture__teams")
print(teams.string)

competition = doc.find(class_="fixture__competition")
print(competition.string)

teams = doc.find(class_="fixture__teams")
print(teams.string)

matchdate = fixturedate.string
todaysdate = "Friday 3rd February 2023"

if todaysdate == matchdate:
    print(f"MATCHDAY: {teams.string}at {time.string}")
else:
    print("error")



