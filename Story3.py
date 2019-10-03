from Getword import *

def Story3(debug = False):
    if debug: print("Story3 Function")
    
    print("\n")
    weekDay1 = getDay("Enter a weekday: ", debug)
    marioCharacter1 = getCharacter("Enter a character: ", debug)
    marioCharacter2 = getCharacter("Enter another character: ", debug)
    marioCharacter3 = getCharacter("Enter another character: ", debug)
    marioCharacter4 = getCharacter("Enter another character: ", debug)
    marioCharacter5 = getCharacter("Enter another character: ", debug)
    
    
    
    
    out = "\n"
    out += "Today was " + weekDay1 + ","
    out += "\n"
    out += "Mario Kart day!"
    out += "\n"
    out += "my friends and I got our controllers and selected characters."
    out += "Kaden wanted to play as " + marioCharacter1 + ","
    out += "\n"
    out += "Carter wanted to play as " + marioCharacter2 + ","
    out += "\n"
    out += "Troy wanted to play as " + marioCharacter3  + ","
    out += "\n"
    out += "Sean wanted to play as " + marioCharacter4 + ","
    out += "\n"
    out += "I wanted to play as " + marioCharacter5 + "."
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    return out
