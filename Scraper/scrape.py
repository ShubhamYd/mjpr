import requests
from bs4 import BeautifulSoup
import csv

URL = "https://venturebeat.com"
page = requests.get(URL)

soup = BeautifulSoup(page.content,'html.parser')

article_elements = soup.find_all('article',class_='ArticleListing')

images = []
titles = []
links = []

for artelem in article_elements[:8]:
	imglink = artelem.find('img',class_='ArticleListing__image')

	if(imglink['src']):
		images.append(imglink['src'])
	else:
		continue
	
	titlelink = artelem.find('h2',class_="ArticleListing__title")
	titles.append(titlelink.text)

	linkers = artelem.find('a',class_="ArticleListing__image-link")
	links.append(linkers['href'])


for i in images:
	print("images ",i)

for t in titles:
	print("titles ",t)

for l in links:
	print("links ",l)

fields=['images','links','titles']
rows =[]
for i in range(8):
	rows.append([images[i],links[i],titles[i]])


with open('latest.csv','w') as f:
	write = csv.writer(f)
	write.writerow(fields)
	write.writerows(rows)
