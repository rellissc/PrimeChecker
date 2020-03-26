import tkinter as tk
from tkinter import ttk
from functools import partial



class PrimeCheckerApp(tk.Tk):
    def RevealFrame(self, frame):
        frame.grid(column=1, row=0)

    def donothing(self):
        print("Refresh")

    def __init__(self, Dict, title, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title(title)
        menuBar=tk.Menu(self)
        filemenu=tk.Menu(menuBar, tearoff=0)
        filemenu.add_command(label='Refresh', command=self.donothing)
        menuBar.add_cascade(label="File", menu=filemenu)
        self.config(menu=menuBar)


        #  print(Dict)
        tabControl = ttk.Notebook(self)
        listOfdictOfFrames = []  # this is unused
        style = ttk.Style(tabControl)
        style.configure('LeftTab.TNotebook', tabposition='wn')
        for gallery in Dict:
            tab = ttk.Frame(tabControl)
            tabControl.add(tab, text=gallery)
            
            notebook = ttk.Notebook(tab, style='LeftTab.TNotebook')
            for prime in Dict[gallery]:
                f = tk.Frame(notebook, width=200, height=200)
                row = 0
                for part in prime['listOfParts']:
                    ttk.Label(f, text=part['name']+':').grid(row=row, column=0, sticky='e')
                    sb = ttk.Spinbox(f, from_=0, to=part['amount'])
                    sb.delete(0,"end")
                    sb.insert(0,part['amountOwned'])
                    sb.grid(row=row, column=1)
                    ttk.Label(f, text='/'+str(part['amount'])).grid(row=row, column=2, sticky='w')
                    row += 1
                notebook.add(f, text=prime['name'])
                #  frame=ttk.Frame(tab)
                #  label=ttk.Label(frame,text=prime['name'])
                
                #  frame.grid(column=1, row=0)
                #  revealFunc=partial(self.revealFrame,frame)
                #  ttk.Button(tab,text=prime['name'], command=revealFunc).grid(column=0,row=row, sticky='ew')
                #  row+=1
            notebook.pack(expand=1, fill='both')

            tabControl.pack(expand=1, fill='y')
