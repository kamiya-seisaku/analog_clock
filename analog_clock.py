# Started from: Aman Khrweal: Analog Clock with Python
# https://thecleverprogrammer.com/2020/05/19/analog-clock-with-python/
# 

try:
	import Tkinter
except:
	import tkinter as Tkinter

import ctypes
import time	# Required For Time Handling
import math	# Rejuired For Coordinates Calculation
from PIL import Image, ImageOps
import platform

ctypes.windll.shcore.SetProcessDpiAwareness(1)

class main(Tkinter.Tk):
    def __init__(self):
        Tkinter.Tk.__init__(self)
        self.resolution = 800
        self.x = self.resolution // 2
        self.y = self.resolution // 2
        self.attributes('-alpha',0.5) #https://www.geeksforgeeks.org/transparent-window-in-tkinter/
        self.geometry(f'{self.resolution}x{self.resolution}+2050+1000')
        self.call('tk', 'scaling', self.resolution / 100.0)
        self.hand_length = self.resolution * 0.25
        self.theme = "default"  # Add a theme attribute
        self.creating_all_function_trigger()
        self.bind('<space>', invert_canvas)

    # Creating Trigger For Other Functions
    def creating_all_function_trigger(self):
        self.create_canvas_for_shapes()
        self.create_background()
        self.creating_hands()
        return

	# Creating Background
    def create_background(self):
        # self.image=ImageOps.invert(Tkinter.PhotoImage(file='clock.gif'))
        self.image=Tkinter.PhotoImage(file=f'{self.theme}_clock.gif')  # theme-based background
        # self.canvas.create_image(self.x, self.y, image=self.image)
        self.hands=[]

        # Procedural background drawing
        color = ['red','white','white','white','white']
        width = [4,1,1,1,1,1]
        for i in range(60):  # 60 lines for each minute/second on the clock
            angle = math.radians(i * 6)  # 6 degrees for each line
            x1, y1 = self.x + self.hand_length * 0.9 * math.cos(angle), self.y - self.hand_length * 0.9 * math.sin(angle)
            x2, y2 = self.x + self.hand_length * math.cos(angle), self.y - self.hand_length * math.sin(angle)
            line_color = color[i % len(color)]
            line_width = width[i % len(width)]
            self.canvas.create_line(x1, y1, x2, y2, width=line_width, fill=line_color)

        return

	# creating Canvas
    def create_canvas_for_shapes(self):
        self.canvas=Tkinter.Canvas(self, bg='black')
        self.canvas.pack(expand='yes',fill='both')
        self.canvas.bind("<Configure>", self.on_resize)  # Bind the resize event
        return

    def on_resize(self, event):
        pass
        # self.resolution = event.width  # Update resolution
        # self.x, self.y = event.width // 2, event.height // 2  # Update center points
        # self.hand_length = self.resolution * 0.25  # Update hand length
        # self.canvas.delete("all")  # Delete all canvas elements
        # self.creating_all_function_trigger()  # Recreate all elements
 
	# Creating Moving Hands
    def creating_hands(self):
        self.hands=[]
        # color = ['white','green','red']
        color = self.get_theme_colors()  # Make the stick colors theme-based
        width = [4, 4, 1]
        for i in range(3):
            # store=self.canvas.create_line(self.x, self.y,self.x+self.length,self.y+self.length,width=2, fill='red')
            store=self.canvas.create_line(self.x, self.y,self.x+self.hand_length,self.y+self.hand_length,width=width[i], fill=color[i])
            self.hands.append(store)
        return

    # New function to get theme-based colors
    def get_theme_colors(self):
        theme_colors = {
            "default": ['white', 'white', 'red'],
            "starry_night": ['yellow', 'yellow', 'blue'],
            # Add more themes here
        }
        return theme_colors.get(self.theme, ['white', 'white', 'red'])

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
            # print(f'n:{n} i:{i}')
            x,y=self.canvas.coords(self.hands[n])[0:2]
            cr=[x,y]
            cr.append(len[n]*self.hand_length*math.cos(math.radians(i*6)-math.radians(90))+self.x)
            cr.append(len[n]*self.hand_length*math.sin(math.radians(i*6)-math.radians(90))+self.y)

            self.canvas.coords(self.hands[n],cr)
            self.canvas.coords(self.hands[n], tuple(cr))
            self.after(1000, self.update_class)  # Reschedule the method to run again after 1 second

        self.after_cancel(self._job)
        self._job = self.after(1000, self.update_class)  # Reschedule the method to run again after 1 second
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
    root.after(1000, root.update_class)
    root.mainloop()