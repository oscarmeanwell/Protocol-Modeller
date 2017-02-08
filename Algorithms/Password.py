Pwd = input('Please enter a password: ')
Error = ''
LowerFlag = False
UpperFlag = False
NumberFlag = False
LenFlag = False
NotContFlag = False
if len(Pwd) > 5:
    LenFlag = True

for j in range(1, len(Pwd) + 1):
    Ascii = ord(Pwd[j - 1])
    if Ascii > 96 and Ascii < 123:
        LowerFlag = True
    
    if Ascii > 64 and Ascii < 91:
        UpperFlag = True

    if Ascii > 47 and Ascii < 58:
        NumberFlag = True

if not LenFlag:
    Error += "Your password is a little on the short side...\n"
    
if not LowerFlag:
    Error += "Maybe add a few lower case letters?\n"
    
if not UpperFlag:
    Error += "Maybe add a few upper case letters?\n"
    
if not NumberFlag:
    Error += "Maybe add a few Numbers?\n"
    
if len(Error) > 0:
    print("Password Strength", "These Errors were found!\n")
