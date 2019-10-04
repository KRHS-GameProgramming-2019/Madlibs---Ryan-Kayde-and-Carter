from Getword import *

def Story2(debug = False):
    if debug: print("Story2 Function")
    
    print("\n")
    friendName1 = getWord("Enter a name: ", debug)
    adjective1 = getAdjective("Enter an adjective: ", debug)
    adjective2 = getAdjective("Enter another adjective: ", debug)
    place1 = getPlace("Enter a place: ", debug)
    food1 = getFood("Enter a food: ", debug)
    food2 = getFood("Enter another food: ", debug)
    verb1 = getVerb("Enter a verb: ", debug)
    verb2 = getVerb("Enter another verb: ", debug)
    game1 = getGame("Enter a game: ", debug)
    
    
    
    out = "\n"
    out += "I went to my friend's house earlier"
    out += "\n"
    out += "His name was " + friendName1
    out += "\n"
    out += "I absolutely " + verb1 + " him in " + game1 + "!"
    out += "\n"
    out += "After that, we " + verb2 + " our way to " + place1
    out += "\n"
    out += "" + friendName1 + " wanted to eat " + food1 + " so we did"
    out += "\n"
    out += "Then we went back to playing " + game1
    out += "\n"
    out += "This match was so " + adjective1 + "!"
    out += "\n"
    out += "Afterwards we were both so " + adjective2 + "!"
    out += "\n"
    out += "My mom made us " + food2 + ", it wasn't too good though"
    out += "\n"
    out += "" + friendName1 + " never wants to play " + game1 + " anymore"


    

    
    
    
    return out
