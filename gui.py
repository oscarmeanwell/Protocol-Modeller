from tkinter import *
from tkinter import filedialog
import datetime, pickle, re, body, os
DefColor = "steel blue"
DefBtn = "light blue"
LINE = float(1)
def MainConstructor(self):
    self.parent.configure(background="steel blue")
    self.parent.iconbitmap("mail.ico")
    self.parent.grid()
    self.parent.resizable(0,0)

def AddFrames(self):
    self.LstFrm = Frame(self.parent, bg = DefColor)
    self.BtnFrm = Frame(self.parent, bg = DefColor)
    self.LblFrm = Frame(self.parent, bg = DefColor)
    self.LstFrm.grid(column = 0, row = 1)
    self.BtnFrm.grid(column = 0, row = 2)
    self.LblFrm.grid(column = 0, row = 0)

def AddEntrys(self):
    self.UserName = Entry(self.LstFrm, bd = 4, width = 25, font = ("Calibri", 10))
    self.Password = Entry(self.LstFrm, bd = 4, width = 25, font = ("Calibri", 10), show = '*')
    self.UserName.insert(END, "Username")
    self.Password.insert(END, "Password")
    self.UserName.bind("<FocusIn>", self.ClearUsername)
    self.Password.bind("<FocusIn>", self.ClearPassword)
    self.UserName.grid(column = 0, row = 1, padx = 70, pady = 10)
    self.Password.grid(column = 0, row = 2, padx = 70, pady = 10)

def AddLabel(self):
    self.WelcomeLbl = Label(self.LstFrm, text = "Welcome, please enter your details", bg = DefColor, font = ("Calibri", 12))
    self.WelcomeLbl.grid(column = 0, row = 0, padx = 10, pady = 10)

def AddButtons(self):
    self.LoginBtn = Button(self.BtnFrm, text = "Login", height = 2, width = 10, fg = "black", activebackground = "yellow", bg = DefBtn, command = self.Login)
    self.CreateUsrBtn = Button(self.BtnFrm, text = "Create User", height = 2, width = 10, fg = "black", activebackground = "yellow", bg = DefBtn, command = self.CreateUser)
    self.LoginBtn.grid(row = 3, column = 0, padx = 10, pady = 10)
    self.CreateUsrBtn.grid(row = 3, column = 1, padx = 10, pady = 10)

def AddUser_AddLables(self):
    self.Header = Label(self.LblFrm, text = "Welcome, please complete!", bg = DefColor, font = ("Calibri", 12))
    self.UsrNmLbl = Label(self.LstFrm, text = "Username: ", bg = DefColor, font = ("Calibri", 12))
    self.PwdLbl = Label(self.LstFrm, text = "Password: ", bg = DefColor, font = ("Calibri", 12))
    self.PwdConfLbl = Label(self.LstFrm, text = "Confirm: ", bg = DefColor, font = ("Calibri", 12))
    self.Header.grid(row = 0, column = 0, padx = 20, pady = 20)
    self.UsrNmLbl.grid(row = 1, column = 0, padx = 20, pady = 20)
    self.PwdLbl.grid(row = 2, column = 0, padx = 20, pady = 20)
    self.PwdConfLbl.grid(row = 3, column = 0, padx = 20, pady = 20)
        
def AddUser_AddEntries(self):
    self.UserNameEnt = Entry(self.LstFrm, bd = 4, width = 25, font = ("Calibri", 10))
    self.PwdEnt = Entry(self.LstFrm, bd = 4, width = 25, font = ("Calibri", 10), show = '*')
    self.PwdConfEnt = Entry(self.LstFrm, bd = 4, width = 25, font = ("Calibri", 10), show = '*')
    self.UserNameEnt.grid(row = 1, column = 1, padx = 20, pady = 20)
    self.PwdEnt.grid(row = 2, column = 1, padx = 20, pady = 10)
    self.PwdConfEnt.grid(row = 3, column = 1, padx = 20, pady = 20)

