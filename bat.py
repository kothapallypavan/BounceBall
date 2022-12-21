from tkinter import *

class Bat:
    def __init__(self,canvas):
        self.xpos = 100
        self.ypos = 110
        self.x=200
        self.y=550
        self.velx = 0
        self.canvas = canvas
        self.img = canvas.create_rectangle(self.x,self.y,self.x+100,self.y+15,fill='white')
        self.p = self.canvas.coords(self.img)

    def bat_left(self):
        try:
            a = self.canvas.coords(self.img)
            if a[0]<=0:
                self.canvas.move(self.img,0,0)
            else:
                self.canvas.move(self.img,-50,0)
        except:
            pass

    def bat_right(self):
        try:
            print(self.canvas.coords(self.img))
            a = self.canvas.coords(self.img)
            if a[0]>=545:
                self.canvas.move(self.img,0,0)
            else:
                self.canvas.move(self.img,50,0)
        except:
            pass

    def destorybat(self):
        self.canvas.delete(self.img)

    def re(self):
        return self.canvas.coords(self.img)
