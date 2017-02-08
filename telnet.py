import gui, subprocess, socket, os
from tkinter import *
from tkinter import messagebox
def BuildCons(self):
    self.parent = Tk()
    self.parent.title('Modelling Telnet')
    self.parent.geometry("1000x750")
    gui.MainConstructor(self)
    gui.AddFtp(self)
    self.Commence()
    
def commence(self, dosCMDS, TELNETDIR):
    gui.flushtelnet(self)
    for i in range(len(dosCMDS)):
        self.CMDLst.insert(i, dosCMDS[i - 1])
    self.SOCK = subprocess.Popen('SocketServer.py 1', shell=True)
    self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.server_address = ('127.1.1.1', 1000)
    self.sock.connect(self.server_address)
    gui.PopulateTelnet(self, TELNETDIR)
    self.LogTxt.insert(END, ("--> Sending TELNET command to protocol server on port 23...\
                             \n<-- Waiting for Login details...\
                             \n--> Sending Empty string\
                             \n<-- Logging in as anomalous user\
                             \n<-- Success!"))

def execute(self, dosCMDS):
    self.selection = self.CMDLst.curselection()
    self.value = self.CMDLst.get(self.selection[0])
    if self.value == dosCMDS[0]: self.Tree()
    elif self.value == dosCMDS[1]: self.Exit()
    elif self.value == dosCMDS[2]: self.MKDir()
    elif self.value == dosCMDS[3]: self.Dir()
    elif self.value == dosCMDS[4]: self.Ver()
    elif self.value == dosCMDS[5]: self.TaskList()
    elif self.value == dosCMDS[6]: self.IPconfig()
    elif self.value == dosCMDS[7]: self.NetStat()
def tree(self):
    gui.ExcCmd(self, 'tree')
    
def exitc(self):
    gui.ExcCmd(self, 'exit')
    self.SOCK.kill()
        
def mkdir(self):
    if len(self.InpEnt.get()) <1:
        messagebox.showerror("Make Directory", "Please enter a directory name into the entry above!")
    else:
        self.Obj = self.InpEnt.get()
        self.LogTxt.insert(END, ("\n--> Sending mkdir command to server..."))
        self.LogTxt.insert(END, ("\n<-- Command recived and executed\
                              \n<-- Response: Directory Creation Succesful"))
def dirm(self):
    gui.ExcCmd(self, 'dir')
def ver(self):
    gui.ExcCmd(self, 'ver')

def tasklist(self):
    gui.ExcCmd(self, 'tasklist')

def ipconfig(self):
    gui.ExcCmd(self, 'ipconfig')
    
def netstat(self):
    gui.ExcCmd(self, 'netstat')
