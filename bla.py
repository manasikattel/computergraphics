from tkinter import *
import tkinter as tk


def get_line(x0,y0,xn,yn):

    x=[]
    x.append(x0)
    y=[]
    y.append(y0)


    dx = xn - x0
    dy = yn - y0

    # Determine how steep the line is


    # Rotate line
    if abs(dy) <= abs(dx):
        p=[]
        p0=(2*dy) - dx
        p.append(p0 )
        for i in range(0,dx-1-1):

            if p[i]<0:
                p.append(p[i] + 2 * dy)
                x.append(x[i]+1)
                y.append(y[i])
                canvas.create_text(x[i]+1, y[i], fill="darkblue", font="Times 8 bold", text=".")#plot xk+1,yk)
            else:
                p.append( p[i] + 2*dy - 2*dx)
                x.append(x[i] + 1)
                y.append(y[i] + 1)
                canvas.create_text(x[i] + 1, y[i]+1, fill="darkblue", font="Times 8 bold", text=".")
                #plotxk,yk+1)

    if abs(dy) > abs(dx):
        p=[]
        p0=(2*dx) - dy
        p.append(p0 )
        for i in range(0,dy-1):

            if p[i]<0:
                p.append(p[i] + 2 * dx)
                x.append(x[i])
                y.append(y[i]+1)
                canvas.create_text(x[i], y[i]+1, fill="darkblue", font="Times 8 bold", text=".")#plot xk+1,yk)
            else:
                p.append( p[i] + 2*dx - 2*dy)
                x.append(x[i] + 1)
                y.append(y[i] + 1)
                canvas.create_text(x[i] + 1, y[i]+1, fill="darkblue", font="Times 8 bold", text=".")
                #plotxk,yk+1)


root=Tk()
canvas=Canvas(root, width=800,height=800)

canvas.pack()

canvas.create_text(100,10,fill="darkblue",font="Times 10 italic bold",text=".")



print("enter x values")
x=[]
x = list(map(int, input().split()))
print("enter y values")
y=[]
y = list(map(int, input().split()))

get_line(100,500,750,500)
get_line(100,5,100,500)

highestx=x[0]
highesty=y[0]
a=[]
b=[]
a=list(x)
b=list(y)
print(a)

for i in range(1,len(x)):

    if x[i]>highestx:
        highestx=x[i]

    if y[i]>highesty:
        highesty=y[i]

print('highestx'+str(highestx))

for i in range(0,len(x)):
    if x[i]!=highestx:
        x[i]=float(600/highestx)*x[i]+100


    if y[i]!=highesty:
        y[i]=500-float(490/highesty)*y[i]

for i in range(0,len(x)):
    if x[i]==highestx:
        x[i]=700
    if y[i]==highesty:
        y[i]=10

for i in range(0,len(x)-1):
    for j in range(0,len(x)-i-1):
        if(x[j]>x[j+1]):
            temp=x[j]
            x[j]=x[j+1]
            x[j+1]=temp
            temp=y[j]
            y[j]=y[j+1]
            y[j+1]=temp

for i in range(0,len(x)):
    get_line(int(x[i])-20,int(y[i]),int(x[i])+20,int(y[i]))
    get_line(int(x[i]) - 20, int(y[i]), int(x[i]) - 20, 500)
    get_line(int(x[i]) + 20, int(y[i]), int(x[i]) + 20, 500)

for i in range(0,len(x)):
    canvas.create_text(x[i], 500, fill="darkblue", font="Times 20 bold", text=".")
    canvas.create_text(x[i], 550, fill="darkblue", font="Times 10 bold", text=str(a[i]))
    canvas.create_text(60, y[i]+10, fill="darkblue", font="Times 10 bold", text=str(b[i]))
    canvas.create_text(100, y[i], fill="darkblue", font="Times 20 bold", text=".")



canvas.pack()


mainloop()