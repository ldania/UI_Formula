from tkinter import *
import math



split = 0.5







def cos(a):
    return(math.cos(a/math.pi * 180))

def sin(a):
    return(math.sin(a/math.pi * 180))





class pindex(object):
    
    
    def __init__(self, canvas, centerx, centery, size):
        self.angle      = 0
        
        
        self.centerx    = centerx
        self.centery    = centery
        self.size       = size
        self.canvas     = canvas
        
        self.index      = canvas.create_polygon(
                [       self.centerx + self.size * cos(angle)     ,  self.centery + self.size * sin(angle)  ,
                        self.centerx + self.size * cos(angle + 90) , self.centery + self.size * sin(angle + 90),
                        self.centerx + self.size * cos(angle + 180), self.centery + self.size * sin(angle + 180) ,  
                        self.centerx + self.size * cos(angle + 270), self.centery + self.size * sin(angle + 270)] ,     
                        outline='gray', 
                        fill='gray', width=2)
    
    def rotate(self):
        self.angle += 1




class Layout(object):
    
    def __init__(self, parent):
        self.split = 0.15
        
        self.left1 = Frame(parent, bd=1, relief=RAISED)
        self.left2 = Frame(parent, bd=1, relief=RAISED)
        self.left3 = Frame(parent, bd=1, relief=RAISED)
        
        
        self.mid1 = Frame(parent, bd=1, relief=SUNKEN)
        self.mid2 = Frame(parent, bd=1, relief=SUNKEN)
        
        self.right1 = Frame(parent, bd=1, relief=RAISED)
        self.right2 = Frame(parent, bd=1, relief=RAISED)
        self.right3 = Frame(parent, bd=1, relief=RAISED)       
        #self.
        
        
        
    def display(self):
        self.left1.place(relx = 0   , rely = 0,     relheight = 0.33  , relwidth = 0.15)
        self.left2.place(relx = 0   , rely = 0.33,  relheight = 0.33  , relwidth = 0.15)
        self.left3.place(relx = 0   , rely = 0.66,  relheight = 0.33  , relwidth = 0.15)
        
        
        
        self.mid1.place( relx = 0.15, rely = 0,     relheight  =0.5, relwidth= 1- 2*self.split)
        self.mid2.place( relx = 0.15, rely = 0.5,   relheight =0.5, relwidth= 1 - 2* self.split)
        

        self.right1.place(relx = 1- self.split  , rely = 0   ,  relheight = 0.33  , relwidth = 0.15)
        self.right2.place(relx = 1- self.split  , rely = 0.33,  relheight = 0.33  , relwidth = 0.15)
        self.right3.place(relx = 1- self.split  , rely = 0.66,  relheight = 0.33  , relwidth = 0.15)
        
  

    def callback(self,event):
        if( self.split == 0.9):
            self.split  = 0.5
        
        else:
            self.split = 0.9
            print("EVENT")
        
        self.display()
            



windowX = 1200
windowY = 840    
 
winsize = str(windowX) + 'x' + str(windowY)
master = Tk()
master.geometry(winsize)


                
    
Lay = Layout(master)



Lay.display()






Lay.left1.bind("<Button-1>", Lay.callback)

 
master.update()
master.mainloop()




