import tkinter as tk

root = tk.Tk()

canvas_width = 600
canvas_height = 400
w, h  = canvas_width // 2, canvas_height // 2
canvas = tk.Canvas(root, width=canvas_width, height = canvas_height)

import tkinter as tk
 
root = tk.Tk()
 
canvas_width = 600
canvas_height = 400
w, h  = canvas_width // 2, canvas_height // 2
canvas = tk.Canvas(root, width=canvas_width, height = canvas_height)
canvas.pack()
 
r1 = canvas.create_rectangle(w,h, w+10, h+10)
                              
def keypress(event):
	x, y = 0, 0
	if event.char == "a": x = -10; 
	elif event.char == "d": x = 10
	elif event.char == "w": y = -10
	elif event.char == "s": y = 10
	canvas.move(r1, x, y)
 
root.bind("<Key>", keypress)
 
root.mainloop()
