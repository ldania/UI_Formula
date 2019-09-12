import tkinter as tk
from PIL import ImageTk
from PIL import Image


class SimpleApp(object):
    def __init__(self, master, filename, **kwargs):
        self.master = master
        self.filename = filename
        self.canvas = tk.Canvas(master, width=500, height=500)
        self.canvas.pack()

        self.update = self.draw().__next__
        master.after(100, self.update)

    def draw(self):
        image = Image.open(self.filename)
        angle = 0
        dir = 1
        while True:
            tkimage = ImageTk.PhotoImage(image.rotate(angle, center=(250,200)))
            canvas_obj = self.canvas.create_image(
                250, 250, image=tkimage)
            self.master.after_idle(self.update)
            yield
            self.canvas.delete(canvas_obj)
            angle += dir
            if(angle == 180 or angle == 0):
                dir  -= dir

root = tk.Tk()
app = SimpleApp(root, 'pointer.png')
root.mainloop()