import hashlib, gui
from tkinter import messagebox
from tkinter import *

def Constructor(self):
    self.parent = Tk()
    self.parent.title("CreateUser - Modelled")
    self.parent.geometry("360x400")
    gui.MainConstructor(self)
    gui.AddFrames(self)
    gui.AddUser_AddLables(self)
    gui.AddUser_AddEntries(self)
    gui.AddUser_AddCheckBox(self)
    gui.AddUser_AddButton(self)
def CreateUser(self, SALT):
    with open('UserNames.txt', 'r') as UsrNmFile:
        CurrentUsers = UsrNmFile.read()
    
    self.UsrNm = self.UserNameEnt.get()
    self.Pwd = self.PwdEnt.get()
    self.EncUsr = hashlib.sha512((self.UsrNm + SALT).encode()).hexdigest()
     
    if self.Pwd != (self.PwdConfEnt.get()):
         messagebox.showerror("User Creation", "Passwords do not match...")

    elif len(self.UsrNm) < 1:
        messagebox.showerror("Username Creation", "Username must have characters! Please choose an alternative")

    elif len(self.Pwd) < 1:
        messagebox.showerror("Password Creation", "Password Must have characters!")  
        
    elif self.EncUsr in CurrentUsers:
        messagebox.showerror("Username Creation", "Username already exists! Please choose an alternative")
        
    else:
        self.Error = ''
        self.LowerFlag = False
        self.UpperFlag = False
        self.NumberFlag = False
        self.LenFlag = False
        self.NotContFlag = False
        if len(self.Pwd) > 5:
            self.LenFlag = True

        for j in range(1, len(self.Pwd) + 1):
            Ascii = ord(self.Pwd[j - 1])
            if Ascii > 96 and Ascii < 123:
                self.LowerFlag = True
            
            if Ascii > 64 and Ascii < 91:
                self.UpperFlag = True

            if Ascii > 47 and Ascii < 58:
                self.NumberFlag = True

        if not self.LenFlag:
            self.Error += "Your password is a little on the short side...\n"
            
        if not self.LowerFlag:
            self.Error += "Maybe add a few lower case letters?\n"
            
        if not self.UpperFlag:
            self.Error += "Maybe add a few upper case letters?\n"
            
        if not self.NumberFlag:
            self.Error += "Maybe add a few Numbers?\n"
            
        if len(self.Error) > 0:
            self.Question = messagebox.askyesno("Password Strength", "These Errors were found!\n" + self.Error + "Continue Regardless?")
              
        if not self.Question:
            self.PwdEnt.delete(0, END)
            self.PwdConfEnt.delete(0, END)
            self.NotContFlag = True
            self.StaffBoolBox.destroy()
            self.StudentBoolBox.destroy()
            gui.AddUser_AddCheckBox(self)

            
            
        if not self.NotContFlag:
            with open('UserNames.txt', 'a') as self.File:
                self.File.write(hashlib.sha512((self.UsrNm + SALT).encode()).hexdigest() + '\n')
                
            with open('Passwords.txt', 'a') as self.PwdFile:
                self.PwdFile.write(hashlib.sha512((self.Pwd + SALT).encode()).hexdigest() + '\n')
                
            self.parent.destroy()
    
