from tkinter import *
from PIL import ImageTk
from PIL import Image
import math
import time
import gc

#==============================================Global Variables==============================
global WindowX            
windowX = 1200

global WindowY
windowY = 840  

global FormulaOrange1
FormulaOrange1 =  '#ee6d24'


global FormulaBlue1
FormulaBlue1 =  '#12bfd7'

global FormulaBlack1
FormulaBlack1 = '#1d323e'

def mydebug(s):
    print(s)




##=======Starting Multithreading===============================================================================




##====Simple Approach to Drawing A Polygon============================================================================================

class poly:
    
    def __init__(self, window, centerx, centery, corners):
        self.centerx = centerx
        self.centery = centery
        self.window =  window
        
        self.angle  = 0
        self.corners = corners
        self.corner_points = []
        self.corner_sides = []
        self.size = 1
        self.angle_step = int(360/corners)
        self.pol = 0
        self.fill = 'snow'
        #mydebug(f'self.angle_step {self.angle_step}')



        for i in range(0, self.corners):
            self.corner_sides.append(1)
         
            
        for i in range(0, self.corners):
            self.corner_points.append([  int(self.centerx + self.corner_sides[i]      * self.size * math.cos(math.radians(self.angle + i * self.angle_step)))      
                                        ,int(self.centery + self.corner_sides[i]      * self.size * math.sin(math.radians(self.angle + i * self.angle_step))  )])
    
    def delete(self):
        #mydebug(f"WinMid.delete_Poly() self.pol={self.pol}")
        if self.pol > 0: # avoid list of arrows now for simplicity
            self.window.delete(self.pol)
               
     
        
        
    def draw(self):
        
        #mydebug(f"PolyDraw")
        self.delete()
        for i in range(0, self.corners):
            self.corner_points[i][0] = int(self.centerx + self.corner_sides[i]      * self.size * math.cos(math.radians(self.angle + i * self.angle_step)))
            self.corner_points[i][1] = int(self.centery + self.corner_sides[i]      * self.size * math.sin(math.radians(self.angle + i * self.angle_step)))
        
        #mydebug(f"WinMid.draw() self.pol={self.pol}")
        
        #print(self.corner_points)   
                    # draw new arrow
        self.pol = self.window.create_polygon(self.corner_points, fill=self.fill, outline = self.outline)   
        #mydebug(f"poly.draw() self.pol={self.pol}")
  


      
    def set_angle(self, val):
        self.angle += val
       # print(self.angle)
        
    
    def set_size(self, val):
        for i in range(0, self.corners):
            self.corner_sides[i-1] = int(val)
        
        
    def stretch_corner(self, point, val):

        if(type(point) == int):
            if(point > self.corners or point == 0):
                print("out of bounds")
                return 0
            self.corner_sides[point-1] = self.corner_sides[point-1]* int(val)
        else:
            for i in point:
                if(i > self.corners or i == 0):
                    print("out of bounds")
                    next
                else:
                    self.corner_sides[i-1] = self.corner_sides[i-1] * int(val)
  


      
    def set_color(self, fill = None, outline = None):
        if(type(fill or outline) != str):
            print("error")
        else:
            self.fill = fill
            self.outline = outline
            


##====Simple Approach to Drawing A Polygon============================================================================================

class rect:
    
    def __init__(self, window, centerx, centery, sizex, sizey = None, fill = None):
        self.centerx = centerx
        self.centery = centery
        self.window =  window
        self.sizex = sizex
        self.sizey = None
        self.fill = fill

        self.rec = 0
        
        
        if(self.sizey == None):
            self.sizey = sizex
        
        
        if(fill == None):
            self.fill = 'snow'
 
    

            
            
            
        #mydebug(f'self.angle_step {self.angle_step}')



    def delete(self):
        #mydebug(f"WinMid.delete_Poly() self.pol={self.pol}")
        if self.rec > 0:
            self.window.delete(self.rec)
                 
     
        
        
    def draw(self):
        
        self.delete()
        self.window.create_rectangle(self.centerx, self.centery, self.centerx+ self.sizex, self.centery + self.sizex, fill = self.fill)
  


      
    def set_angle(self, val):
        self.angle += val
        #print(self.angle)
        
    
    def set_size(self, val):
        for i in self.corners:
            self.corner_sides[i-1] = int(val)
        
        
    def set_color(self, fill = None, outline = None):
        if(type(fill or outline) != str):
            print("error")
        else:
            self.fill = fill
            self.outline = outline        
"""     
    def stretch_corner(self, point, val):

        if(type(point) == int):
            if(point > self.corners or point == 0):
                print("out of bounds")
                return 0
            self.corner_sides[point-1] = self.corner_sides[point-1] * int(val)
        else:
            for i in point:
                if(i > self.corners or i == 0):
                    print("out of bounds")
                    next
                else:
                    self.corner_sides[i-1] = self.corner_sides[i-1] * int(val)
  

"""
      

            
        

#=============================================================================================

