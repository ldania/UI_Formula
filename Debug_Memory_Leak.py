from tkinter import *
import math
import time

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

import sys

##==== Object Method to Drawing A Polygon ============================================================================================

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
        


        for i in range(0, self.corners):
            self.corner_sides.append(1)
         
            
        for i in range(0, self.corners):
            self.corner_points.append([  int(self.centerx + self.corner_sides[i]      * self.size * math.cos(math.radians(self.angle + i * self.angle_step)))      
                                        ,int(self.centery + self.corner_sides[i]      * self.size * math.sin(math.radians(self.angle + i * self.angle_step))  )])
    
    def delete(self):
        #mydebug(f"WinMid.delete_Poly() self.pol={self.pol}")
        if self.pol > 0: # avoid list of arrows now for simplicity
            self.window.delete(self.pol)
            #del self.pol
            self.pol = 0
               
     
        
        
    def draw(self):
        
        #mydebug(f"PolyDraw")
        self.delete()
        
        for i in range(0, self.corners):
            self.corner_points[i][0] = int(self.centerx + self.corner_sides[i]      * self.size * math.cos(math.radians(self.angle + i * self.angle_step)))
            self.corner_points[i][1] = int(self.centery + self.corner_sides[i]      * self.size * math.sin(math.radians(self.angle + i * self.angle_step)))
        

       
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
 
    def delete(self):
       
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

   
        

#=============================================================================================

class MainMidWindow:
    def __init__(self, window):
       
        self.window = window
        self.centerx = 840/2
        self.centery = 420/2
        self.MainMidWindow = Canvas(self.window, width= 840, height=420,borderwidth = 0.0, bg=FormulaBlack1)
        self.MainMidWindow.pack()
       
        
        
        
##===================== Creating an instance of Poly========
        self.arrow = poly(self.MainMidWindow, 200, 100, 6)
        self.arrow.set_size(30)
        self.arrow.stretch_corner(1, 4)
        self.arrow.set_color(fill = 'blue', outline = 'red')
        
        self.rect1 = rect(self.MainMidWindow, 400, 100, 50) 
        
        
        
##============================================  ANimation=====
       
        
    def Update_val(self):
        
        self.arrow.draw()
        self.rect1.draw()
         





#Window For Second Middle screen. ==============================
class BottomWindow:

    def __init__(self, window):

        self.window = window
       
     


#Code for layout and buttons
class Layout(Frame, BottomWindow):

    def __init__(self, parent =  None):

        
        self.time_mark = time.time()
        Frame.__init__(self, parent)
        self.master =  parent


        self.height_split = 0.333
        self.width_split = 0.15


        self.mid1 = Frame(parent, bd=1, relief=FLAT, bg=FormulaBlack1)
        #self.mid2 = Frame(parent, bd=1, relief=FLAT, bg = 'snow')
        
        
        
 ##=============================================Main and Bot window frames.       
        
        self.MainMid = MainMidWindow(self.mid1)
        #self.BotMid = BottomWindow(self.mid2)
        


    def display(self):
        self.pack(fill = BOTH, expand  = 1)
     
        self.mid1.place( relx = self.width_split, rely = 0,     relheight  =0.5, relwidth= 1 - 2*self.width_split)
        #self.mid2.place( relx = self.width_split, rely = 0.5,   relheight =0.5,  relwidth= 1 -  2*self.width_split)

        self.screen_Updater()
        
        

    #Call function to execute the object for the second window screen    
    def screen_Updater(self):
        self.MainMid.arrow.set_angle(1)
        #print(int(time.time()*1000 - self.time_mark))
        #self.time_mark = time.time()*1000
#        self.BotMid.function_choose()
        print(sys.getrefcount(self.MainMid.arrow.corner_points))
        self.MainMid.Update_val()
        self.master.after(10, self.screen_Updater)


            
        
            
          
        
        
        
        
        
            
#START THE MAIN FUNCTION       ========================================================================     
winsize = str(windowX) + 'x' + str(windowY)
global master
master = Tk()
master.geometry(winsize)
Lay = Layout(master)
Lay.display()
master.mainloop()




