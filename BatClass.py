class Bat:
    def __init__(self,canvas):
        self.canvas=canvas
        self.bar=canvas.create_rectangle(150,380,100,390,outline="black",fill="#FFFFFF")

    def move_left(self):
        self.canvas.move(self.bar,-5,0)

    def move_right(self):
        self.canvas.move(self.bar,+5,0)
        
        