def AddUser_AddCheckBox(self):
    self.StaffBoolBox = Checkbutton(self.LstFrm, text = "Teacher", command = self.StaffClear, bg = DefColor, font = ("Calibri", 12))
    self.StudentBoolBox = Checkbutton(self.LstFrm, text = "Student", bg = DefColor, font = ("Calibri", 12))
    self.StaffBoolBox.grid(row = 4, column = 1, padx = 20, pady = 20)
    self.StudentBoolBox.grid(row = 4, column = 0, padx = 20, pady = 20)

def AddUser_AddButton(self):
    self.SubBtn = Button(self.BtnFrm, text = "Create", height = 2, width = 10, fg = "black", activebackground = "yellow", bg = DefBtn, command = self.Create)
    self.SubBtn.grid(row = 0, column = 0, padx = 20, pady = 20)

def StaffLogin_AddStuff(self):
    self.Lbl = Label(self.parent, text = "Enter Staff Password", bg = DefColor, font = ("Calibri", 12))
    self.Ent = Entry(self.parent, bd = 4, width = 25, font = ("Calibri", 10), show = '*')
    self.Btn = Button(self.parent, text = "Login", height = 2, width = 10, fg = "black", activebackground = "yellow", bg = DefBtn, command = self.Check)
    self.Lbl.grid(row = 0, column = 0, padx = 20, pady = 20)
    self.Ent.grid(row = 1, column = 0, padx = 20, pady = 20)
    self.Btn.grid(row = 2, column = 0, padx = 20, pady = 20)

def MainMenu_AddLbls(self):
    self.WelcomeLbl = Label(self.LblFrm, text = "Welcome, please choose an option!", bg = DefColor, font = ("Calibri", 12))
    self.WelcomeLbl.grid(row = 0, column = 0, padx = 20, pady = 20)

def MainMenu_AddLstBox(self):
    self.MainMenuLst = Listbox(self.LstFrm, width = 25, font = ("Calibri", 12))
    self.MainMenuLst.grid(row = 0, column = 0, padx = 20, pady = 20)

def MainMenu_AddButton(self):
    self.SelectBtn = Button(self.BtnFrm, text = "Select", height = 2, width = 10, fg = "black", activebackground = "yellow", bg = DefBtn, command = self.GetSelection)
    self.SelectBtn.grid(row = 0, column = 0, padx = 20, pady = 20)

def AddTextBox(self):
    self.BackBtn =  Button(self.LblFrm, text = "<--", height = 2, width = 4, fg = "black", activebackground = "yellow", bg = DefBtn, command = self.Back)
    self.ContentsLbl = Text(self.LblFrm, width = "80", height = "30", bg = "white", wrap = NONE, bd = 4, font = ("Calibri", 12))
    self.Scroll = Scrollbar(self.LblFrm)
    self.HScroll = Scrollbar(self.LblFrm, orient = HORIZONTAL)
    self.ContentsLbl.grid(row = 1, column = 0, padx = 20, pady = 20)
    self.BackBtn.grid(row = 0, column = 0, padx = 20, pady = 20)
    self.Scroll.grid(row = 1, column = 1, padx = 20, pady = 20, sticky = 'ns')
    self.HScroll.grid(row = 2, column = 0, padx = 20, pady = 20, sticky = 'ew')
    self.ContentsLbl.config(yscrollcommand = self.Scroll.set)
    self.ContentsLbl.config(xscrollcommand = self.HScroll.set)
    self.Scroll.config(command = self.ContentsLbl.yview)
    self.HScroll.config(command = self.ContentsLbl.xview)
    self.ContentsLbl.insert(END, self.Contents)

def PopProtocols(self, PROTOCOLS):
    self.MainMenuLst.delete(0, END)
    for i in range(len(PROTOCOLS)):
        self.MainMenuLst.insert(i, PROTOCOLS[i])

