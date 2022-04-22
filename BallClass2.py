class Ball2:
    def __init__(self,canvas):
        self.canvas=canvas
        self.xpos = 100
        self.ypos = 0
        self.dia = 10
        self.dx = 1
        self.dy = 3
        self.img = canvas.create_oval(self.xpos,self.ypos,self.xpos+self.dia,self.ypos+self.dia,fill="blue")

    def move(self):
        self.canvas.move(self.img,self.dx,self.dy)
        self.xpos += self.dx
        self.ypos += self.dy
        if(self.ypos + self.dia > 400 or self.ypos<0):
            self.dy=-self.dy
        if(self.xpos + self.dx > 430 or self.xpos<0):
            self.dx=-self.dx
