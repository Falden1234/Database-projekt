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
    select_label = Label(master, text='')
    a2 = inkoebs_liste.get(ACTIVE)
    print("Du har Købt: " + str(a2))
    inkoebs_liste.delete(0,END)
    id = d.name_id(a2)
    print(id)
    ordre = d.add_ordre(id)
    print(d.show_ordre(ordre))

def add():
    select_label = Label(master, text='')
    a2 = produkt_liste.get(ANCHOR)
    print("Du har valgt: " + str(a2) )
    inkoebs_liste.insert(END, a2)

def Fjern():
    select_label = Label(master, text='')
    a2 = inkoebs_liste.get(ANCHOR)
    idx = inkoebs_liste.get(0, END).index(a2)
    inkoebs_liste.delete(idx)
    print("Du har fjernet: " + str(a2) )

Add_to_shopping_cart = Button(master, text="Add to shopping cart", width = 17, height = 2, command = add, bg = ColorInput).place(x=85, y=240)

Buy = Button(master, text="Buy", width = 15, height = 2, command = buy, bg = ColorInput).place(x=250, y=240)

Fortryd = Button(master, text="Fjern fra kurv", width = 15, height = 2, command = Fjern, bg = ColorInput).place(x=185, y=310)


produkt_liste = Listbox(master, width=15)
produkt_liste.place(x=85, y=25)
for p in d.product_id():
    navn = d.id_name(p)
    produkt_liste.insert(END, navn)


inkoebs_liste = Listbox(master, width=15)
inkoebs_liste.place(x=275, y=25)
# inkoebs_liste.insert(END, '')





def slut ():
    master.destroy()

SlutKnap = Button(master, text="End", width = 15, height = 2, command = slut, bg = ColorInput).place(x=185, y=400)

master.mainloop()
