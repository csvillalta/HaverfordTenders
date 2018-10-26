from bs4 import BeautifulSoup
import requests
import datetime

r = requests.get('https://www.haverford.edu/dining-services/dining-center')
soup = BeautifulSoup(r.content, 'lxml')

menus = soup.select('.meal-container')

def checktendies():
	menu_num = 3
	if datetime.datetime.today().weekday() == 6:
		menu_num = 2
	for item in menus[:menu_num]:
		entries = item.select('p')
		for entry in entries:
			if "tenderloins" in entry.getText().lower(): # this should check for 'chicken breast tenderloins', but for testing purposes I often change the value
				return item.h4.getText().lower()
	return False

