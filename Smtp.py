import smtplib, gui
from tkinter import *
from tkinter import messagebox
def BuildConstruc(self, smtpCMDS):
    self.parent = Tk()
    self.parent.title('Modelling SMTP')
    self.parent.geometry("760x800")
    gui.MainConstructor(self)
    gui.AddFrames(self)
    self.UpTo = ''
    gui.AddLog(self, self.UpTo, smtpCMDS)
    self.UpTo = 'HELO'
    gui.ResetLbl(self, self.UpTo)
    self.HELO()

def nextcmd(self, SMTPArray):
    if self.UpTo == SMTPArray[0]: self.MAILFROM()
    elif self.UpTo == SMTPArray[1]: self.RCPTTO()
    elif self.UpTo == SMTPArray[2]: self.DATA()
    elif self.UpTo == SMTPArray[3]: self.QUIT()
    
def Connect(self):
    try:
        self.Server = smtplib.SMTP('smtp.gmail.com', 587)
    except:
        messagebox.showerror("Connect to server", "Failed to connect to Gmails SMTP server...\nCheck your internet connection")
        self.parent.destroy()

def helo(self):
    self.ConnectToServer()
    self.Ehlo = self.Server.ehlo()
    self.Server.starttls()
    if 250 in self.Ehlo:
        self.LogTxt.insert(END, "--> Sending Request to connect to Gmail mail server (smtp.gmail.com)\
                       \nRequest sent to port 587\
                       \nGetting Relay response from Server\
                       \n<-- Resonse 220 - Connection succesful\
                       \n--> Sending HELO command to Server\
                       \nGetting Relay response from Server\
                       \n<-- Response 250 - mx.google.com at your service\
                       \nServer Ready and waiting...\n\n")
    else:
        self.LogTxt.insert(END, "Connection failed...\
                                  \nCheck your internet connection...\n\n")

def mailfrom(self, EMAILFROM, PASSWORD):
    self.UpTo = 'MAIL FROM'
    gui.ResetLbl(self, self.UpTo)
    self.LogTxt.insert(END, ("--> Send MAIL FROM command to Server\
                             \n<-- Server recived and listening\
                             \n--> Send email address to server " + EMAILFROM + "\
                             \n<-- Server recived - waiting for password\
                             \n--> Send Password to server - *********\
                             \nAttempting to Login to server using sent details..."))
    try:
        self.Server.login(EMAILFROM, PASSWORD)
        self.LogTxt.insert(END, "\n<-- Response 235 - Accepted\n")
    except:
        self.LogTxt.insert(END, "\n<-- Response Error - Check your internet connection...\n\n")
def rcptto(self):
    self.UpTo = 'RCPT TO'
    gui.ResetLbl(self, self.UpTo)
    self.InpTxt.insert(END, "Please clear this box and input who you want to send\
                              \nthe email to - If you want to send to multiple recipients\
                              \nseperate them with a comma! - Hit Submit when done")

def submit(self, EMAILFROM, PASSWORD):
    if self.UpTo == 'RCPT TO':           
        self.TO = []
        self.Holder = ''
        self.Hold = (self.InpTxt.get(1.0, END)) + ','
        for Line in self.Hold:
            
            if Line == ',':
                if len(self.Holder) < 1: break
                else:
                    self.TO.append(self.Holder.strip())
                    self.Holder = ''
            else:
                self.Holder += Line
        self.LogTxt.insert(END, ("\n--> Sending RCTP TO command to server\
                                 \n<-- Server waiting for packet"))
        self.LogTxt.insert(END, ("\n--> Sending packet to server... " + str(self.TO) + "\
                                  \n<-- Response 220 - Sucess"))
    elif self.UpTo == 'DATA':
        self.LogTxt.insert(END, ("\n\n--> Sending DATA command to server\
                                  \n<-- Server waiting for packet"))
        self.LogTxt.insert(END, "\n--> Sending packet to server...")
        try:
            self.Server.sendmail(EMAILFROM, [self.TO], (self.InpTxt.get(1.0, END)))
            self.LogTxt.insert(END, "\n<-- Response 220 - Message sent sucessfully!\n")
        except:
            self.LogTxt.insert(END,"\n<-- Response - Transmission failed...\n\n")       
    
def data(self):
    self.UpTo = 'DATA'
    gui.ResetLbl(self, self.UpTo)
    self.InpTxt.delete(1.0, END)
    self.InpTxt.insert(END, "Clear this and enter the message you want to send!\
                              \nThen hit submit!")

def quit(self):
    self.UpTo = 'QUIT'
    gui.ResetLbl(self, self.UpTo)
    self.Server.quit()
    self.LogTxt.insert(END,"\n--> 221 closing connection\
                             \n<-- Connection closed Succesfully!\n\n")
