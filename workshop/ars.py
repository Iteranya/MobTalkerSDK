from core.modules import VisualNovelModule
from core.compiler import compile
# -------------------------------------------------------
# This is the Example of a Single File Script
# -------------------------------------------------------

# So like, a standalone script will compile into a single script
# Think of it like a single 100k words word document.
# If that your style, this is how you do it

from characters import Cupa,Andr # Import characters you've defined in characters.py
vn = VisualNovelModule()
c = Cupa 
a = Andr
p = "Ars" 
storyName = "ars" # This will be the name of the Json File

def story():


    # Come on now, it's intuitive enough~
    vn.setVar("background",False)

    vn.start()
    # vn.play_music("haggstrom")
    vn.label("start") # This is a 'Label', it will be used by the jump and choice to know where to go
    vn.show_custom("asset","black_screen",16,9,16,10,1,1)
    vn.say(p,"Imma keep it real with you guys, I... I don't know how to edit video","p-90")
    vn.say(p,"Everything you hear and about to see are raw Minecraft Footage","p-91")
    vn.say(p,"From OBS and straight into youtube","p-92")
    vn.say(p,"The music, voice overs, visuals, and everything else are handled by the mod, rendered in real time in Minecraft","p-93")
    vn.say(p,"Please, enjoy the video...","p-94")
    vn.remove("asset","black_screen")
    vn.say(p,"Hey guys, welcome to my new channel, today I'm going to talk about the revival of the old Mob Talker mod","p-72")
    vn.show_custom("asset","old_mod",16,9,10,6,4,1)
    vn.say(p,"If you don't know, this is the old Mob Talker mod, it's a mod that adds a microphone and let you talk with mob girls.","p-73")
    vn.say(p,"Anyway, without further ado, let's see this mod in action, shall we???","p-74")
    vn.stop_music()
    vn.finish()


    return vn.dialogueDict


def main():compile(storyname=storyName,script=story()) # Yeah, just run this file :v

if __name__ == "__main__":
    main() 