from MadlibsScreens import *
def getMenuOption(debug = False):
    if debug: print("getMenuOption Function")
    
    goodInput = False
    
    while not goodInput:
        option = input("Please select an option: ")
        option = option.lower()
        
        if (option == "q" or 
        option == "quit" or
        option == "x" or 
        option == "exit"):
            option = "q"
            goodInput = True
        
        elif (option == "1" or 
        option == "one" or
        option == "Story1" or
        option == "StoryOne" or 
        option == "Storyone"):
            option = "1"
            goodInput = True
        elif (option == "2" or 
        option == "two" or
        option == "Story2" or
        option == "StoryTwo" or 
        option == "Storytwo"):
            option = "2"
            goodInput = True
        elif (option == "3" or 
        option == "three" or
        option == "Story3" or
        option == "StoryThree" or 
        option == "Storythree"):
            option = "3"
            goodInput = True
        elif (option == "4" or 
        option == "four" or
        option == "Story4" or
        option == "StoryFour" or 
        option == "Storyfour"):
            option = "4"
            goodInput = True
        elif (option == "stonks"):
            option = "stonks"
            goodInput = True
            
        else:
            print("Please make a valid choice")

    return option




def getWord(prompt, debug = False):
    if debug: print("getWord Function")
    
    goodInput = False
    
    while not goodInput:
        word = input(prompt)
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print ("Don't use language like that")
        
        
    return word
    
def getName(prompt, debug = False):
    if debug: print("getWord Function")
    
    goodInput = False
    
    while not goodInput:
        word = input(prompt)
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print ("Don't use language like that")
        
        
    return word


def getSpecificName(prompt, debug = False):
    if debug: print("getSpecificName Function")
    
    goodInput = False
    
    specificName = ["k3arsarg3",
    ]
    
    while not goodInput:
        word = input(prompt)
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print ("Don't use language like that")
        elif word.lower() not in specificName:
            goodInput = False
            print ("That's not my name, try again")
    return word
    
    
    
def getSpecificConsole(prompt, debug = False):
    if debug: print("getSpecificName Function")
    
    goodInput = False
    
    specificConsole = ["sega dreamcast",
    ]
    
    while not goodInput:
        word = input(prompt)
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print ("Don't use language like that")
        elif word.lower() not in specificConsole:
            goodInput = False
            print ("YOU WILL NEVER GUESS IT, try again!")
    return word


    
    
    
#Written by Kaden/Ryan
def getSport(prompt, debug = False):
    if debug: print("getSport Function")
    
    goodInput = False
    
    sports = ["soccer",
              "football",
              "basketball",
              "tennis",
              "wiffle ball",
              "hockey",
              "field hockey",
              "lacrosse",
              "bad minton",
              "swimming",
              "swim",
              "cheerleading",
              "boxing",
              "chinese wiffle boxing",
              "lumberjack",
              "hobbyhorsing",
              "volleyball",
              "tag",
              "parkour",
              "world chase tag",
              "jousting",
              "cardboard fighting",
              "cardboard tube fighting league",
              "horse riding",
              "horseback riding",
              "bowling",
              "track",
              "field",
              "track and field",
              "snowboarding",
              "skiing",
              "wrestling",
              "esports",
    ]
    
    while not goodInput:
        word = input(prompt)
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print ("Don't use language like that")
        elif word.lower() not in sports:
            goodInput = False
            print ("That's not a sport stupid, try again")
    return word
    
    
    
#Written by Kaden/Ryan   
def isSwear(word, debug = False):
    if debug: print("isSwear Function")
    if word.lower() in swearList:
        return True
    else:
        return False

swearList = ["poop",
             "pee",
             "sex",
             "damn",
             "bernie sanders",
             "hillary clinton",
             "kyle",
             "mackenna",
             "42",
             "shit",
             "booty",
             "booty hole",
             "butt",
             "butthole",
             "nigger",
             "fuck",
             "penis",
             "dick",
             "beef whistle",
             "pork sword",
             "vagina",
             "pussy",
             "meat curtains",
             "cunt",
             "roast beef wallet",
             "bitch",
             "karen",
             "big k",
             "kkk",
             "douche",
             "douche bag",
             "shit bag",
             "fucked",
             
             
             
            
]

#Written by Kaden/Ryan 
def getAdjective(prompt, debug = False):
    if debug: print("getWord Function")
    
    goodInput = False
    
    while not goodInput:
        word = input(prompt)
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print ("Don't use language like that")
        
    return word

#Written by Kaden/Ryan 
def getPlace(prompt, debug = False):
    if debug: print("getWord Function")
    
    goodInput = False
    
    while not goodInput:
        word = input(prompt)
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print ("Don't use language like that")
        
    return word

#Written by Kaden/Ryan 
def getFood(prompt, debug = False):
    if debug: print("getWord Function")
    
    goodInput = False
    
    while not goodInput:
        word = input(prompt)
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print ("Don't use language like that")
        
    return word
    
    
