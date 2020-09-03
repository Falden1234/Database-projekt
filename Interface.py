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

image=ImageTk.PhotoImage(Image.open("C:robot.png"))

canvas.create_image(0,0,anchor=NW,image=image)
canvas.pack()

#color#
ColorInput = "light sky blue"

Color = "snow"

A = 1
B = 1
w1 = 1
w2 = 1
k1 = 1
k2 = 1
phi = 1
#v = 1

A1 = StringVar()
A1.set(" ")
B1 = StringVar()
B1.set(" ")
C1 = StringVar()
C1.set(" ")
D1 = StringVar()
D1.set(" ")
E1 = StringVar()
E1.set(" ")
F1 = StringVar()
F1.set(" ")
G1 = StringVar()
G1.set(" ")
# H1 = StringVar()
# H1.set(" ")

t_vals = [v *0.01 for v in range((2*314))]

def x(t):
    return A * math.sin(w1 * t * phi) + k1

def y(t):
    return B * math.sin(w2 * t) + k2



A = Label(master, text= "A = ", width = 5, height = 1, bg = ColorInput).place(x=120, y=60)


a = Entry(master,textvariable= A1, bg = Color)
a.place(x=185, y= 60)

B = Label(master, text= "B = ", width = 5, height = 1, bg = ColorInput).place(x=120, y=80)

b = Entry(master,textvariable= B1, bg = Color)
b.place(x=185, y= 80)

w1 = Label(master, text= "w1 = ", width = 5, height = 1, bg = ColorInput).place(x=120, y=100)

W_1 = Entry(master,textvariable= C1, bg = Color)
W_1.place(x=185, y= 100)

w2 = Label(master, text= "w2 = ", width = 5, height = 1, bg = ColorInput).place(x=120, y=120)

W_2 = Entry(master,textvariable= D1, bg = Color)
W_2.place(x=185, y= 120)

k1 = Label(master, text= "k1 = ", width = 5, height = 1, bg = ColorInput).place(x=120, y=140)

k_1 = Entry(master,textvariable= E1, bg = Color)
k_1.place(x=185, y= 140)

k2 = Label(master, text= "k2 = ", width = 5, height = 1, bg = ColorInput).place(x=120, y=160)

k_2 = Entry(master,textvariable= F1, bg = Color)
k_2.place(x=185, y= 160)

phi = Label(master, text= "Φ = ", width = 5, height = 1, bg = ColorInput).place(x=120, y=180)

phi_phi = Entry(master,textvariable= G1, bg = Color)
phi_phi.place(x=185, y= 180)


def clear():
    global A1
    global B1
    global C1
    global D1
    global E1
    global F1
    global G1
    #global H1

    A1.set(" ")
    B1.set(" ")
    C1.set(" ")
    D1.set(" ")
    E1.set(" ")
    F1.set(" ")
    G1.set(" ")
    #H1.set(" ")


def random():
    global A1
    global B1
    global C1
    global D1
    global E1
    global F1
    global G1
    #global H1

    A1.set(randint(1,9))
    B1.set(randint(1,9))
    C1.set(randint(1,9))
    D1.set(randint(1,9))
    E1.set(randint(1,9))
    F1.set(randint(1,9))
    G1.set(randint(1,9))

def x(t):
    A = float(a.get())
    B = float(b.get())
    w1 = float(W_1.get())
    w2 = float(W_2.get())
    k1 = float(k_1.get())
    k2 = float(k_2.get())
    phi = float(phi_phi.get())
    return A * math.sin(w1 * t * phi) + k1

def y(t):
    A = float(a.get())
    B = float(b.get())
    w1 = float(W_1.get())
    w2 = float(W_2.get())
    k1 = float(k_1.get())
    k2 = float(k_2.get())
    phi = float(phi_phi.get())
    return B * math.sin(w2 * t) + k2

def plot():

    x_vals = [x(t) for t in t_vals]
    y_vals = [y(t) for t in t_vals]


    plt.plot(x_vals, y_vals,"blue")
    plt.show()

    input()


def RobotTegning ():

    global x_vals
    global y_vals

    x_vals = [x(t) for t in t_vals]
    y_vals = [y(t) for t in t_vals]

    l = [[x_vals[i],y_vals[i]] for i in range(0,len(x_vals))]
    minx = miny = 10000
    maxx = maxy = -10000
    sumx = 0
    sumy = 0
    for p in l:
        sumx += p[0]
        sumy += p[1]
        if p[0] > maxx:
            maxx = p[0]
        if p[0] < minx:
            minx = p[0]
        if p[1] > maxy:
            maxy = p[1]
        if p[1] < miny:
            miny = p[1]
    avgx = sumx / len(l)
    avgy = sumy / len(l)
    scalex = maxx - minx
    scaley = maxy - miny
    print("Tegningens størrelse: {},{}".format(scalex,scaley))
    for p in l:
        p[0] -= avgx
        p[1] -= avgy
        p[0] /= scalex
        p[1] /= scaley
        p[0] *= 0.10
        p[1] *= 0.10
        p[0] += prog.tegne_limits[0] + math.fabs(prog.tegne_limits[0]-prog.tegne_limits[2])/2
        p[1] += prog.tegne_limits[1] + math.fabs(prog.tegne_limits[1]-prog.tegne_limits[3])/2



    prog.move_path(l)


def move_home():
    prog.move_home()


def move():
    prog.move_xyz(-0.480,-0.298,0.342)

PlotKnap = Button(master, text="Tegning", width = 15, height = 2, command = plot, bg = "medium spring green").place(x=185, y=240)

RandomKnap = Button(master, text="Random", width = 15, height = 2, command = random, bg = ColorInput).place(x=300, y=240)

Clear = Button(master, text="Clear", width = 15, height = 2, command = clear, bg = ColorInput).place(x=75, y=240)

Robot = Button(master, text="Robot", width = 15, height = 2, command = RobotTegning, bg = "red").place(x=105, y=300)


Home = Button(master, text="Home", width = 15, height = 2, command = move_home, bg = "red").place(x=245, y=300)



def slut ():
    master.destroy()

SlutKnap = Button(master, text="End", width = 15, height = 2, command = slut, bg = ColorInput).place(x=185, y=400)

master.mainloop()
