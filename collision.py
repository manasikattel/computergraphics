from tkinter import *
from tkinter import Tk
import tkinter as tk
import random
import time
import os

def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)


def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
tk.Canvas.create_circle = _create_circle

def sel():
    print(var.get())
    if var.get() == 1:
        run = Button(canvas, text='Run', font="Times 15 bold", command=elastic_collision)
    else:
        run = Button(canvas, text='Run', font="Times 15 bold", command=inelastic_collision)
    canvas.create_window(370, oy + 130, window=run, height=25, width=50)

def inelastic_collision():
    u1 = float(u1_entry.get())
    u2 = float(u2_entry.get())
    m1 = float(m1_entry.get())
    m2 = float(m2_entry.get())

    KE=1/2* m1 *u1*u1 + 1/2* m2* u2*u2
    KE1=canvas.create_text(900, oy + 135, text=round(KE), font="Times 15 bold")
    mom1=canvas.create_text(800, oy + 135, text=round(m1*u1,2), font="Times 15 bold")
    mom2=canvas.create_text(800, oy + 175, text=round(m2*u2,2), font="Times 15 bold")

    r_max = 50
    if (m1 > m2):
        r1 = r_max
        r2 = m2 / m1 * r1

    else:
        r2 = r_max
        r1 = m1 / m2 * r2

    if (r1 > 1 and r2 > 1):
        ball1 = canvas.create_circle(ox + 100, 300 - r1, r1, fill='orange')
        ball2 = canvas.create_circle(ox + 800, 300 - r2, r2, fill='orange')
    elif (r1 > r2):
        r1 = 50
        r2 = 5
        ball1 = canvas.create_circle(ox + 100, 300 - r1, r1, fill='orange')
        ball2 = canvas.create_circle(ox + 800, 300 - r2, r2, fill='orange')
    elif (r1 < r2):
        r1 = 5
        r2 = 50
        ball1 = canvas.create_circle(ox + 100, 300 - r1, r1, fill='orange')
        ball2 = canvas.create_circle(ox + 800, 300 - r2, r2, fill='orange')

    v = (m1*u1 + m2*u2)/(m1+m2)
    canvas.create_text(650, oy + 135, text=round(v,2), font="Times 15 bold")
    canvas.create_text(650, oy + 175, text=round(v,2), font="Times 15 bold")

    clock = 0.001

    t = 0
    x = 0
    x1 = 0
    x2 = 0
    #print(((ox + 100 + x1) - (ox + 800 - x2)))
    #print(r1 + r2)
    while (-(ox + 100 + x1) + (ox + 800 - x2)) >= r1 + r2:
        #print('a')
        x1 = (u1 * t)
        x2 = (u2 * t)
        tk.update()
        time.sleep(clock)
        canvas.delete(ball1)
        canvas.delete(ball2)

        ball1 = canvas.create_circle(ox + 100 + x1, 300 - r1, r1, fill='orange')
        ball2 = canvas.create_circle(ox + 800 - x2, 300 - r2, r2, fill='red')
        a = ox + 100 + x1
        b = ox + 800 - x2

        t += clock
    canvas.delete(ball1)
    canvas.delete(ball2)
    canvas.delete(mom1)
    canvas.delete(mom2)
    mom1 = canvas.create_text(800, oy + 135, text=round(m1 * u1, 2), font="Times 15 bold")
    mom2 = canvas.create_text(800, oy + 175, text=round(m2 * u2, 2), font="Times 15 bold")

    KE=1/2* (m1+m2)*v*v
    canvas.delete(KE1)
    KE1=canvas.create_text(900, oy + 135, text=round(KE), font="Times 15 bold")
    t = 0
    while (1):
        ball1 = canvas.create_circle(a + x1, 300 - r1, r1, fill='orange')
        ball2 = canvas.create_circle(b + x2, 300 - r2, r2, fill='red')

        x1 = (-v * t)
        x2 = (-v * t)

        #print(x2)
        tk.update()
        time.sleep(clock)
        canvas.delete(ball1)
        canvas.delete(ball2)

        t += clock


