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
             
             
             
            
]


def getAdjective(prompt, debug = False):
    if debug: print("getAdjective Function")
    
    goodInput = False
    
    adjective = ["juicy",
                 "wet",
                 "tall",
                 "short",
                 "mad",
                 "raging",
                 "sad",
                 "peppa piggish",
                 "bad",
                 "great",
                 "rubbery",
                 "big",
                 "red",
                 "blue",
                 "fast",
                 "slow",
                 "dry",
                 "weak",
                 "strong",
    
    ]
    
    while not goodInput:
        word = input(prompt)
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print ("Don't use language like that")
        elif word.lower() not in adjective:
            goodInput = False
            print ("I don't know that adjective try again")
    return word
