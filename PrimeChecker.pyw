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
		

def createJSONFile(listOfGalleries):
	galleryJSON = '{"Galleries":['
	firstGallery = True
	for key in listOfGalleries:
		if not firstGallery:
			galleryJSON += ','
		firstGallery = False
		galleryJSON += '{"galleryName":"'+key+'", "primes":['
		firstPrime = True
		for prime in listOfGalleries[key]:
			if firstPrime:
				galleryJSON += prime.JSONFormat()
				firstPrime = False
			else:
				galleryJSON += ','+prime.JSONFormat()
		galleryJSON = galleryJSON + ' ]}'

	galleryJSON = galleryJSON + ']}'

	with open('galleryJSON.json', 'w+') as myJSON:
		myJSON.write(galleryJSON)
	print(galleryJSON)


def readJSONFile(fileName):
	with open(fileName) as f:
		toReturn = json.load(f)
	return toReturn


def windowCreation(dictionaryOfGalleries):

	Window = Tk()
	Window.title('Prime List')
	# window.geometry('900x900')
	tabControl = ttk.Notebook(Window)
	
	for gallery in dictionaryOfGalleries:
		tab = ttk.Frame(tabControl)
		tabControl.add(tab, text=gallery['galleryName'])
		col = 0
		row = 0

		for prime in gallery['primes']:
			ttk.Button(tab, text=prime['name']).grid(column=0, row=row, sticky='ew')
			row += 1
	tabControl.pack(expand=1, fill='both')
	# TAB_CONTROL=ttk.Notebook(window)
	# TAB1=ttk.Frame(TAB_CONTROL)
	# TAB_CONTROL.add(TAB1,text='Warframes')

	# TAB2=ttk.Frame(TAB_CONTROL)
	# TAB_CONTROL.add(TAB2,text='Primaries')
	# TAB_CONTROL.pack(expand=1, fill='both')
	# ttk.Label(TAB1, text='Warframes go here').grid(column=0,row=0,padx = 10,pady = 10)
	# ttk.Label(TAB2, text='Primary Weapons go here').grid(column=0,row=0,padx=10,pady=10)
	Window.mainloop()


# createJSONFile(GetPrimeList())
Dict = readJSONFile('galleryJSON.json')['Galleries']
window = PrimeCheckerApp(Dict, title='Warframe Prime Checker')
window.mainloop()
# windowCreation(dict)
