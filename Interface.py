import tkinter
from tkinter import *
from PIL import ImageTk,Image
import socket
import time

from Database import Data
d = Data()

master = Tk()
master.title("Tegninger")
e = Entry(master)

canvas=Canvas(master,width=500,height=450)
#hej
#562 x 446
image=ImageTk.PhotoImage(Image.open("robot2.jpg"))

canvas.create_image(250,225,anchor=CENTER,image=image)
canvas.pack()

#color#
ColorInput = "light sky blue"

Color = "snow"

produkt_liste = Listbox(master, width=15)
produkt_liste.place(x=50, y=25)
pris_pro = Listbox(master, width=11)
pris_pro.place(x=145, y=25)
for p in d.product_id():
    navn = d.id_name(p)
    produkt_liste.insert(END, navn)
    pris = d.pris(p)
    pris_pro.insert(END, pris)


pris_liste = Listbox(master, width=14)
pris_liste.place(x=370, y=25)

inkoebs_liste = Listbox(master, width=15)
inkoebs_liste.place(x=275, y=25)
# inkoebs_liste.insert(END, '')


def status():
    TCP_PORT = 29999
    BUFFER_SIZE = 1024
    TCP_IP = '10.130.58.14' #INDTAST DEN RIGTIGE IP-ADRESSE HER!
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(10)
    try:
        s.connect((TCP_IP, TCP_PORT))
        response = s.recv(BUFFER_SIZE)
    except socket.error:
        print("Socket error")
        s.close()
    s.send(b"programState\n")
    response = s.recv(BUFFER_SIZE)
    print(response)
    s.close()
    return str(response)

task = inkoebs_liste.get(ANCHOR)

roed_klods = "roed_klods"

def perform_task(cmd):
    TCP_PORT = 29999
    BUFFER_SIZE = 1024
    TCP_IP = '10.130.58.14' #INDTAST DEN RIGTIGE IP-ADRESSE HER!
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(10)
    try:
        s.connect((TCP_IP, TCP_PORT))
        response = s.recv(BUFFER_SIZE)
    except socket.error:
        print("Socket error")
        s.close()


    x = "skaldefalde/roed_klods"
    y = "skaldefalde/gul_klods"
    z = "skaldefalde/blaa_klods"
    select_label = Label(master, text='')
    a2 = inkoebs_liste.get(ANCHOR)
    print("Du har Købt: " + str(a2))
    inkoebs_liste.delete(0,END)
    id = d.name_id(a2)
    print(id)
    ordre = d.add_ordre(id)
    print(d.show_ordre(ordre))

    if a2 == "DeadPool":
        task = "skaldefalde/roed_klods"
    if a2 == "SuperMan":
        task = "skaldefalde/blaa_klods"
    if a2 == "BatMan":
        task = "skaldefalde/gul_klods"
    print(task)


    st = "load /programs/{}.urp\n".format(task)
    s.send(bytearray(st,'utf8'))
    response = s.recv(BUFFER_SIZE)
    s.send(b"play\n")
    response = s.recv(BUFFER_SIZE)
    s.close()




def stop_task(cmd):
    TCP_PORT = 29999
    BUFFER_SIZE = 1024
    TCP_IP = '10.130.58.14' #INDTAST DEN RIGTIGE IP-ADRESSE HER!
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(10)
    try:
        s.connect((TCP_IP, TCP_PORT))
        response = s.recv(BUFFER_SIZE)
    except socket.error:
        print("Socket error")
        s.close()

    st = "load /programs/{}.urp\n".format(cmd)
    s.send(bytearray(st,'utf8'))
    response = s.recv(BUFFER_SIZE)
    s.send(b"stop\n")
    response = s.recv(BUFFER_SIZE)
    s.close()
    x = "roed_klods"



def buy():
    select_label = Label(master, text='')
    a2 = inkoebs_liste.get(ACTIVE)
    print("Du har Købt: " + str(a2))
    inkoebs_liste.delete(0,END)
    id = d.name_id(a2)
    print(id)
    ordre = d.add_ordre(id)
    print(d.show_ordre(ordre))

    if a2 == "DeadPool":
        task = x
    if a2 == "SuperMan":
        task = z
    if a2 == "Batman":
        task = y

def add():
    select_label = Label(master, text='')
    a2 = produkt_liste.get(ANCHOR)
    print("Du har valgt: " + str(a2) )
    inkoebs_liste.insert(END, a2)
    id = d.name_id(a2)
    pris = d.pris(id)
    pris_liste.insert(END, pris)

def Fjern():
    select_label = Label(master, text='')
    a2 = inkoebs_liste.get(ANCHOR)
    idx = inkoebs_liste.get(0, END).index(a2)
    inkoebs_liste.delete(idx)
    pris_liste.delete(idx)
    print("Du har fjernet: " + str(a2) )


Add_to_shopping_cart = Button(master, text="Add to shopping cart", width = 22, height = 2, command = add, bg = ColorInput).place(x=50, y=190)

Buy = Button(master, text="Buy", width = 15, height = 2, command = lambda: perform_task(task), bg = ColorInput).place(x=260, y=190)

Fortryd = Button(master, text="Fjern fra kurv", width = 15, height = 2, command = Fjern, bg = ColorInput).place(x=375, y=190)


def slut ():
    master.destroy()

SlutKnap = Button(master, text="End", width = 15, height = 2, command = slut, bg = ColorInput).place(x=185, y=400)

master.mainloop()