def PopMenu(self, STAFFPM, MAINMENU):
    for i in range(len(MAINMENU)):
        if i == 2:
            if STAFFPM:
                self.MainMenuLst.insert(i, MAINMENU[i])
        else:
            self.MainMenuLst.insert(i, MAINMENU[i])
   
def PopProtocolCmds(self, ToAdd):
    for i in range(len(ToAdd)):
        self.MainMenuLst.insert(i, ToAdd[i])

def FlushFrm(self):
    self.MainMenuLst.destroy()
    self.SelectBtn.destroy()
    self.parent.geometry("700x710")

def AddLog(self, UpTo, cmds):
    self.BackBtn =  Button(self.LblFrm, text = "<--", height = 2, width = 4, fg = "black", activebackground = "yellow", bg = DefBtn, command = self.Back)
    self.ProtocolLbl = Label(self.LblFrm, text = cmds, bg = DefColor, font = ("Calibri", 12))
    self.CurrentPcl = Label(self.LblFrm, text = ("Currently Been Executed: " + UpTo), bg = DefColor, font = ("Calibri", 12))
    self.LogLbl = Label(self.LblFrm, text = "Log", bg = DefColor, font = ("Calibri", 12))
    self.LogTxt = Text(self.LblFrm, width = "80", height = "15", bg = "white", wrap = NONE, bd = 4, font = ("Calibri", 12))
    self.InpLbl = Label(self.LblFrm, text = "Input", bg = DefColor, font = ("Calibri", 12))
    self.InpTxt = Text(self.LblFrm, width = "80", height = "5", bg = "white", wrap = NONE, bd = 4, font = ("Calibri", 12))
    self.SvLog =  Button(self.BtnFrm, text = "Save Log", height = 2, width = 8, fg = "black", activebackground = "yellow", bg = DefBtn, command = self.SaveLog)
    self.ClearBtn =  Button(self.BtnFrm, text = "Clear Input", height = 2, width = 9, fg = "black", activebackground = "yellow", bg = DefBtn, command = self.Clear)
    self.NextBtn =  Button(self.BtnFrm, text = "Execute Next Command", height = 2, width = 19, fg = "black", activebackground = "yellow", bg = DefBtn, command = self.Next)
    self.SubBtn =  Button(self.BtnFrm, text = "Submit", height = 2, width = 19, fg = "black", activebackground = "yellow", bg = DefBtn, command = self.Submit)
    self.ScrollB = Scrollbar(self.LblFrm)
    self.ScrollB.grid(row = 4, column = 2, padx = 20, pady = 20, sticky = 'ns')
    self.LogTxt.config(yscrollcommand = self.ScrollB.set)
    self.ScrollB.config(command = self.LogTxt.yview)
    self.BackBtn.grid(row = 0, column = 1, padx = 20, pady = 20)
    self.ProtocolLbl.grid(row = 1, column = 1)
    self.CurrentPcl.grid(row = 2, column = 1)
    self.LogLbl.grid(row = 3, column = 1)
    self.LogTxt.grid(row = 4, column = 1, padx = 20, pady = 20)
    self.InpLbl.grid(row = 5, column = 1)
    self.InpTxt.grid(row = 6, column = 1, padx = 20, pady = 20)
    self.SvLog.grid(row = 7, column = 1, padx = 20, pady = 20)
    self.ClearBtn.grid(row = 7, column = 2, padx = 20, pady = 20)
    self.NextBtn.grid(row = 7, column = 3, padx = 20, pady = 20)
    self.SubBtn.grid(row = 7, column = 4, padx = 20, pady = 20)


def ResetLbl(self, UpTo):
    self.CurrentPcl.destroy()
    self.CurrentPcl = Label(self.LblFrm, text = ("Currently Been Executed: " + UpTo), bg = DefColor, font = ("Calibri", 12))
    self.CurrentPcl.grid(row = 2, column = 1)   
    
def ClearInp(self):
    self.InpTxt.delete(1.0, END)

