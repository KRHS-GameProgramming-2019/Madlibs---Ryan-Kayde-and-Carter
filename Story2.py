from Getword import *

def Story2(debug = False):
    if debug: print("Story1 Function")
    
    print("\n")
    friendName1 = getWord("Enter a name: ", debug)
    sport1 = getSport("Enter a sport: ", debug)
    adjective1 = getAdjective("Enter an adjective: ", debug)
    adjective2 = getAdjective("Enter another adjective: ", debug)
    adjective3 = getAdjective("Enter another adjective: ", debug)
    place1 = getPlace("Enter a place: ", debug)
    place2 = getPlace("Enter another place: ", debug)
    food1 = getFood("Enter a food: ", debug)
    youtuber1 = getYou("Enter a youtuber: ", debug)
    youtuber2 = getYou("Enter another youtuber: ", debug)
    verb1 = getVerb("Enter a verb: ", debug)
    
    
    
    
    out = "\n"
    out += "I went to my friend's house earlier"
    out += "His name was " + friendName1
    out += "I absolutely " + adjective3 + " him!"
    out += "After that, we " + verb1 + " to " + place1
    
    

    
    
    
    return out
