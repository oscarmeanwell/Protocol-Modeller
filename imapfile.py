import gui, imaplib, email, re
from tkinter import *
from tkinter import messagebox
def Construct(self, imapCMDS):
    self.parent = Tk()
    self.parent.title('Modelling IMAP')
    self.parent.geometry("760x800")
    gui.MainConstructor(self)
    gui.AddFrames(self)
    self.UpTo = ''
    gui.AddLog(self, self.UpTo, imapCMDS)
    gui.DestroyInp(self)
    self.UpTo = 'LOGIN'
    gui.ResetLbl(self, self.UpTo)
    self.Login()
    
def login(self, EMAILFROM, PASSWORD):
    try:
        self.IMAPserver = imaplib.IMAP4_SSL('imap.gmail.com', 993)
        self.IMAPserver.login(EMAILFROM, PASSWORD)
        self.LogTxt.insert(END, ("--> Connecting to imap.gmail.com on port 993...\
                                    \n<-- Connection Succesful!"))
    except:
        self.LogTxt.insert(END, ("Connection to imap.gmail.com on port 993, failed...\
                                    \nCheck your internet connection!"))

def nextcmd(self, IMAPARRAY):
    if self.UpTo == IMAPARRAY[0]: self.Examine()
    elif self.UpTo == IMAPARRAY[1]: self.List()
    elif self.UpTo == IMAPARRAY[2]: self.Fetch()
    elif self.UpTo == IMAPARRAY[3]: self.Logout()
        
def examine(self):
    self.UpTo = 'EXAMINE'
    gui.ResetLbl(self, self.UpTo)
    try:
        self.ResponseMsg, self.cnt = self.IMAPserver.select('Inbox')
        if self.ResponseMsg == 'OK':
            self.LogTxt.insert(END, ("\n--> Sending 'EXAMINE Inbox' request\
                                     \n<-- OK, Inbox selected"))
    except:
        self.LogTxt.insert(END, ("\n--> Sending 'EXAMINE Inbox' request\
                                       \n<-- NO, Unknown Mailbox!\
                                       \n<-- (now in authenticated state) (Failure)"))
def list1(self):
    self.UpTo = 'LIST'
    gui.ResetLbl(self, self.UpTo)
    self.ResponseMsg, self.Data = self.IMAPserver.search(None, 'All')
    self.Regex = re.compile('[0-9]+')
    self.No = ''
    for Char in str(self.Data): #Gets the amount of emails in the inbox.
        for j in Char:
            x = self.Regex.search(j)
            if bool(x):
                self.No = ''
                self.No += j
                x = False
    print(self.No)
    if self.ResponseMsg == 'OK':
        self.LogTxt.insert(END, ("\n--> Sending LIST INBOX request\
                                  \n<-- OK\
                                  \n<-- There is %s emails in your inbox") % self.No)
    else:
        self.LogTxt.insert(END, ("\n<-- NO, problem listing emails...\
                                 \n<-- Check your internet connection!"))
    
def fetch(self):
    self.UpTo = 'FETCH'
    gui.ResetLbl(self, self.UpTo)
    for i in self.Data[0].split():
        self.ResponseMsg, self.Data = self.IMAPserver.fetch((i), '(RFC822)') #FETCH
        Message = email.message_from_bytes((self.Data[0][1]))
        if Message.is_multipart():
            for part in Message.walk():       
                if part.get_content_type() == "text/plain":
                    try:
                        body = part.get_payload(decode = True) 
                        Body = body.decode()

                    except:
                        pass


    self.EmailBody = ("To: %s \nFrom: %s\nSubject: %s\n%s" % (Message['To'], Message['From'], Message['Subject'], Body))               
    if 'OK' in self.ResponseMsg:
        self.LogTxt.insert(END, ("\n--> Sending FETCH command...\
                                  \n<-- OK\
                                  \n<-- Transmitting email at index location 1\
                                   \n %s") % self.EmailBody)
    else:
        self.LogTxt.insert(END, ("\n<-- NO, problem fetching emails...\
                                 \n<-- Check your internet connection!"))
def logout(self):
    self.UpTo = 'LOGOUT'
    gui.ResetLbl(self, self.UpTo)
    self.cl = self.IMAPserver.close()
    self.Lo = self.IMAPserver.logout()
    if 'OK' in self.cl:
        self.LogTxt.insert(END, ("\n--> Sending request to close connection...\
                                  \n<-- OK, Returned to authenticated state. <Sucess>"))
    else:
        self.LogTxt.insert(END, ("\n--> Sending request to close connection...\
                                  \n<-- NO, Cannot to authenticated state. <Failure>"))
    if 'BYE' in self.Lo:
        self.LogTxt.insert(END, ("\n--> Sending request to Logout...\
                                   \n<-- BYE, LOGOUT Requested"))
    else:
        self.LogTxt.insert(END, ("\n--> Sending request to Logout...\
                                   \n<-- NO, LOGOUT Failed"))
