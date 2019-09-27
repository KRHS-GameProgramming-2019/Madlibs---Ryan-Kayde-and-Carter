from Getword import *

def Story1(debug = False):
    if debug: print("Story1 Function")
    
    print("\n")
    friendName1 = getWord("Enter a name: ", debug)
    sport1 = getSport("Enter a sport: ", debug)
    adjective1 = getAdjective("Enter an adjective: ", debug)
    adjective2 = getAdjective("Enter an adjective: ", debug)
    
    
    out = "\n"
    out += "One day me and my friend, " + friendName1
    out += " were out playing " + sport1 
    out += "\n"
    out += "We were having so much fun!"
    out += "\n"
    out += "Unfortunately, the ground was " + adjective1
    out += "\n"
    out += "This made our game " + adjective2
    
    
    
    return out
