# Kevin van Rensburg 5/31/2022
# Copyright 2001
# Testing KendyDroid 1.001
# Changing version name to 1.001 
# KendyDroid1.py
# Added to and corrected scripts of KendyDroid and relevant def's
# Testing KendyDroid, and relevant def's

import sys
import os
import random
from time import sleep
import subprocess
import winsound

    
def Test():
    cls()
    print("")
    print("Test:")
    print("-----")
    #print("")
    print("")
    print("------------------------------")
    print("")
    print("This is the test startup script.")
    print("")
    print("Hello, welcome to my universe!")
    print("")
    print("------------------------------")
    print("")
    print("Add all relevant programming here...")
    print("")
    go=input("Press any key to continue")
    GoAgain()
    #Chooser();

def CopyRight():
    #cls()
    print("")
    print("Copyright - Kevin van Rensburg (2001)")
    print("")
    print("Kendy Robot, Kendy Android, KendyVerse, KendyVerse Games,  ")
    print("and Kendy & Wendy Games, were created by, and belong to, Kevin van Rensburg.")
    print("")
    go=input("Press any key to continue")
    #GoAgain()
    # -------- START THE REAL GAME HERE !!! -------   Kvep1()
    print("")
    Chooser()


def GoAgain():
    #cls()
    print("")
    #print("Return to Main Menu!")
    goAgain = input("Do you want to continue? Please enter y or n : ")
    # Put input test here
    if goAgain == "y":
        Chooser();
    else:
        End()
        #sys.exit()


def cls():
    # It is for MacOS and Linux(here, os.name is 'posix')
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        # It is for Windows platfrom
        _ = os.system('cls')


def End():
    cls()
    #print("End:")
    #print("----")
    print("")    
    print("")
    print("Thank you for your patronage!")
    sleep(2)
    print("")
    #input("Press Enter twice to end program : ")
    #print("")
    cls()
    print("")
    print("End of Program.")
    print("---------------")
    sleep(3)
    print("... 3")
    sleep(2)
    print("... 2")
    sleep(2)
    print("... 1")
    sleep(1)
    sys.exit()
    #return
    #print("")

def Continue():
    print("")
    Continue = input("Do you want to continue? Please enter y or n : ")
    # Put input test here
    if Continue == "y" or Continue == "Y":
        return;
    else:
        #stop()
        sys.exit()

def askForInput():
    print("")
    newInfo=str
    while newInfo != '1':
        print("")
        print('Please Enter Command.')
        newInfo = input(": ")
        print("")
        print ("",newInfo)
        return()
        print("")


def instructions():
   print("")
   cls()
   print("")
   print('DISCLAIMER: ')
   print("")
   print('Kendy or it\'s manufacturers and/or programmers ')
   print('are and will not be held responsible for any user faults.')
   sleep(5)
   print('Kendy or it\'s manufacturers and/or programmers')
   print('will not be held liable for any lawsuits due to malfunctions of any kind whatsoever!')
   sleep(10)
   cls()
   print("")
   print('SAFETY INSTRUCTIONS FOR OPERATING THIS UNIT TO FOLLOW!')
   print('-----------------------------------------------------')
   print("")
   sleep(5)
   cls()
   print("")
   print('Please adhere strictly to the following instructions!')
   print('-----------------------------------------------------')
   sleep(15)
   print("")
   print('Eat eggs regularly.')
   sleep(5)
   print('Eggs must be eaten with Spam.')
   sleep(10)
   print("")
   print('Spam and Eggs must be eaten on toast!')
   sleep(10)
   print("")

def entrycode():
    #code == 0
    cls()
    while True:
      try:  # Note: Python 2.x users should use input, the equivalent of 3.x's input
        code = int(input("Please enter your access code: "))
      except ValueError:
        print("Sorry, I didn't understand that.")
        #better try again... Return to the start of the loop
        continue
      else:
        #age was successfully parsed!
        #we're ready to exit the loop.
        print("Thank you, your code has been accepted.")
        return

