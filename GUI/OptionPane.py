started = 0.0
def moneyinvest(): 
	canvas = Canvas(root, width=1800, height = 1050)
	root = Tk()
	root.geometry("1800x1050")
	frame = Frame(root)
	invest = Entry(root, text= "How much money do you want to invest?")
	root.mainloop()

def lt(): #TODO: Use functions for machine learning but long term here
	root = Tk()
	root.geometry("1800x1050")
	canvas = Canvas(root, width=1800, height = 1050)
	frame = Frame(root)
	text1 = Text(top)
	text1.insert(INSERT, "You have selected a Long-Term Investment")
	text1.insert(END, ".")
	text1.pack()
	root.mainloop()

def st(): #TODO: Use functions for machine learning but short term here
	root = Tk()
	root.geometry("1800x1050")
	canvas = Canvas(root, width=1800, height = 1050)
	frame = Frame(root)
	text2 = Text(top)
	text2.insert(INSERT, "You Have Selected a Short-Term Investment")
	text2.insert(END, ".")
	text2.pack()
	root.mainloop()

def stlt():
	root = Tk()
	root.geometry("1800x1050")
	canvas = Canvas(root, width=1800, height = 1050)
	frame = Frame(root)
	LongTerm = Button(root, text="Long-Term")
	ShortTerm = Button(root, text="Short-Term")
	LongTerm.pack()
	ShortTerm.pack()
	LongTerm.config(command=lt)
	ShortTerm.config(command=st)
	root.mainloop()

def v():
	frame = Frame(root)
	root = Tk()
	root.geometry("1280x720")
	canvas = Canvas(root, width=1800, height = 1050)
	hv = Button(root)
	hv.pack()
	hv.config(command) #Add Volatility Graph/Suggestions (ML)
	lv = Button(root)
	lv.pack()
	root.mainloop()



from Tkinter import *
from PIL import ImageTk, Image

def LV():
	print('longer yay')

def HV(): #Change 
	HV = Tk()
	HV.geometry("1280x720")


def Volatility():
	yeet = Tk()
	yeet.geometry("1280x720")
	C = Canvas(yeet, height=720, width = 1280)
	Starting_Image = PhotoImage(file= "//Users//abhinavkeswani//Desktop//Stockboi//Icons//slide1.jpeg")
	Button1 = Button(yeet, text= "High Volatility")
	Button1.pack()
	Button2 = Button(yeet, text="Low Volatility")
	Button2.pack()
	Button1.config(command=HV)
	Button2.config(command=LV)
	root.mainloop()

def Starting():
	yeet = Tk()
	yeet.geometry("1234x720")
	filename = ImageTk.PhotoImage(file = "/Users/abhinavkeswani/Desktop/Stockboi/Icons/slide2edit.gif")
	background_label = Label(yeet, image=filename)
	background_label.pack()
	background_label.place(x=0, y=0, relwidth=1, relheight=1)
	button2 = Button(yeet, text="")
	button2.pack(height=130, width=981)
	button2.place(x=53, y=370)
	button2.config(command=Volatility)
	yeet.mainloop()

#actual code is one line lol

window = Tk()
window.geometry("1234x720")

StartButton = Button(window, text="Press To Start")

StartButton.pack()

StartButton.place(anchor=N)

StartButton.config(command=Starting)
# window.mainloop()

C = Canvas(window, bg="blue", height=720, width=1234)
filename = ImageTk.PhotoImage(file = "/Users/abhinavkeswani/Desktop/Stockboi/Icons/slide2edit.gif")
background_label = Label(window, image=filename)
background_label.pack()
background_label.place(x=0, y=0, relwidth=1, relheight=1)

window.mainloop()







