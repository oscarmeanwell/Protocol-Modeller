import gui, os
from ftplib import FTP
from tkinter import *
from tkinter import messagebox
FTPCMDS = ["cd", "bye", "close", "delete", "get", "ls", "mkdir", "put", "pwd", "rmdir"]
def BuildC(self):
    self.parent = Tk()
    self.parent.title('Modelling FTP')
    self.parent.geometry("1000x750")
    gui.MainConstructor(self)
    self.Commence()
    self.Changedir = False
    self.UpTo = 'ftp'
    
def Connect(self):
    gui.AddFtp(self)
    for i in range(len(FTPCMDS)):
        self.CMDLst.insert(i, FTPCMDS[i - 1])
    
def Login1(self):
    self.FtpServer = FTP('syke.mooo.com')
##    self.FtpServer = FTP('192.168.1.10')
    self.LogIn = self.FtpServer.login('ftp1', 'f')
    self.LogTxt.insert(END, ("--> Connecting to FTP server...\
                                  \n<-- Connection Succesful\
                                  \n<-- Waiting for Login Credentials\
                                  \n--> Sending Username (ftp1) and Password ******"))
    
    if '230' in self.LogIn:
        self.LogTxt.insert(END, ("\n<-- 230 Login Succesful"))
        self.FtpServer.cwd('files')
        gui.PopulateRemote(self)
        
    else:
        self.LogTxt.insert(END, ("\n<-- 530 Login Incorrect"))
        
def GetCommand(self):
    self.selection = self.CMDLst.curselection()
    self.value = self.CMDLst.get(self.selection[0])
    if self.value == FTPCMDS[0]: self.Cd()
    elif self.value == FTPCMDS[1]: self.Bye()
    elif self.value == FTPCMDS[2]: self.Close()
    elif self.value == FTPCMDS[3]: self.Del1()
    elif self.value == FTPCMDS[4]: self.Get()
    elif self.value == FTPCMDS[5]: self.Ls()
    elif self.value == FTPCMDS[6]: self.MKdirs()
    elif self.value == FTPCMDS[7]: self.put()
    elif self.value == FTPCMDS[8]: self.Pwd()
    elif self.value == FTPCMDS[9]: self.RMDir()
    
    
def MakeD(self):
    self.FNm = self.InpEnt.get()
    if len(self.FNm) < 1:
        gui.ShowError(self)
    else:
        self.LogTxt.insert(END, ("\n--> Sending mkd (Make Directory) command to server...\
                                      \n <-- Waiting for directory name...\
                                      \n--> Sending direcotry name %s") % self.FNm)
        try:
            self.Query = self.FtpServer.mkd(self.FNm)
            self.LogTxt.insert(END, ("\n<-- Directory Creation Succesful!\
                                       \n<-- Created %s") % self.Query)
        except:
            self.LogTxt.insert(END, ("\n<-- 530, Directory Creation Failed!\
                                       \n<-- File name cannot contain \ / : * ? ' < > | "))
        gui.PopulateRemote(self)

def PWD(self):
    try:
        self.LogTxt.insert(END, ("\n--> Sending pwd Command (Get Remote Directory)...\
                                  \n<-- Current remote directory is: %s") % self.FtpServer.pwd())
    except:
        self.LogTxt.insert(END, ("\n--> Sending pwd Command (Get Remote Directory)...\
                                   \n <-- Error! Check your connection"))
def LS(self):
    self.LogTxt.insert(END, ("\n--> Sending nlst (List Remote Directory) Command..."))
    try:
        self.RDLS = self.FtpServer.nlst()
        self.Holder = ''
        for Char in self.RDLS:
            self.Holder += (Char + '\n\t')
        self.LogTxt.insert(END, ("\n<-- Directory Listing Succesful!\n%s") % self.Holder)
    except:
        self.LogTxt.insert(END, ("\n<-- 530, Could not list remoted directory...\
                                  \nCheck your connection!"))

def CloseConnection(self):
    self.LogTxt.insert(END, ("\n--> Sending close command (closes connection)"))
    self.LogTxt.insert(END, ("\n<-- %s" % self.FtpServer.quit()))

        
def DeleteFile(self):
    gui.AreYouSure(self)
    if self.Del:
        self.LogTxt.insert(END, ("\n--> Sending delete command to server..."))
        try:
            self.LogTxt.insert(END, ("\n<-- %s" % self.FtpServer.delete(self.Txt)))
        except:
            self.LogTxt.insert(END, ("\n<-- 550, Delete Operation failed!\
                                     \nThis command works only for files...\
                                     \n Is %s a directory? If so use rmdir" % self.Txt))
        gui.PopulateRemote(self)
    else:pass   
    
def RMdir(self):
    gui.AreYouSure(self)
    if self.Del:
        self.LogTxt.insert(END, ("\n--> Sending rmdir (delete a directory) command to server..."))
        try:
            self.LogTxt.insert(END, ("\n<-- %s" % self.FtpServer.rmd(self.Txt)))
        except:
            self.LogTxt.insert(END, ("\n<-- 550, Remove Directory operation failed."))
        gui.PopulateRemote(self)
    else:pass   
    
def Put(self):
    gui.OpenFile(self)
    self.Hold = os.path.basename(self.filename)
    self.LogTxt.insert(END, ("\n--> Sending put (upload file) command to server..."))
    try:
        with open(self.filename, 'rb') as self.Upload:
            self.FtpServer.storbinary(("STOR " + self.Hold), self.Upload)
        self.LogTxt.insert(END, ("\n<-- 150, OK to send data\
                                  \n--> Sending file %s\
                                  \n<-- 226 Transfer Complete" % self.Hold))
    except:
        self.LogTxt.insert(END, ("\nFile not found..."))
    gui.PopulateRemote(self)   
    
def GetF(self):
    gui.AskGetFile(self)
    if self.Bool:
        self.LogTxt.insert(END, ("\n--> Sending get (download file) command to server..."))
        try:
            with open(self.Txt, 'wb') as self.File:
                self.FtpServer.retrbinary(('RETR ' + self.Txt), self.File.write)
            self.LogTxt.insert(END, ("\n<-- 150, Opening Binary mode data connection for %s\
                                      \n<-- 226, Transfer Complete" % self.Txt))
        except:
            self.LogTxt.insert(END, ("\n<-- 550, Failed to open file..."))    
def CD(self):
    self.LogTxt.insert(END, ("\n--> Sending cd (Change Directory) command to server...\
                              \n<-- Waiting for remote directory name\
                              \n--> Sending Directory name..."))    
    if self.InpEnt.get() == '..':
        try:
            self.FtpServer.cwd('..')
            self.LogTxt.insert(END, ("\n<-- 250, Directory change succesful"))
        except:
            self.LogTxt.insert(END, ("\n<-- 550, Directory change unsuccesful"))
    else:
        try:
            self.FtpServer.cwd(self.Txt)
            self.LogTxt.insert(END, ("\n<-- 250, Directory change succesful"))
        except:
            self.LogTxt.insert(END, ("\n<-- 550, Directory change unsuccesful"))
        
        gui.RemoteDirInfo(self)
        
    self.InpEnt.delete(0, END)   
    gui.PopulateRemote(self)      
def svlog(self):
    gui.SaveLog(self, 'ftp')
