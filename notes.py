class main(Tkinter.Tk):
    def __init__(self):
        Tkinter.Tk.__init__(self)
+       self.resolution = 200  # New attribute for resolution
-       self.x= 100
-       self.y= 100
+       self.x = self.resolution // 2  # Dynamic center point x
+       self.y = self.resolution // 2  # Dynamic center point y
        ...
-       self.geometry('200x200+2050+1000')
+       self.geometry(f'{self.resolution}x{self.resolution}+2050+1000')  # Dynamic geometry
-       self.call('tk', 'scaling', 200.0)
+       self.call('tk', 'scaling', self.resolution / 100.0)  # Dynamic scaling
-       self.hand_length=50
+       self.hand_length = self.resolution * 0.25  # Dynamic hand length
        ...

    def on_resize(self, event):
+       self.resolution = event.width  # Update resolution
+       self.x, self.y = event.width // 2, event.height // 2  # Update center points
+       self.hand_length = self.resolution * 0.25  # Update hand length
+       self.canvas.delete("all")  # Delete all canvas elements
+       self.creating_all_function_trigger()  # Recreate all elements
