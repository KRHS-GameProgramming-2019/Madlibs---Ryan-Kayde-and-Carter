from Getword import *

def Story1(debug = False):
    if debug: print("Story1 Function")
    
    print("\n")
    friendName1 = getWord("Enter a name: ", debug)
    sport1 = getSport("Enter a sport: ", debug)
    adjective1 = getAdjective("Enter an adjective: ", debug)
    adjective2 = getAdjective("Enter another adjective: ", debug)
    place1 = getPlace("Enter a place: ", debug)
    place2 = getPlace("Enter another place: ", debug)
    food1 = getFood("Enter a food: ", debug)
    youtuber1 = getYou("Enter a youtuber: ", debug)
    youtuber2 = getYou("Enter another youtuber: ", debug)
    videoGame1 = getGame("Enter a videogame: ", debug)
    
    
    
    
    
    out = "\n"
    out += "One day me and my friend, " + friendName1
    out += " were out playing " + sport1 
    out += "\n"
    out += "We were having so much fun!"
    out += "\n"
    out += "Unfortunately, the ground was " + adjective1
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