def SaveLog(self, UpTo):
    FileName = "SavedSessions/" + UpTo + '_' + str(datetime.datetime.now())
    FileNameStripped = ''
    for i in FileName:
        if i not in [':', '.']:
            FileNameStripped += i
        else:
            FileNameStripped += '-'       
    print(FileNameStripped)        
    with open(FileNameStripped + '.txt', 'wb') as self.File:
        pickle.dump(self.LogTxt.get(1.0, END), self.File)


def AddFtp(self):
    self.LstFrm = Frame(self.parent, bg = DefColor)
    self.TxtFrm = Frame(self.parent, bg = DefColor)
    self.LstFrm.grid(row = 1, column = 0)
    self.TxtFrm.grid(row = 1, column = 1)
    self.BackBtn = Button(self.parent, text = "<--", height = 2, width = 4, fg = "black", activebackground = "yellow", bg = DefBtn, command = self.Back)
    self.TitleLbl = Label(self.parent, text = "FTP (Files Transmission Protocol) Modelled", bg = DefColor, font = ("Calibri", 12))
    self.InpEnt = Entry(self.LstFrm, bd = 4, width = 25, font = ("Calibri", 10))
    self.Selected = Label(self.LstFrm, text = "Selected: ", bg = DefColor, font = ("Calibri", 12))
    self.CMDLst = Listbox(self.LstFrm, width = 25, height = 19, font = ("Calibri", 12))
    self.RDLbl = Label(self.TxtFrm, text = "Remote Directory", bg = DefColor, font = ("Calibri", 12))
    self.RDTxt = Listbox(self.TxtFrm, width = 80, height = 11, font = ("Calibri", 12))
    self.LogLbl = Label(self.TxtFrm, text = "Log", bg = DefColor, font = ("Calibri", 12))
    self.LogTxt = Text(self.TxtFrm, width = "80", height = "10", bg = "white", wrap = NONE, bd = 4, font = ("Calibri", 12))
    self.ExeBtn = Button(self.LstFrm, text = "Execute", height = 2, width = 8, fg = "black", activebackground = "yellow", bg = DefBtn, command = self.Exe)
    self.SvLog = Button(self.TxtFrm, text = "Save Log", height = 2, width = 9, fg = "black", activebackground = "yellow", bg = DefBtn, command = self.SVLog)
    self.BackBtn.grid(row = 0, column = 0, padx = 20, pady = 20)
    self.TitleLbl.grid(row = 0, column = 1, padx = 20, pady = 20)
    self.InpEnt.grid(row = 0, column = 0, padx = 20, pady = 20)
    self.Selected.grid(row = 1, column = 0, padx = 40, pady = 20)
    self.CMDLst.grid(row = 2, column = 0, padx = 20, pady = 20)
    self.RDLbl.grid(row = 0, column = 0)
    self.RDTxt.grid(row = 1, column = 0, padx = 20, pady = 20)
    self.LogLbl.grid(row = 2, column = 0)
    self.LogTxt.grid(row = 3, column = 0, padx = 20, pady = 20)
    self.ExeBtn.grid(row = 3, column = 0, padx = 20, pady = 20)
    self.SvLog.grid(row = 4, column = 0, padx = 20, pady = 20)
    self.RDTxt.bind('<<ListboxSelect>>', self.UpdateLbl)
    self.ScrollBa = Scrollbar(self.TxtFrm)
    self.ScrollBa.grid(row = 1, column = 1, padx = 20, pady = 20, sticky = 'ns')
    self.RDTxt.config(yscrollcommand = self.ScrollBa.set)
    self.ScrollBa.config(command = self.RDTxt.yview)
    self.ScrollBar = Scrollbar(self.TxtFrm)
    self.ScrollBar.grid(row = 3, column = 1, padx = 20, pady = 20, sticky = 'ns')
    self.LogTxt.config(yscrollcommand = self.ScrollBar.set)
    self.ScrollBar.config(command = self.LogTxt.yview)
    
