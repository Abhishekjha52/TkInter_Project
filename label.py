class Bat:
    def __init__(self,canvas):
        self.xpos=
        self.ypos=
        self.canvas=canvas
        self.img=canvas.create_oval(50,50,20,20,outline="black",fill="#FFFFFF")

    def move(self):
        self.canvas.move(self.img,5,5)