#Written by Kaden/Ryan 
def getYou(prompt, debug = False):
    if debug: print("getYou Function")
    
    goodInput = False
    
    youtuber = ["smosh",
                "t-series",
                "pewdiepie",
                "ninja",
                "myth",
                "loveliveserve",
                "the king of random",
                "the game theorists",
                "bob ross",
                "ted-ed",
                "jontron",
                "markiplier",
                "rocketjump",
                "ben phillips",
                "good mythical morning",
                "mismag822",
                "ryan higa",
                "nigahiga",
                "the men who do nothing",
                "game grumps",
                "the grumps",
                "hellthy junkfood",
                "unbox therapy",
                "minecraft",
                "nintendo",
                "brackeys",
                "blackthornprod",
                "cody ko",
                "noel miller",
                "dani",
                "metal jesus rocks",
                "metaljesusrocks",
                "ifht films",
                "gmbn",
                "ben shapiro",
                "edp445",
                "mbest11x",
                "adam calhoun",
            
                
    
    ]
    
    while not goodInput:
        word = input(prompt)
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print ("Don't use language like that")
        elif word.lower() not in youtuber:
            goodInput = False
            print ("I don't know that youtuber try again")
        elif word == "metaljesusrocks":
            print (EasterEggScreen())
    return word
    
    
#Written by Kaden/Ryan     
def getGame(prompt, debug = False):
    if debug: print("getWord Function")
    
    goodInput = False
    
    while not goodInput:
        word = input(prompt)
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print ("Don't use language like that")
        
    return word
    
    
#Written by Ryan     
def getDay(prompt, debug = False):
    if debug: print("getDay Function")
    
    goodInput = False
    
    day = ["monday",
           "tuesday",
           "wednesday",
           "thursday",
           "friday",
           "saturday",
           "sunday",
    
    ]
    
    while not goodInput:
        word = input(prompt)
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print ("Don't use language like that")
        elif word.lower() not in day:
            goodInput = False
            print ("I don't know that day try again")
    return word       
                 
                
            
#Written by Kaden/Ryan                 
def getVerb(prompt, debug = False):
    if debug: print("getWord Function")
    
    goodInput = False
    
    while not goodInput:
        word = input(prompt)
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print ("Don't use language like that")
        
    return word




#Written by Ryan 
def getTrack(prompt, debug = False):
    if debug: print("getTrack Function")
    
    goodInput = False
    
    track = ["baby park",
             "donut plains 3",
             "music park",
             "maple treeway",
             "koopa troopa beach",
             "cheese land",
             "electrodome",
             "coconut mall",
             "tick tock clock",
             "dk jungle parkway",
             "moo moo meadows",
             "walugi pinball",
             "ghost valley 1",
             "bowser's castle",
             "rainbow road",
             "wario stadium",
             "luigi circuit",
             "big blue",
             
                 
           
        
    
    ]
    
    while not goodInput:
        word = input(prompt)
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print ("Don't use language like that")
        elif word.lower() not in track:
            goodInput = False
            print ("I don't know that track try again")
    return word
    
    
    
    
#Written by Ryan     
def getItem(prompt, debug = False):
    if debug: print("getItem Function")
    
    goodInput = False
    
    item = ["coin",
            "banana",
            "green shell",
            "red shell",
            "fake item box",
            "triple bananas"
            "mushroom",
            "triple shells"
            "bobomb",
            "bomb",
            "blooper",
            "blue shell",
            "triple mushrooms",
            "lucky seven",
            "golden mushroom",
            "bullet",
            "lightning",
            "star",
            "fireball",
            "boomerang",
            "piranha plant",
            "super horn",
            "feather",
            "boo",
            "mega mushroom",
             
                 
           
        
    
    ]
    
    while not goodInput:
        word = input(prompt)
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print ("Don't use language like that")
        elif word.lower() not in item:
            goodInput = False
            print ("I don't know that item try again")
    return word
    
#written by Carter
def getMonster(prompt, debug = False):
    if debug: print("getWord Function")
    
    goodInput = False

    monsters = ["angel",
                "archon",
                "basilisk",
                "beholder",
                "bulette",
                "cyclops",
                "death knight",
                "demon",
                "devil",
                "dragon",
                "dragonborn",
                "drake",
                "drider",
                "dryad",
                "duergar",
                "dwarf",
                "elemental",
                "elf",
                "gargoyle",
                "ghoul",
                "gnome",
                "goblin",
                "golem",
                "hag",
                "human",
                "lizalfos",
                "bakoblin",
                "medusa",
                "minotaur",
                "mummy",
                "ogre",
                "orc",
                "octorok",
                "moblin",
                "wizrobe",
                "lynel",
                "chuchu",
                "guardian",
                "keese",
                "pebblit",
                "yiga",
                "ghost",
                "wizard",
                "seproth",
                ]
    while not goodInput:
        word = input(prompt)
        goodInput = True
        if isSwear (word, debug):
            goodInput = False
            print ("Thats not a monster")
        elif word.lower()in monsters:
            
            goodInput = True
    
    return word
    
