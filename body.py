import hashlib, os, gui, body, smtplib, ftpfile, adduser, Smtp, pickle, firstwindow, imapfile, telnet
from tkinter import *
from tkinter import messagebox
from ftplib import FTP
FTPCMDS = ["cd", "bye", "close", "delete", "get", "ls", "mkdir", "mget", "mput", "pwd", "rmdir"]
CONSTANTFILES = ['Passwords.txt', 'TeacherUsers.txt', 'UserNames.txt']
MAINMENU = ["Protocol List", "Load Previous", "View Source Code", "View Protocol Documents", "Help", "Exit"]
PROTOCOLS = ["SMTP", "IMAP" ,"FTP", "TELNET"]
SMTPArray = ["HELO", "MAIL FROM", "RCPT TO", "DATA", "QUIT"]
IMAPARRAY = ["LOGIN", "EXAMINE", "LIST", "FETCH", "LOGOUT"]
SOURCEFILES = ["adduser", "body", "ftpfile", "gui", "main", "Smtp", "imapfile", "SocketServer", "telnet"]
TELNETDIR = ["Stuff", "BoringStuff", "Secretfile.txt", "BarryMainlow.mp3", "ToyStory3.m4a"]
SALT = 'q1R{?zM,+& 9q%P|&g$^'
smtpCMDS = "SMTP COMMANDS: HELO, MAIL FROM, RCPT TO, DATA, QUIT"
imapCMDS = "IMAP COMMANDS: LOGIN, EXAMINE, LIST, FETCH, LOGOUT"
dosCMDS = ["tree", "exit", "mkdir", "dir", "ver", "tasklist", "ipconfig", "netstat"]
EMAILFROM = "fitssmodder@gmail.com"
PASSWORD = "protocols"
FileName = ''
STAFFPM = False
LOGGEDIN = False
def FlushDir():
    DIRCONTENTS = os.listdir()
    for i in range(len(CONSTANTFILES)):
        if CONSTANTFILES[i] not in DIRCONTENTS:
            for i in range(len(CONSTANTFILES)):
                FileCreate = open(CONSTANTFILES[i], 'w')
                FileCreate.close()     
            break
        
class FirstWindow():
    def __init__(self, parent):
        firstwindow.BuildConstruct(self, parent)
        self.X = False
        self.Z = False
    def ClearUsername(self, event):
        self.UserName.delete(0, END)
        
    def ClearPassword(self, event):
        self.Password.delete(0, END)

    def CreateUser(self):
        AddUser()

    def Login(self):
        firstwindow.login(self, SALT, self.X)
        if self.X:
            global STAFFPM
            STAFFPM = True
        if self.Z:
            MainMenu()

class AddUser():
    def __init__(self):
        adduser.Constructor(self)
        
    def Create(self):
        adduser.CreateUser(self, SALT)
           
    def StaffClear(self):
        x = self.UserNameEnt.get()
        StaffLogin(x)
    
class StaffLogin():
    def __init__(self, user):
        self.user = user
        self.parent = Tk()
        self.parent.title('StaffCredentials - Modelled')
        self.parent.geometry("250x250")
        gui.MainConstructor(self)
        gui.StaffLogin_AddStuff(self)

    def Check(self):
        if (self.Ent.get()) != 'stilton':
            messagebox.showerror("User Validation", "Password incorrect - Enter the correct password or a student account will be automaticaaly made.")
        else:
            global STAFFPM
            STAFFPM = True
            with open('TeacherUsers.txt', 'a') as self.File:
                self.File.write(hashlib.sha512((self.user + SALT).encode()).hexdigest() + '\n')            
            self.parent.destroy()

class MainMenu():
    def __init__(self):
        self.parent = Tk()
        self.parent.title('Main Menu')
        self.parent.geometry("280x400")
        gui.MainConstructor(self)
        gui.AddFrames(self)
        gui.MainMenu_AddLbls(self)
        gui.MainMenu_AddLstBox(self)
        gui.MainMenu_AddButton(self)
        gui.PopMenu(self, STAFFPM, MAINMENU)

    def GetSelection(self):
        self.selection = self.MainMenuLst.curselection()
        self.value = self.MainMenuLst.get(self.selection[0])        
        if self.value == MAINMENU[0]: ModelProtocols()
        if self.value == MAINMENU[1]: LoadPrevious()
        if self.value == MAINMENU[2]: ViewSource()
        if self.value == MAINMENU[3]: ViewDocs()
        if self.value == MAINMENU[4]: Help()
        if self.value == MAINMENU[5]: self.parent.destroy(); sys.exit()

