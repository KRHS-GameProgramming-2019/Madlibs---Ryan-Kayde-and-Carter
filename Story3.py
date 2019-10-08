from Getword import *

def Story3(debug = False):
    if debug: print("Story3 Function")
    
    print("\n")
    weekDay1 = getDay("Enter a weekday: ", debug)
    marioCharacter1 = getWord("Enter a character: ", debug)
    marioCharacter2 = getWord("Enter another character: ", debug)
    marioCharacter3 = getWord("Enter another character: ", debug)
    marioCharacter4 = getWord("Enter another character: ", debug)
    marioCharacter5 = getWord("Enter another character: ", debug)
    track1 = getTrack("Enter a track: ",debug)
    track2 = getTrack("Enter another track: ",debug)
    item1 = getItem("Enter an item: ",debug)
    food1 = getFood("Enter a food: ", debug)
    verb1 = getVerb("Enter a verb: ",debug)
    verb2 = getVerb("Enter another verb: ",debug)
    verb3 = getVerb("Enter another verb: ",debug)
    verb4 = getVerb("Enter an -ing verb: ",debug)
    place1 = getPlace("Enter a place: ",debug)
    adjective1 = getAdjective("Enter an adjective: ",debug)
    
    
    
    
    out = "\n"
    out += "Today was " + weekDay1 + ","
    out += "\n"
    out += "Mario Kart day!"
    out += "\n"
    out += "my friends and I got our controllers and selected characters"
    out += "\n"
    out += "Kaden wanted to play as " + marioCharacter1  
    out += "\n"
    out += "Carter wanted to play as " + marioCharacter2 
    out += "\n"
    out += "Troy wanted to play as " + marioCharacter3  
    out += "\n"
    out += "Sean wanted to play as " + marioCharacter4 
    out += "\n"
    out += "and I wanted to play as " + marioCharacter5 
    out += "\n"
    out += "Once we got our characters ready, I selected the first race, " + track1
    out += "\n"
    out += "We were in the middle of lap 3..."
    out += "\n"
    out += "The final item box was going to be the deciding factor..."
    out += "\n"
    out += "I hit the item box and I pulled a " + item1
    out += "\n"
    out += "I used it and won the race!"
    out += "\n"
    out += "troy was so mad that he " + verb1
    out += "\n"
    out += "He " + verb2 + " my cabinets for " + food1
    out += "\n"
    out += "I " + verb3 + " him out of the " + place1
    out += "\n"
    out += "Everyone else was " + verb4 + " and they selected the next race, " + track2
    out += "\n"
    out += "Everyone had a " + adjective1 + " time"
    out += "\n"
    out += "\n"
    out += "\n"
    out += "Story 3 end"
    out += "\n"
    out += "\n"
    out += "Created by: Ryan St. Lawrence"
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    return out
