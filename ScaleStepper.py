import tkinter as tk
from tkinter import ttk
import math
import functools

class ScaleStepper(ttk.Scale):

	def __init__(self,*args,**kwargs):
		self.step=kwargs.pop('step')
		self.name=kwargs.pop('name')
		self.chain=kwargs.pop('command', lambda *a: None)
		super(ScaleStepper,self).__init__(*args, command=self._value_changed, **kwargs)

	def get(self):
		#print("overridden")
		val=super(ScaleStepper,self).get()
		return math.floor(float(val)/self.step)*self.step

	def _value_changed(self, newvalue):
		newvalue = math.floor(float(newvalue)/self.step)*self.step
		#newvalue = round(float(newvalue), self.step)
		self.winfo_toplevel().globalsetvar(self.cget('variable'), (newvalue))
		self.chain(int(newvalue))
		#self.snapToValue()# Call user specified function.

	def snapToValue(self):
		self.set(self.get())

def printVal(event):
	name=event.widget.name
	val=event.widget.get()
	event.widget.snapToValue()
	print(name + ' ' + str(val))
	
window=tk.Tk()
testList=['a','b','c']
for item in testList:
	scale=ScaleStepper(window, from_=0, to=3, step=1, name=item)
	scale.bind('<ButtonRelease-1>',printVal )
	scale.pack()
window.mainloop()