from tkinter import *

window = Tk()

window.title("Formula UI")
window.geometry('1200x700')

def UI_object(object):
    def __init__(self, master):
        self.master = master

# Create a rectangular area
canvas = Canvas(window, width=350, height=200)
canvas.pack()

# Draw some lines on it
canvas.create_line(0, 80, 350, 80)

# Draw a rectangle bar 1
canvas.create_rectangle(10, 50, 50, 200, fill="red")

# Draw a rectangle bar 2
canvas.create_rectangle(60, 30, 100, 200, fill="orange")

# Draw a rectangle bar 3
canvas.create_rectangle(110, 80, 150, 200, fill="blue")

window.mainloop()