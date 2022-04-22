import random
class Ball:
    def __init__(self,canvas):
        self.canvas=canvas
        self.xpos = random.randint(0,400)
        self.ypos = random.randint(0,400)
        self.dia = random.randint(0,30)
        self.dx = random.randint(0,30)
        self.dy = random.randint(0,30)
        r=random.randint(0,255)
        g=random.randint(0,255)
        b=random.randint(0,255)
        self.img = canvas.create_oval(self.xpos,self.ypos,self.xpos+self.dia,self.ypos+self.dia,fill="cyan")

    def move(self):
        self.canvas.move(self.img,self.dx,self.dy)
        self.xpos += self.dx
        self.ypos += self.dy
        if(self.ypos + self.dia > 400 or self.ypos<0):
            self.dy=-self.dy
        if(self.xpos + self.dx > 430 or self.xpos<0):
            self.dx=-self.dx
