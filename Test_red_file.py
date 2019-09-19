from tkinter import *
import math

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
    
    


class MainMid:
    def __init__(self, window):
        mydebug(f"WinMid.__init__()")    # f-string of Python 3.6+
        self.window = window
        self.angle  = 0
        self.size = 30
        self.choice = 0
        self.p_width = 2
        self.arrow_dir = 1
        
        #PointerLengths
        self.L_N = 0.5
        self.L_E = 1
        self.L_S = 0.5
        self.L_W = 6
        
        # ALL attributes of class here
        self.red_rect = 0   # no rectangle yet
        self.gre_rect = 0   # no rectangle yet
        
        self.index = 0  # no arrow yet
        self.mid_sc = 0 # no canvas yet
        
        
        self.centerx = 840/2
        self.centery = 420/2
        self.mid_sc = Canvas(self.window, width= 840, height=420,borderwidth = 0.0, bg=FormulaBlack1)
        self.mid_sc.pack()


    #Animated Polygon, Animated Polygon currently not updating        
    def delete_Poly(self):
        mydebug(f"WinMid.delete_Poly() self.index={self.index}")
        if self.index > 0: # avoid list of arrows now for simplicity
            self.mid_sc.delete(self.index)
            self.index = 0
    
    def delete_red_rect(self):
        if self.red_rect > 0: # avoid list of rects now for simplicity
            self.mid_sc.delete(self.red_rect)
            self.red_rect = 0
            
    def delete_gre_rect(self):
        if self.gre_rect > 0: # avoid list of rects now for simplicity
            self.mid_sc.delete(self.gre_rect)
            self.gre_rect = 0
            
            
    def Update_val(self):
        mydebug(f"WinMid.rotate_Poly() self.angle={self.angle} self.index={self.index} self.red_rect={self.red_rect}")
        self.angle += self.arrow_dir # .. was 1 (too small to see something)
        
        
        
        
        if(self.angle >= 180 or self.angle <=0 ):
            self.arrow_dir = -self.arrow_dir

        # delete old arrow delete Old Rectngles
        
        #self.delete_Poly()  
        self.delete_Poly()              
        self.delete_red_rect()
        self.delete_gre_rect()



        #update rectangles
        self.red_rect = self.mid_sc.create_rectangle(40, 300, 140, (180-self.angle), fill='red')
        self.gre_rect = self.mid_sc.create_rectangle(800, 300, 700, (self.angle), fill='green')
        # draw new arrow
        self.index = self.mid_sc.create_polygon(
            [       self.centerx + self.L_E  * self.size * math.cos(math.radians(self.angle))      ,  self.centery + self.L_E * self.size * math.sin(math.radians(self.angle))  ,
                    self.centerx + self.L_S  * self.size * math.cos(math.radians(self.angle + 90)) , self.centery + self.L_S * self.size*  math.sin(math.radians(self.angle + 90)),
                    self.centerx + self.L_W  * self.size * math.cos(math.radians(self.angle + 180)), self.centery + self.L_W * self.size * math.sin(math.radians(self.angle + 180)) ,  
                    self.centerx + self.L_N *  self.size * math.cos(math.radians(self.angle + 270)), self.centery + self.L_N  * self.size * math.sin(math.radians(self.angle + 270))
            ] , fill='red'        )    
        


   
    

        




#Code for layout and buttons
class Layout(Frame, WinMid):

    def __init__(self, parent =  None):
        Frame.__init__(self, parent)
        self.master =  parent
        self.colordict ="navy"

        self.height_split = 0.333
        self.width_split = 0.15
        
        self.mid1 = Frame(parent, bd=1, relief=FLAT, bg=FormulaBlack1)
        self.main_window = MainMid(self.mid1)

    def display(self):
        self.pack(fill = BOTH, expand  = 1)
        self.mid1.place( relx = self.width_split, rely = 0,     relheight  =0.5, relwidth= 1 - 2*self.width_split)
        self.master.after(20, self.screen_Updater)

    #Call function to execute the object for the second window screen    
    def screen_Updater(self):

        self.main_window.Update_val()
        self.display()



        
#START THE MAIN FUNCTION            
winsize = str(windowX) + 'x' + str(windowY)
global master
master = Tk()
master.geometry(winsize)
Lay = Layout(master)
Lay.display()
master.mainloop()