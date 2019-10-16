from tkinter import *
<<<<<<< Updated upstream
=======
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
>>>>>>> Stashed changes

import math



split = 0.5



global colorscheme

<<<<<<< Updated upstream
colorscheme = [['SteelBlue1', 'mint cream', 'CadetBlue1'],
               ['SteelBlue2', "navy"      , 'CadetBlue2'],
               ['SteelBlue3', 'gray'      , 'CadetBlue3']]


global colordict 
=======
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
        self.L_N = 1
        self.L_E = 3
        self.L_S = 1
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
        mydebug(f"WinMid.rotate_Poly() self.angle={self.angle} self.index={self.index}")
        self.angle += self.arrow_dir # .. was 1 (too small to see something)
        
        
        
        
        if(self.angle >= 180 or self.angle <=0 ):
            self.arrow_dir = -self.arrow_dir

        # delete old arrow delete Old Rectngles
        
        self.delete_Poly()                
        self.delete_red_rect()
        self.delete_gre_rect()



        #update rectangles
        self.red_rect = self.mid_sc.create_rectangle(40, 300, 140, ((180-self.angle)/180)*100, fill='red')
        self.gre_rect = self.mid_sc.create_rectangle(800, 300, 700, (self.angle/180)*100, fill='green')
        # draw new arrow
        self.index = self.mid_sc.create_polygon(
            [       self.centerx + self.L_E  * self.size * math.cos(math.radians(self.angle))      ,  self.centery + self.L_E * self.size * math.sin(math.radians(self.angle))  ,
                    self.centerx + self.L_S  * self.size * math.cos(math.radians(self.angle + 90)) , self.centery + self.L_S * self.size*  math.sin(math.radians(self.angle + 90)),
                    self.centerx + self.L_W  * self.size * math.cos(math.radians(self.angle + 180)), self.centery + self.L_W * self.size * math.sin(math.radians(self.angle + 180)) ,  
                    self.centerx + self.L_N *  self.size * math.cos(math.radians(self.angle + 270)), self.centery + self.L_N  * self.size * math.sin(math.radians(self.angle + 270))
            ] , fill='snow'        )    
        


   
    
>>>>>>> Stashed changes

        

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
        




<<<<<<< Updated upstream
        
       
=======
    def __init__(self, window):
        mydebug(f"WinMid.__init__()")    # f-string of Python 3.6+
        self.window = window
        self.angle  = 0
<<<<<<< Updated upstream
        self.temp = 0
        self.size = 30
        self.choice = 0
        self.p_width = 2
        self.arrow_dir = 1
        self.temp_dir  = 0.3
            
=======
        self.counter = 0
        self.size = 30
        self.choice = 0
        self.p_width = 2
        
        self.centerx = 410
        self.centery = 210
        self.old_choice = 0
        self.color = '#000000'
>>>>>>> Stashed changes
        
        #PointerLengths
        self.L_N = 1
        self.L_E = 1
        self.L_S = 1
        self.L_W = 7
        
        # ALL attributes of class here
        self.rect = 0   # no rectangle yet
        self.index = 0  # no arrow yet
<<<<<<< Updated upstream
        self.mid_sc = 0 # no canvas yet
        
        self.color = '#000000'
        self.text_temp = 0
        
        
        




    def function_choose(self):
        mydebug(f"WinMid.function_choose() self.choice={self.choice}")

        # don't create new canvas each call!
        # i would prefer this in __init__() but this requires rework in Layout()
        if self.mid_sc == 0:
            self.centerx = self.window.winfo_width()/2
            self.centery = self.window.winfo_height()/2
            self.mid_sc = Canvas(self.window, width= self.window.winfo_width(), height=self.window.winfo_height())
            self.mid_sc.pack()
=======
        self.BotCanvas = 0 # no canvas yet
        
        
        #PointerLengths
        self.screen_1 = [3,3,3,-1]
    def update_val(self):
        self.angle += 10
        
        

    def function_choose(self):
        self.update_val()
        mydebug(f"WinMid.function_choose() self.choice={self.choice} self.old_choice = {self.old_choice}")
        #self.color_update()
        
        if(self.choice != self.old_choice):
            mydebug(f"WinMid.function_choose() self.screen_clear()")
            self.screen_clear()
            self.old_choice = self.choice
        
        if self.BotCanvas == 0:
            self.BotCanvas = Canvas(self.window, width= 840, height=420,borderwidth = 0.0, bg='snow')
            self.BotCanvas.pack()
>>>>>>> Stashed changes


        if(self.choice == 1):
            self.rotate_Poly()
            
                        
        elif(self.choice == 2):

            self.rect = self.BotCanvas.create_rectangle(100, 100, 200, 200, fill='red')
            
            
        elif(self.choice == 3):
