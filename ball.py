from tkinter import *
from bat import *
from random import *

class Ball:

    def __init__(self,canvas,bat):
        self.score = 0
        self.sc="SCORE : "
        self.xpos = randint(100,500)
        self.ypos = 50
        self.x=10
        self.y=5
        self.c=0
        self.canvas = canvas
        self.bat = bat
        self.img = canvas.create_oval(self.xpos,self.ypos,self.xpos+50,self.ypos+50,fill='red')
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.text = StringVar()
        self.text.set(self.sc+"0")
        self.label = Label(self.canvas, textvariable=self.text,bg="yellow",font=(None,15))
        self.label.place(x=500,y=30)
        self.getvalue = 0

    def move(self):
        try:
            self.c+=1
            if self.c%100==0 and self.c<700:
                print(self.c)
                if self.x<0:
                    self.x-=1
                if self.y<0:
                    self.y-=1
                if self.x>0:
                    self.x+=1
                if self.y>0:
                    self.y+=1

            self.canvas.move(self.img,self.x,self.y)
            pos = self.canvas.coords(self.img)
            batp = self.bat.re()
            if pos[1]<=0:
                self.y = -self.y
            if pos[0]<=0:
                self.x = -self.x
            if pos[2]>=650:
                self.x = -self.x

            if pos[0] > batp[0]-30 and pos[2] < batp[2]+30 and abs(pos[3]-batp[3])<=5:
                self.y = -self.y
                self.score+=1
                self.scoretext = self.sc+str(self.score)
                self.text.set(self.scoretext)
            if pos[3]>batp[3]+20:
                self.canvas.move(self.img,0,0)
            if pos[3]>650:
                self.label.place(x=260,y=280)
                self.getvalue = 1
                self.bat.destorybat()
        except:
            pass


    def retvalue(self):
        return self.getvalue


