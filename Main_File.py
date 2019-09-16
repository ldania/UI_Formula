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


class frames_data:
    def __init__(self, relx, rely, relheight, relwidth, rel2x = None, rel2y = None, rel2height = None, rel2width = None):
        
        self.toggle = 1
        self.relx = relx
        self.rely = rely
        self.relheight = relheight
        self.relwidth  = relwidth
        
        
        self.rel1x = relx
        self.rel1y = rely
        self.rel1height = relheight
        self.rel1width  = relwidth
        
        self.rel2x = rel2x
        self.rel2y = rel2y
        self.rel2height = rel2height
        self.rel2width  = rel2width

    def repos_val(self, rel2x = None, rel2y =  None, rel2height = None, rel2width = None):
        self.rel2x = rel2x
        self.rel2y = rel2y
        self.rel2height = rel2height
        self.rel2width  = rel2width

    
    def repos(self):
        if(self.toggle == 1):
            self.relx = self.rel1x
            self.rely = self.rel1y
            self.relheight = self.rel1height
            self.relwidth = self.rel1width
            self.toggle = 0
        
        else:
            self.relx = self.rel2x
            self.rely = self.rel2y
            self.relheight = self.rel2height
            self.relwidth = self.rel2width
            self.toggle = 1
            
        
        
       

class Layout(Frame):
    
    def __init__(self, parent =  None):
        Frame.__init__(self, master)
        self.master =  master

        
        
        
        self.left1_button = Button(self, text = "Test", command = self.test)
        self.left2_button = Button(self, text = "Test", command = self.test)
        self.left3_button = Button(self, text = "Test", command = self.test)
        
        
        self.mid1 = Frame(parent, bd=1, relief=SUNKEN, bg = 'snow')
        # Left 1 Data and Reposition value
        """
        self.left1_data = frames_data( 0, 0, 0.33, 0.15)
        self.left1_data.repos_val( 0.15, 0.5, 0.5, 0.7)
        self.left1 = Frame(parent, bd=1, relief=RAISED, bg = 'BLUE')
        
        
        self.left2_data = frames_data( 0, 0.33, 0.33, 0.15)
        self.left2_data.repos_val( 0.15, 0.5, 0.5, 0.7)
        self.left2 = Frame(parent, bd=1, relief=RAISED, bg = 'yellow')
        
        
        
        self.left3_data = frames_data( 0, 0.66, 0.33, 0.15)
        self.left3_data.repos_val( 0.15, 0.5, 0.5, 0.7)
        self.left3 = Frame(parent, bd=1, relief=RAISED, bg = 'red')
        
        
        

        self.mid2 = Frame(parent, bd=1, relief=SUNKEN)
        
        self.right1 = Frame(parent, bd=1, relief=RAISED)
        self.right2 = Frame(parent, bd=1, relief=RAISED)
        self.right3 = Frame(parent, bd=1, relief=RAISED)       
        #self.
        
        """
        
        
    def display(self):

        self.pack(fill = BOTH, expand  = 1)
        self.left1_button.place(relx = 0, rely = 0, relwidth = 0.15, relheight = 0.33)
        
        self.pack(fill = BOTH, expand  = 1)
        self.left2_button.place(relx = 0, rely = 0.33, relwidth = 0.15, relheight = 0.33)

        self.pack(fill = BOTH, expand  = 1)
        self.left3_button.place(relx = 0, rely = 0.66, relwidth = 0.15, relheight = 0.33)        
        """
        self.left1.place(relx = self.left1_data.relx   
                        ,rely = self.left1_data.rely
                        ,relheight = self.left1_data.relheight  
                        ,relwidth = self.left1_data.relwidth)
        """
        
        """
        
        self.left2.place(relx = self.left2_data.relx   
                        ,rely = self.left2_data.rely
                        ,relheight = self.left2_data.relheight  
                        ,relwidth = self.left2_data.relwidth)
        
        
        self.left3.place(relx = self.left3_data.relx   
                        ,rely = self.left3_data.rely
                        ,relheight = self.left3_data.relheight  
                        ,relwidth = self.left3_data.relwidth)
        """
        #self.left2.place(relx = 0   , rely = 0.33,  relheight = 0.33  , relwidth = 0.15)
        #self.left3.place(relx = 0   , rely = 0.66,  relheight = 0.33  , relwidth = 0.15)
        
        
        

        

        #self.right1.place(relx = 1- self.split  , rely = 0   ,  relheight = 0.33  , relwidth = 0.15)
        #self.right2.place(relx = 1- self.split  , rely = 0.33,  relheight = 0.33  , relwidth = 0.15)
        #self.right3.place(relx = 1- self.split  , rely = 0.66,  relheight = 0.33  , relwidth = 0.15)
               
        self.mid1.place( relx = 0.15, rely = 0,     relheight  =0.5, relwidth= 0.7)
        #self.mid2.place( relx = 0.15, rely = 0.5,   relheight =0.5,  relwidth= 1 - 2* self.split)
        
    def split_val(self, split_val):
        self.old_relx = relx
        self.old_rely = rely
        self.old_height = relheight
        self.old_relwidth = relwidth


    def callback(self, event):
        self.left1_data.repos()

        self.display()
        
    def test(self):
        print("Test")

    


 
        


windowX = 1200
windowY = 840    
 
winsize = str(windowX) + 'x' + str(windowY)
master = Tk()
master.geometry(winsize)


                
    
Lay = Layout(master)



Lay.display()






 
master.update()
master.mainloop()




