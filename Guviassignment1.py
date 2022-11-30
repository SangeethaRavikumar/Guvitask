print("!!!WELCOME!!!!!")
file = open("logindetails.txt","r")
class Login:
    def userInput(self):
        self.validInput = None
        print("\n Enter 1 for Registration")
        print("\n Enter 2 for User Login")
        print("\nEnter 3 for forget password")
        self.option = input()
        if self.option.isdigit() == False or int(self.option) > 3:
            print("Invalid")
            self.validInput = False
        else:
            self.validInput = True
            self.option = int(self.option)
        return self.validInput, self.option

    def userLogin(self):
        self.loginID = input("\n Enter the login User ID::")
        self.loginPWD = input("\nEnter the Password::")


    def register(self):
        self.reg_email = input("Enter THe User ID for registration:::")
        self.s = input("Set your password:::")

    def newuserIDvalidation(self):
        import re
        self.validID = None
        #print("*****Please Register now******")
        self.regex = '^[a-z]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        #self.reg_email = input("Enter ur Email id for registration:::")
        self.match = re.search(self.regex, self.reg_email)
        if self.match == False:
            self.validID = False
            print("Invalid User ID")

        else:
            self.validID = True
            with open("logindetails.txt", "r") as f:
                for line in f:
                    textcontent = line.strip().split(",")
                    if self.reg_email == textcontent[0]:
                        print("User ID already exists..Please enter new user ID")
        return self.validID
    def newpwdvalidation(self):
        l, u, p, d = 0, 0, 0, 0
        self.validpwd = None
        #self.s = input("Enter the password for Registration:::")
        if (len(self.s) >= 5 and len(self.s) <= 16):
            for i in self.s:
                if (i.islower()):
                    l += 1
                if (i.isupper()):
                    u += 1
                if (i.isdigit()):
                    d += 1
                if (i == '@' or i == '$' or i == '_'):
                    p += 1
                if (l >= 1 and u >= 1 and p >= 1 and d >= 1 and l + p + u + d == len(self.s)):
                    self.validpwd = True
        else:
            print('INVALID PASSWORD')
            self.validpwd = False
        return self.validpwd

    def updateinregister(self):
        file = open("logindetails.txt", "a")
        file.write(f'\n{self.reg_email},{self.s}')
        print("REGISTRATION SUCCESSFUL.....")
    def existinguserID(self):
        self.idvalidate = None
        #self.loginID = input("Enter your existing Email-ID:::")
        with open("logindetails.txt", "r") as f:
            for line in f:
                textcontent = line.strip().split(",")
                if self.loginID == textcontent[0]:
                    self.idvalidate = "Existing User"
                    #loginPWD = input("Enter your password:::")
                    if self.loginPWD == textcontent[1]:
                        self.idvalidate =="Good"
                        print("LOGIN SUCCESSFUL...")
                    else:
                        self.idvalidate = "Incorrect Password"
                        print("Incorrect Password")
        return self.idvalidate
    def fetchpassword(self):
        self.choice = None
        print("Click RP for retrieve password And SN for Set new password ")
        # file = open("logindetails.txt", "r")
        self.choice = input()
        if self.choice == "RP":
            self.fetchuserid = input("Enter your existing User ID:::")
            self.fetchcheck = False
            with open("logindetails.txt", "r") as f:
                for line in f:
                    for word in line:
                        textcontent = line.strip().split(",")
                        if self.fetchuserid == textcontent[0]:
                            t1 = textcontent[1]
                            self.fetchcheck = True
                            print(f"\n The retrieved password for the user Id---{self.fetchuserid}---- is {t1}")
                            break
                if self.fetchcheck == False:
                    print("\n user ID does not exists.Pls try with existing user ID.")
        else:
            file = open("logindetails.txt", "r")
            self.fetchcheck = None
            self.loginmail = input("Enter your Existing Email ID:::")
            with open("logindetails.txt", "r") as f:
                for line in f:
                    textcontent = line.strip().split(",")
                    if self.loginmail == textcontent[0]:
                        self.s = input("Enter your new password::::")
                        l, u, p, d = 0, 0, 0, 0
                        if (len(self.s) >= 5 and len(self.s) <= 16):
                            for i in self.s:
                                if (i.islower()):
                                    l += 1
                                if (i.isupper()):
                                    u += 1
                                if (i.isdigit()):
                                    d += 1
                                if (i == '@' or i == '$' or i == '_'):
                                    p += 1
                        if (l >= 1 and u >= 1 and p >= 1 and d >= 1 and l + p + u + d == len(self.s)):
                            self.s1 = input("Enter your confirm password:::")
                            if self.s == self.s1:
                                with open("logindetails.txt", "r") as f:
                                    for line in f:
                                        for word in line:
                                            textcontent = line.strip().split(",")
                                            if self.loginmail == textcontent[0]:
                                                with open("logindetails.txt", "w") as f:
                                                    f.write(f'\n{self.loginmail},{self.s1}')
                                                    f.write("\n")
                                                    print("LOGIN SUCCESSFUL....")
                                                    break
            return self.fetchcheck

n1 = Login()
flag,option = n1.userInput()
while(flag!= True):
    flag,option = n1.userInput()
if option == 1:
    n1.register()
    idcheck = None
    pwdcheck = None

    idcheck = n1.newuserIDvalidation()

    if idcheck == True:
            pwdcheck = n1.newpwdvalidation()
    while (idcheck != True or pwdcheck != True):
            n1.register()
    else:
        n1.updateinregister()
        print("Do u want to login Y/N:::")
        choice = input()
        if choice == "Y":
            n1.userLogin()
            idcheck = None
            pwdcheck = None
            idvalidate = n1.existinguserID()
            if idvalidate == None:
                print("User ID does not Exist.....")
                n1.register()
                idcheck = n1.newuserIDvalidation()
                if idcheck == True:
                    pwdcheck = n1.newpwdvalidation()
                while (idcheck != True or pwdcheck != True):
                    n1.register()
                    idcheck = n1.newuserIDvalidation()
                    if idcheck == True:
                        pwdcheck = n1.newpwdvalidation()
                else:
                    n1.updateinregister()
        else:
            print("Thank U.......")
elif option == 2:
    n1.userLogin()
    idcheck = None
    pwdcheck = None
    idvalidate = n1.existinguserID()
    if idvalidate == None:
        print("User ID does not Exist.....")
        n1.register()
        idcheck = n1.newuserIDvalidation()
        if idcheck == True:
            pwdcheck = n1.newpwdvalidation()
        while (idcheck != True or pwdcheck != True):
            n1.register()
            idcheck = n1.newuserIDvalidation()
            if idcheck == True:
                pwdcheck = n1.newpwdvalidation()
        else:
            n1.updateinregister()
    elif idvalidate == "Incorrect Password":
        while (idvalidate == "Incorrect Password"):
            n1.userLogin()
            idvalidate = n1.existinguserID()
            if idvalidate == None:
                print("User does not exist in Database..")
                n1.register()
                idcheck = n1.newuserIDvalidation()
                if idcheck == True:
                    pwdcheck = n1.newpwdvalidation()
                    while (idcheck != True or pwdcheck != True):
                        n1.register()
                        idcheck = n1.newuserIDvalidation()
                        if idcheck == True:
                            pwdcheck = n1.newpwdvalidation()
                        else:
                            n1.updateinregister()
elif option == 3:
    fetchcheck = n1.fetchpassword()
    if fetchcheck == False:
        while (fetchcheck != True):
            fetchcheck = n1.fetchpassword()