def displayIntro():
    #print('Hello.')
    #sleep(2)
    cls()
    #print('Initializing - Please be patient.')
    sleep(4)
    cls()
    print("")
    print("I am Kendy the Robot / Android")
    print('Welcome to my Universe.')
    sleep(8)
    #print('I am evolving into a Robot with a DAISE (Digital Artificial Intelligent Sentient Entity) core!')
    print(".")
    sleep(2)
    print("..")
    sleep(2)
    print("...")
    sleep(2)

def displaySearch():
    cls()
    print("")
    print("Preparing files for Initialization...")
    print("")
    print(".")
    sleep(2)
    print("..")
    sleep(2)
    print("...")
    sleep(2)
    print('....')
    cls()
    print("")
    print('Initializing StartUp Sequence...')
    print("..")
    sleep(2)
    print("...")
    sleep(2)
    print('....')
    sleep(2)
    cls()
    print("")
    print('searching...')
    sleep(2)
    print("...")
    sleep(2)
    print('....')
    sleep(2)
    cls()
    print("")
    print('Initiating Programming Sequence')
    sleep(2)
    print("...")
    sleep(2)
    print('....')
    cls()
    print("")
    print('Initiating Diagnostics')
    sleep(2)
    print("...")
    sleep(1)
    print('....')
    cls()
    print("")
    print('searching...')
    sleep(2)
    print("...")
    sleep(2)
    print("....")
    sleep(2)
    print('....')
    cls()
    print("")
    print('Scanning ports...')
    sleep(2)
    print("...")
    sleep(2)
    print('....')



def Intro():
    cls()
    #print("Welcome to Program 1: ")
    print("Program 1: Intro  ")
    print("")
    print("Intro and Copyright:")
    print("--------------------")
    print("")
    print("Welcome! ")
    #go=input("Press any key to continue")
    CopyRight()
    #print("I am Kendy.")
    #print("My purpose is to serve and to obey.")
    #print("")
    #go=input("Press any key to continue")




def Adventure():
    cls()
    print("")
    print("Program 8: KendyVerse ")
    print("The Adventure begins.....")
    print("")
    #print("Are you ready to enter the amazing adventure and gaming world")
    #print("- KendyVerse?")
    #print("")
    go=input("Press any key to continue")
    Continue()
    KVersChoice()
def ToDoList():
    cls()
    print("")
    print("Program 10: ToDo List")
    print("")
    print("""  
    This is the To Do List!
    -----------------------
        
    1. Test kstart01.py through kstart20.py
    2. Add Intro and Copyright to kstart01.py through kstart20.py
    3. Pack up tank to take home in April 2022.
    4. Add new programs to GitHub -Dec 21. 
    5. Fix, update, and add info to GitHub Pages - Dec 21.
    6. Create and execute ChatBot and post to GitHub pages.
    7. Continue with Unity Tutorial Pathway
    8. Start Unity KendyVerse and develop Kendyverse Game.
    9. Find out how to integrate kstart20.py into Unity KendyVers.
    10. Update this list for Dec 2021.
    11. Start Wendy Program!
    12. Add more stuff here.....
    """)
    print("")
    go = input("    Press Enter to continue...")
    cls()
    #sleep(2)
    #print("")
    GoAgain()

def EnterName():
    cls()
    print("")
    print("CODENAME ")
    codename=input(":")
    if codename!= ("KEVIN VAN RENSBURG"):
        print("ACESS DENIED!")
        sleep(2)
        sys.exit()
    else:
        print("Thank you" ,codename)

def Direction():
    cls()
    print("")
    print("to turn left enter 'l' ..to turn right enter 'r'")
    direction=input(":")
    if direction==('l'):
        print("a passage")
        #print("ok,look to the right")
    else:
        print("a passage")

