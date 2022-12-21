from tkinter import *
from ball import *
from bat import *

import time as time

win = Tk()
win.title("Bouncing ball")
win.geometry("800x600")
win.resizable(False,False)
canv = Canvas(win,width=800,height=600,bg="grey")
canv.grid(row=0,column=1)


side = Frame(win,height=600,width=150,bg="#B1E693")
side.grid(row=0,column=0)


bat = Bat(canv)
b=Ball(canv,bat)


def keypress(key):
    if(key.keysym=="Left" or key.keysym=="a"):
        bat.bat_left()
    if(key.keysym=="Right" or key.keysym=="d"):
        bat.bat_right()

win.bind('<Key>',lambda i:keypress(i))
win.update()

def startgame():
    while True:
        b.move()
        win.update()
        time.sleep(0.02)
        if b.getvalue == 1:
            btn2 = Button(side, text='RESTART', width=10,
                          height=1, bd='3', command=startgame)
            btn2.place(x=30, y=200)

btn = Button(side, text='START', width=10,
			height=1, bd='3', command=startgame)

btn.place(x=30, y=100)

btn2 = Button(side, text='STOP', width=10,
			height=1, bd='3', command=win.destroy)

btn2.place(x=30, y=150)

ctrlabel = Label(side,text ="USE ARROWS\nor\n'A' & 'D'",bg="#B1E693",font=(None,15))
ctrlabel.place(x=6,y=260)

def startgame():
    while True:
        b.move()
        win.update()
        time.sleep(0.02)
        if b.getvalue == 1:
            btn2 = Button(side, text='RESTART', width=10,
                          height=1, bd='3', command=startgame)
            btn2.place(x=30, y=200)

win.mainloop()
