import matplotlib.pyplot as plt
import math
from random import randint
import random
import tkinter
from tkinter import *
from PIL import ImageTk,Image


master = Tk()
master.title("Tegninger")
e = Entry(master)



canvas=Canvas(master,width=500,height=450)

#562 x 446
image=ImageTk.PhotoImage(Image.open("robot2.jpg"))

canvas.create_image(250,225,anchor=CENTER,image=image)
canvas.pack()

#color#
ColorInput = "light sky blue"

Color = "snow"

def buy():
    pass


def add():
    pass












Buy = Button(master, text="Buy", width = 15, height = 2, command = buy, bg = ColorInput).place(x=250, y=240)

Add_to_shopping_cart = Button(master, text="Add to shopping cart", width = 17, height = 2, command = add, bg = ColorInput).place(x=85, y=240)





def slut ():
    master.destroy()

SlutKnap = Button(master, text="End", width = 15, height = 2, command = slut, bg = ColorInput).place(x=185, y=400)

master.mainloop()
