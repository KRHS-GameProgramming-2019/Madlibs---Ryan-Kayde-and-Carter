#Made by Kaden Schusler
from Getword import *
from MadlibsScreens import *



def Story2(debug = False):
    if debug: print("Story2 Function")
    
    print("\n")
    friendName1 = getWord("Enter a name: ", debug)
    adjective1 = getAdjective("Enter an adjective: ", debug)
    adjective2 = getAdjective("Enter another adjective: ", debug)
    adjective3 = getAdjective("Enter another adjective: ", debug)
    adjective4 = getAdjective("Enter another adjective: ", debug)
    place1 = getPlace("Enter a place: ", debug)
    food1 = getFood("Enter a food: ", debug)
    food2 = getFood("Enter another food: ", debug)
    verb1 = getVerb("Enter a verb: ", debug)
    verb2 = getVerb("Enter another verb: ", debug)
    verb3 = getVerb("Enter another verb: ", debug)
    verb4 = getVerb("Enter another verb (future tense): ", debug)
    game1 = getGame("Enter a game: ", debug)
    youtuber1 = getYou("Enter a youtuber: ", debug)
    
    
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
    out += "\n"
    out += "I had to return him to his house, he looked back and said,"
    out += " 'I " + adjective3 + " you, we aren't friends anymore'"
    out += "\n"
    out += "I was " + adjective4 + ", I honestly don't even care though"
    out += "\n"
    out += "He is just too salty that I " + verb3 + " him"
    out += "\n"
    out += "I am kind of upset that " + friendName1 + " isn't my friend"
    out += "\n"
    out += "But you know what... " + verb4 + " 'em!"
    out += "\n"
    out += "I just went home and watched " + youtuber1 + " for the rest of the day" 
    
    

    
    
    
    return out