class ViewDocs():
    def __init__(self):
        self.parent = Tk()
        self.parent.title('View Protocol Specifications')
        self.parent.geometry("250x320")
        gui.MainConstructor(self)
        gui.AddFrames(self)
        gui.MainMenu_AddLstBox(self) 
        gui.MainMenu_AddButton(self)
        gui.PopProtocols(self, PROTOCOLS)
        
    def GetSelection(self):
        self.selection = self.MainMenuLst.curselection()
        self.value = self.MainMenuLst.get(self.selection[0])
        self.FlushFrm()
        with open("Docs/" + self.value + ".txt", "r") as self.File:
            self.Contents = self.File.read()
            gui.AddTextBox(self)

    def FlushFrm(self):
        self.MainMenuLst.destroy()
        self.SelectBtn.destroy()
        self.parent.geometry("750x750")
        
    def Back(self):
        self.parent.destroy()
        ViewDocs()

class Help():
    def __init__(self):
        self.parent = Tk()
        self.parent.title('Help')
        self.parent.geometry("250x320")
        gui.MainConstructor(self)
        gui.AddFrames(self)
        gui.MainMenu_AddLstBox(self)
        gui.MainMenu_AddButton(self)
        gui.PopMenu(self, STAFFPM, MAINMENU)
        
    def GetSelection(self):
        self.selection = self.MainMenuLst.curselection()
        self.value = self.MainMenuLst.get(self.selection[0])
        if self.value == MAINMENU[0]:
            gui.PopProtocols(self, PROTOCOLS)

        else:
            gui.FlushFrm(self)
            self.FileName = "help/" + self.value + ".txt"
            with open(self.FileName, "r") as self.File:
                self.Contents = self.File.read()
                gui.AddTextBox(self)

    def Back(self):
        self.parent.destroy()
        Help()
        
class ViewSource():
    def __init__(self):
        self.parent = Tk()
        self.parent.title('View Source Code (Staff Only)')
        self.parent.geometry("250x320")
        gui.MainConstructor(self)
        gui.AddFrames(self)
        gui.MainMenu_AddLstBox(self)
        gui.MainMenu_AddButton(self)
        gui.AddSources(self, SOURCEFILES, STAFFPM)

    def GetSelection(self):
        self.selection = self.MainMenuLst.curselection()
        self.value = self.MainMenuLst.get(self.selection[0])
        with open((self.value + '.py'), "r") as self.File:
            self.Contents = self.File.read()
        self.parent.geometry("750x750")
        gui.AddTextBox(self)

    def Back(self):
        self.parent.destroy()
        ViewSource()

class ModelProtocols():
    def __init__(self):
        self.parent = Tk()
        self.parent.title('Modelling Protocols')
        self.parent.geometry("250x320")
        gui.MainConstructor(self)
        gui.AddFrames(self)
        gui.MainMenu_AddLstBox(self)
        gui.MainMenu_AddButton(self)
        gui.PopProtocols(self, PROTOCOLS)

    def GetSelection(self):
        self.selection = self.MainMenuLst.curselection()
        self.value = self.MainMenuLst.get(self.selection[0])
        self.parent.destroy()
        if self.value == PROTOCOLS[0]: SMTP()
        elif self.value == PROTOCOLS[1]: IMAP()
        elif self.value == PROTOCOLS[2]: ftp1()
        elif self.value == PROTOCOLS[3]: TELNET1()

class SMTP():
    def __init__(self):
        global LOGGEDIN
        if not LOGGEDIN:
            self.Question = messagebox.askyesno("Connect to Server", "Do you want to use your own Gmail account?\nIf not a defualt one will be used")
            if not self.Question:
                LOGGEDIN = True
            else:
                GmailLogin(self.Question, 'smtp') 
            
        if LOGGEDIN:
            Smtp.BuildConstruc(self, smtpCMDS)
                      
    def Clear(self):
        gui.ClearInp(self)

    def Next(self):
        Smtp.nextcmd(self, SMTPArray)

    def Back(self):
        self.parent.destroy()
        ModelProtocols()
        
    def SaveLog(self):
        gui.SaveLog(self, self.UpTo)

    def ConnectToServer(self):
        Smtp.Connect(self)
            
    def HELO(self):
        Smtp.helo(self)
        
    def MAILFROM(self):
        Smtp.mailfrom(self, EMAILFROM, PASSWORD)
            
    def RCPTTO(self):
        Smtp.rcptto(self)

    def Submit(self):
        Smtp.submit(self, EMAILFROM, PASSWORD)
        
    def DATA(self):
        Smtp.data(self)
        
    def QUIT(self):
        Smtp.quit(self)
       
                
class GmailLogin():
    def __init__(self, OwnAcc, CMD):
        self.CMD = CMD
        if OwnAcc:
            self.parent = Tk()
            self.parent.title('Input Gmail Details')
            self.parent.geometry("330x230")
            gui.MainConstructor(self)
            gui.AddFrames(self)
            gui.AddLabel(self)
            gui.AddEntrys(self)
            gui.MainMenu_AddButton(self)
        else:pass
        
    def GetSelection(self):
        global EMAILFROM, PASSWORD
        EMAILFROM = self.UserName.get()
        PASSWORD = self.Password.get()
        self.parent.destroy()
        global LOGGEDIN
        LOGGEDIN = True
        if self.CMD == 'imap':
            IMAP()
        else:
            SMTP()
        
    def ClearUsername(self, event):
        self.UserName.delete(0, END)
        
    def ClearPassword(self, event):
        self.Password.delete(0, END)

