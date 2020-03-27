import tkinter as tk
from tkinter import ttk

window=tk.Tk();
window.title='test';
testDict={'credits':25, 'neuroptics':1,'systems':1,'chassis':1,'orokin cells':5}
tDictVar={}
row=0
for key in testDict:
    tDictVar[key]=tk.IntVar(window)
    tDictVar[key].set(testDict[key])
    ttk.Scale(window, from_=1, to=25, step=1, variable=tDictVar[key]).grid(row=row, column=0)
    ttk.Label(window, textvar=tDictVar[key]).grid(row=row, column=1)
    row+=1

window.mainloop()


