from tkinter import *
from PIL import ImageTk
from PIL import Image
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

def mydebug(s):
    print(s)


class values:
    def __init__(self):
        self.angle = 33

##============================================================================================
class shapes:
    
    def __init__(self, window):
        self.points = [1,1,1,1]
        self.size = 10
        self.window = window

    #Object Deletion functions ==============================================================   
    def delete(self):
        mydebug(f"WinMid.delete_Poly() self.index={self.index}")
        if self.pol > 0: # avoid list of arrows now for simplicity
            del self.pol
            self.pol = 0
    

 
    
##======Draw================================
    def poly4_draw(self, Cx, Cy, angle):

                # draw new arrow
        self.pol = self.window.create_polygon(
            [      [ Cx + self.points[0]  * self.size * math.cos(math.radians(angle))      , Cy + self.points[0] * self.size * math.sin(math.radians(angle))  ],
                   [ Cx + self.points[1]  * self.size * math.cos(math.radians(angle + 90)) , Cy + self.points[1] * self.size*  math.sin(math.radians(angle + 90))],
                   [ Cx + self.points[2]  * self.size * math.cos(math.radians(angle + 180)), Cy + self.points[2] * self.size * math.sin(math.radians(angle + 180))] ,  
                   [ Cx + self.points[3]  * self.size * math.cos(math.radians(angle + 270)), Cy + self.points[3] * self.size * math.sin(math.radians(angle + 270))]
            ] , fill='snow'        )  



    
    
    
    
#=============================================================================================

class MainMidWindow(shapes):
    def __init__(self, window):
        mydebug(f"WinMid.__init__()")    # f-string of Python 3.6+
        self.window = window

        self.arrow_dir = 1
       
        
        self.centerx = 840/2
        self.centery = 420/2
        self.MidWindow = Canvas(self.window, width= 840, height=420,borderwidth = 0.0, bg=FormulaBlack1)
        self.MidWindow.pack()

        self.angle = values()
        shapes.__init__(self,self.MidWindow)



#========================================================================================
            
    def Update_val(self):
#        mydebug(f"WinMid.rotate_Poly() self.angle={self.angle} self.index={self.index}")
  
        
        if(self.angle.angle >= 180 or self.angle.angle <=0 ):
            self.arrow_dir = -self.arrow_dir

        self.poly4_draw(100, 100, self.angle.angle)

        # delete old arrow delete Old Rectngles

        


   
    


        




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
            self.rotate_Poly()
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

    #Animated Polygon, Animated Polygon currently not updating        
    def delete_Poly(self):
        mydebug(f"WinMid.delete_Poly() self.index={self.index}")
        if self.index > 0: # avoid list of arrows now for simplicity
            self.BonCanvas.delete(self.index)
            self.index = 0
    
    def rotate_Poly(self):
        mydebug(f"WinMid.rotate_Poly() self.angle={self.angle} self.index={self.index}")
        self.angle += 10 # .. was 1 (too small to see something)
        self.l1 += 0
        # delete old arrow
        self.delete_Poly() 
        # draw new arrow
        self.index = self.BotCanvas.create_polygon(
            [       self.centerx + self.size * math.cos(math.radians(self.angle))      ,  self.centery + self.size * math.sin(math.radians(self.angle))  ,
                    self.centerx + self.size * self.size * math.cos(math.radians(self.angle + 90)) , self.centery + self.size* self.l1 * math.sin(math.radians(self.angle + 90)),
                    self.centerx + self.size * math.cos(math.radians(self.angle + 180)), self.centery + self.size * math.sin(math.radians(self.angle + 180)) ,  
                    self.centerx + self.size * math.cos(math.radians(self.angle + 270)), self.centery + self.size * math.sin(math.radians(self.angle + 270))
            ] )    


##=====WINDOWS 2 TEMPERATURE COOLANT=====
    def delete_rect(self):
        mydebug(f"WinMid.delete_rect()")
        if self.rect > 0: # avoid list of rects now for simplicity
            self.BotCanvas.delete(self.rect)
            self.rect = 0

    def draw_rect(self):
        mydebug(f"WinMid.draw_rect()")
        self.delete_rect()
        self.rect = self.BotCanvas.create_rectangle(0, 10, 100, 100, fill='red')
        
      
    def screen_clear(self):
        mydebug(f"WinMid.screen_clear()")
        self.delete_rect()
        self.delete_Poly()









#Code for layout and buttons
class Layout(Frame, BotMidWindow):

    def __init__(self, parent =  None):
        Frame.__init__(self, parent)
        self.master =  parent
        self.colordict ="navy"

        self.height_split = 0.333
        self.width_split = 0.15
        self.time_mark = time.time()

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

        self.screen_Updater()

    #Call function to execute the object for the second window screen    
    def screen_Updater(self):
        self.BotMid.function_choose()
        self.MainMid.Update_val()
        print(int(time.time()*1000 - self.time_mark))
        self.time_mark = time.time()*1000
        #self.s_pointer.mid_sc.next
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