class ftp1():
    def __init__(self):
        ftpfile.BuildC(self)
        
    def Commence(self):
        ftpfile.Connect(self)
        self.Login()

    def Login(self):
        ftpfile.Login1(self)
        
    def Back(self):
        try:
            self.FtpServer.quit()
        except:pass
        self.parent.destroy()
        ModelProtocols()

    def SVLog(self):
        ftpfile.svlog(self)

    def Exe(self):
        ftpfile.GetCommand(self)

    def MKdirs(self):
        ftpfile.MakeD(self)  

    def Pwd(self):
        ftpfile.PWD(self)
            
    def Bye(self):
        ftpfile.CloseConnection(self)
        
    def Close(self):
        ftpfile.CloseConnection(self)

    def Ls(self):
        ftpfile.LS(self)
    
    def Del1(self):
        ftpfile.DeleteFile(self)
        
    def Get(self):
        ftpfile.GetF(self)
        
    def RMDir(self):
        ftpfile.RMdir(self)
        
    def Cd(self):
        ftpfile.CD(self)

    def put(self):
        ftpfile.Put(self)
    
    def UpdateLbl(self, event):
        self.Widget = event.widget
        self.Selection = self.Widget.curselection()
        self.Txt = self.Widget.get(self.Selection[0])
        gui.FlushFlb(self, self.Txt)

class LoadPrevious():
    def __init__(self):
        self.parent = Tk()
        self.parent.title('Load Previous')
        self.parent.geometry("250x320")
        gui.MainConstructor(self)
        gui.AddFrames(self)
        gui.MainMenu_AddLstBox(self)
        gui.MainMenu_AddButton(self)
        self.DirLst = os.listdir('SavedSessions')
        gui.AddSources(self, self.DirLst, STAFFPM)
        
    def GetSelection(self):
        self.selection = self.MainMenuLst.curselection()
        self.value = self.MainMenuLst.get(self.selection[0])
        with open(("SavedSessions/" + self.value), "rb") as self.File:
            self.Contents = pickle.load(self.File)
        self.parent.geometry("750x750")
        gui.AddTextBox(self)
    
    def Back(self):
        self.parent.destroy()
        LoadPrevious()

class IMAP():
    def __init__(self):
        global LOGGEDIN
        if not LOGGEDIN:
            self.Question = messagebox.askyesno("Connect to Server", "Do you want to use your own Gmail account?\nIf not a defualt one will be used")
            if not self.Question:
                LOGGEDIN = True
            else:
                GmailLogin(self.Question, 'imap')
        if LOGGEDIN:
            imapfile.Construct(self, imapCMDS)

    def Login(self):
        imapfile.login(self, EMAILFROM, PASSWORD)
        
    def Next(self):
        imapfile.nextcmd(self, IMAPARRAY)

    def Examine(self):
        imapfile.examine(self)
        
    def List(self):
        imapfile.list1(self)
        
    def Fetch(self):
        imapfile.fetch(self)
        
    def Logout(self):
        imapfile.logout(self)

    def Back(self):
        self.parent.destroy()
        ModelProtocols()

    def SaveLog(self):
        gui.SaveLog(self, self.UpTo)

    def Clear(self):
        gui.ClearInp(self)

    def Submit(self):pass

class TELNET1():
    def __init__(self):
        telnet.BuildCons(self)
        
    def Commence(self):
        telnet.commence(self, dosCMDS, TELNETDIR)

    def Back(self):
        self.parent.destroy()
        ModelProtocols()

    def Exe(self):
        telnet.execute(self, dosCMDS)

    def SVLog(self):
        gui.SaveLog(self, 'TELNET')

    def UpdateLbl(self, event):
        self.Widget = event.widget
        self.Selection = self.Widget.curselection()
        self.Txt = self.Widget.get(self.Selection[0])
        gui.FlushFlb(self, self.Txt)

    def Tree(self):
        telnet.tree(self)
        
    def Exit(self):
        telnet.exitc(self)
        
    def MKDir(self):
        telnet.mkdir(self)
        if bool(self.Obj):
            global TELNETDIR
            TELNETDIR.append(self.Obj)
            self.Obj = ''
        gui.PopulateTelnet(self, TELNETDIR)
        
    def Dir(self):
        telnet.dirm(self)
        
    def Ver(self):
        telnet.ver(self)
        
    def Mem(self):
        telnet.mem(self)
        
    def TaskList(self):
        telnet.tasklist(self)

    def IPconfig(self):
        telnet.ipconfig(self)

    def NetStat(self):
        telnet.netstat(self)






        
