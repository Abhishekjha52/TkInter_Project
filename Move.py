import tkinter as tk
import time

root = tk.Tk()

canvas = tk.Canvas(root)
canvas.pack()

canvas.create_rectangle(150, 50, 0, 0, tags="Bob", fill='light blue', outline='green')


for _ in range(600):
    canvas.move("Bob", 5, 0)
    canvas.update()
    time.sleep(0.05)

root.mainloop()
