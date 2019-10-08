from Getword import *

def Story4(debug = False):
    if debug: print("Story4 Function")
    
    print("\n")
    friendName1 = getName("Enter a name: ", debug)
    place2 = getPlace("Enter a place: ", debug)
    adjective2 = getAdjective("Enter adjective: ", debug)
    adjective3 = getAdjective("Enter another adjective: ", debug)
    food1 = getFood("Enter a food: ", debug)
    place2 = getPlace("Enter another place: ", debug)
    food1 = getFood("Enter a food: ", debug)
    youtuber1 = getYou("Enter a youtuber: ", debug)
    youtuber2 = getYou("Enter another youtuber: ", debug)
    food1 = getFood("Enter a food: ", debug)
    verb1 = getVerb("Enter a verb: ", debug)

    out = "\n"
    out += "One day me and my friend, " + friendName1
    out += " we went to " + place1 
    out += "\n"
    out += "We were having so much fun!"
    out += "\n"
    out += "Unfortunately,  " + adjective1
    out += "\n"
    out += "This made our game " + adjective2
    out += "\n"
    out += "Afterwards, we crawled to " + place1
    out += "\n"
    out += "We bought " + food1
    out += "\n"
    out += "We went back to my " + place2
    out += " and watched my favorite youtuber, " + youtuber1
    out += "\n"
    out += "My friend however, wanted to watch " + youtuber2
    out += "\n"
    out += "We decided to play " + videoGame1 + " instead."
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    return out
