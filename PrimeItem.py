

class PrimeBlueprint:
	"""Blueprint of Prime Item. Holds references to the required parts"""
	
	def __init__(self, name, url='NO', vaulted=False, listOfParts=None, tags=[]):
		self.name = name
		if url == 'NO':
			url = str(name).replace(' ', '_')
		self.url = 'https://warframe.fandom.com'+url
		self.vaulted = vaulted
		if listOfParts is None:
			self.listOfParts = []
		else:
			self.listOfParts = listOfParts
		self.tags = []
		self.completed=False

	def __str__(self):
		return self.name

	def __repr__(self):
		return self.name

	def getURL(self):
		return self.url

	def AddPart(self, part):
		self.listOfParts.append(part)

	def JSONFormatReady(self):
		partsList=[]
		for part in self.listOfParts:
			partsList.append(part.JSONFormatReady())

		jsonDict={"name":str(self.name), 
			"url":self.url,
			"listOfParts":partsList,
			"completed":self.completed}

		return jsonDict

		#jsonString = '{"name":"'+self.name + '",\n'
		#jsonString += '"url":"'+self.url + '",\n'
		## jsonString+='"vaulted":"'+self.vaulted +'",\n'
		#jsonString += '"listOfParts":['
		#first = True
		#for part in self.listOfParts:
		#	if first:
		#		jsonString += part.JSONFormat()
		#		first = False
		#	else:
		#		jsonString += ',\n'+part.JSONFormat()
		#jsonString = jsonString+']'
		#jsonString += '}'

		#return jsonString


class PrimePart:
	"""Parts of Primes """
	
	def __init__(self, name, amount = 1, amountOwned = 0):
		self.name = name
		self.amount = amount
		self.amountOwned = 0

	def __str__(self):
		return '<'+self.name+', '+str(self.amount)+'>'

	def __repr__(self):
		return str(self)

	def JSONFormatReady(self):
		jsonDict = {"name": self.name,
			  "amount": self.amount,
			  "amountOwned" : self.amountOwned}
		return jsonDict
		#jsonString = '{"partName":"'+self.name+'",'
		#jsonString += '"amount":'+str(self.amount)+''

		#jsonString += '}'

		#return jsonString
