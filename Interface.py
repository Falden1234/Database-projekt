import tkinter
from tkinter import *
from PIL import ImageTk,Image

from Database import Data
d = Data()

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
    a2 = produkt_liste.get(ANCHOR)
    print("Printer: " + str(a2))



def add():
    select_label = Label(master, text='')
    a2 = produkt_liste.get(ANCHOR)
    print("Du har valgt: " + str(a2))



Buy = Button(master, text="Buy", width = 15, height = 2, command = buy, bg = ColorInput).place(x=250, y=240)

Add_to_shopping_cart = Button(master, text="Add to shopping cart", width = 17, height = 2, command = add, bg = ColorInput).place(x=85, y=240)


produkt_liste = Listbox(master, width=15)
produkt_liste.place(x=85, y=25)

for p in d.product():
    pro = p
    produkt_liste.insert(END, pro)
    print(p)

# produkt_liste.insert(END, "Gul Legoklods")
# produkt_liste.insert(END, "Blå Legoklods")
# produkt_liste.insert(END, "Rød Legoklods1")

inkoebs_liste = Listbox(master, width=15)
inkoebs_liste.place(x=275, y=25)
inkoebs_liste.insert(END,'')





def slut ():
    master.destroy()

SlutKnap = Button(master, text="End", width = 15, height = 2, command = slut, bg = ColorInput).place(x=185, y=400)

master.mainloop()