def PopulateRemote(self):
    self.RDTxt.delete(0, END)
    self.DirLst = self.FtpServer.nlst()
    for i in range(len(self.DirLst)):
        self.RDTxt.insert(i, (self.DirLst[i - 1]))

def EnterDirName(self):
    self.Lbl = Label(self.parent, text = "Enter Folder Name", bg = DefColor, font = ("Calibri", 12))
    self.Ent = Entry(self.parent, bd = 4, width = 25, font = ("Calibri", 10))
    self.Btn = Button(self.parent, text = "Create", height = 2, width = 10, fg = "black", activebackground = "yellow", bg = DefBtn, command = self.Create)
    self.Lbl.grid(row = 0, column = 0, padx = 20, pady = 20)
    self.Ent.grid(row = 1, column = 0, padx = 20, pady = 20)
    self.Btn.grid(row = 2, column = 0, padx = 20, pady = 20)
    
def InsertLog(self, TEXT):
    self.LogTxt.insert(END, TEXT)

def ShowError(self):
    messagebox.showerror("Folder Creation", "Please enter a file name in the entry above")

def FlushFlb(self, Txt):
    self.Selected.destroy()
    self.TEXT = ('Selected: ' + Txt)
    self.Selected = Label(self.LstFrm, text = self.TEXT, bg = DefColor, font = ("Calibri", 12))
    self.Selected.grid(row = 1, column = 0, padx = 40, pady = 20)

def AreYouSure(self):
    self.Del = messagebox.askyesno("Delete Query", ("Delete '" + self.Txt + "'\nAre you sure?"))
def OpenFile(self):
    self.filename = filedialog.askopenfilename()
def AskGetFile(self):
    self.Bool = messagebox.askyesno("Get File?", ("Get File '" +  self.Txt + "'\nFiles are downloaded to current directory"))
def RemoteDirInfo(self):
    messagebox.showinfo("Directory Change", "To change down, enter .. into the entry and execute cd again.")


def AddSources(self, F, STAFFPM):
    for i in range(len(F)):
        if i == 2:
            if STAFFPM:
                self.MainMenuLst.insert(i, F[i])
        else:
            self.MainMenuLst.insert(i, F[i])
def flushtelnet(self):
    self.TitleLbl.destroy()
    self.TitleLbl = Label(self.parent, text = "TELNET Modelled", bg = DefColor, font = ("Calibri", 12))
    self.TitleLbl.grid(row = 0, column = 1, padx = 20, pady = 20)

def PopulateTelnet(self, D):
    self.RDTxt.delete(0, END)
    for i in range(len(D)):
        self.RDTxt.insert(i, (D[i - 1]))

def ExcCmd(self, CMD):
    global FLOAT
    self.LogTxt.insert(END, ("\n--> Sending %s command to server..." % CMD))
    self.LogTxt.tag_add("here", "1.0", "2.0")
    self.LogTxt.tag_config("here", foreground = "red")
    try:
        self.sock.send((CMD.encode('utf-8')))
        Cmd = os.popen(CMD).read()
        self.LogTxt.insert(END, ("\n<-- Command recived and executed\
                              \n<-- Response: \n%s" % Cmd))
    except:
        self.LogTxt.insert(END, ("\nError, connection to remote host lost..."))

def DestroyInp(self):
    self.InpTxt.destroy()
    self.LogTxt.destroy()
    self.InpLbl.destroy()
    self.SubBtn.destroy()
    self.ClearBtn.destroy()
    self.LogTxt = Text(self.LblFrm, width = "80", height = "23", bg = "white", wrap = NONE, bd = 4, font = ("Calibri", 12))
    self.LogTxt.grid(row = 4, column = 1, padx = 20, pady = 20)
    self.LogTxt.config(yscrollcommand = self.ScrollB.set)
    self.ScrollB.config(command = self.LogTxt.yview)
