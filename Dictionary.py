import PyDictionary
import pyttsx3
import tkinter
from tkinter import *
from PIL import ImageTk, Image

#-------------------------------------------------------------------------------------------------------------------------------------------------

# Creating PyDictionary Object
pydict = PyDictionary.PyDictionary()
# Initializing pyttsx3
speech = pyttsx3.init()
# Delcaring result global string
res = ""

# All function's definition

def onClick_enbtn():
	global speech
	a = entry.get()	
	if a is not None:
		speech.say(a)
		speech.runAndWait()

def onClick_sbtn():
	global res
	a = entry.get()
	if len(a) != 0:
		mean = pydict.meaning(a)
		mean["Synonym"] = pydict.synonym(a)
		mean["Antonym"] = pydict.antonym(a)
		res = "\n\n" \
			.join(f"{k}: {v[:2]}" \
			for k, v in mean.items() \
			if v is not None)
		dtext.set(res)
				
def onClick_mnbtn():
	global res, speech
	if res is not None:
		speech.say(res)
		speech.runAndWait()

def onClick_clr():
	global res
	res = ""
	entry.delete(0, "end")
	dtext.set("")

#-------------------------------------------------------------------------------------------------------------------------------------------------

# Creating window
root = tkinter.Tk()

# Setting title of created window
root.title("English dictionary")

# Setting size of crreated window
root.geometry("600x400")

# Making window unresizable
root.resizable(0,0)

# Stting Background colour of created window
root.configure(bg = "black")

#-------------------------------------------------------------------------------------------------------------------------------------------------

# WIDGETS Section

# Creating ENTER WORD Label
enlabel = Label(
	root, 
	text  = "Enter Word: ",
	font = ("Verdana", 15),
	bg = "#000000",
	fg = "#ffffff",
	)
enlabel.pack()

# Crating ENTRY widget to get search element
entry = Entry(
	root,
	bg = "cyan",
	fg = "#000000",
	font = ("comic sans ms", 13),
	)
entry.pack()

# Creating BUTTON to read search element
img = ImageTk.PhotoImage(Image.open("mic_image.png"))
enbtn = Button(
	root, 
	image = img,
	bg = "#000000",
	command = onClick_enbtn,
	)
enbtn.pack()

# Creating SERACH button
sbtn = Button(
	root, 
	text = "Search",
	font = ("Times new roman", 15),
	bg = "#0A79DF",
	fg = "#ffffff",
	command = onClick_sbtn,
	)
sbtn.pack()

# Creating LABEL menu to display meaning
dtext = StringVar()
mnlabel = Label(
	root, 
	text = "",
	bg = "#F9DDA4",
	fg = "#000000",
	font = ("Verdana", 10),
	textvariable = dtext,
	wraplength = 425,
	anchor = NW,
	justify = LEFT,
	width = 52,
	height = 14,
	border = 2,
	)
mnlabel.pack(ipadx = 10, ipady = 10)

# Creating BUTTON mbtn
mnbtn = Button(
	root, 
	image = img,
	bg = "#000000",
	command = onClick_mnbtn,
	)
mnbtn.pack()

# Creating QUIT button
qbtn = Button(
	root,
	text = "Quit",
	font = ("Times new roman", 15),
	bg = "#0A79DF",
	fg = "white",
	command = root.quit,
	)
qbtn.pack()

# Creating CLEAR button
clr = Button(
	root,
	text = "Clear",
	font = ("Times new roman", 15),
	bg = "#0A79DF",
	fg = "white",
	command = onClick_clr,
	)
clr.pack()

#-------------------------------------------------------------------------------------------------------------------------------------------------

# Positioning of WIDGETS
enlabel.place(x = 150, y = 17)
entry.place(x = 280 , y = 20)
enbtn.place(x = 525, y = 19)
sbtn.place(x = 275, y = 75)
mnlabel.place(x = 85, y = 140)
mnbtn.place(x = 525, y = 140)
qbtn.place(x = 20, y = 335)
clr.place(x = 525, y = 335)

#-------------------------------------------------------------------------------------------------------------------------------------------------

# Refreshes the window all the time
root.mainloop()