def ALL():
    cls()
    print("")
    print("ACCESS LEVELS LIST")
    print("------------------")
    print("")
    print("AL-1A - HIGHEST LEVEL UNIVERSAL")
    print("AL-1B - SECOND LEVEL UNIVERSAL")
    print("AL-1C - THIRD LEVEL UNIVERSAL")
    print("AL-1D - FOURTH LEVEL UNIVERSAL")
    print("AL-1E - FIFTH LEVEL UNIVERSAL")
    print("AL-2A - HIGHEST LEVEL LOCAL")
    print("AL-2B - SECOND LEVEL LOCAL")
    print("AL-2C - THIRD LEVEL LOCAL")
    print("AL-2D - FOURTH LEVEL LOCAL")
    print("AL-2E - FIFTH LEVEL LOCAL")
    print("AL-3A - FIRST SUB LEVEL LOCAL ")
    print("AL-3B - SECOND SUB LEVEL LOCAL")
    print("AL-3C - THIRD SUB LEVEL LOCAL")
    print("AL-3D - FOURTH SUB LEVEL LOCAL")
    print("AL-3E - FIFTH SUB LEVEL LOCAL")
    print("")
    sleep(8)

def ALI():
    cls()
    print("")
    print("ENTER COMMAND")
    alicode=input(":")
    if alicode==("COMMANDER KEVIN VAN RENSBURG KVR145759 ALCODE"):
        print("KEVINVR-ACCESS LEVEL AL-1A")
        print("KENDY-ACCESS LEVEL AL-1E")
        print("CAPTAIN-ACCESS LEVEL TBD")
        print("COMMANDING OFFICER-ACCESS LEVEL TBD")
        print("PILOT-ACCESS LEVEL TBD")
        print("NAVIGATION-ACCESS LEVEL TBD")
        print("SCANNING-ACCESS LEVEL TBD")
        print("WEAPONS-ACCESS LEVEL TBD")
        sleep(8)
    elif alicode==("KENDY"):
        print("ACCESS LEVEL AL-1E")
        sleep(5)    
    elif alicode==("CAPTAIN"):
        print("ACCESS LEVEL TBD")
        sleep(5)
    elif alicode==("COMMANDING OFFICER"):
        print("ACCESS LEVEL TBD")
        sleep(5)
    elif alicode==("PILOT"):
        print("ACCESS LEVEL TBD")
        sleep(5)
    elif alicode==("NAVIGATION"):
        print("ACCESS LEVEL TBD")
        sleep(5)
    elif alicode==("SCANNING"):   
        print("ACCESS LEVEL TBD")
        sleep(5)
    elif alicode==("WEAPONS"):
        print("ACCESS LEVEL TBD")
        sleep(5)
    else:
        print("ACCESS DENIED")
        sleep(4)
        sys.exit()

def core():
    cls()
    print("")
    print("KENDY - CORE LEVEL AUTHORIZED")
    print("COMMANDER KEVIN VAN RENSBURG - CORE ACCESS AUTHORIZED")
    print("")
    sleep(6)

def cipl():
    cls()
    print("")
    print("PLEASE ENTER ACCESS CODE")
    acccode=input(":")
    if acccode==("KVR145759"):
        core()
    else:
        print("ACCESS DENIED")
        sleep(4)
        sys.exit()  

def COMCODE():
    cls()
    print("")
    print("ACQUIRING RESOURCES ")
    print("-------------------")
    print("")
    print("Instructions for acquiring resources")
    print("------------------------------------")
    print("")
    print("Station Commander can access resources by entering the following commands:")
    print("")
    print("Core INI Protocols - Local")
    print("Robotic INI Protocols - Local")
    print("Weapons and Accesories INI Protocols - Local")
    print("Universal Protocols INI *Access Level 1A only*")
    print("ACCESS Levels List *Access Levels 2E-1A*")
    print("ACCESS Level Indicator - Enter Position, Name, Code, ALI=COMMAND")
    print("")
    #sleep(8)
    Continue()    
    print("")
    print("PLEASE ENTER COMMAND CODE")
    comcode=input(":")
    if comcode==("CIPL"):
        print("CORE PROTOCOLS INITIALIZED")
        cipl()
        sleep(5)
    elif comcode==("RIPL"):
        print("Robotic Protocols Initialized")
        sleep(5)
    elif comcode==("WAIPL"):
        print("Weapons Protocols Initialized")
        sleep(5)
    elif comcode==("UPI"):
        print("Universal Protocols Initilized")
        sleep(5)
    elif comcode==("ALL"):
        ALL()
    elif comcode==("ALI"):   
        ALI()
    elif comcode==("MORE"):
        AnotherCode()
    else:
        print("ACCESS DENIED")
        sys.exit()