class MainMidWindow:
    def __init__(self, window):
        #mydebug(f"WinMid.__init__()")    # f-string of Python 3.6+
        self.window = window
        self.angle  = 0
        self.size = 30
        self.choice = 0
        self.p_width = 2
        self.arrow_dir = 1
        self.text = []
        
        

        
        
        self.centerx = 840/2
        self.centery = 420/2
        self.MainMidWindow = Canvas(self.window, width= 840, height=420,borderwidth = 0.0, bg=FormulaBlack1)
        self.MainMidWindow.pack()
        
        self.arrow = poly(self.MainMidWindow, 200, 100, 6)
        self.arrow.set_size(30)
        self.arrow.stretch_corner(1, 4)
        self.arrow.set_color(fill = 'blue', outline = 'red')
        
        self.rect1 = rect(self.MainMidWindow, 400, 100, 50) 

       
        
    def Update_val(self):
        
        self.arrow.draw()
        self.rect1.draw()
         
#Object Deletion functions ==============================================================   

    
 


#========================================================================================
            

        
        
        

        


   
    


        

    
    
    
    
    
    
    




#Window For Second Middle screen. ==============================
class BottomWindow:

    def __init__(self, window):
        #mydebug(f"WinMid.__init__()")    # f-string of Python 3.6+
        self.window = window
   
        
        
        # ALL attributes of class here
        self.rect = 0   # no rectangle yet
        self.index = 0  # no arrow yet
        self.BotCanvas = 0 # no canvas yet
        
        
        
        
        
        

    def function_choose(self):
        #mydebug(f"WinMid.function_choose() self.choice={self.choice}")

        # don't create new canvas each call!
        # i would prefer this in __init__() but this requires rework in Layout()
        if self.BotCanvas == 0:
            self.centerx = self.window.winfo_width()/2
            self.centery = self.window.winfo_height()/2
            self.BotCanvas = Canvas(self.window, width= self.window.winfo_width(), height=self.window.winfo_height())
            self.BotCanvas.pack()


        
        # all drawing done
        # forget actual button press now
        # => no endless creation of rectangles...
        self.choice = 0



    








#Code for layout and buttons
class Layout(Frame, BottomWindow):

    def __init__(self, parent =  None):
        
        self.counter = 0
        
        self.time_mark = time.time()
        Frame.__init__(self, parent)
        self.master =  parent
        self.colordict ="navy"

        self.height_split = 0.333
        self.width_split = 0.15

        #self.left1_button = Button(self, text = "Angle Steering", command = self.left1_, bg = FormulaOrange1)
        #self.left2_button = Button(self, text = "Temperature Coolant", command = self.left2_, bg = FormulaOrange1)
        #self.left3_button = Button(self, text = "", command = self.left3_, bg = FormulaOrange1)

        #self.right1_button = Button(self, text = "Test", command = self.right1_, bg = FormulaBlue1)
        #self.right2_button = Button(self, text = "Test", command = self.right2_, bg = FormulaBlue1)
        #self.right3_button = Button(self, text = "Test", command = self.right3_, bg = FormulaBlue1)




        self.mid1 = Frame(parent, bd=1, relief=FLAT, bg=FormulaBlack1)
        self.mid2 = Frame(parent, bd=1, relief=FLAT, bg = 'snow')
        
        
        
 ##=============================================Main and Bot window frames.       
        
        self.MainMid = MainMidWindow(self.mid1)
        self.BotMid = BottomWindow(self.mid2)
        


    def display(self):
        self.pack(fill = BOTH, expand  = 1)
        #self.left1_button.place(relx = 0, rely = 0, relwidth = self.width_split, relheight = self.height_split)
        #self.left2_button.place(relx = 0, rely =  self.height_split, relwidth = self.width_split, relheight = self.height_split)
        #self.left3_button.place(relx = 0, rely = 2* self.height_split, relwidth = self.width_split, relheight = self.height_split)        
        #self.right1_button.place(relx = 0.85, rely = 0, relwidth = self.width_split, relheight = self.height_split)
        #self.right2_button.place(relx = 1- self.width_split, rely = self.height_split, relwidth = self.width_split, relheight = self.height_split)
        #self.right3_button.place(relx = 1-self.width_split, rely = 2* self.height_split, relwidth = self.width_split, relheight = self.height_split)   
        self.mid1.place( relx = self.width_split, rely = 0,     relheight  =0.5, relwidth= 1 - 2*self.width_split)
        self.mid2.place( relx = self.width_split, rely = 0.5,   relheight =0.5,  relwidth= 1 -  2*self.width_split)

        self.master.after(10, self.screen_Updater)

    #Call function to execute the object for the second window screen    
    def screen_Updater(self):
        #self.MainMid.arrow.set_angle(1)
        self.BotMid.function_choose()
        self.MainMid.Update_val()
        print(int(time.time()*1000 - self.time_mark))
        self.time_mark = time.time()*1000
        self.master.after(10, self.screen_Updater)

    def left1_(self):
        self.BotMid.choice = 1     

    def left2_(self):
        self.BotMid.choice = 2     

    def left3_(self):
        self.BotMid.choice = 3        

    def right1_(self):
        self.BotMid.choice = 4     

    def right2_(self):
        self.BotMid.choice = 5     

    def right3_(self):
        self.BotMid.choice = 6     

            
        
            
          
        
        
        
        
        
            
#START THE MAIN FUNCTION       ========================================================================     
winsize = str(windowX) + 'x' + str(windowY)
global master
master = Tk()
master.geometry(winsize)
Lay = Layout(master)
Lay.display()
master.mainloop()




