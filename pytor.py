#!/usr/bin/env python3

from tkinter import *
from tkinter.filedialog import *

filename = None

def newFile():
	global filename
	filename = "Untitled"
	text.delete(0.0, END)

def saveFile():
	t = text.get(0.0, END)
	f = open(filename, 'w')
	f.write(t)
	f.close()

def saveAs():	
	f = asksaveasfile(mode='w', defaultextension='.txt')
	t = text.get(0.0, END)
	try:
		f.write(t.rstrip())
	except:
		showerror(title="Error", message="Unable to save file...")

def openFile():
	f = askopenfile(mode='r')
	t = f.read()
	text.delete(0.0, END)
	text.insert(0.0, t)

root = Tk()
root.title("Pytor Editor")
root.minsize(width=400, height=400)
root.maxsize(width=9999, height=9999)

textBox = Text(root, width=400, height=400)
textBox.pack()

menubar = Menu(root)
filemenu = Menu(menubar)
filemenu.add_command(label="New File", command=newFile)
filemenu.add_command(label="Save File", command=saveFile)
filemenu.add_command(label="Save As", command=saveAs)
filemenu.add_command(label="Open File", command=openFile)
filemenu.add_separator()
filemenu.add_command(label="Quit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

root.config(menu=menubar)
root.mainloop()

