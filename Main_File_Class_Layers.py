from tkinter import *
from PIL import ImageTk
from PIL import Image
import math

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




##====Simple Approach to Drawing A Polygon============================================================================================

class Poly:
    
    def __init__(self, window, centerx, centery, corners):
        self.centerx = centerx
        self.centery = centery
        self.window =  window
        
        self.angle  = 15
        self.corners = corners
        self.corner_points = []
        self.corner_sides = []
        self.size = 30
        self.angle_step = int(360/corners)
        self.pol = 0
        mydebug(f'self.angle_step {self.angle_step}')



        for i in range(0, self.corners):
            self.corner_sides.append(1)
         
            
        for i in range(0, self.corners):
            self.corner_points.append([  int(self.centerx + self.corner_sides[i]      * self.size * math.cos(math.radians(self.angle + i * self.angle_step)))      
                                        ,int(self.centery + self.corner_sides[i]      * self.size * math.sin(math.radians(self.angle + i * self.angle_step))  )])
    
    def delete(self):
        #mydebug(f"WinMid.delete_Poly() self.pol={self.pol}")
        if self.pol > 0: # avoid list of arrows now for simplicity
            self.window.delete(self.pol)
            self.pol = 0      
     
        
        
    def draw(self):
        
        mydebug(f"PolyDraw")
        self.delete()
        for i in range(0, self.corners):
            self.corner_points[i][0] = int(self.centerx + self.corner_sides[i]      * self.size * math.cos(math.radians(self.angle + i * self.angle_step)))
            self.corner_points[i][1] = int(self.centery + self.corner_sides[i]      * self.size * math.sin(math.radians(self.angle + i * self.angle_step)))
        
        mydebug(f"WinMid.draw() self.pol={self.pol}")
        
        print(self.corner_points)   
                    # draw new arrow
        self.pol = self.window.create_polygon(self.corner_points, fill='snow')   
        mydebug(f"poly.draw() self.pol={self.pol}")
    def set_angle(self, val):
        self.angle += val
        print(self.angle)
        

    

        

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
        
        self.arrow = Poly(self.MainMidWindow, 200, 100, 3)
        
    def Update_val(self):
        
        self.arrow.draw()
         
#Object Deletion functions ==============================================================   

    
 


#========================================================================================
            

        
        
        

        


   
    


        

    
    
    
    
    
    
    




#Window For Second Middle screen. ==============================
class BotMidWindow:

    def __init__(self, window):
        mydebug(f"WinMid.__init__()")    # f-string of Python 3.6+
        self.window = window
        self.angle  = 0
        self.size = 30
        self.choice = 0
        self.p_width = 2
        self.l1 = 3
        
        
        # ALL attributes of class here
        self.rect = 0   # no rectangle yet
        self.index = 0  # no arrow yet
        self.BotCanvas = 0 # no canvas yet
        
        
        
        
        

    def function_choose(self):
        mydebug(f"WinMid.function_choose() self.choice={self.choice}")

        # don't create new canvas each call!
        # i would prefer this in __init__() but this requires rework in Layout()
        if self.BotCanvas == 0:
            self.centerx = self.window.winfo_width()/2
            self.centery = self.window.winfo_height()/2
            self.BotCanvas = Canvas(self.window, width= self.window.winfo_width(), height=self.window.winfo_height())
            self.BotCanvas.pack()

        if(self.choice == 1):
            self.arrow.draw()
        elif(self.choice == 2):
            self.screen_clear()
        elif(self.choice == 3):
            self.draw_rect()
        else:
            print("Do Nothing")
        
        # all drawing done
        # forget actual button press now
        # => no endless creation of rectangles...
        self.choice = 0



    








#Code for layout and buttons
class Layout(Frame, BotMidWindow):

    def __init__(self, parent =  None):
        Frame.__init__(self, parent)
        self.master =  parent
        self.colordict ="navy"

        self.height_split = 0.333
        self.width_split = 0.15

        self.left1_button = Button(self, text = "Angle Steering", command = self.left1_, bg = FormulaOrange1)
        self.left2_button = Button(self, text = "Temperature Coolant", command = self.left2_, bg = FormulaOrange1)
        self.left3_button = Button(self, text = "", command = self.left3_, bg = FormulaOrange1)

        self.right1_button = Button(self, text = "Test", command = self.right1_, bg = FormulaBlue1)
        self.right2_button = Button(self, text = "Test", command = self.right2_, bg = FormulaBlue1)
        self.right3_button = Button(self, text = "Test", command = self.right3_, bg = FormulaBlue1)

        self.mid1 = Frame(parent, bd=1, relief=FLAT, bg=FormulaBlack1)
        self.mid2 = Frame(parent, bd=1, relief=FLAT, bg = 'snow')
        self.BotMid = BotMidWindow(self.mid2)
        self.MainMid = MainMidWindow(self.mid1)

    def display(self):
        self.pack(fill = BOTH, expand  = 1)
        self.left1_button.place(relx = 0, rely = 0, relwidth = self.width_split, relheight = self.height_split)
        self.left2_button.place(relx = 0, rely =  self.height_split, relwidth = self.width_split, relheight = self.height_split)
        self.left3_button.place(relx = 0, rely = 2* self.height_split, relwidth = self.width_split, relheight = self.height_split)        
        self.right1_button.place(relx = 0.85, rely = 0, relwidth = self.width_split, relheight = self.height_split)
        self.right2_button.place(relx = 1- self.width_split, rely = self.height_split, relwidth = self.width_split, relheight = self.height_split)
        self.right3_button.place(relx = 1-self.width_split, rely = 2* self.height_split, relwidth = self.width_split, relheight = self.height_split)   
        try:
            self.mid2.update() 
        except:
            print("Mid Not Updated")
        self.mid1.place( relx = self.width_split, rely = 0,     relheight  =0.5, relwidth= 1 - 2*self.width_split)
        self.mid2.place( relx = self.width_split, rely = 0.5,   relheight =0.5,  relwidth= 1 -  2*self.width_split)

        self.master.after(100, self.screen_Updater)

    #Call function to execute the object for the second window screen    
    def screen_Updater(self):
        self.MainMid.arrow.set_angle(1)
        self.BotMid.function_choose()
        self.MainMid.Update_val()
        #self.s_pointer.mid_sc.next
        self.display()

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




