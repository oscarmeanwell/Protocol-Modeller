def HelpMenu():
    print('\nWelcome to the Help menu!')
    Choice = input("""\nWhat would you like help with?

     1. SMTP
     2. IMAP
     3. FTP
     4. TELNET
     Input --> : """)
    if Choice == '1':
        File = 'SMTP.txt'
    elif Choice == '2':
        File = 'IMAP.txt'
    elif Choice == '3':
        File = 'FTP.txt'
    elif Choice == '4':
        File = 'TELNET.txt'
        
    with open(File, 'r') as FILE:
        print(FILE.read())
HelpMenu()
