  class main(Tkinter.Tk):
      def __init__(self):
          Tkinter.Tk.__init__(self)
          ...
+         self.theme = "default"  # Add a theme attribute
          self.creating_all_function_trigger()
          self.bind('<space>', invert_canvas)
  
  # Creating Background
      def create_background(self):
          # self.image=ImageOps.invert(Tkinter.PhotoImage(file='clock.gif'))
-         self.image=Tkinter.PhotoImage(file='clock.gif')
+         self.image=Tkinter.PhotoImage(file=f'{self.theme}_clock.gif')  # Make the background theme-based
          self.canvas.create_image(self.x, self.y, image=self.image)
          self.sticks=[]
  
  # Creating Moving Sticks
      def creating_sticks(self):
          self.sticks=[]
-         color = ['white','white','red']
+         color = self.get_theme_colors()  # Make the stick colors theme-based
          width = [4, 4, 1]
          for i in range(3):
              store=self.canvas.create_line(self.x, self.y,self.x+self.hand_length,self.y+self.hand_length,width=width[i], fill=color[i])
              self.sticks.append(store)
          return
  
+     # New function to get theme-based colors
+     def get_theme_colors(self):
+         theme_colors = {
+             "default": ['white', 'white', 'red'],
+             "starry_night": ['yellow', 'yellow', 'blue'],
+             # Add more themes here
+         }
+         return theme_colors.get(self.theme, ['white', 'white', 'red'])
  
  # Main Function Trigger
  if __name__ == '__main__':
      root=main()
  
      # Creating Main Loop
-     while True:
-         root.update()
-         root.update_idletasks()
-         root.update_class()
+     root.after(1000, root.update_class)  # Use Tkinter's after method for updates
