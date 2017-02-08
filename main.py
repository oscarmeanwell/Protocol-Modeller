from tkinter import *
from tkinter import messagebox
import hashlib, os, gui, body, adduser, firstwindow, ftpfile, Smtp
root = Tk()

if __name__ == "__main__":
    body.FlushDir()
    firstwindow = body.FirstWindow(root)
    root.mainloop()
    

