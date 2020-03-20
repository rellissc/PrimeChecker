
import bs4 as BS
import urllib.request
from PrimeItem import PrimeItem
from tkinter import *


source = urllib.request.urlopen('https://warframe.fandom.com/wiki/Prime').read()
soup=BS.BeautifulSoup(source,'html.parser')
testDiv=soup.find('div', id='gallery-0')
x=PrimeItem()
gal0divs=testDiv.find_all('div',class_='lightbox-caption')
#gal0divs=testDiv.find_all('div',class_='wikia-gallery-item')
for div in gal0divs:
	print(div.span.get('data-param'))
	print(div.span.a.get('href'))
	#print(div.find('div',class_='lightbox-caption'))

print('done')