def elastic_collision():
    u1 = float(u1_entry.get())
    u2 = float(u2_entry.get())
    m1 = float(m1_entry.get())
    m2 = float(m2_entry.get())

    KE=1/2* m1 *u1*u1 + 1/2* m2* u2*u2
    KE1=canvas.create_text(900, oy + 135, text=round(KE), font="Times 15 bold")
    r_max = 50
    if (m1 > m2):
        r1 = r_max
        r2 = m2 / m1 * r1

    else:
        r2 = r_max
        r1 = m1 / m2 * r2


    if(r1>1 and r2>1):
        ball1 = canvas.create_circle(ox + 100, 300 - r1, r1, fill='orange')
        ball2 = canvas.create_circle(ox + 800, 300 - r2, r2, fill='orange')
    elif(r1>r2):
        r1=50
        r2=5
        ball1 = canvas.create_circle(ox + 100, 300 - r1, r1, fill='orange')
        ball2 = canvas.create_circle(ox + 800, 300 - r2, r2, fill='orange')
    elif (r1 < r2):
        r1 = 5
        r2 = 50
        ball1 = canvas.create_circle(ox + 100, 300 - r1, r1, fill='orange')
        ball2 = canvas.create_circle(ox + 800, 300 - r2, r2, fill='orange')

    v1=((m1-m2)/(m1+m2))*u1 + 2*m2*u2 /(m1+m2)
    v2 = ((m2 - m1) / (m1 + m2)) * u2 + 2 * m1 * u1 / (m1 + m2)
    #print(v1,v2)
    canvas.create_text(650, oy + 135, text=round(v1,2), font="Times 15 bold")
    canvas.create_text(650, oy + 175, text=round(v2,2), font="Times 15 bold")
    mom1 = canvas.create_text(800, oy + 135, text=round(m1 * u1, 2), font="Times 15 bold")
    mom2 = canvas.create_text(800, oy + 175, text=round(m2 * u2, 2), font="Times 15 bold")

    clock = 0.001

    t=0
    x=0
    x1=0
    x2=0
    #print(((ox + 100+x1) -(ox + 800-x2)))
    #print(r1+r2)
    while (-(ox + 100+x1) +(ox + 800-x2))>=r1+r2:
            #print('a')
            x1 = (u1 * t )
            x2=(u2*t)
            tk.update()
            time.sleep(clock)
            canvas.delete(ball1)
            canvas.delete(ball2)

            ball1 = canvas.create_circle(ox + 100+x1, 300 - r1, r1, fill='orange')
            ball2 = canvas.create_circle(ox + 800-x2, 300 - r2, r2, fill='red')
            a=ox + 100+x1
            b=ox + 800-x2


            t += clock
    canvas.delete(ball1)
    canvas.delete(ball2)
    canvas.delete(mom1)
    canvas.delete(mom2)

    mom1 = canvas.create_text(800, oy + 135, text=round(m1 * v1, 2), font="Times 15 bold")
    mom2 = canvas.create_text(800, oy + 175, text=round(m2 * v2, 2), font="Times 15 bold")

    t=0
    while(1):
        ball1 = canvas.create_circle(a + x1, 300 - r1, r1, fill='orange')
        ball2 = canvas.create_circle(b - x2, 300 - r2, r2, fill='red')

        x1 = (-v1 * t )
        x2=(-v2*t)

        #print(x2)
        tk.update()
        time.sleep(clock)
        canvas.delete(ball1)
        canvas.delete(ball2)


        t += clock


tk=Tk()


tk.title('collision')


canvas=Canvas(tk, width=tk.winfo_screenwidth(),height=tk.winfo_screenheight())

canvas.pack()

ox,oy=100,450


var = IntVar()


table = canvas.create_polygon(50, 300, 1000, 300, 1000, 310, 50, 310, fill='PaleVioletRed1')

canvas.create_text(20,oy+100, text="Ball",font="Times 15 bold")
canvas.create_text(20,oy+135, text="A",font="Times 15 bold")
canvas.create_text(20,oy+175, text="B",font="Times 15 bold")
canvas.create_text(100,oy+100, text="Mass (kg)",font="Times 15 bold")
canvas.create_text(250,oy+100, text="initial velocity (m/s)",font="Times 15 bold")
canvas.create_text(650,oy+100, text="final velocity (m/s)",font="Times 15 bold")
canvas.create_text(600,oy+135, text="v1 =",font="Times 15 bold")
canvas.create_text(600,oy+175, text="v2 =",font="Times 15 bold")
canvas.create_text(800,oy+100, text="Momentum =",font="Times 15 bold")
canvas.create_text(950,oy+100, text="Kinetic Energy =",font="Times 15 bold")




u1_label=Label(canvas, text="u1:",font="Times 15 bold")
m1_label=Label(canvas, text="m1: ",font="Times 15 bold")
u2_label=Label(canvas, text="u2:",font="Times 15 bold")
m2_label=Label(canvas, text="m2: ",font="Times 15 bold")

canvas.create_window(220, oy+135, window=u1_label, height=25, width=40)
canvas.create_window(220, oy+170, window=u2_label, height=25, width=40)

canvas.create_window(100, oy+135, window=m1_label, height=25, width=40)
canvas.create_window(100, oy+170, window=m2_label, height=25, width=40)

u1_entry = Entry(canvas)
u2_entry = Entry(canvas)
m1_entry = Entry(canvas)
m2_entry = Entry(canvas)

canvas.create_window(270, oy+135, window=u1_entry, height=25, width=50)
canvas.create_window(270, oy+170, window=u2_entry, height=25, width=50)
canvas.create_window(140, oy+135, window=m1_entry, height=25, width=50)
canvas.create_window(140, oy+170, window=m2_entry, height=25, width=50)

#tk1=Frame(canvas)

global comm
R1=Radiobutton(canvas,text='Elastic collision',width = 20,padx = 100,variable=var,value=1,command=sel)
R2=Radiobutton(canvas,text='Inelastic collision',width = 20,padx = 100,variable=var,value=2,command=sel)

canvas.create_window(470, oy+130, window=R1, height=25, width=100)
canvas.create_window(470, oy+170, window=R2, height=25, width=100)


clear=Button(canvas, text='Clear',font="Times 15 bold", command=restart_program)
canvas.create_window(370, oy+170, window=clear, height=25, width=60)

    
mainloop()
