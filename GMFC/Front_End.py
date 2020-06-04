import tkinter as tk

class GMFC(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "GCSE Mathematics Formula Calculator")
        tk.Tk.wm_geometry(self, "1024x768")
        tk.Tk.wm_resizable(self, False, False)
        