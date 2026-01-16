
import tkinter
from tkinter import *


win = Tk()
f = Frame(win)
b1 = Button(f, text="One")
b2 = Button(f, text="Two")
b3 = Button(f, text="Three")


b1.pack(side=LEFT)
b2.pack(side=LEFT)
b3.pack(side=LEFT)

def but1():
    print("Button one was pushed")

b1.configure(text="Uno", command=but1)


blabel1 = Label(win, text="This label is over all buttons")
blabel1.pack()
f.pack()
 
