from core.modules import VisualNovelModule
# This is the Example Script, obviously~

from characters import Monika # Import characters you've defined in characters.py
vn = VisualNovelModule()
m = Monika 
p = "Player" 

# By the way, if you're wondering how it works
# It's just gonna combine all of the script into one big script
# So jumpTo and label works across file
# Because everything will be in one big file
def story():

    vn.setVar(m.outfit,"school")
        
        
        
        
        
    return vn.dialogueDict
