##import hashlib
##SALT = 'a18fmh($@.,dg1GKUR9*/D'
##UserName = input('Please enter a Username: ')
##Password = input('Please enter a Password: ')
##ConfPwd = input('Please confirm your Password: ')
##Credentials = input('Teacher (t) or Student (s): ').lower()
##if Password != ConfPwd:
##    print('Passwords do not match!!')
##else:
##    with open('UserNames.txt', 'a') as File:
##        File.write(hashlib.sha512((UserName + SALT).encode()).hexdigest() + '\n')
##                
##    with open('Passwords.txt', 'a') as PwdFile:
##        PwdFile.write(hashlib.sha512((Password + SALT).encode()).hexdigest() + '\n')
##
##    if Credentials == 't':
##        with open('StaffUsers.txt', 'a') as File:
##            File.write(hashlib.sha512((UserName + SALT).encode()).hexdigest() + '\n')

import hashlib
UserNamesArray = []
PasswordsArray = []
StaffUsersArray = []
Credentials = 'Student'
SALT = 'a18fmh($@.,dg1GKUR9*/D'
UserName = input('Please enter a Username: ')
Password = input('Please enter a Password: ')
UserHold = hashlib.sha512((UserName + SALT).encode()).hexdigest()
PwdHold = hashlib.sha512((Password + SALT).encode()).hexdigest()
Files = ['UserNames.txt', 'Passwords.txt', 'StaffUsers.txt']
for i in range(len(Files)):
    with open(Files[i], 'r') as TempFile:
        for Line in TempFile:
            if i == 0: UserNamesArray.append(Line.strip())
            if i == 1: PasswordsArray.append(Line.strip())
            if i == 2: StaffUsersArray.append(Line.strip())
if UserHold in UserNamesArray:
    if PwdHold == PasswordsArray[UserNamesArray.index(UserHold)]:
        if UserHold in StaffUsersArray:
            Credentials = 'Staff'
        print('Login Sucessful! Welcome ' + Credentials + ' User!')
    else:
        print('Password Incorrect')
else:
    print('Username does not exist')