<<<<<<< Updated upstream
            self.draw_rect()
        elif(self.choice == 4):
            self.temp_gradient()
=======
            self.rect = self.BotCanvas.create_rectangle(200, 200, 200 + (self.angle//10)%1000 , 300, fill='blue')
            
        elif(self.choice == 4):

            self.rect = self.BotCanvas.create_rectangle(300, 300, 400, 400, fill=self.color)
         
        elif(self.choice == 5):

            self.rect = self.BotCanvas.create_rectangle(300, 300, 400, 400, fill=self.color)
        
        elif(self.choice == 6):
            self.rect = self.BotCanvas.create_rectangle(300, 300, 400, 400, fill=self.color)
           
            
            
            
>>>>>>> Stashed changes
        else:
            print("Do Nothing")
        

        # all drawing done
        # forget actual button press now
<<<<<<< Updated upstream
        # => no endless creation of rectangles...
        #self.choice = 1
=======

>>>>>>> Stashed changes

    #Animated Polygon, Animated Polygon currently not updating        
    def delete_Poly(self):
        mydebug(f"WinMid.delete_Poly() self.index={self.index}")
        if self.index > 0: # avoid list of arrows now for simplicity
<<<<<<< Updated upstream
            self.mid_sc.delete(self.index)
=======
            self.BotCanvas.delete(self.index)
>>>>>>> Stashed changes
            self.index = 0
    
    
    def colorize(self,a,b,c):
        self.color = '#%02x%02x%02x' % (a, b, c)
        print(self.color, b)

        
    def temp_gradient(self):
        self.temp += self.temp_dir # .. was 1 (too small to see something)
        
        if(self.temp >= 250 or self.temp <=0 ):
            self.temp_dir = -self.temp_dir
            
            
        self.del_temp()   
        self.colorize(255, self.angle, 0)
        mydebug(f"WinMid.temp_gradient() self.temp_gradient={self.angle}")
        self.mid_sc.configure(bg = self.color)

            
            
        self.text_temp = self.mid_sc.create_text(420,240, text = int(self.temp/250*60) , fill="black", font = ("Purisa", 30))
    
    def del_temp(self):
        if(self.text_temp > 0):
            self.mid_sc.delete(self.text_temp)
            self.text_temp = 0
    
    
    
    
    
    
    
    def rotate_Poly(self):
        mydebug(f"WinMid.rotate_Poly() self.angle={self.angle} self.index={self.index}")
<<<<<<< Updated upstream
        self.angle += self.arrow_dir # .. was 1 (too small to see something)
        
        if(self.angle >= 180 or self.angle <=0 ):
            self.arrow_dir = -self.arrow_dir

        # delete old arrow
        self.delete_Poly() 
        # draw new arrow
        self.index = self.mid_sc.create_polygon(
            [       self.centerx + self.L_E  * self.size * math.cos(math.radians(self.angle))      ,  self.centery + self.L_E * self.size * math.sin(math.radians(self.angle))  ,
                    self.centerx + self.L_S  * self.size * math.cos(math.radians(self.angle + 90)) , self.centery + self.L_S * self.size*  math.sin(math.radians(self.angle + 90)),
                    self.centerx + self.L_W  * self.size * math.cos(math.radians(self.angle + 180)), self.centery + self.L_W * self.size * math.sin(math.radians(self.angle + 180)) ,  
                    self.centerx + self.L_N *  self.size * math.cos(math.radians(self.angle + 270)), self.centery + self.L_N  * self.size * math.sin(math.radians(self.angle + 270))
            ] 
        )    

=======
         # .. was 1 (too small to see something)
        
        # delete old arrow
        self.delete_Poly() 
        # draw new arrow
        self.index = self.BotCanvas.create_polygon(
            [       self.centerx + self.screen_1[0] * self.size * math.cos(math.radians(self.angle))      , self.centery + self.screen_1[0] * self.size* math.sin(math.radians(self.angle))  ,
                    self.centerx + self.screen_1[1] * self.size * math.cos(math.radians(self.angle + 90)) , self.centery + self.screen_1[1] * self.size *math.sin(math.radians(self.angle + 90)),
                    self.centerx + self.screen_1[2] * self.size * math.cos(math.radians(self.angle + 180)), self.centery + self.screen_1[2] * self.size * math.sin(math.radians(self.angle + 180)) ,  
                    self.centerx + self.screen_1[3] * self.size * math.cos(math.radians(self.angle + 270)), self.centery + self.screen_1[3] * self.size * math.sin(math.radians(self.angle + 270))
            ] )    
    
    def _from_rgb(rgb):
        return "#%02x%02x%02x" % rgb 
>>>>>>> Stashed changes

    def color_update(self):
        
        
        self.color = self._from_rgb((0,0,(self.angle//100)))
        
        
        
        

    def delete_rect(self):
        mydebug(f"WinMid.delete_rect()")
        if self.rect > 0: # avoid list of rects now for simplicity
            self.mid_sc.delete(self.rect)
            self.rect = 0

<<<<<<< Updated upstream
    def draw_rect(self):
        mydebug(f"WinMid.draw_rect()")
        self.delete_rect()
        self.rect = self.mid_sc.create_rectangle(0, 10, 100, 100, fill='red')

=======
   
        
      
>>>>>>> Stashed changes
    def screen_clear(self):
        mydebug(f"WinMid.screen_clear()")
        self.delete_rect()
        self.delete_Poly()

#Code for layout and buttons
class Layout(Frame, WinMid):
>>>>>>> Stashed changes

class Layout(Frame):
    
    
    def __init__(self, parent =  None):
        Frame.__init__(self, parent)
        self.master =  parent
        self.colordict ="navy"
        
        self.height_split = 0.333
        self.width_split = 0.15
<<<<<<< Updated upstream
        

        
        self.left1_button = Button(self, text = "Angle Steer", command = self.left1_, bg = FormulaOrange1)
        self.left2_button = Button(self, text = "Temperature Coolant", command = self.left2_, bg = FormulaOrange1)
        self.left3_button = Button(self, text = "Test", command = self.left3_, bg = FormulaOrange1)
        
        self.right1_button = Button(self, text = "Test", command = self.right1_, bg = FormulaBlue1)
        self.right2_button = Button(self, text = "Test", command = self.right2_, bg = FormulaBlue1)
        self.right3_button = Button(self, text = "Test", command = self.right3_, bg = FormulaBlue1)
        
        
=======
        self.time_mark = time.time()

        self.left1_button = Button(self, text = "Test1", command = self.left1_, bg = FormulaOrange1)
        self.left2_button = Button(self, text = "", command = self.left2_, bg = FormulaOrange1)
        self.left3_button = Button(self, text = "", command = self.left3_, bg = FormulaOrange1)

        self.right1_button = Button(self, text = "", command = self.right1_, bg = FormulaBlue1)
        self.right2_button = Button(self, text = "", command = self.right2_, bg = FormulaBlue1)
        self.right3_button = Button(self, text = "", command = self.right3_, bg = FormulaBlue1)

>>>>>>> Stashed changes
        self.mid1 = Frame(parent, bd=1, relief=FLAT, bg=FormulaBlack1)
        self.mid2 = Frame(parent, bd=1, relief=FLAT, bg = 'snow')
<<<<<<< Updated upstream
=======
        self.bot_window = WinMid(self.mid2)
>>>>>>> Stashed changes

        
        
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
        

<<<<<<< Updated upstream
        
    def split_val(self, split_val):
        self.old_relx = relx
        self.old_rely = rely
        self.old_height = relheight
        self.old_relwidth = relwidth


    def callback(self, event):
        self.left1_data.repos()
=======
        self.screen_Updater()
>>>>>>> Stashed changes

<<<<<<< Updated upstream
=======
    #Call function to execute the object for the second window screen    
    def screen_Updater(self):
<<<<<<< Updated upstream
        self.bot_window.function_choose()
        self.main_window.Update_val()
#        self.main_window.draw_rect()
        #self.s_pointer.mid_sc.next
>>>>>>> Stashed changes
        self.display()
        
        
    def test(self):
        print("Test") 
        
        
        
    def screen_Updater(self):
        print("DO Nothing")

=======
        self.BotMid.function_choose()
        self.MainMid.Update_val()
        print(int(time.time()*1000 - self.time_mark))
        self.time_mark = time.time()*1000
        #self.s_pointer.mid_sc.next
        self.master.after(10, self.screen_Updater)
>>>>>>> Stashed changes


    def left1_(self):
<<<<<<< Updated upstream
        self.colordict = colorscheme[0][1]        
=======
        self.bot_window.choice = 1     
>>>>>>> Stashed changes

        
    def left2_(self):
<<<<<<< Updated upstream
        self.colordict = colorscheme[0][1]
=======
        self.bot_window.choice = 2     
>>>>>>> Stashed changes

        
    def left3_(self):
<<<<<<< Updated upstream
        self.colordict = colorscheme[0][2]    
=======
        self.bot_window.choice = 3        
>>>>>>> Stashed changes

            
    def right1_(self):
<<<<<<< Updated upstream
        self.colordict = colorscheme[2][0]
=======
        self.bot_window.choice = 4     
>>>>>>> Stashed changes

           
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




