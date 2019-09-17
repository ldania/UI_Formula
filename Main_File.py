from tkinter import *

import math



split = 0.5



global colorscheme

colorscheme = [['SteelBlue1', 'mint cream', 'CadetBlue1'],
               ['SteelBlue2', "navy"      , 'CadetBlue2'],
               ['SteelBlue3', 'gray'      , 'CadetBlue3']]


global colordict 


global FormulaOrange1
FormulaOrange1 =  '#ee6d24'


global FormulaBlue1
FormulaBlue1 =  '#12bfd7'

global FormulaBlack1
FormulaBlack1 = '#1d323e'

def cos(a):
    return(math.cos(a/math.pi * 180))

def sin(a):
    return(math.sin(a/math.pi * 180))




class pindex(object):
    
    
    def __init__(self, canvas, centerx, centery, size):
        self.angle      = 0
        self.colordict = 'navy'
        
        self.centerx    = centerx
        self.centery    = centery
        self.size       = size
        self.canvas     = canvas
    
        self.index      = canvas.create_polygon(
                [       self.centerx + self.size * cos(self.angle)     ,  self.centery + self.size * sin(self.angle)  ,
                        self.centerx + self.size * cos(self.angle + 90) , self.centery + self.size * sin(self.angle + 90),
                        self.centerx + self.size * cos(self.angle + 180), self.centery + self.size * sin(self.angle + 180) ,  
                        self.centerx + self.size * cos(self.angle + 270), self.centery + self.size * sin(self.angle + 270)] ,     
                        outline='gray', 
                        fill='gray', width=2)
        self.rotate()
    def rotate(self):
        self.angle += 1
        




        
       

class Layout(Frame):
    
    
    def __init__(self, parent =  None):
        Frame.__init__(self, parent)
        self.master =  parent
        self.colordict ="navy"
        
        self.height_split = 0.333
        self.width_split = 0.15
        

        
        self.left1_button = Button(self, text = "Angle Steer", command = self.left1_, bg = FormulaOrange1)
        self.left2_button = Button(self, text = "Temperature Coolant", command = self.left2_, bg = FormulaOrange1)
        self.left3_button = Button(self, text = "Test", command = self.left3_, bg = FormulaOrange1)
        
        self.right1_button = Button(self, text = "Test", command = self.right1_, bg = FormulaBlue1)
        self.right2_button = Button(self, text = "Test", command = self.right2_, bg = FormulaBlue1)
        self.right3_button = Button(self, text = "Test", command = self.right3_, bg = FormulaBlue1)
        
        
        self.mid1 = Frame(parent, bd=1, relief=FLAT, bg=FormulaBlack1)
        self.mid2 = Frame(parent, bd=1, relief=FLAT, bg = 'snow')

        
        
    def display(self):
        
        
        
        self.pack(fill = BOTH, expand  = 1)
        self.left1_button.place(relx = 0, rely = 0, relwidth = self.width_split, relheight = self.height_split)
        
        self.pack(fill = BOTH, expand  = 1)
        self.left2_button.place(relx = 0, rely =  self.height_split, relwidth = self.width_split, relheight = self.height_split)

        self.pack(fill = BOTH, expand  = 1)
        self.left3_button.place(relx = 0, rely = 2* self.height_split, relwidth = self.width_split, relheight = self.height_split)        
        
        
        self.pack(fill = BOTH, expand  = 1)
        self.right1_button.place(relx = 0.85, rely = 0, relwidth = self.width_split, relheight = self.height_split)
        
        self.pack(fill = BOTH, expand  = 1)
        self.right2_button.place(relx = 1- self.width_split, rely = self.height_split, relwidth = self.width_split, relheight = self.height_split)

        self.pack(fill = BOTH, expand  = 1)
        self.right3_button.place(relx = 1-self.width_split, rely = 2* self.height_split, relwidth = self.width_split, relheight = self.height_split)   
     
         
        self.mid1.place( relx = self.width_split, rely = 0,     relheight  =0.5, relwidth= 1 - 2*self.width_split)
        self.mid2.place( relx = self.width_split, rely = 0.5,   relheight =0.5,  relwidth= 1 -  2*self.width_split)
        
        
        C = Canvas(self.mid2, bg = "blue", height = 0.2*self.mid2.winfo_height(), width = 0.3*self.mid2.winfo_width())
        print(self.mid2.winfo_height())
        coord = 10, 50, 240, 210
        arc = C.create_arc(coord, start = 0, extent = 150, fill = "red")
        line = C.create_line(10,10,200,200,fill = 'white')
        C.pack()
        self.screen_Updater()
        

        
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
        
        
        
    def screen_Updater(self):
        print("DO Nothing")



    def left1_(self):
        self.colordict = colorscheme[0][1]        

        
    def left2_(self):
        self.colordict = colorscheme[0][1]

        
    def left3_(self):
        self.colordict = colorscheme[0][2]    

            
    def right1_(self):
        self.colordict = colorscheme[2][0]

           
    def right2_(self):
        self.colordict = colorscheme[2][1]

           
    def right3_(self):
        self.colordict = colorscheme[2][2]



            
            
            
            
#START THE MAIN FUNCTION            
            
windowX = 1200
windowY = 840    
 
winsize = str(windowX) + 'x' + str(windowY)
global master
master = Tk()
master.geometry(winsize)


                
    
Lay = Layout(master)



master.after(100, Lay.display)
master.mainloop()




