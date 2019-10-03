from MadlibsScreens import *
from Getword import *
from Story1 import *
from Story2 import *
from Story3 import *
from Story4 import *

def Madlibs(debug = False):
    if debug: print("Welcome to debug")
    
    print(TitleScreen(debug))
    try:

        input("Press enter to continue")
    except:
        pass
        
    done = False
    
    while not done:
        print(MainMenu(debug))
        choice = getMenuOption (debug)
        
        if choice == "q":
            exit();
        elif choice == "1":
            print(Story1())
            print("\n")
            input("Press enter to continue")
        elif choice == "2":
            print(Story2())
            print("\n")
            input("Press enter to continue")
        elif choice == "3":
            print(Story3())
            print("\n")
            input("Press enter to continue")
        elif choice == "4":
            print(Story4())
            print("\n")
            input("Press enter to continue")
Madlibs(False)

