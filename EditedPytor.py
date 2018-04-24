#!/usr/bin/env python3

from tkinter import *
from tkinter.filedialog import *

filename = None

def newFile():
	global filename
	filename = "Untitled.txt"
	textBox.delete(0.0, END)

def saveFile():
	t = textBox.get(0.0, END)
	try:
		f = open(filename, 'w')
		f.write(t)
		f.close()
	except:
		saveAs()
	#fix the problem of the first unsave file

def saveAs():	
	f = asksaveasfile(mode='w', defaultextension='.txt')
	t = textBox.get(0.0, END)
	try:
		f.write(t.rstrip())
	except:
		showerror(title="Error", message="Unable to save file...")

def openFile():
	f = askopenfile(mode='r')
	t = f.read()
	textBox.delete(0.0, END)
	textBox.insert(0.0, t)

def undo():
	textBox.event_generate('<<Undo>>')

def redo():
	textBox.event_generate('<<Redo>>')

def cut():
	textBox.event_generate('<<Cut>>')

def copy():
	textBox.event_generate('<<Copy>>')

def paste():
	textBox.event_generate('<<Paste>>')





root = Tk()
root.title("Pytor Editor")
root.minsize(width=1024, height=400)
root.maxsize(width=1520, height=800)

textBox = Text(root, width=400, height=400)
textBox.pack()

menubar = Menu(root)
#file menu
filemenu = Menu(menubar)
filemenu.add_command(label="New File", command=newFile)
filemenu.add_command(label="Save File", command=saveFile)
filemenu.add_command(label="Save As", command=saveAs)
filemenu.add_command(label="Open File", command=openFile)
filemenu.add_separator()
filemenu.add_command(label="Quit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)


#edit menu
editmenu = Menu(menubar)
editmenu.add_command(label="Undo", command=undo)
editmenu.add_command(label="Redo", command=redo)
editmenu.add_separator()
editmenu.add_command(label="Copy", command=copy)
editmenu.add_command(label="Cut", command=cut)
editmenu.add_command(label="Paste", command=paste)
menubar.add_cascade(label="Edit", menu=editmenu)

root.config(menu=menubar)
root.mainloop()
