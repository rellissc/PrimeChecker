class PrimeBlueprint:
	"""Blueprint of Prime Item. Holds references to the required parts"""
	
	def __init__(self, name, url='NO',vaulted=False, listOfParts=None, tags=[]):
		self.name=name
		if (url=='NO'):
			url=str(name).replace(' ','_')
		self.url='https://warframe.fandom.com'+url
		self.vaulted=vaulted
		if listOfParts is None:
			self.listOfParts=[]
		else:
			self.listOfParts=listOfParts
		self.tags=[]

	def __str__(self):
		return self.name

	def __repr__(self):
		return self.name

	def getURL(self):
		return self.url

	def AddPart(self, part):
		self.listOfParts.append(part)



class PrimePart:
	"""Parts of Primes """
	
	def __init__(self, name, amount=1, listOfParts=[]):
		self.name=name
		self.amount=amount
		self.listOfParts=listOfParts

	def __str__(self):
		return '<'+self.name+', '+str(self.amount)+'>'

	def __repr__(self):
		return str(self)







