  try:
      import Tkinter
  except:
      import tkinter as Tkinter

+ import win32gui
+ import win32con
  import ctypes
  import time  # Required For Time Handling
  import math  # Rejuired For Coordinates Calculation
  ...

  class main(Tkinter.Tk):
      def __init__(self):
          Tkinter.Tk.__init__(self)
          ...
+         hwnd = self.winfo_id()
+         win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
+                                win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED | win32con.WS_EX_TRANSPARENT)
          self.creating_all_function_trigger()
          ...
