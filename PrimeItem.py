class PrimeBlueprint:
	"""Blueprint of Prime Item. Holds references to the required parts"""
	
	def __init__(self, name, url='NO',vaulted=False, listOfParts=[], tags=[]):
		self.name=name
		if (url=='NO'):
			url='https://warframe.fandom.com/wiki/'+str(name).replace(' ','_')
		self.url=url
		self.vaulted=vaulted
		self.listOfParts=listOfParts
		self.tags=[]

	def __str__(self):
		return self.name

	def __repl__(self):
		return self.name




class PrimePart:
	"""Parts of Primes """
	
	def __intit__(self, name, listOfParts=[]):
		self.name=name
		self.listOfParts=listOfParts

	def __str__(self):
		return self.name

	def __repl__(self):
		return self.name





