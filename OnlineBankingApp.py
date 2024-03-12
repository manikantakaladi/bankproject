#signin 
import math
def signin():
    global name
    global pin 
    global cb 
    name=str(input("Create Your Username : "))
    pin=str(input("Please Create Your Six Digit Pin : "))
    if len(pin)==6:
        pin=pin
    else:
        print("The Pin Has to be Six Digit in lenth")
        newpin=str(input("Please Create Your Six Digit Pin : "))
        if len(newpin)!=6:
            print("The Pin Has to be Six Digit in Length")
            signin()
        else:
            pin=newpin
    print("Thanks For Creating Bank Account")
    mainmenu()

#forgotpin
def forgotpin():
    recoverpin=str(input("Please Enter your new 6 Digit pin : "))
    if len(recoverpin)!=6:
        print("The Pin has to be in 6 Digits")
        forgotpin()
    else:
        print("The New Pin has been stored , Please Login")
        pin=recoverpin
        login()

#Compound Intrest
def depositIntrest(p,r,t):
    #A=Pe^rt Formula to Find Compound Intrest
    #A Final Price #P Principal Amount(Initial Value) #r Rate of Intrest #t time period
    p=float(p)
    r=float(r)
    t=float(t)
    rt=r*t
    e=math.exp(rt)
    a=p*e
    return a
    print("Final Price = ",depositIntrest(1000,0.038,6))
def login():
    name1=str(input("Enter User Name : "))
    pin1=str(input("Enter User Pin : "))
    if name1==name and pin1==pin:
        print("Welcome to Canara Bank : "+name1)
        print("Please Check the Below Menu : ")
        listmenu=["1-Deposit","2-Withdraw","3-Transfer","4-Check Balance","5-Deposit Intrest Rate","6-Calculate compound Intrest"]
        for h in listmenu:
            print(h)
        option=int(input("Enter Number of your choice : "))
        d=0
        w=0
        cb=0
        if option==1:
            d=int(input("Enter Deposit Amount : "))
            cb=d
            print("Current Balance is : "+str(cb)+" $")
            login()
        elif option==2:
            w=int(input("Enter Withdrawl Amount : "))
            if w>cb:
                print("Current Balance is not sufficient for the Transcation")
                login()
            else:
                cb=d-w
                print(str(w)+" has been Withdrawn from your account ")
                print("Current Balance is : "+str(cb))
            
        elif option==3:
            dest=str(input("Enter Receiver Account Number in 8 Digits : "))
            if len(dest)==8:
                amount=int(input("Enter amount to Transfer : "))
                if amount>cb:
                    print("Current Balance is Not Sufficient for this Transaction")
                    login()
                else:
                    cb=d-amount
                    print("Transaction of "+str(amount)+" has been transfered to "+str(dest))
                    print("Your Current Balance is : "+str(cb))
            else:
                print("Transaction Rejected since Receiver account is invalid ")
                login()
        elif option==4:
            print("Your Current Balance is : "+str(cb))
            login()
        elif option==5:
            if d>50000:
                rate=3
            elif d>30000:
                rate=2
            else:
                rate=1.5
            print("Your Current Deposit intrest rate is : "+str(rate))
            
        elif option==6:
            listoption=["1-Calculate Your Deposit Compoung Intrest Based on your CB","2-Calculate your deposit compound intrest based on your deposit"]
            for n in listoption:
                print(n)
            option=int(input("Enter Your Choice : "))
            if option==1:
                timing=str(input("How Many years you want to invest money : "))
                if d>50000:
                    ratex=3/100
                elif d>30000:
                    ratex=2/100
                else:
                    ratex=1.5/100
                print("Your Current Balance in "+timing+" "+"years will be : ")
                print(depositIntrest(cb,ratex,timing))
            elif option==2:
                timing1=str(input("How Many years you want to invest money : "))
                money=str(input("Enter Deposit Money : "))
                money=int(money)
                if d>50000:
                    ratex=3/100
                elif d>30000:
                    ratex=2/100
                else:
                    ratex=1.5/100
                print("Your Current Balance in "+timing+" "+"years will be : ")
                print(depositIntrest(cb,ratex,timing1))
            else:
                print("Option is Not Available")
                login()
            
    else:
        print("Either User Name or Pin are Incorrect,Did You Created Your account?")
        list1=["1-YES","2-NO"]
        for i in list1:
            print(i)
        option=int(input("Enter Your Choice Below : "))
        if option==1:
            list2=["1-Do You Want to Login again?","2-Forgot Your Pin"]
            for e in list2:
                print(e)
            theanswer=str(input("Enter Choice : "))
            theanswer=int(theanswer)
            if theanswer==1:
                login()
            elif theanswer==2:
                forgotpin()
            else:
                print("Option is Not Available")
                login()
        elif option==2:
            print("Please Create Your Account")
            signin()

def mainmenu():
    optionone=int(input("Choose 1 to Signin,Choose 2 to Login "))
    if optionone == 1:
        signin()
    elif optionone == 2:
        login()
    else:
        print("Option is Not Available")
        mainmenu()
    exit()

def exit():
    option=str(input("Do You Still want to Make Transaction : ?, Yes/No"))
    if(option=="Yes"):
        login()
    elif(option=="No"):
        print("Thank You for Using the App")
    else:
        print("Option is not available")
        mainmenu()
        
mainmenu()