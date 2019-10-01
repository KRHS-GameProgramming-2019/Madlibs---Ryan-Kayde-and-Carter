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


def getPlace(prompt, debug = False):
    if debug: print("getPlace Function")
    
    goodInput = False
    
    place = ["walmart",
             "house",
             "home",
             "school",
             "target",
             "mcdonalds",
             "burger king",
             "pizza chef",
             "market basket",
             "frenchs park",
             "french's park",
             "wendys",
             "dunkin donuts",
             "paris",
             "best buy",
             "store",
             "taco bell",
             "bed bath and beyond",
             "hospital",
             "kmart",
             "tj maxx",
             "dicks sporting goods",
             "dick's",
             "bjs",
             "pet smart",
             "yo mama",
             "your mama",
             
             
    
    ]
    
    while not goodInput:
        word = input(prompt)
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print ("Don't use language like that")
        elif word.lower() not in place:
            goodInput = False
            print ("I don't know that place try again")
    return word


def getFood(prompt, debug = False):
    if debug: print("getFood Function")
    
    goodInput = False
    
    food = ["pizza",
            "burger",
            "spaghetti",
            "sandwich",
            "turkey sandwich",
            "ham sandwich",
            "ice cream",
            "ben and jerry's tonight dough",
            "ben and jerry's",
            "chips",
            "cheez itz",
            "fried chicken",
            "chicken",
            "waffles",
            "pancakes",
            "chocolate",
            "tacos",
            "burritos",
            "cinnamon rolls",
            "m'n'ms",
            "french fries",
            "brownies",
            "cake",
            "cupcakes",
            "cleanex",
            "bleach",
            "tide pods",
            "dog",
            "cat",
            "stromboli",       
    
    ]
    
    while not goodInput:
        word = input(prompt)
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print ("Don't use language like that")
        elif word.lower() not in food:
            goodInput = False
            print ("I don't know that food try again")
    return word
    
    
    
def getYou(prompt, debug = False):
    if debug: print("getFood Function")
    
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
    return word
    
    
    
def getGame(prompt, debug = False):
    if debug: print("getFood Function")
    
    goodInput = False
    
    videogame = ["smash",
                 "legend of zelda",
                 "overwatch",
                 "paladins",
                 "fortnite",
                 "minecraft",
                 "call of duty",
                 "hearthstone",
                 "league of legends",
                 "hotline miami",
                 "gta",
                 "mario",
                 "kirby",
                 "pac man",
                 "ms pac man",
                 "terraria",
                 "breath of the wild",
                 "fire emblem",
                 "mario kart",
                 "no man's sky",
                 "animal crossing",
                 "luigi's mansion",
                 "pokemon",
                 "moonlighter",
                 "guitar hero",
                 "splatoon",
                 "splatoon 2",
                 "star fox",
                 "star fox zero",
                 
                
            
                
    
    ]
    
    while not goodInput:
        word = input(prompt)
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print ("Don't use language like that")
        elif word.lower() not in videogame:
            goodInput = False
            print ("I don't know that videogame try again")
    return word
