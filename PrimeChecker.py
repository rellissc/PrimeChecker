
import bs4 as BS
import urllib.request
#import PrimeItem
from PrimeItem import PrimeBlueprint, PrimePart
from tkinter import *
from tkinter import ttk
import json




#reload(PrimeItem)
def GetPrimeList():
	source = urllib.request.urlopen('https://warframe.fandom.com/wiki/Prime').read()
	soup=BS.BeautifulSoup(source,'html.parser')
	dictOfGalleries={'gallery-0':'Warframe','gallery-1':'Primary','gallery-2':'Secondary','gallery-3':'Melee','gallery-4':'Comanion','gallery-6':'Archwing'}
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
				galleriesBlueprints.append(PrimeBlueprint(div.a.get('title')))

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
		#print('Not creatable in foundery')
	#except:
	#	print('Not creatable in the foundery, source is :'+blueprint.getURL())



def windowCreation():
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

#ListToPrint=GetPrimeList()
testJ=PrimeBlueprint('Test Warframe',url="192.168.0.1/here")
testJ.AddPart(PrimePart('Credits',25000))
testJ.AddPart(PrimePart('Neruoptics',1))
testJ.AddPart(PrimePart('Chassis',1))
testJ.AddPart(PrimePart('System',1))
testJ.AddPart(PrimePart('Orokin Cell',10))

print(testJ.JSONFormat())
#windowCreation()

