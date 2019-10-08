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
    
    out = "\n"
    out += "we were in the darkness of the night, it got so dark it led my friend and I apart, " + friendName1
    out += " we got spereated and I found myself in " + place2 
    out += "\n"
    out += "We were having so much fun!"
    out += "\n"
    out += "Unfortunately,  " + adjective2
    out += "\n"
    out += "This made our game " + adjective3
    out += "\n"
    out += "Afterwards, we crawled to " + place2
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
