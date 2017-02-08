import gui, hashlib, body
from tkinter import *
from tkinter import messagebox

def BuildConstruct(self, parent):
    self.parent = parent
    self.parent.title('Log In - Modelled')
    self.parent.geometry("330x230")
    gui.MainConstructor(self)
    gui.AddFrames(self)
    gui.AddLabel(self)
    gui.AddEntrys(self)
    gui.AddButtons(self)
    
def login(self, SALT, X):
    if len(self.UserName.get()) < 1:
            messagebox.showerror("Login", "Login Failed, Username must have Characters")
    else:
        self.Breaker = False                                                        # Breaker to evaluate if username is correct before looking for password
        self.UsrName = hashlib.sha512((self.UserName.get() + SALT).encode()).hexdigest()                                       #Gets the Username from the entry
        self.Pwd = hashlib.sha512((self.Password.get() + SALT).encode()).hexdigest()                                       #Gets the Password form the entry
        self.UsrArray = []
        self.PwdArray = []
        with open("UserNames.txt", "r") as self.UsrNamesFile:
            for Line in self.UsrNamesFile:
                self.UsrArray.append(Line.strip())                                      #Add usernames to array
        with open("Passwords.txt", "r") as self.PwdFile:
            for Line in self.PwdFile:
                self.PwdArray.append(Line.strip())                                      #Add passwords to array
            
        try:
            self.IndexHolder = self.UsrArray.index(self.UsrName)                    #See if the username exists if so set breaker
            self.Breaker = True
            
        except ValueError:
            messagebox.showerror("Login", "Login Failed, Username incorrect")
            
        if self.Breaker:

            if str(self.PwdArray[self.IndexHolder]).strip() == self.Pwd.strip():  #If the password is correct, Log in
                with open('TeacherUsers.txt', 'r') as self.File:
                    if self.UsrName in self.File.read():
##                        STAFFPM = True
##                        print('SDADDSD',STAFFPM)
                        self.X = True
                    else:
                        pass
                if self.X:
                    messagebox.showinfo("Login", "Login succesful, Welcome " + self.UserName.get() + "! (Teacher user!)")
                    self.parent.destroy()
##                    body.MainMenu()
                    self.Z = True
                else:
                    messagebox.showinfo("Login", "Login succesful, Welcome " + self.UserName.get() + "! (Student user!)")
                    self.parent.destroy()
##                    body.MainMenu()
                    self.Z = True
            else:
                messagebox.showerror("Login", "Login Failed, Password incorrect")
    
    