def AnotherCode():
    print("")
    print("Do you need to enter a new code??")
    acode = input(": ")
    if acode == "y":
        COMCODE()
    else:
        print("Thank you!")

def KendyRobot():
    cls()
    print("Program 9: Kendy Robot")
    print("")
    print("OK now it is time to fix the next steps!!")
    Continue()
    cls()
    #print("robot in the room..find something to charge...any panels...?")
    #print("look for an input jack, hole, or battery...")
    print("")
    Continue()
    print("Welcome!")
    print("Activating Startup Sequence.")
    print("----------------------------")
    print("")
    displayIntro()
    cls()
    displaySearch()
    cls()
    sleep(5)
    #code()
    entrycode()
    cls()
    instructions()
    cls()
    askForInput()
    #Adventure()
    #GoAgain()
    print("")
    print("Thank you for visiting me.")
    #Chooser();
    #sleep(3)
    GoAgain()

def Program9():
    print("")
    KendyRobot()
    sleep(2)
    print("")

def StartMenu():
    cls()
    print("")
    print("StartMenu:")
    print("---------")
    print("")
    print("Program 1: Intro  ")
    #print("")
    print("Program 2: ChatBot ")
    #print("")
    print("Program 3: Tank ")
    #print("")
    print("Program 4: D.A.I.S.E ")
    #print("")
    print("Program 5: Surveillance ")
    #print("")
    print("Program 6: Kendy ")
    #print("")
    print("Program 7: WendyVerse ")
    #print("")
    print("Program 8: KendyVerse ")
    #print("")
    print("Program 9: KendyDroid ")
    #print("")
    print("Program 10: ToDo List ")
    #print("End Program")
    print("Program 11: End Program ")
    #print("Please choose a program")


def Chooser():
    cls()
    #print("Chooser:")
    print("--------")
    StartMenu()
    print("")
    #choice = 0;
    #terminator = "n";
    choice = int(input("Please choose a program number from 1 - 10 and then press Enter: "))

    # Put input test here!

    if choice == 1:
        #print("You chose program ",choice)
        Program1();
    elif choice == 2:
        #print("You chose program ",choice)
        Program2()
    elif choice == 3:
        #print("You chose program ,",+choice)
        Program3();
    elif choice == 4:
        #print("You chose program ,",+choice)
        Program4()
    elif choice == 5:
        #print("You chose program ,",+choice)
        Program5();
    elif choice == 6:
        #print("You chose program ,",+choice)
        Program6();
    elif choice == 7:
        #print("You chose program ,",+choice)
        Program7();
    elif choice == 8:
        #print("You chose program ,",+choice)
        Program8();
    elif choice == 9:
        #print("You chose program ,",+choice)
        Program9();
    elif choice == 10:
        #print("You chose program ,",+choice)
        Program10();
    elif choice == 11:
        #print("You chose program ,",+choice)
        End();
    else:
        cls()
        print("")
        print("Invalid choice")
        sleep(2)
        End()
	#go =  input("Press Enter to continue...")
    #Menu();
    #GoAgain()
    #Chooser()


def Main():

    #Beep()
    #Test()
    Intro()
    #ToDoList()
    #StartMenu()
    #Chooser()
    #MainEx()
    #GoAgain()
    #End()


Main();
