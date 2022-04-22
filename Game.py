from tkinter import *
from BallClass import *
from BatClass import *
import time
win=Tk()
win.title("GameProject")
win.geometry("700x600")

canvas=Canvas(win,width=450,height=400,bg="Black")
canvas.grid(row=0,column=1)


sidenav=Frame(win,width=150,height=400,bg="Blue")
sidenav.grid(row=0,column=0)

ballsList = []
for _ in range(10):
    ballsList.append(Ball(canvas))
    
win.update()
def start():
    while(1):
        for ball in ballsList:
            ball.move()
        win.update()
        time.sleep(0.05)

run = True
def stop():
    global run
    if run:
        win.after_cancel(run)
        run=False


bar=Bat(canvas)

def left(event):
    bar.move_left()

def right(event):
    bar.move_right()

win.bind('<Left>',left)
win.bind('<Right>',right)






win.update()

    

b=Button(win,text="Start", command=start)
b.grid(row=0,column=0)

b1=Button(win,text="Stop",command=stop)
b1.grid(row=1,column=0)


    
win.update()
    




win.mainloop()
