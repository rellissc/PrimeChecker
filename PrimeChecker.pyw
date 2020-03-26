import bs4 as bs
import urllib.request
# import PrimeItem
from PrimeItem import PrimeBlueprint, PrimePart
from GUIManager import PrimeCheckerApp
from tkinter import *
from tkinter import ttk
import json


def GetPrimeList():
	source = urllib.request.urlopen('https://warframe.fandom.com/wiki/Prime').read()
	soup = bs.BeautifulSoup(source, 'html.parser')
	dictOfGalleries = {'gallery-0': 'Warframe', 'gallery-1': 'Primary', 'gallery-2': 'Secondary', 'gallery-3': 'Melee', 'gallery-4': 'Comanion', 'gallery-6': 'Archwing'}
	dictionaryOfBlueprints = {}
	for key in dictOfGalleries:
		galleriesBlueprints = []
		galleryDiv = soup.find('div', id=key)
		divs = galleryDiv.find_all('div', class_='lightbox-caption')
		if key != 'gallery-4' and key != 'gallery-6':  # Companion and Archwing sections structured differently
			for div in divs:
				u = div.span.a.get('href')
				bp = PrimeBlueprint(div.span.get('data-param'), url=u)
				bp = FillBlueprint(bp)
				galleriesBlueprints.append(bp)

		else:
			for div in divs:
				u = div.a.get('href')
				bp = PrimeBlueprint(div.a.get('title'), url=u)
				bp = FillBlueprint(bp)
				galleriesBlueprints.append(bp)

		dictionaryOfBlueprints[dictOfGalleries[key]] = galleriesBlueprints
	return dictionaryOfBlueprints


def FillBlueprint(blueprint: PrimeBlueprint):
	source = urllib.request.urlopen(blueprint.getURL())
	bpSoup = bs.BeautifulSoup(source, 'html.parser')
	bpTable = bpSoup.find('table', class_='foundrytable')
	# try:
	if bpTable:
		element = bpTable.find_all('tr')
		tdList = element[1].find_all('td')
		# listOfParts=[]
		i = 0
		while i < 5:
			if tdList[i].a:
				try:
					amount = int(tdList[i].text.replace(',', ''))
				except:
					amount = 1

				blueprint.AddPart(PrimePart(tdList[i].a.get('title'), amount))
				# listOfParts.append(tdList[i].a.get('title'))
				# check contents for number of items

			i += 1
		# listOfParts.append(tdList[1].a.get('title'))
		# listOfParts.append(tdList[2].a.get('title'))
		# listOfParts.append(tdList[3].a.get('title'))
		# print(blueprint.name+': '+str(listOfParts))
		# print(blueprint.listOfParts)
	return blueprint
		

def CreateJSONFile(listOfGalleries):
	galleryDict={}
	for key in listOfGalleries:
		primeJSON=[]
		for prime in listOfGalleries[key]:
			primeJSON.append(prime.JSONFormatReady())
		galleryDict[key]=primeJSON
	with open('galleryJSON.json','w+') as myJSON:
		json.dump(galleryDict, myJSON)

	#galleryJSON = '{"Galleries":['
	#firstGallery = True
	#for key in listOfGalleries:
	#	if not firstGallery:
	#		galleryJSON += ','
	#	firstGallery = False
	#	galleryJSON += '{"galleryName":"'+key+'", "primes":['
	#	firstPrime = True
	#	for prime in listOfGalleries[key]:
	#		if firstPrime:
	#			galleryJSON += prime.JSONFormat()
	#			firstPrime = False
	#		else:
	#			galleryJSON += ','+prime.JSONFormat()
	#	galleryJSON = galleryJSON + ' ]}'

	#galleryJSON = galleryJSON + ']}'

	#with open('galleryJSON.json', 'w+') as myJSON:
	#	myJSON.write(galleryJSON)
	#print(galleryJSON)


def ReadJSONFile(fileName):
	with open(fileName) as f:
		toReturn = json.load(f)
	return toReturn


#CreateJSONFile(GetPrimeList())
Dict = ReadJSONFile('galleryJSON.json')
window = PrimeCheckerApp(Dict, title='Warframe Prime Checker')
window.mainloop()
# windowCreation(dict)
