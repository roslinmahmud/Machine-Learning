from tkinter import *
import random

# intializing canvas width & height
width = 600
height = 600

# initializing weight, bias & learning rate
m = 1
b = 0
lr = 0.0

# update learning rate respect to scale
def setLR(val):
    global lr
    lr = float(val)

# map function for normalization & coordinate conversion
def map(n, start1, stop1, start2, stop2):
    return ((n-start1)/(stop1-start1))*(stop2-start2)+start2

# reset the canvas data [reset Button]
def reset():
    points.clear()
    drawing_area.delete("all")
    m = 1
    b = 0

# Gradient Descent Algorithm for loss/error optimization
def gradientDescent():
    global m
    global b
    for x, y in points:
        Y = m*x+b
        error = Y-y
        m = m-(error*x*lr)
        b = b-(error*lr)
    #print(m, b)

# Draw points in the canvas
points = []
def drawPoint(event):
    x = event.x
    y = event.y

    x1, y1 = (x - 1), (y + 1)
    x2, y2 = (x + 1), (y - 1)
    drawing_area.create_oval(x1, y1, x2, y2, fill="black")

    x = map(x, 0, width, 0, 1)
    y = map(y, 0, height, 1, 0)
    points.append((x, y))

# Draw linear line 
lineId = None
def drawLine():
    global lineId
    if len(points) >= 2:
        gradientDescent()

        x1 = 0
        x2 = 1
        y1 = m*x1+b
        y2 = m*x2+b

        x1 = map(x1, 0, 1, 0, width)
        y1 = map(y1, 0, 1, height, 0)
        x2 = map(x2, 0, 1, 0, width)
        y2 = map(y2, 0, 1, height, 0)

        if lineId is not None:
            drawing_area.delete(lineId)
        lineId = drawing_area.create_line(x1, y1, x2, y2)

    drawing_area.after(100, drawLine)



root = Tk()
root.title("Linear Regression")

header = Frame(root)
header.pack(side=TOP)

lrScale = Scale(header, orient=HORIZONTAL, length=400, from_=0, to=1, resolution=0.01, label="Learning Rate", command=setLR)
lrScale.grid(row=0, column=0, rowspan=2)

resetBtn = Button(header, text="Reset", background="#d9534f", command=reset)
resetBtn.grid(row=0, column=1, padx=50)

drawing_area = Canvas(root, width=width, height=height,background="white")
drawing_area.bind("<Button-1>", drawPoint)
drawing_area.pack()


drawLine()

root.mainloop()
