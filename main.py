try:
	import Tkinter
except:
	import tkinter as Tkinter

import ctypes
import time	# Required For Time Handling
import math	# Rejuired For Coordinates Calculation
from PIL import Image, ImageOps

ctypes.windll.shcore.SetProcessDpiAwareness(1)

class main(Tkinter.Tk):
    def __init__(self):
        Tkinter.Tk.__init__(self)
        self.x= 100 # Center Point x
        self.y= 100 # Center Point
        self.attributes('-alpha',0.5) #https://www.geeksforgeeks.org/transparent-window-in-tkinter/
        self.geometry('200x200+2050+1000')
        self.call('tk', 'scaling', 200.0)
        self.length=50	# Stick Length
        self.creating_all_function_trigger()
        self.bind('<space>', invert_canvas)

    # Creating Trigger For Other Functions
    def creating_all_function_trigger(self):
        self.create_canvas_for_shapes()
        self.create_background()
        self.creating_sticks()
        return

	# Creating Background
    def create_background(self):
        # self.image=ImageOps.invert(Tkinter.PhotoImage(file='clock.gif'))
        self.image=Tkinter.PhotoImage(file='clock.gif')
        self.canvas.create_image(self.x, self.y, image=self.image)
        self.sticks=[]

        # # procedual background drawing
        # # color = ['white','green','red']
        # color = ['red','white','white','white','white']
        # width = [4,1,1,1,1,1]
        # for i in range(5):
        #     # store=self.canvas.create_line(self.x, self.y,self.x+self.length,self.y+self.length,width=2, fill='red')
        #     store=self.canvas.create_line(
        #         len[n]*self.length*math.
        #         cos(math.radians(i*6)-math.radians(90))+self.x)
        #     store=self.canvas.create_line(self.x, self.y,self.x+self.length,self.y+self.length,width=width[i], fill=color[i])
        #     self.sticks.append(store)

        return

	# creating Canvas
    def create_canvas_for_shapes(self):
        self.canvas=Tkinter.Canvas(self, bg='black')
        self.canvas.pack(expand='yes',fill='both')
        return

	# Creating Moving Sticks
    def creating_sticks(self):
        self.sticks=[]
        # color = ['white','green','red']
        color = ['white','white','red']
        width = [4, 4, 1]
        for i in range(3):
            # store=self.canvas.create_line(self.x, self.y,self.x+self.length,self.y+self.length,width=2, fill='red')
            store=self.canvas.create_line(self.x, self.y,self.x+self.length,self.y+self.length,width=width[i], fill=color[i])
            self.sticks.append(store)
        return

	# Function Need Regular Update
    def update_class(self):
        now=time.localtime()
        t = time.strptime(str(now.tm_hour), "%H")
        # hour = int(time.strftime( "%I", t ))*5
        hour = int(time.strftime( "%I", t ))*5
        # hour = now.tm_hour + now.tm_min / 60
        now=(hour+now.tm_min/12,now.tm_min,now.tm_sec)
        len=[.7,1,1]
        # Changing Stick Coordinates
        for n,i in enumerate(now):
            print(f'n:{n} i:{i}')
            x,y=self.canvas.coords(self.sticks[n])[0:2]
            cr=[x,y]
            cr.append(len[n]*self.length*math.cos(math.radians(i*6)-math.radians(90))+self.x)
            # self.canvas.coords(self.sticks[n],cr)
            # self.canvas.coords(self.sticks[n], tuple(cr))
        return


def invert_color(color):    # Invert color
    if type(color) == str: rgb = canvas.winfo_rgb(color)
    else: rgb = color
    rgb = (65535-rgb[0], 65535-rgb[1], 65535-rgb[2])
    tk_rgb = "#%04x%04x%04x" % (rgb)
    return tk_rgb

def invert_canvas(event):
    # Check or select canvas items:
    items = canvas.find_withtag('all')
    # Loop through canvas items
    for item in items:
        fill = canvas.itemcget(item, "fill")        # Get fill color
        if fill != '': fill = invert_color(fill)
        if canvas.type(item) in ['rectangle','arc']:
            outline = canvas.itemcget(item, "outline")  # Get outline color
            outline = invert_color(outline)
            canvas.itemconfig(item, fill=fill, outline=outline) # Set colors
        else:
            canvas.itemconfig(item, fill=fill) # Set colors

# Main Function Trigger
if __name__ == '__main__':
	root=main()

	# Creating Main Loop
	while True:
		root.update()
		root.update_idletasks()
		root.update_class()