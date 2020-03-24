
import bs4 as BS
import urllib.request
#import PrimeItem
from PrimeItem import PrimeBlueprint, PrimePart
from tkinter import *
from tkinter import ttk
import json


def GetPrimeList():
	source = urllib.request.urlopen('https://warframe.fandom.com/wiki/Prime').read()
	soup=BS.BeautifulSoup(source,'html.parser')
	dictOfGalleries={'gallery-0':'Warframe','gallery-1':'Primary','gallery-2':'Secondary','gallery-3':'Melee','gallery-4':'Comanion','gallery-6':'Archwing'}
	#dictOfGalleries={'gallery-0':'Warframe','gallery-1':'Primary'}
	dictionaryOfBlueprints={}
	for key in dictOfGalleries:
		galleriesBlueprints=[]
		galleryDiv=soup.find('div',id=key)
		divs=galleryDiv.find_all('div',class_='lightbox-caption')
		if (key != 'gallery-4' and key != 'gallery-6'): #Companion and Archwing sections structured differently
			for div in divs:
				u=div.span.a.get('href')
				bp=PrimeBlueprint(div.span.get('data-param'), url=u)
				bp=FillBlueprint(bp)
				galleriesBlueprints.append(bp)

				#print(galleriesBlueprints.pop())

				#print(div.span.get('data-param'))
		else:
			for div in divs:
				u=div.a.get('href')
				bp=PrimeBlueprint(div.a.get('title'),url=u)
				bp=FillBlueprint(bp)
				galleriesBlueprints.append(bp)

				#print(div.a.get('title'))
		dictionaryOfBlueprints[dictOfGalleries[key]]=galleriesBlueprints
	#testDiv=soup.find('div', id='gallery-0')

	#gal0divs=testDiv.find_all('div',class_='lightbox-caption')
	##gal0divs=testDiv.find_all('div',class_='wikia-gallery-item')
	#for div in gal0divs:
	#	print(div.span.get('data-param'))
	#	print(div.span.a.get('href'))
	#	#print(div.find('div',class_='lightbox-caption'))
	#print(dictionaryOfBlueprints)

	return dictionaryOfBlueprints


def FillBlueprint(blueprint:PrimeBlueprint):
	source=urllib.request.urlopen(blueprint.getURL())
	bpSoup=BS.BeautifulSoup(source,'html.parser')
	bpTable=bpSoup.find('table', class_='foundrytable')
	#try:
	if(bpTable):
		element=bpTable.find_all('tr')
		tdList=element[1].find_all('td')
		#listOfParts=[]
		i=0
		while i<5:
			if(tdList[i].a):
				try:
					amount=int(tdList[i].text.replace(',',''))
				except:
					amount=1

				blueprint.AddPart(PrimePart(tdList[i].a.get('title'),amount))
				#listOfParts.append(tdList[i].a.get('title'))
				# check contents for number of items

			i+=1
		#listOfParts.append(tdList[1].a.get('title'))
		#listOfParts.append(tdList[2].a.get('title'))
		#listOfParts.append(tdList[3].a.get('title'))
		#print(blueprint.name+': '+str(listOfParts))
		#print(blueprint.listOfParts)
	return blueprint
		

def createJSONFile(listOfGalleries):
	galleryJSON='{"Galleries":['
	firstGallery=True
	for key in listOfGalleries:
		if not firstGallery:
			galleryJSON+=','
		firstGallery=False
		galleryJSON+='{"'+key+'":['
		firstPrime=True
		for prime in listOfGalleries[key]:
			if firstPrime:
				galleryJSON+=prime.JSONFormat()
				firstPrime=False
			else:
				galleryJSON+=','+prime.JSONFormat()
		galleryJSON=galleryJSON+']}'

	galleryJSON=galleryJSON+']}'

	with open('galleryJSON.json','w+') as myJSON:
		myJSON.write(galleryJSON)
	print(galleryJSON)


def readJSONFile(fileName):
	toReturn={}
	with open(fileName) as f:
		toReturn=json.load(f)
	return toReturn


def windowCreation(dictionaryOfGalleries):
	window=Tk()
	window.title('Prime List')
	window.geometry('900x900')
	TAB_CONTROL=ttk.Notebook(window)
	TAB1=ttk.Frame(TAB_CONTROL)
	TAB_CONTROL.add(TAB1,text='Warframes')

	TAB2=ttk.Frame(TAB_CONTROL)
	TAB_CONTROL.add(TAB2,text='Primaries')
	TAB_CONTROL.pack(expand=1, fill='both')
	ttk.Label(TAB1, text='Warframes go here').grid(column=0,row=0,padx=10,pady=10)
	ttk.Label(TAB2, text='Primary Weapons go here').grid(column=0,row=0,padx=10,pady=10)
	window.mainloop()


#createJSONFile(GetPrimeList())
print(readJSONFile('galleryJSON.json')['Galleries'])

#windowCreation()

