from tkinter import *
import tkinter as tk



def ROUND(a):
	return int(a + 0.5)

def drawDDA(x1,y1,x2,y2):
	x,y = x1,y1
	length = (x2-x1) if (x2-x1) > (y2-y1) else (y2-y1)
	dx = (x2-x1)/float(length)
	dy = (y2-y1)/float(length)
	print ('x = %s, y = %s' % (((ROUND(x),ROUND(y)))))
	for i in range(length):
		x += dx
		y += dy
		canvas.create_text(ROUND(x), ROUND(y), fill="darkblue", font="Times 8 bold", text=".")


root=Tk()

canvas=Canvas(root, width=800,height=800)

canvas.pack()

canvas.create_text(100,10,fill="darkblue",font="Times 10 italic bold",text=".")

drawDDA(100,5,100,500)
drawDDA(100,500,700,500)

print("enter x values")
x=[]
x = list(map(int, input().split()))
print("enter y values")
y=[]
y = list(map(int, input().split()))
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
print(a)
for i in range(0,len(x)-1):
    drawDDA(int(x[i]),int(y[i]),int(x[i+1]),int(y[i+1]))

for i in range(0,len(x)):
    canvas.create_text(x[i], 500, fill="darkblue", font="Times 20 bold", text=".")
    canvas.create_text(x[i], 550, fill="darkblue", font="Times 10 bold", text=str(a[i]))
    canvas.create_text(60, y[i]+10, fill="darkblue", font="Times 10 bold", text=str(b[i]))

    canvas.create_text(100, y[i], fill="darkblue", font="Times 20 bold", text=".")

canvas=Canvas(root, width=800,height=800)

canvas.pack()


mainloop()